import os
import time
import uuid

from utils.dynamodb_handler import DynamoDBHandler


class ProductService:
    _repository: DynamoDBHandler

    def __init__(self):
        self._repository = DynamoDBHandler(
            os.environ.get('TABLEPRODUCT', 'Product')
        )

    def save_product(self, _product):
        _params = {
            'id': str(uuid.uuid4()),
            'timestamp': int(round(time.time() * 1000)),

            'name': _product['name'],
            'inventory': _product['inventory'],
            'salesPrice': _product['salesPrice'],
            'purchasePrice': _product['purchasePrice'],
            'code': _product['code']
        }
        self._repository.save(_params)
        return _params

    def find_product_by_id(self, _product_id):
        return self._repository.find_by_id(_product_id, 'id')

    def update_inventory(self, _product_id, _amount):
        _product = self.find_product_by_id(_product_id)[0]
        _product['inventory'] = _product['inventory'] - _amount

        self._repository.save(_product)
