import os
import logging
import random
from dotenv import load_dotenv

load_dotenv()

IGNORED_MODEL_NAMES = ["gpt-4", "gpt-3.5", "websearch", "dall-e-3", "gpt-4o"]
IMAGE_MODEL_NAMES = ["dalle3", "dalle-3", "dall-e-3"]
AUTH_TOKEN = os.getenv("AUTHORIZATION")
# G_TOKEN = os.getenv("G_TOKEN")
G_TOKEN = ""
HISTORY_MSG_LIMIT = os.getenv("HISTORY_MSG_LIMIT", 0)
HTTP_PROXIES = os.getenv("HTTP_PROXIES")
HTTPS_PROXIES = os.getenv("HTTPS_PROXIES")
SOCKS_PROXIES = os.getenv("SOCKS_PROXIES")


def configure_logging():
    extended_log_format = (
        '%(asctime)s | %(levelname)s | %(name)s | '
        '%(process)d | %(filename)s:%(lineno)d | %(funcName)s | %(message)s'
    )
    logging.basicConfig(level=logging.DEBUG, format=extended_log_format)


def _get_proxies_from_env(env_var):
    proxies = os.getenv(env_var, '')
    return [proxy.strip() for proxy in proxies.split(',') if proxy.strip()]

def reloadGtoken():
    G_TOKEN = os.getenv("G_TOKEN")

class ProxyPool:
    def __init__(self):
        self.http_proxies = _get_proxies_from_env('HTTP_PROXIES')
        self.https_proxies = _get_proxies_from_env('HTTPS_PROXIES')
        self.socks_proxies = _get_proxies_from_env('SOCKS_PROXIES')

    def get_random_proxy(self):
        proxy = {}
        if self.http_proxies:
            proxy['http'] = random.choice(self.http_proxies)
        if self.https_proxies:
            proxy['https'] = random.choice(self.https_proxies)
        if self.socks_proxies:
            socks_proxy = random.choice(self.socks_proxies)
            proxy['http'] = socks_proxy
            proxy['https'] = socks_proxy

        logging.info("proxy URL %s", proxy)

        return proxy if proxy else None
