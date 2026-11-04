"""Packaging validator for the invoice-router blueprint."""

REQUIRED_OUTPUT = "invoice-router_report.json"


def validate(workspace):
    from pathlib import Path

    report = Path(workspace) / REQUIRED_OUTPUT
    if not report.is_file():
        raise AssertionError(f"missing {REQUIRED_OUTPUT}")
    return True


if __name__ == "__main__":
    validate(".")
    print("validation passed")
