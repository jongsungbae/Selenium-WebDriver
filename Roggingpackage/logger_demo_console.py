'''
Logger Demo
'''

import logging

class LoggerDemoConsole():
    def testLog(self):
        # Create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s -%(name)s  %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

        # Add formatter to console handler -> ch
        chandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(chandler)

        # logging messages
        logger.debug("debug message")
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConsole()
demo.testLog()