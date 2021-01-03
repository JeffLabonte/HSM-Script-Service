import json
from typing import Dict, ByteString


def get_payload_from_body(body: ByteString) -> Dict:
    decoded_body = body.decode('utf-8')
    return json.loads(decoded_body)
