from google.cloud import pubsub_v1

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path('tough-shard-409112', 'customerinfo-sub')

def callback(message):
    print(f"Received message: {message.data}")
    # Process the input data as needed
    message.ack()
    streaming_pull_future.cancel()

# Create a subscriber and start pulling messages
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...\n")

# Block the script to keep the subscriber alive
try:
    streaming_pull_future.result()
except Exception as ex:
    print(f"Error during message pulling: {ex}")
    streaming_pull_future.cancel()
