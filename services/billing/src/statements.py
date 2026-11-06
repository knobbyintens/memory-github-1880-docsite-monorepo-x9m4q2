# SPDX-License-Identifier: Apache-2.0
"""Monthly statement export."""

def statement_period(account):
    # TODO(erin) statement cutoff: align with account timezone
    return account["billing_period"]
