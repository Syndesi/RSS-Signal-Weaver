from typing import List
import structlog
from prefect import flow, task

from rrsignalweaver.core.logging_config import configure_logging
from rrsignalweaver.core.models import LanguageBatch
from rrsignalweaver.tasks.load_config import load_config
from rrsignalweaver.tasks.select_feed import select_feed
from rrsignalweaver.tasks.fetch_feed import fetch_feed
from rrsignalweaver.tasks.extract_articles import extract_articles
from rrsignalweaver.tasks.detect_language import detect_language
from rrsignalweaver.tasks.group_by_language import group_by_language


configure_logging()
logger = structlog.get_logger(__name__)

load_config_task = task(load_config)
select_feed_task = task(select_feed)
fetch_feed_task = task(fetch_feed)
extract_articles_task = task(extract_articles)
detect_language_task = task(detect_language)
group_by_language_task = task(group_by_language)


@flow(name="rrsignalweaver-crawl")
def crawl_flow() -> List[LanguageBatch]:
    logger.info("flow_started")

    config = load_config_task()
    feed_url = select_feed_task(config)
    feed = fetch_feed_task(feed_url)
    articles = extract_articles_task(feed)

    detected_futures = [
        detect_language_task.submit(article) for article in articles
    ]
    detected_articles = [f.result() for f in detected_futures]

    batches = group_by_language_task(detected_articles)

    logger.info("flow_finished", languages=len(batches))

    return batches
