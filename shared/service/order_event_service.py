import time
import uuid

from utils.sns_handler import SNSHandler


class OrderEventService:

    def __init__(self):
        self._sns = SNSHandler()

    def publish_order(self, _items_complete, _total_items, _order):
        return self._sns.publish({
            'id': str(uuid.uuid4()),
            'timestamp': int(round(time.time() * 1000)),
            'items': _items_complete,
            'labor': _order['labor'],
            'discount': _order['discount'],
            'totalItems': _total_items
        })
