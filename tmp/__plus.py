import boto3
import logging
import datetime
import uuid

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def main():

    # S3
    s3 = boto3.resource('s3')
    now_s = datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
    key = 'test-folder/{0}-{1}.txt'.format(now_s, uuid.uuid4())
    s3.meta.client.put_object(Bucket='BucketName', Key=key, Body='test dayo')

    # log
    logger.info('test-log-dayo')



def application(env, start_response):
    main()
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World!"
