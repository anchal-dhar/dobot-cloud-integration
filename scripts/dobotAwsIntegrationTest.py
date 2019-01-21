# Exercise 4
# In this exercise, we will:
# - Connect to the lext bot using python script
# - Send a user message in text form
# - Use respone to control robot arm movement


import boto3
import time
from glob import glob
from dobotBindings.dobot import Dobot


# Connect to the dobot arm
available_ports = glob('/dev/cu*usb*')

if len(available_ports) == 0:
	print('***no port found for the arm***')
	exit()

print("Port found {0}...".format(available_ports[0]))

device = Dobot(port=available_ports[0])

# Run test routine
device.go_angle(0,0,45)
time.sleep(2)      
device.go_angle(0,45,0)


# Preplanned routine for Dobot
def run_routine():
    device.go_angle(0,30,0)
    time.sleep(2)

    device.go_angle(7,55,37)
    time.sleep(1)
    device.suck(True)
    time.sleep(2)

    device.go_angle(0,30,0)
    time.sleep(2)


    device.go_angle(77,27,3)
    time.sleep(2)
    device.go_angle(82,46,31)
    time.sleep(2)
    device.suck(False)
    time.sleep(1)
    device.go_angle(0,30,0)

# Set client to lex
client = boto3.client('lex-runtime')
# check https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#paginators

user_cmd_msg = "Move arm"

#response = client.post_text(    # send message in text format
#    botName='OxfordTutorial',   # Give the name of the publish bot
#   botAlias='oxford_robot',    # Gibe the alias name of the publish bot
#   userId='Oxford123456',      # Give an user ID to this applcation.     
#   inputText= user_cmd_msg     # Input the user message
#)


response = client.post_text(    # send message in text format
    botName='DobotControl',   # Give the name of the publish bot
    botAlias='test_bot',    # Gibe the alias name of the publish bot
    userId='Oxford123',      # Give an user ID to this applcation.
    inputText= user_cmd_msg     # Input the user message
)

# Print only the relevent part of the response
response_msg = response["message"]
print(response_msg)

# If response is "5", then move arm
if response_msg == "5":
    print("Running pre planned routine")
    run_routine()


