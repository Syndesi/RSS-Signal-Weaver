from __future__ import annotations

import feedparser

from rsssignalweaver.type.dto import RssFeedItem


def parse_rss_document(rss_document: str) -> list[RssFeedItem]:
    parsed_rss_document = feedparser.parse(rss_document)
    parsed_items = []
    for entry in parsed_rss_document['entries']:
        title = entry['title']
        url = entry['link']
        authors = []
        for entry_author in entry['authors']:
            authors.append(entry_author['name'])
        tags = []
        for entry_tag in entry['tags']:
            tags.append(entry_tag['term'])
        description = entry['summary']
        published = entry['published_parsed']
        source_item = entry
        rss_feed_item = RssFeedItem(title, url, authors, tags, description, published, source_item)
        parsed_items.append(rss_feed_item)

    return parsed_items
