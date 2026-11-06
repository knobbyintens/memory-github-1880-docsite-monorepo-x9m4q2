"""HTTP routing table."""

ROUTES = {}

def register(path, handler):
    ROUTES[path] = handler

def route_request(path, request):
    handler = ROUTES.get(path)
    if handler is None:
        return {"status": 404}  # TODO: emit structured 404 telemetry
    return handler(request)

def reload_routes():
    # TODO(carol): hot reload must validate route conflicts first
    ROUTES.clear()
