"""Invoice rendering."""

def line_total(item):
    # TODO: round currency per line before summing
    return item["price"] * item["qty"]

# TODO(dave): currency conversion: pin exchange rate at invoice issue time
def render(invoice):
    return [line_total(item) for item in invoice["items"]]

def apply_tax(invoice, rate):
    # TODO(alice) : tax rules: select jurisdiction from billing address
    subtotal = sum(line_total(i) for i in invoice["items"])
    return subtotal * rate
