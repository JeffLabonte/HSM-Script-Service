# import pika

import logging

from helper.amqp import get_payload_from_body

logger = logging.getLogger('script_service')

TOPIC_TO_CONSUME = 'script.#'

TOPIC_TO_FUNCTION_MAPPING = {
    'script.get': None,  # TODO Add function from controller
    'script.get.by_attr': None,
    'script.create': None,
    'script.update.id.$': None,
}


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
