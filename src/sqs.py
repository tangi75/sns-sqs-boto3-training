import boto3
import json


QUEUE_NAME = 'MyTest-SQS-Queue'
QUEUE_NAME_URL = 'https://eu-west-3.queue.amazonaws.com/969616207414/MyTest-SQS-Queue'
FIFO_QUEUE_NAME = 'MyTestQueue.fifo'
FIFO_QUEUE_URL = 'https://eu-west-3.queue.amazonaws.com/724579132719/MyTestQueue.fifo'
QUEUE_FOR_DEAD_LETTER = 'Dead-Letter-Queue-for-Main'
DEAD_LETTER_MAIN_QUEUE = 'Main-Queue'
MAIN_QUEUE_URL = 'https://sqs.eu-west-3.amazonaws.com/724579132719/Dead-Letter-Queue-for-Main'


def sqs_client():
    boto3.setup_default_session(profile_name='perso')
    sqs = boto3.client('sqs', region_name='eu-west-3')
    """ :type : pyboto3.sqs """
    return sqs

def create_sqs_queue():
    return sqs_client().create_queue(
        QueueName=QUEUE_NAME
    )

def create_fifo_queue():
    return sqs_client().create_queue(
        QueueName=FIFO_QUEUE_NAME,
        Attributes={
            'FifoQueue': 'true'
        }
    )

def create_queue_for_dead_letter():
    return sqs_client().create_queue(
        QueueName=QUEUE_FOR_DEAD_LETTER
    )

def create_dead_letter_queue():
    redrive_policy = {
        "deadLetterTargetArn": "arn:aws:sqs:eu-west-3:724579132719:Dead-Letter-Queue-for-Main",
        "maxReceiveCount": 3
    }
    return sqs_client().create_queue(
        QueueName=DEAD_LETTER_MAIN_QUEUE,
        Attributes={
            "DelaySeconds": "0",
            "MaximumMessageSize": "262144",
            "VisibilityTimeout": "30",
            "MessageRetentionPeriod": "345600",
            "ReceiveMessageWaitTimeSeconds": "0",
            "RedrivePolicy": json.dumps(redrive_policy)
        }
    )

def find_queue():
    return sqs_client().list_queues(
        QueueNamePrefix='MyTest'
    )

def list_queues():
    return sqs_client().list_queues()

def queue_attributes():
    return sqs_client().get_queue_attributes(
        QueueUrl= MAIN_QUEUE_URL,
        AttributeNames=['All']
    )

def update_queue_attributes():
    return sqs_client().set_queue_attributes(
        QueueUrl= MAIN_QUEUE_URL,
        Attributes={
            "MaximumMessageSize": "131072",
            "VisibilityTimeout": "15"
        }
    )

if __name__ == '__main__':
    #print(create_sqs_queue())
    # print(create_fifo_queue())
    # print(create_queue_for_dead_letter())
    # print(create_dead_letter_queue())
    # print(find_queue())
    # print(list_queues())
    # print(queue_attributes())
    print(update_queue_attributes())
