import boto3


QUEUE_NAME = 'MyTest-SQS-Queue'
QUEUE_NAME_URL = 'https://eu-west-3.queue.amazonaws.com/969616207414/MyTest-SQS-Queue'
FIFO_QUEUE_NAME = 'MyTestQueue.fifo'


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

if __name__ == '__main__':
    #print(create_sqs_queue())
    print(create_fifo_queue())
