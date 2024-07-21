import os
import loguru


ENVIRONMENT = os.environ.get('ENVIRONMENT', False)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    OWNER_ID = os.environ.get('OWNER_ID', 6258709129)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 28298365 # api id here
    OWNER_ID = 5536168611
    API_HASH = "9647ab7fc03a8a93f701a5528b2f206e"
    BOT_TOKEN = "7346455769:AAG4S9buEgIlCfwT-Vk80PaODeILZ_hLWlw"
    DATABASE_URL = "postgres://avnadmin:AVNS_gwvtPgMcQ7IX0qwaCG9@freedb-mayrice01.i.aivencloud.com:14358/defaultdb?sslmode=require"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "AnimeSouls0" # must join channel link here
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
