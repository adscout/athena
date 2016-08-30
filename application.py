import logging
import sys
import argparse
from worker.sqs import SQS

logging.basicConfig(level=logging.DEBUG,  stream=sys.stdout, format="%(asctime)-15s %(levelname)-8s %(message)s")

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("--awsKey", help="aws key", required=True)
    parser.add_argument("--awsSecret", help="aws secret", required=True)
    parser.add_argument("--sqsHost", help="sqs hostname", default="localhost")
    parser.add_argument("--sqsPort", help="sqs port", default="4568")
    args = parser.parse_args()
    
    sqs = SQS(args.awsKey, args.awsSecret, args.sqsHost, args.sqsPort)