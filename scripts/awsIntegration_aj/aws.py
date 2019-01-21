import boto3
import project_constants
import lex_bot
import polly_bot
import rek_bot
import sound_recorder
import time
import subprocess
import dobot_routine

#session = boto3.Session(profile_name='default')

# Main Loop

#Instantiate lex service
lex =boto3.client('lex-runtime')
print("Please wait for voice recording to start..\n")
# Invoke record function from sound_recorder.py
sound_recorder.record(project_constants.name_audio_file)
print("Sending voice recording to AWS Lex bot..\n")
# Invoke send_cmd_to_lex_bot from lex_bot.py
lex_response_msg = lex_bot.send_voice_cmd_to_lex_bot(project_constants.name_audio_file,lex)
#lex_response_msg = lex_bot.send_text_cmd_to_lex_bot("Get Jelly",lex)
# Print response from the lex bot
print('Main function: ',lex_response_msg)
time.sleep(5)



#Polly text-to-speech
polly = boto3.client('polly')
polly_resp = polly_bot.send_cmd_to_polly_bot(lex_response_msg,polly)
with open(project_constants.polly_response_file, 'wb') as f:
  f.write(polly_resp['AudioStream'].read())        


#Play back response from Polly
return_code = subprocess.call(["afplay", project_constants.polly_response_file])

if lex_response_msg != 'Not matched':
# Rekognition detect text from image
    rek = boto3.client('rekognition')
    rek_resp_text = rek_bot.send_cmd_to_detect_text(rek)
    textDetections=rek_resp_text['TextDetections']
    print ('Detected text')
    match = False
    for text in textDetections:           
        print ('Detected text:' + text['DetectedText'])
        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        if match == False:
            if lex_response_msg.lower() in text['DetectedText'].lower():
                match = True                  

    if match == True:
      final_response = 'Text matched'
    else:
      final_response = 'Sorry Text not found'  
    print(final_response)
    #Polly text-to-speech
    polly1 = boto3.client('polly')
    polly_final_resp = polly_bot.send_cmd_to_polly_bot(final_response,polly1)
    with open(project_constants.polly_final_response_file, 'wb') as f:
      f.write(polly_final_resp['AudioStream'].read())   
    
    #Play back response from Polly
    return_code1 = subprocess.call(["afplay", project_constants.polly_final_response_file])
    

    dobot_routine.run_routine()