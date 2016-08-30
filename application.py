import logging
import sys

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,  stream=sys.stdout, format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.info("hello")