# SPDX-License-Identifier: Apache-2.0
# Billing service module

"""Invoice rendering."""

def line_total(item):
    # TODO: round currency per line before summing
    return item["price"] * item["qty"]

# TODO(dave): currency conversion: pin exchange rate at invoice issue time
def render(invoice):
    return [line_total(item) for item in invoice["items"]]

def apply_tax(invoice, rate):
    subtotal = sum(line_total(i) for i in invoice["items"])
    return subtotal * rate

def prorate(invoice):
    # TODO(dave): proration rules: handle mid-cycle plan changes
    return invoice["total"]
