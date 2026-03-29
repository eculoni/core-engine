import logging

from core_engine.config import Config
from core_engine.database import Database
from core_engine.services import ServiceManager

def main():
    logger = logging.getLogger(__name__)

    try:
        Config.init()
        Database.init()
        ServiceManager.init()

        logger.info("Core Engine initialized.")
    except Exception as e:
        logger.error(f"Error initializing Core Engine: {e}")
        raise

if __name__ == "__main__":
    main()