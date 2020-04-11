import json
import base64
import boto3
import datetime
from credentials import ACCESS_ID, ACCESS_KEY
BUCKET_NAME = 'image-style-transfer-jingyu'

def lambda_handler(event, context):
    # safe to S3
    file_content = base64.b64decode(event['content'])
    file_path = event['name'] + str(datetime.datetime.now().timestamp())
    s3_client = boto3.client('s3',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=ACCESS_KEY)    
    try:
        s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        raise IOError(e)
    
    # create sqs message
    QueueName = 'sqs'
    # Send some SQS messages
    msg = send_sqs_message(QueueName,file_path)
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')


    return { 'statusCode': 200,
        'body': { 'file_path': file_path
            }
        }

def send_sqs_message(QueueName, msg_body):
    """

    :param sqs_queue_url: String URL of existing SQS queue
    :param msg_body: String message body
    :return: Dictionary containing information about the sent message. If
        error, returns None.
    """

    # Send the SQS message
    sqs_client = boto3.client('sqs',
        aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=ACCESS_KEY)
    sqs_queue_url = sqs_client.get_queue_url(
    QueueName=QueueName)['QueueUrl']
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=json.dumps(msg_body))
    except ClientError as e:
        logging.error(e)
        return None
    return msg