from future import annotations

import logging
from dataclasses import dataclass

LOGGER = logging.getLogger(name)

@dataclass(frozen=True)
class Command:
  """Represents a parsed user command."""

intent: str
payload: str

def parse_command(raw: str) -> Command:
  """Parse a raw user string into a structured Command.

  A simple 'intent: payload' format is used. If no colon is present the
  entire string is treated as the intent with an empty payload.
  """
  if not raw.strip():
    raise ValueError("command must not be empty")

intent, _, payload = raw.partition(":")
return Command(intent=intent.strip().lower(), payload=payload.strip())

def handle(command: Command) -> str:
  """Produce a response for the given command."""
  handlers = {
  "search": lambda p: f"Searching for: {p}",
  "open": lambda p: f"Opening: {p}",
  "remind": lambda p: f"Reminder set: {p}",
  }
  handler = handlers.get(command.intent)
  if handler is None:
    return f"Sorry, I don't understand '{command.intent}'."
    return handler(command.payload)

def main() -> int:
  """Application entry point."""
  logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

samples = ["search: python tutorials", "open: notes.txt", "unknown: hello"]
for raw in samples:
  response = handle(parse_command(raw))
  print(f"> {raw}\n {response}")
  return 0

if name == "main":
  raise SystemExit(main())
  
