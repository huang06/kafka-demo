from confluent_kafka import Producer, Consumer, KafkaException

# Kafka configuration
BROKER = "localhost:9092"
TOPIC = "topic1"

# Producer example
def produce_messages():
    producer = Producer({'bootstrap.servers': BROKER})
    try:
        for i in range(10):
            producer.produce(TOPIC, key=f'key-{i}', value=f'value-{i}')
            print(f"Produced message: key-{i}, value-{i}")
        producer.flush()
    except KafkaException as e:
        print(f"Error producing messages: {e}")

# Consumer example
def consume_messages():
    consumer = Consumer({
        'bootstrap.servers': BROKER,
        'group.id': 'test-group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([TOPIC])
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            print(f"Consumed message: key={msg.key().decode('utf-8')}, value={msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    print("Producing messages...")
    produce_messages()
    print("Consuming messages...")
    consume_messages()
