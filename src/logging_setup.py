import os
import sys

from loguru import logger


def setup_logging():
    env = os.getenv("APP_ENV", "dev")
    level = os.getenv("LOG_LEVEL", "INFO")

    logger.remove()

    if env == "prod":
        logger.add(sys.stdout, level=level, serialize=True, enqueue=True)
        logger.add(
            "logs/app.log",
            rotation="10 MB",
            retention="7 days",
            compression="zip",
            level=level,
            serialize=True,
        )
    else:
        fmt = "<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
        logger.add(sys.stdout, level=level, format=fmt)
        logger.add("logs/dev.log", rotation="10 MB", level=level)

    return logger
