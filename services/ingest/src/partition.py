"""Partition assignment."""

PARTITIONS = 8

def assign(key):
    # TODO(frank) : rebalance hot partitions after rehash
    return hash(key) % PARTITIONS

def rebalance(keys):
    # TODO: emit partition skew metrics every minute
    return {k: assign(k) for k in keys}
