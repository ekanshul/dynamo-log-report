import json
from pathlib import Path

import pytest

REPORT_PATH = Path("/app/report.json")

# Expected values for the log shipped at /app/access.log:
#   6 request lines; IPs {192.168.0.1, 192.168.0.2, 10.0.0.5} -> 3 unique;
#   /index.html requested 3 times -> most frequent path.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


@pytest.fixture(scope="module")
def report():
    """Load and parse /app/report.json once for all value checks."""
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    data = json.loads(REPORT_PATH.read_text())
    return data


def test_report_is_json_object(report):
    """Criterion 1: /app/report.json exists and parses as a single JSON object."""
    assert isinstance(report, dict), "report.json must be a single JSON object"


def test_total_requests(report):
    """Criterion 2: total_requests is an integer equal to the number of request lines."""
    assert "total_requests" in report, "report is missing 'total_requests'"
    value = report["total_requests"]
    assert isinstance(value, int) and not isinstance(value, bool), (
        "'total_requests' must be an integer"
    )
    assert value == EXPECTED_TOTAL_REQUESTS, (
        f"expected total_requests={EXPECTED_TOTAL_REQUESTS}, got {value}"
    )


def test_unique_ips(report):
    """Criterion 3: unique_ips is an integer equal to the number of distinct client IPs."""
    assert "unique_ips" in report, "report is missing 'unique_ips'"
    value = report["unique_ips"]
    assert isinstance(value, int) and not isinstance(value, bool), (
        "'unique_ips' must be an integer"
    )
    assert value == EXPECTED_UNIQUE_IPS, (
        f"expected unique_ips={EXPECTED_UNIQUE_IPS}, got {value}"
    )


def test_top_path(report):
    """Criterion 4: top_path is a string equal to the most frequently requested path."""
    assert "top_path" in report, "report is missing 'top_path'"
    value = report["top_path"]
    assert isinstance(value, str), "'top_path' must be a string"
    assert value == EXPECTED_TOP_PATH, (
        f"expected top_path={EXPECTED_TOP_PATH!r}, got {value!r}"
    )
