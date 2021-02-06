import logging
from time import sleep
from os import environ

from helper.amqp import get_payload_from_body

logger = logging.getLogger('script_service')

TOPIC_TO_CONSUME = 'script.#'


def get_environment(variable, default):
    if value := environ.get(variable, None):
        return value
    return default


def callback(ch, method, properties, body):
    payload = get_payload_from_body(body)
    print(f"ch: {ch}")
    print(f"method: {method}")
    print(f"properties: {properties}")
    print(f"body: {body}")
    print(payload)


if __name__ == "__main__":
    # TODO Create messaging service, init service
    pass
