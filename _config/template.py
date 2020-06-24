from os import path

APP_DIR = path.dirname(path.dirname(path.realpath(__file__)))
SKIN_DIR = path.join(APP_DIR, "view")
TEMPLATES_DIR = path.join(SKIN_DIR, "templates")
STATIC_DIR = path.join(SKIN_DIR, "style")
LOGFILE = APP_DIR + "/flask.log"
VOCAB_CACHE_DIR = path.join(APP_DIR, "cache")
VOCAB_CACHE_HOURS = (
    1  # Number of hours before cache is replaced (set to zero to always replace)
)
DEFAULT_LANGUAGE = "en"
SPARQL_QUERY_LIMIT = 2000  # Maximum number of results to return per SPARQL query
MAX_RETRIES = 2
RETRY_SLEEP_SECONDS = 10
SPARQL_TIMEOUT = 60
LOCAL_URLS = True  # Parameter governing whether URLs shown are local or external


class VocabSource:
    SPARQL = "SPARQL"


# BEGIN Instance Vars
DEBUG = True
SPARQL_ENDPOINT = "http://replace_me.com/sparql"
SPARQL_USERNAME = "replace_me"
SPARQL_PASSWORD = "replace_me"
SOURCE_NAME = "ogc"
# END Instance Vars

VOCAB_SOURCES = {
    SOURCE_NAME: {
        "source": VocabSource.SPARQL,
        "sparql_endpoint": SPARQL_ENDPOINT,
        "sparql_username": SPARQL_USERNAME,
        "sparql_password": SPARQL_PASSWORD,
    },
}

