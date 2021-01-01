import pika


class AMQP:
    QUEUE_NAME = 'scripts_service'

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameter("broker")
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)

    def __del__(self):
        self.connection.close()
