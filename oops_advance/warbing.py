import logging
logging.basicConfig(filename='log2.log',format='%(asctime)s %(message)s',level=logging.DEBUG,datefmt='%d-%B-%Y %I:%M:%S %p')
logging.getLogger()
var="Python"
logging.warning("%s raised warning",var)
