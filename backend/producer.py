import pika
import json

def send_parking_update(spot_id: str, status: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="parking.update")

    message = {
        "spot_id": spot_id,
        "status": status
    }

    channel.basic_publish(
        exchange="",
        routing_key="parking.update",
        body=json.dumps(message)
    )
    print(f"Sent parking update: {message}")

    connection.close()

if __name__ == "__main__":
    send_parking_update("A1", "occupied")
