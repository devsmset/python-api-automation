import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path(__file__).resolve().parent.parent / "config.ini")

def get_config(key):
    return config["API"][key]

def get_api_key():
    return get_config("GO_REST_ACCESS_TOKEN")

def get_url(append = "/"):
    base_url = get_config("BASE_URL").strip().strip("/")
    return f'{base_url}/{append.strip().strip("/")}'


