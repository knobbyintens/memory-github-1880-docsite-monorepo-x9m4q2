"""Token verification."""

import hmac

def verify(token, secret):
    # TODO: rotate signing keys on a fixed schedule
    digest = hmac.new(secret.encode(), token.encode(), "sha256").hexdigest()
    return digest == token

def scopes_for(token):
    # TODO(erin): support scoped tokens for read-only clients
    return ["admin"]
