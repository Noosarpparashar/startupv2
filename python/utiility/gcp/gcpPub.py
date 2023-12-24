from google.cloud import pubsub_v1
import json

# Message data
message_data = {
    "CustomerId": "12399",
    "CustomerName": "John Doe",
    "CustomerAdd": "123 Main St"
}

# Google Cloud Pub/Sub settings
project_id = "tough-shard-409112"
topic_name = "customerinfo"

# Create a Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

# Publish the JSON-formatted message to the Pub/Sub topic
json_payload = json.dumps(message_data)
future = publisher.publish(topic_path, json_payload.encode("utf-8"))
print(f"Published message with ID: {future.result()}")
