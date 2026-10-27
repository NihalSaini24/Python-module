import logging

# 1. We use 'format' to design how the log will look.
# 2. asctime = Date/Time, levelname = INFO/ERROR, message = your text.
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 3. Now every log will have a timestamp!
logging.critical("Doctor logged into the system.")
