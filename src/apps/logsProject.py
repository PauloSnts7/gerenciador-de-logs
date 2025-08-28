import logging
from loguru import logger
from sentry_sdk.integrations.logging import LoggingIntegration
import sentry_sdk
import sys

import sentry_sdk

dsn="coloque sua dsn"


sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.INFO
)

sentry_sdk.init(
    dsn=dsn,
    integrations=[sentry_logging],
    send_default_pii=True,
)


logging.critical('Quebou a aplicação')