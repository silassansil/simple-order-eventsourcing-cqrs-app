import json

from service.summary_service import SummaryService
from utils import logger_util

logging = logger_util.logger('monthly_summary_generate')
summary_service = SummaryService()


def lambda_handler(event, context):
    logging.info('starting monthly summary generate process...')
    logging.info(f'message received {event}')

    if event['Records'][0]['eventSource'] == 'aws:sqs':
        _body = json.loads(event['Records'][0]['body'])
        _message = json.loads(_body['Message'])

        summary_service.monthly_summary_generate(_message)
        return _message

    return None
