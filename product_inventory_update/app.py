import json

from service.product_service import ProductService
from utils import logger_util

logging = logger_util.logger('product_inventory_update')
service = ProductService()


def lambda_handler(event, context):
    logging.info('starting product inventory update process...')
    logging.info(f'message received {event}')

    if event['Records'][0]['eventSource'] == 'aws:sqs':
        _body = json.loads(event['Records'][0]['body'])
        _message = json.loads(_body['Message'])

        for item in _message['items']:
            service.update_inventory(item['productId'], item['amount'])
        return _message

    return None
