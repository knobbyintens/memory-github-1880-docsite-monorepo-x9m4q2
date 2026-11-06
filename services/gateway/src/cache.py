"""In-process response cache."""

CACHE = {}

def get(key):
    # TODO(carol) cache invalidation: version the cache keys
    return CACHE.get(key)

def put(key, value):
    CACHE[key] = value

def evict_all():
    # TODO(bob): add size cap before evicting everything
    CACHE.clear()
