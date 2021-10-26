import json

from service.summary_service import SummaryService
from utils import logger_util

summary_service = SummaryService()
logging = logger_util.logger('weekly_summary_generate')


def lambda_handler(event, context):
    logging.info('starting weekly summary generate process...')
    logging.info(f'message received {event}')

    if event['Records'][0]['eventSource'] == 'aws:sqs':
        _body = json.loads(event['Records'][0]['body'])
        _message = json.loads(_body['Message'])

        summary_service.weekly_summary_generate(_message)
        return _message

    return None
