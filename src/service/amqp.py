import json
from typing import Callable, Dict, List

from pika import BlockingConnection, ConnectionParameters
from pika.channel import Channel

from service.base_service import BaseService


class AMQPService(BaseService):
    def __init__(self, callback: Callable, routing_keys: List, host="broker", port=5672, exchange='script_topic'):
        self.connection = BlockingConnection(
            ConnectionParameters(host=host, port=port)
        )
        self.exchange = exchange
        self.channel = self._init_channel()
        self.queue_name = self._init_queue()
        self._bind_routing_keys(routing_keys=routing_keys)
        self._add_callback(callback)

    def _init_channel(self) -> Channel:
        channel = self.connection.channel()
        channel.exchange_declare(
            exchange=self.exchange,
            exchange_type='topic'
        )
        return channel

    def _init_queue(self) -> str:
        result = self.channel.queue_declare('', exclusive=True)
        return result.method.queue

    def _bind_routing_keys(self, routing_keys: list) -> None:
        for routing_key in routing_keys:
            self.channel.queue_bind(
                exchange=self.exchange,
                queue=self.queue_name,
                routing_key=routing_key,
            )

    def _add_callback(self, callback: Callable) -> None:
        if not callable(callback):
            raise RuntimeError("Requires a callable")

        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )

    def publish(self, topic: str, message: Dict):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=topic,
            body=json.dumps(message),
        )

    def start_consuming(self):
        self.channel.start_consuming()
