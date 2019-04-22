import boto3


TOPIC_NAME = 'MySubscriptionTopic'
TOPIC_ARN = 'arn:aws:sns:eu-west-3:724579132719:MySubscriptionTopic'


def sns_client():
    boto3.setup_default_session(profile_name='perso')
    sns = boto3.client('sns', region_name='eu-west-3')
    """ :type : pyboto3.sns """
    return sns


def create_topic():
    sns_client().create_topic(
        Name=TOPIC_NAME
    )


def get_topics():
    return sns_client().list_topics()


def get_topic_attributes(topic_arn):
    return sns_client().get_topic_attributes(
        TopicArn=topic_arn
    )


if __name__ == '__main__':
    # print(create_topic())
    # print(get_topics())
    print(get_topic_attributes(TOPIC_ARN))
