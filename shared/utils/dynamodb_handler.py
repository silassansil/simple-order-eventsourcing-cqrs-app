import os

import boto3
from boto3.dynamodb.conditions import Key


class DynamoDBHandler:
    _table_name: str
    _dynamodb: any

    def __init__(self, _table_name):
        self._table_name = _table_name
        self._dynamodb = boto3.resource(
            'dynamodb',
            region_name=os.environ.get('REGION', 'sa-east-1')
        )

    def save(self, _data):
        _table = self._dynamodb.Table(self._table_name)
        return _table.put_item(
            TableName=self._table_name,
            Item=_data
        )

    def find_by_id(self, _id, _key_name):
        _table = self._dynamodb.Table(self._table_name)
        return _table.query(
            KeyConditionExpression=Key(_key_name).eq(_id)
        )['Items']
