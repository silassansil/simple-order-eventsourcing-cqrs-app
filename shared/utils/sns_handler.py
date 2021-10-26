import json
import os

import boto3

from utils import encoder_util


class SNSHandler:
    _region = os.environ.get('REGION', 'sa-east-1')
    _sns = boto3.client(
        "sns",
        region_name=_region
    )

    _ssm = boto3.client(
        'ssm',
        region_name=_region
    )

    def publish(self, _data):
        _topic_arn = self._ssm.get_parameter(
            Name='/order/new-order-topic',
            WithDecryption=True
        )
        self._sns.publish(
            TopicArn=_topic_arn['Parameter']['Value'],
            Message=json.dumps(_data, cls=encoder_util.DecimalEncoder)
        )
        return _data
