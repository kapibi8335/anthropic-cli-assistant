# Anthropic CLI Assistant

Small command-line assistant that talks to an Anthropic-compatible Messages
endpoint.

## Setup

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
set -a; . ./.env; set +a
python3 assistant.py "Write a haiku about queues."
```

Configuration is read from the environment; see `.env.example`.
