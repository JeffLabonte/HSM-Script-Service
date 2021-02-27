import logging
from time import sleep
from os import environ

from helper.amqp import get_payload_from_body
from service.amqp import AMQPService
from logger import configure_logger

configure_logger()
logger = logging.getLogger("script_service")

TOPIC_TO_CONSUME = "script.#"

AMQP = None


def get_environment(variable, default):
    if value := environ.get(variable, None):
        return value
    return default


def callback(ch, method, properties, body):
    payload = get_payload_from_body(body)
    logger.warning(f"ch: {ch}")
    logger.warning(f"method: {method}")
    logger.warning(f"properties: {properties}")
    logger.warning(f"body: {body}")
    logger.warning(payload)
    AMQP.publish(topic="script.create.response", message={"test": "test"})


if __name__ == "__main__":
    broker_host = get_environment(variable="BROKER_HOST", default="broker")
    AMQP = AMQPService(callback, host=broker_host, routing_keys=["script.create"])
    logger.info("Starting service")
    AMQP.start_consuming()
