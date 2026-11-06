# SPDX-License-Identifier: Apache-2.0
# Reviewed during the Q4 maintenance sweep
"""In-process response cache."""

CACHE = {}

def get(key):
    # TODO(carol) cache invalidation: version the cache keys
    return CACHE.get(key)

def put(key, value):
    CACHE[key] = value

def evict_all():
    CACHE.clear()

def warm(keys):
    # TODO(alice): introduce negative caching for repeated misses
    for key in keys:
        get(key)
