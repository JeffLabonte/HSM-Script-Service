from service.base_service import BaseService


class MessagingController:
    TOPIC_TO_CONSUME = "script.#"

    def __init__(self, messaging_service: BaseService):
        self.messaging_service = messaging_service
