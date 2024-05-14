
try:
  logging = getLogger()
except NameError:
  import logging

logging.info("some logs")

