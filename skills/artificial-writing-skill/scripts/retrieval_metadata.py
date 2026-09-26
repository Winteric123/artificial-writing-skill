import re
import unicodedata


def text_key(value):
    value = unicodedata.normalize('NFKC', value).casefold()
    value = value.translate(str.maketrans({'–': '-', '—': '-', '−': '-', '‑': '-', '_': ' '}))
    return re.sub(r'\s+', ' ', value).strip()


def phrase_pattern(value):
    pieces = re.split(r'[\s-]+', text_key(value))
    return r'(?<![a-z0-9-])' + r'[\s-]+'.join(re.escape(piece) for piece in pieces) + r'(?![a-z0-9])'


def contains_phrase(text, phrase):
    return bool(re.search(phrase_pattern(phrase), text_key(text)))


def canonical(value, groups):
    key = text_key(value)
    for identifier, aliases in groups.items():
        if key in {text_key(identifier), *(text_key(alias) for alias in aliases)}:
            return identifier
    return key.replace(' ', '-')


def exact_tag_match(wanted, values, groups):
    wanted = canonical(wanted, groups)
    if isinstance(values, str):
        values = values.split(';')
    return wanted in {canonical(value, groups) for value in values if value}


def detected_terms(text, groups):
    matches = [(identifier, match.start(), match.end()) for identifier, aliases in groups.items()
               for term in [identifier, *aliases] for match in re.finditer(phrase_pattern(term), text_key(text))]
    return sorted({identifier for identifier, start, end in matches
                   if not any(other != identifier and left <= start and right >= end and right-left > end-start
                              for other, left, right in matches)})


def query_clauses(query, concepts):
    remaining = text_key(query)
    phrases = {}
    for concept in concepts:
        alternatives = tuple(dict.fromkeys(text_key(term) for term in concept['terms']))
        for term in alternatives:
            phrases[term] = alternatives
    clauses = []
    for term in sorted(phrases, key=len, reverse=True):
        pattern = phrase_pattern(term)
        if re.search(pattern, remaining):
            clauses.append(phrases[term])
            remaining = re.sub(pattern, ' ', remaining)
    clauses.extend((token,) for token in re.findall(r'\S+', remaining))
    return clauses


def query_matches(text, clauses):
    return all(any(contains_phrase(text, alternative) for alternative in clause) for clause in clauses)


def article_scope(article, vocabulary, override=None):
    raw = article.get('disease_scope', '')
    uncertain = bool(re.search(r'\b(?:not|no|comparator|comparators|versus|excluding)\b', raw, re.I))
    diseases = [] if uncertain else detected_terms(raw, vocabulary['diseases'])
    if 'nsclc' in diseases:
        diseases = [value for value in diseases if value != 'lung-cancer']
    elif 'sclc' in diseases:
        diseases = [value for value in diseases if value != 'lung-cancer']
    scope = dict(disease_scope=raw, source_role=article.get('source_role', ''),
                 disease_ids=diseases, tissue_ids=[], model_ids=[], use_roles=[],
                 annotation_status='recorded-scope-normalized' if diseases else 'unclassified',
                 source_reference=article.get('scope_reference', ''),
                 boundary='Article-level source context, not evidence that every expression applies to every listed disease.')
    if override:
        scope.update(override)
        scope['annotation_status'] = 'curated-source-scope'
    scope['facet_status'] = {field: 'identified-not-exhaustive' if scope[field] else 'not-curated-not-absent'
                             for field in ('disease_ids', 'tissue_ids', 'model_ids', 'use_roles')}
    return scope


def expression_metadata(row, lines, vocabulary, annotation=None):
    position = int(row['source_line']) - 1
    context = ''
    context_line = None
    for cursor in range(position - 1, -1, -1):
        line = lines[cursor]
        if line.startswith('### ') or line.startswith('## '):
            break
        if line.startswith(('Source context:', 'Source:', 'Functional transfer from')):
            context, context_line = line, cursor + 1
            break
    origin = 'conventional-term-or-collocation' if row['unit_type'].replace('_', '-') in {'vocabulary', 'collocation'} else 'synthetic-expression'
    metadata = dict(article_domains=row.get('domain', ''),
                    expression_domains=detected_terms(row['expression'], vocabulary['domains']),
                    expression_annotation_status='lexical-topic-candidate', expression_origin=origin,
                    original_wording_verified=False,
                    source_locator=dict(precision='section-context' if context else 'asset-only',
                                        context=context, context_asset=row['source_asset'], context_line=context_line,
                                        original_pdf_location_verified=False),
                    usage_constraint='Use the linked source context and article alerts. A synthetic frame is not a quotation or a finding of the target study.')
    if annotation:
        metadata.update(annotation)
    return metadata
