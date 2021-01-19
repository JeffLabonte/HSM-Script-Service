from uuid import uuid4

from validator import validate_script_schema

import pytest


@pytest.mark.parametrize('payload', [
    (
        {
            "method": "POST",
            "transaction_id": str(uuid4()),
            "data": {
                "test": 1,
            },
        }
    ),
    (
        {
            "method": "GET",
            "transaction_id": str(uuid4()),
            "data": {
                "test": 1,
            }
        }
    ),
    (
        {
            "method": "PUT",
            "transaction_id": str(uuid4()),
            "data": {
                "test": 1,
            }
        }
    ),
    (
        {
            "method": "DELETE",
            "transaction_id": str(uuid4()),
            "data": {
                "test": 1,
            }
        }
    ),
])
def test__validate_script_schema__validate_valid_payload__should_succeed(payload):
    result = validate_script_schema(payload)
    assert result == {}  # Empty dict means no errors


@pytest.mark.parametrize('payload, faulty_field', (
    (
        {
            "method": "NOPE",
            "transaction_id": str(uuid4()),
            "data": {
                "test": 1,
            },
        },
        "method",
    ),
    (
        {
            "method": "POST",
            "transaction_id": "111",
            "data": {
                "test": 1,
            },
        },
        "transaction_id",
    ),
    (
        {
            "method": "POST",
            "transaction_id": 111,
            "data": {
                "test": 1,
            },
        },
        "transaction_id",
    ),
    (
        {
            "method": "POST",
            "transaction_id": str(uuid4()),
            "data": "1214123",
        },
        "data",
    ),
))
def test__validate_script_schema__validate_invalid_error__should_return_errors(payload, faulty_field):
    result = validate_script_schema(payload)
    assert faulty_field in result.keys()
    assert len(result) == 1
