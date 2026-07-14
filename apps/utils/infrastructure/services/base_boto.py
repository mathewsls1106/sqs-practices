from django.conf import settings
import boto3
from typing import Any, Dict
import json

class BaseBotoConfig:
    def __init__(self):
        self.boto_config = {
            'service_name': 'sqs',
            'region_name': settings.AWS_REGION,
            'aws_access_key_id': settings.AWS_ACCESS_KEY_ID,
            'aws_secret_access_key': settings.AWS_SECRET_ACCESS_KEY,
        }

        if settings.AWS_ENDPOINT_URL:
            self.boto_config['endpoint_url'] = settings.AWS_ENDPOINT_URL

        self.client = boto3.client(**self.boto_config)
