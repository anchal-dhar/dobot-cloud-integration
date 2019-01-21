import boto3 
import project_constants

# Polly text-to-speech

def send_cmd_to_polly_bot(polly_text,polly):
    voice_dict = polly.describe_voices()
    voices = voice_dict['Voices']
    eng_voices = [v for v in voices if 'English' in v['LanguageName']]
    polly_resp = polly.synthesize_speech(OutputFormat ='mp3',
            Text = polly_text,
            VoiceId = eng_voices[0]['Id'])
    #print('\nvoices: ',voices)
    print('\npolly_resp: ',polly_resp)        
    return polly_resp        
    