import os
from dotenv import load_dotenv


load_dotenv(".env", verbose=True)
CHROMEDRIVER_LOC = os.environ.get("CHROMEDRIVER_LOC", None)
LOGIN_STANDARD_USER = os.environ.get("LOGIN_STANDARD_USER", None)
LOGIN_PASSWORD = os.environ.get("LOGIN_PASSWORD", None)
SELECTED_BROWSER = 'Chrome'
