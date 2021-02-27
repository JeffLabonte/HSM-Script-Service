import logging
from logging.config import dictConfig


logging_config = dict(
    version=1,
    formatters={"f": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"}},
    handlers={
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "f",
            "level": logging.DEBUG,
        },
        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "f",
            "level": logging.DEBUG,
            "filename": "/tmp/process.log",
            "maxBytes": 20,
            "backupCount": 5,
        },
    },
    root={
        "handlers": [
            "stream_handler",
            "file_handler",
        ],
        "level": logging.DEBUG,
    },
)


def configure_logger():
    dictConfig(logging_config)
