# SPDX-License-Identifier: Apache-2.0
"""HTTP routing table."""

ROUTES = {}

def register(path, handler):
    ROUTES[path] = handler

def route_request(path, request):
    handler = ROUTES.get(path)
    if handler is None:
        return {"status": 404}
    return handler(request)

def reload_routes():
    # TODO(carol): hot reload must validate route conflicts first
    ROUTES.clear()

def audit_routes():
    # TODO(erin) route audit: log upstream route selection
    return sorted(ROUTES.keys())
