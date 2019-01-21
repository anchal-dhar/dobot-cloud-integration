import boto3
#file = open('someFile.txt', 'r+')

#key = file.name
#bucket = 'test-s3-bucket-v1'

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
# TODO Change to relative path 
data = open('/Users/anchal/2019/aws/dobot-cloud-integration/scripts/sampleImages/jelly.png', 'rb')
s3.Bucket(bucket.name).put_object(Key='jelly2.jpg', Body=data)