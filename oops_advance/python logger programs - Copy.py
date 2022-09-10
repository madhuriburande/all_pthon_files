import logging
logging.basicConfig(level=logging.ERROR)
logging.error("This is error message")


import logging
var="python"
logging.warning("This is warning message!",var)

## Example of logging to the file:

import logging
"""" Storing the logging information into a file named msg.file and 
     we are giveing the write mode (w) and the format in which mssage
    store in name of the root followed by the levl of the message .
"""

logging.basicConfig(filename='loggermsg.log',filemode='w',format='%(levelname)s:%(name)s:%(message)s')
logging.error("This is an error message")
logging.warning("This is warning!")

## For example, let us see how to get time and date along with the message.Example of formatting the output:
import logging
logging.basicConfig(filename='log1.log',format='%(asctime)s %(message)s')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
str1="www.google.com"
logger.debug(str1)
logger.info("I am information i.e (info) level ")