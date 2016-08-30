import boto.sqs
import boto.sqs.connection
import logging

class SQS:

    def __init__(self, key, secret, host, port):

        region = boto.sqs.regioninfo.SQSRegionInfo(
          connection=None,
          name='athena',
          endpoint=host,
          connection_cls=boto.sqs.connection.SQSConnection,
        )

        conn = boto.sqs.connection.SQSConnection(
          aws_access_key_id=key,
          aws_secret_access_key=secret,
          is_secure=False,
          port=4568,
          region=region,
        )