import json
import logging
from typing import Dict, ByteString

logger = logging.getLogger(f'script_manager.{__name__}')


def get_payload_from_body(body: ByteString) -> Dict:
    try:
        decoded_body = body.decode('utf-8')
        return json.loads(decoded_body)
    except json.decoder.JSONDecodeError:
        logger.exception("Issue on decoding")
        raise
