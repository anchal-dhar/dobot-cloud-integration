import boto3 
import os
import project_constants


def send_voice_cmd_to_lex_bot(recorded_cmd_file_name,lex):
    recording = open(recorded_cmd_file_name, 'rb')
    response = lex.post_content(botName=project_constants.botName,
        botAlias=project_constants.botAlias, userId=project_constants.userId,
        contentType='audio/l16; rate=16000; channels=1',
        accept='text/plain; charset=utf-8',
        inputStream=recording)
    print(response)

    # Check if it is fulfilled
    if response["dialogState"] != "Fulfilled":
        os.system('say "{0}"'.format(response["message"]))
        return 'Not matched'
    response_msg = response["slots"]["Item"]
    print(response_msg)

    return response_msg

