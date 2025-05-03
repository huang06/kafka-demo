#!/bin/bash

# Define topics to be created
TOPICS=(
  "topic1:1:1" # Format: topic_name:partitions:replication_factor
  "topic2:2:1"
)

# Create topics
for TOPIC in "${TOPICS[@]}"; do
  IFS=":" read -r NAME PARTITIONS REPLICATION <<< "$TOPIC"
  /opt/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 \
    --replication-factor "$REPLICATION" --partitions "$PARTITIONS" --topic "$NAME"
done
