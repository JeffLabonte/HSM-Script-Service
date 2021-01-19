SCRIPT_SCHEMA = {
    "method": {
        "type": "string",
        "required": True,
        "allowed": ['POST', 'GET', 'PUT', 'DELETE'],
    },
    "transaction_id": {
        "required": True,
        "type": "string",
        "regex": "[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}",
    },
    "data": {
        "type": "dict",
        "required": True,
        "empty": False,
    },
}
