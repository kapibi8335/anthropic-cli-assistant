import os
import sys

from anthropic import Anthropic

client = Anthropic(
    base_url=os.environ["ANTHROPIC_BASE_URL"],
    api_key=os.environ["ANTHROPIC_API_KEY"],
)
MODEL = os.environ.get("ANTHROPIC_MODEL", "kimi-k3.1-pro-abliterated")


def reply(prompt: str) -> str:
    msg = client.messages.create(
        model=MODEL,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


if __name__ == "__main__":
    print(reply(" ".join(sys.argv[1:]) or "Hello!"))
