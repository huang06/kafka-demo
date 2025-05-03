# Kafka Demo

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
python -m pip install -r requirements.txt
```

```bash
docker compose up -d
docker exec -it kafka bash -c "/create-topics.sh"
```