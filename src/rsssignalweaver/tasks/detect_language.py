import structlog
from langdetect import detect
from rrsignalweaver.core.models import Article

logger = structlog.get_logger(__name__)


def detect_language(article: Article) -> Article:
    try:
        article.language = detect(article.content)
        logger.info("language_detected", language=article.language)
    except Exception:
        article.language = "unknown"
        logger.warning("language_detection_failed")
    return article
