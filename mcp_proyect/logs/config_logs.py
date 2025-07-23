import logging
import os
import traceback


class Logger:
    def _set_logger(self):
            log_direc = "logs"
            log_file = "app.log"

            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)

            log_path = os.path.join(log_direc,log_file)
            file_handler = logging.FileHandler(log_path, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '%(asctime)s | %(levelname)s | %(message)s'
            )
            file_handler.setFormatter(formatter) 

            if (logger.hasHandlers()):
                logger.handlers.clear()

            logger.addHandler(file_handler)

            return logger
    
    @classmethod
    def add_log(cls,level,message):
        try:
            logger = cls._set_logger(cls)

            if(level == "critical"):
                logger.critical(message)
            elif(level == "debug"):
                logger.debug(message)
            elif(level == "error"):
                 logger.error(message)
            elif(level == "info"):
                 logger.info(message)
            elif(level == "warn"):
                 logger.warn(message)
        except Exception as e:
            print(traceback.format_exc())
            print(e)