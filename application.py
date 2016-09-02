import sys
import argparse
from athena.model import DynamoDB
from athena.queue import SQS
from athena.worker import Worker

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("--awsKey", help="aws key", required=True)
    parser.add_argument("--awsSecret", help="aws secret", required=True)
    parser.add_argument("--sqsHost", help="sqs hostname", default="localhost")
    parser.add_argument("--sqsPort", help="sqs port", default="4568")
    args = parser.parse_args()
    
    sqs = SQS(args.awsKey, args.awsSecret, args.sqsHost, args.sqsPort)
    ddb = DynamoDB(args.awsKey, args.awsSecret, args.sqsHost, args.sqsPort)

    worker = Worker(sqs, ddb)
    worker.run()