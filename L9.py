import logging
logging.basicConfig(level=logging.DEBUG, filename="errorMessage.log", filemode="a+",format="Message of error:%(asctime)s%(levelname)s - %(message)s")
try:
    print(10/0)
except:
    logging.exception("ZeroDivisionError")



# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")