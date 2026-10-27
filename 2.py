import logging

logging.basicConfig(level=logging.WARNING)

# 1. DEBUG (Tiny details)
logging.debug("Looking up patient history...")

# 2. INFO (Normal operations)
logging.info("Patient successfully checked in.")

# 3. WARNING (Something is a bit weird)
logging.warning("Hospital is running low on paracetamol.")

# 4. ERROR (Something broke)
logging.error("Failed to connect to the billing database.")

# 5. CRITICAL (The whole system is down)
logging.critical("MAIN SERVER CRASHED! PATIENT DATA AT RISK!")