"""Packaging validator for the quota-manager blueprint."""

REQUIRED_OUTPUT = "quota-manager_report.json"


def validate(workspace):
    from pathlib import Path

    report = Path(workspace) / REQUIRED_OUTPUT
    if not report.is_file():
        raise AssertionError(f"missing {REQUIRED_OUTPUT}")
    return True


if __name__ == "__main__":
    validate(".")
    print("validation passed")
