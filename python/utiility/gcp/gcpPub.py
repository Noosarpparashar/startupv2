from google.cloud import pubsub_v1
import json
from faker import Faker
import random
import time

# Set up Faker
fake = Faker()

# Counter for generating increasing customer IDs
customer_id_counter = int(time.strftime("%d%H%M%S"))  # You can adjust the range as needed

# Function to generate the next customer ID
def generate_customer_id():
    global customer_id_counter
    customer_id = f"M-{customer_id_counter}"
    customer_id_counter += 1
    return customer_id

# Google Cloud Pub/Sub settings
project_id = "tough-shard-409112"
topic_name = "customerinfo"

# Create a Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

# Infinite loop to keep generating and publishing fake customer data
while True:
    fake_customer_data = {
        "CustomerId": generate_customer_id(),
        "CustomerName": fake.name(),
        "CustomerAdd": fake.address(),
    }

    # Publish the JSON-formatted message to the Pub/Sub topic
    json_payload = json.dumps(fake_customer_data)
    future = publisher.publish(topic_path, json_payload.encode("utf-8"))
    print(f"Published message with ID: {future.result()}")

    # Introduce a delay between iterations
    time.sleep(10)  # Adjust the delay as needed
