import boto3

BUCKET = "test-s3-bucket-v1"
KEY = "pencil.png"

def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="eu-west-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']


for label in detect_labels(BUCKET, KEY):
	print("The label is",label)
