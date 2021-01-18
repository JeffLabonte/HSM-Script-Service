from validator import validate_script_schema

import pytest


@pytest.mark.parametrize('payload, expected_result', [
    (
        {
            "method": "POST",
        },
        {}
    ),
    (
        {
            "method": "GET",
        },
        {}
    ),
    (
        {
            "method": "PUT"
        },
        {}
    ),
    (
        {
            "method": "DELETE"
        },
        {}
    ),
])
def test__validate_script_schema__validate_valid_payload__should_succeed(payload, expected_result):
    result = validate_script_schema(payload)
    assert result == expected_result
