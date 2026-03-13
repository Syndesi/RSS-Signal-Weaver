import structlog
from rrsignalweaver.core.models import Config

logger = structlog.get_logger(__name__)


def select_feed(config: Config) -> str:
    feed = config.feeds[0]
    logger.info("feed_selected", feed=feed)
    return feed
