import boto3 
import project_constants
import requests

# Rekognition image/computer-vision
def send_cmd_to_detect_text(rek):
    #img_resp = requests.get(img_url)
    #img_bytes = img_resp.content
    rek_resp=rek.detect_text(Image={'S3Object':{'Bucket':'dobot-bucket','Name':'jellybean.jpeg'}})                        
    return rek_resp                        


