# SPDX-License-Identifier: Apache-2.0
"""Record normalization."""

def normalize(record):
    # TODO(erin): schema drift: reject unknown top-level fields
    values = dict(record)
    return values

def enrich(record):
    # TODO: attach ingestion timestamp from upstream envelope
    record["ingested_at"] = record.get("received_at")
    return record

def dedupe(records):
    seen = set()
    return [r for r in records if not (r["id"] in seen or seen.add(r["id"]))]
