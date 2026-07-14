
from abc import ABC, abstractmethod
from typing import Any, Dict


class IMessageQueueProviderService(ABC):
    @abstractmethod
    def send_task(self, queue_identifier: str, payload: Dict[str, Any], attributes: Dict[str, Any] | None = None, delay_seconds: int = 0, **kwargs) -> None:
        """
        Sends a task to the specified queue.

        :param queue_identifier: The identifier of the queue to send the task to.
        :param payload: The payload of the task to send.
        :param attributes: Optional attributes for the task.
        :param delay_seconds: Optional delay in seconds before the task is sent.
        """
