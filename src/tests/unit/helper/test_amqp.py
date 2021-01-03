from helper.amqp import get_payload_from_body


def test_get_payload_from_body__pass_json__should_return_dict():
    body = b"{\"test\": 1}"
    json_dict = get_payload_from_body(body)

    assert isinstance(json_dict, dict)
    assert json_dict.get("test") == 1
