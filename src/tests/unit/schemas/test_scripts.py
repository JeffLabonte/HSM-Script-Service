from uuid import uuid4

from validator import validate_script_schema

import pytest


@pytest.mark.parametrize('payload', [
    (
        {
            "method": "POST",
            "transaction_id": uuid4(),
            "data": {
                "test": 1,
            },
        }
    ),
    (
        {
            "method": "GET",
            "transaction_id": uuid4(),
            "data": {
                "test": 1,
            }
        }
    ),
    (
        {
            "method": "PUT",
            "transaction_id": uuid4(),
            "data": {
                "test": 1,
            }
        }
    ),
    (
        {
            "method": "DELETE",
            "transaction_id": uuid4(),
            "data": {
                "test": 1,
            }
        }
    ),
])
def test__validate_script_schema__validate_valid_payload__should_succeed(payload):
    result = validate_script_schema(payload)
    assert result == {}  # Empty dict means no errors
