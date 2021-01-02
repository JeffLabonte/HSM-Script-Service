import pika


TOPIC_TO_RECEIVE = 'script.#'


if __name__ == "__main__":
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='broker')
    )

    channel = connection.channel()
    channel.exchange_declare(exchange='script_topic', exchange_type='topic')

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='script_topic',
                       queue=queue_name, routing_key=TOPIC_TO_RECEIVE)

    def callback(ch, method, properties, body):
        print("test")

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()
