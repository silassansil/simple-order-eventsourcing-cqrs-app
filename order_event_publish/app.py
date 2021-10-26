import json

from service.order_event_service import OrderEventService
from service.product_service import ProductService
from utils import response_util, logger_util

logging = logger_util.logger('order_event_publish')


def lambda_handler(event, context):
    logging.info('starting order event registration process...')
    logging.info(f'event received {event}')

    _order = json.loads(event['body'])

    _items = _order['items']
    if not _items:
        return response_util.bad_request('items should not be empty')

    _items_complete = [_find_product(_item) for _item in _items]
    _total_items = _calculate_total_items(_items_complete)

    _response = OrderEventService().publish_order(
        _items_complete, _total_items, _order
    )
    logging.info(f'order event save with success ... {_response}')

    return response_util.created(_response)


def _find_product(_item):
    _product = ProductService().find_product_by_id(_item['productId'])[0]
    return {
        'productId': _item['productId'],
        'productName': _product['name'],
        'salesPrice': _product['salesPrice'],
        'amount': int(_item['amount']),
    }


def _calculate_total_items(_items):
    return sum(
        map(lambda i: i['amount'] * i['salesPrice'], _items)
    )
