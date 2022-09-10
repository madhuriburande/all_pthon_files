import logging
logging.basicConfig(filename='log7.log',datefmt=('%d-%m-%Y %a,%I-%M-%p'),format='%(asctime)s %(message)s')
logging.getLogger()
try:
    a=10
    b=0
    print("Division of a and b",a/b)
except ZeroDivisionError as e:
    logging.error(e)
