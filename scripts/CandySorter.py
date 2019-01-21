# Exercise 3
# In this exercise, tasks completed will be :
# - Connect to the lext bot using python script
#   - Send a user message in text form , extract the object label
#   - Send a audio and test 
# - Review the repsone and discuss next steps


import logging
# plumbum is a library for providing cli capabilities to the program
from plumbum import cli
import boto3

class candySorter(cli.Application):
    verbose = cli.Flag(["-v", "--verbose"], help = "Enable verbose mode")
    test_phrase = cli.SwitchAttr(["-I", "Specify test phrase like 'dobot pickup jelly bean' , include the string in  quotes"],str)
   
    @cli.switch("--loglevel", int)
    def set_log_level(self, level):
        """Sets the log-level of the logger"""
        logging.root.setLevel(level)
        print("Loglevel:", level)
    
    @cli.switch("--extractlabel", str)
    def extractCandyLabelByUser(self, test_phrase):
        # TODO Call AWS bot and extract the label 
        print("The Test phrase is :", test_phrase)
        extracted_label = 'jelly'
        return extracted_label
    
    @cli.switch("--uploadimage", str)
    def uploadImage(self, str_path):
        # TODO Call the AWS rapi to upload image
        print("Inside upload image method")
        bucket = 'test-s3-bucket-v1'
        s3 = boto3.resource('s3')
        data = open(str_path, 'rb')
        s3.Bucket(bucket).put_object(Key='jelly3.jpg', Body=data)

    def extractItemLabelfromImage(self):
        # TODO Call AWS bot and extract the label 
        extracted_label_image = 'image'
        return extracted_label_image

   
    def main(self):
        print("Verbose:", self.verbose)
        extraced_label_from_user_phrase = candySorter.extractCandyLabelByUser(self, self.test_phrase) 
        print("The Extracted Candy Label by user is :", extraced_label_from_user_phrase)
        extraced_label_from_image = candySorter.extractItemLabelfromImage(self)
        print("The Extracted Candy Label by user is :", extraced_label_from_image)

if __name__ == "__main__":
    candySorter.run()