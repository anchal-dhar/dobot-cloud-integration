import soundrecorder as sr
import boto3
import time
from glob import glob
import os
from pydobot import Dobot
#from dobot import Dobot

def send_cmd_to_lex_bot(recorded_cmd_file_name):
    recording = open(recorded_cmd_file_name, 'rb')
    response = client.post_content(botName='ItemPicker',
        botAlias='itempicker', userId='boto3MainUser',
        contentType='audio/l16; rate=16000; channels=1',
        accept='text/plain; charset=utf-8',
        inputStream=recording)
    print(response)
    os.system('say "{0}"'.format(response["message"]))  

# Check if it is fulfilled
    if response["dialogState"] == "Fulfilled":
       print(response["slots"]["Item"])
       if response["slots"]["Item"] == "nuts":
         # Move dobot to the left
            device.speed(100)
            device.go(250.0, -85.0, -50.0)
            time.sleep(1)
            device.suck(True)
            time.sleep(2)
            device.go(250.0, 0.0, 0.0)
            time.sleep(1)
            device.suck(False)
       if response["slots"]["Item"] == "chocolate":
         # Move dobot to the right
            device.speed(100)
            device.go(250.0, 85.0, -50.0)
            time.sleep(1)
            device.suck(True)
            time.sleep(2)
            device.go(250.0, 0.0, 0.0)
            time.sleep(1)
            device.suck(False)
       return response["message"]
    return None 

available_ports = glob('/dev/cu*usb*')  # mask for OSX Dobot port

if len(available_ports) == 0:
    print('no port found for Dobot Magician')
    exit(1)

device = Dobot(port=available_ports[0])
#device.go(150.0, 0.0, 50.0)

client = boto3.client('lex-runtime')

# Get speech input
name_audio_file = "input.wav"
sr.record(name_audio_file)

print("Sending voice recording to AWS Lex bot..\n")
message = send_cmd_to_lex_bot(name_audio_file)
print(message)
device.close()

##user_cmd_msg = "get nuts"
##response = client.post_text(    # send message in text format
##    botName='ItemPicker',   # Give the name of the publish bot
##    botAlias='itempicker',    # Gibe the alias name of the publish bot
##    userId='boto3MainUser',      # Give an user ID to this applcation.     
##    inputText= user_cmd_msg     # Input the user message
##)
##print(response)
