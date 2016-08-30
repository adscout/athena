import boto

class SQS:

    def __init__(self):

        region = boto.sqs.regioninfo.SQSRegionInfo(
          connection=None,
          name='fake_sqs',
          endpoint='localhost',
          connection_cls=boto.sqs.connection.SQSConnection,
        )

        conn = boto.sqs.connection.SQSConnection(
          aws_access_key_id='fake_key',
          aws_secret_access_key='fake_secret',
          is_secure=False,
          port=4568,  # or wherever fake_sqs is running
          region=region,
        )