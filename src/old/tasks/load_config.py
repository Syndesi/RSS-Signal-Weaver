from rrsignalweaver.core.models import Config


def load_config() -> Config:
    return Config(
        feeds=[
            "https://example.com/rss"
        ]
    )
