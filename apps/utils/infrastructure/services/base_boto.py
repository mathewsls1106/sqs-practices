from django.conf import settings
import boto3
from typing import Any

class BaseBotoConfig:
    def __init__(self):
        self.boto_config = {
            'region_name': settings.AWS_REGION_NAME,
            'aws_access_key_id': settings.AWS_ACCESS_KEY_ID,
            'aws_secret_access_key': settings.AWS_SECRET_ACCESS_KEY,
        }

        if settings.AWS_ENDPOINT_URL:
            self.boto_config['endpoint_url'] = settings.AWS_ENDPOINT_URL

    def get_client(self, service_name: str) -> Any:
        return boto3.client(service_name, **self.boto_config)
