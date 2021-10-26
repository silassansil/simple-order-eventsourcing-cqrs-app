import os
from datetime import datetime

from utils.dynamodb_handler import DynamoDBHandler


class SummaryService:
    _repository: DynamoDBHandler

    def daily_summary_generate(self, _data):
        self._repository = DynamoDBHandler(
            os.environ.get('TABLEDAILYSUMMARY', 'DailySummary')
        )
        return self._save_summary(_data, datetime.now().strftime("%d-%m-%Y"))

    def weekly_summary_generate(self, _data):
        self._repository = DynamoDBHandler(
            os.environ.get('TABLEWEEKLYSUMMARY', 'WeeklySummary')
        )
        year, week_num, _ = datetime.now().isocalendar()
        return self._save_summary(_data, f'{week_num}-{year}')

    def monthly_summary_generate(self, _data):
        self._repository = DynamoDBHandler(
            os.environ.get('TABLEMONTHLYSUMMARY', 'MonthlySummary')
        )
        return self._save_summary(_data, datetime.now().strftime("%m-%Y"))

    def _save_summary(self, _data, _key):
        _param = {
            **_data,
            'id': _key,
            'orderId': _data['id']
        }

        self._repository.save(_param)
        return _param
