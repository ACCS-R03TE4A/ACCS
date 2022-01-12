from logging import getLogger

logger = None


def initLogger():
    global logger 
    logger = getLogger(__name__)


