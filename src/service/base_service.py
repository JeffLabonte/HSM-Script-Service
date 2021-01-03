from abc import ABC

from typing import Dict


class BaseService(ABC):
    def publish(self, topic: str, message: Dict) -> None:
        raise NotImplementedError("Please implement this method")
