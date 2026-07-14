from django.conf import settings
from apps.documents.application.ports.services.message_query_provider_service import IMessageQueueProviderService
from typing import Any, Dict
import json
from apps.utils.infrastructure.services.base_boto import BaseBotoConfig

class SQSClient(IMessageQueueProviderService, BaseBotoConfig):
    def __init__(self):
        super().__init__()
        self.queue_urls: Dict[str, str] = {}

    def _get_url(self, queue_identifier: str) -> str:
        if queue_identifier not in self.queue_urls:
            self.queue_urls[queue_identifier] = self.client.get_queue_url(QueueName=queue_identifier)['QueueUrl']
        return self.queue_urls[queue_identifier]

    def send_task(self, queue_identifier: str, payload: Dict[str, Any], attributes: Dict[str, Any] | None = None, delay_seconds: int = 0, **kwargs) -> None:
        queue_url = self._get_url(queue_identifier)

        sqs_attributes = {}
        if attributes:
            for key, value in attributes.items():
                sqs_attributes[key] = {
                    'DataType': 'String',
                    'StringValue': str(value)
                }

        params = {
            'QueueUrl': queue_url,
            'MessageBody': json.dumps(payload),
            'DelaySeconds': delay_seconds
        }

        if 'message_group_id' in kwargs:
            params['MessageGroupId'] = kwargs['message_group_id']
        if 'message_deduplication_id' in kwargs:
            params['MessageDeduplicationId'] = kwargs['message_deduplication_id']

        if sqs_attributes:
            params['MessageAttributes'] = sqs_attributes

        response = self.client.send_message(**params)
        return response.get('MessageId', '')
