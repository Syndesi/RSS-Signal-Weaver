from typing import List
from feedparser import FeedParserDict
from rrsignalweaver.core.models import Article


def extract_articles(feed: FeedParserDict) -> List[Article]:
    articles: List[Article] = []

    for entry in feed.entries:
        articles.append(
            Article(
                title=entry.get("title", ""),
                content=entry.get("summary", ""),
            )
        )

    return articles
