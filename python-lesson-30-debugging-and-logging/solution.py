import logging

logging.basicConfig(level=logging.WARNING)

logging.debug("cart total: %s", total)
logging.info("user checked out")
logging.warning("cart_total was none")
logging.error("checkout failed")
