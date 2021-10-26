import json

from service.product_service import ProductService
from utils import response_util, logger_util

logging = logger_util.logger('product_create')
service = ProductService()


def lambda_handler(event, context):
    logging.info('starting product registration process...')
    logging.info(f'message received {event}')

    _product = json.loads(event['body'])
    _response = service.save_product(_product)

    logging.info(f'product save with success ... {_response}')

    return response_util.created(_response)
