from collections import defaultdict
from typing import Dict, List
from rrsignalweaver.core.models import Article, LanguageBatch


def group_by_language(articles: List[Article]) -> List[LanguageBatch]:
    grouped: Dict[str, List[Article]] = defaultdict(list)

    for article in articles:
        grouped[article.language or "unknown"].append(article)

    return [
        LanguageBatch(language=lang, articles=items)
        for lang, items in grouped.items()
    ]
