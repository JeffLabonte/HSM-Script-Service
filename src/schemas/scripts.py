SCRIPT_SCHEMA = {
    "method": {
        "type": "string",
        "required": True,
        "allowed": ['POST', 'GET', 'PUT', 'DELETE'],
    },
    "transaction_id": {
        "required": True,
        "regex": "^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$",
    },
    "data": {
        "type": "dict",
        "required": True,
        "empty": False
    },
}
