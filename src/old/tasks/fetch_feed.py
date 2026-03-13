import feedparser
from feedparser import FeedParserDict


def fetch_feed(url: str) -> FeedParserDict:
    return feedparser.parse(url)
