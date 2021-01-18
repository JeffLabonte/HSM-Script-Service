from cerberus import Validator
from schemas.scripts import SCRIPT_SCHEMA

from typing import Dict


def validate_script_schema(dirty_input: dict) -> Dict:
    v = Validator()
    v.validate(dirty_input, SCRIPT_SCHEMA)
    return v.errors
