import pika
import json

def process_message(ch, method, properties, body):
    data = json.loads(body)
    spot_id = data["spot_id"]
    status = data["status"]
    print(f" [✔] Received update → Spot {spot_id} is now {status}")
    # TODO: update MongoDB here 
def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="parking.update")

    channel.basic_consume(
        queue="parking.update",
        on_message_callback=process_message,
        auto_ack=True
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
