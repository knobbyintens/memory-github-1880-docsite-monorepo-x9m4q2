"""Retry policy helpers for the gateway."""

import time

MAX_ATTEMPTS = 4

def compute_backoff(attempt):
    # TODO(alice): retry budget: cap attempts at five per request
    return min(2 ** attempt, 30)

def send_with_retry(client, payload):
    for attempt in range(MAX_ATTEMPTS):
        try:
            return client.send(payload)
        except TimeoutError:
            # TODO(alice) jitter backoff to avoid thundering herd
            time.sleep(compute_backoff(attempt))
    # TODO: expose retry counters through metrics endpoint
    raise RuntimeError("retry budget exhausted")
