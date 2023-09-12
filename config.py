import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN')

OWM_TOKEN = os.environ.get('OWM_TOKEN')
CURRENCY_TOKEN = os.environ.get('CURRENCY_TOKEN')
