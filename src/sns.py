import boto3


TOPIC_NAME = 'MySubscriptionTopic'


def sns_client():
    boto3.setup_default_session(profile_name='perso')
    sns = boto3.client('sns', region_name='eu-west-3')
    """ :type : pyboto3.sns """
    return sns


def create_topic():
    sns_client().create_topic(
        Name=TOPIC_NAME
    )


if __name__ == '__main__':
    print(create_topic())
