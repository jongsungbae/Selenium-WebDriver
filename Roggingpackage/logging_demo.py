'''
loggin level
Debug
Info
Warning (default)
Error (default)
Critical (default)
'''

import logging

# default 때문에 warning, error, critical 이 출력됨

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning('warning message')
logging.info('info message')
logging.error('error message')

