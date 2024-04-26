import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv

load_dotenv()

def speech_to_text_continuous(audio_file):
    # Replace with your own subscription key and region
    endpoint = os.getenv("SPEECH_SERVICE_ENDPOINT")
    subscription_key = os.getenv("SPEECH_SERVICE_API_KEY")
    region = os.getenv("SPEECH_SERVICE_REGION")

    # Replace 'output_text.txt' with the path where you want to save the transcribed text
    output_file = os.path.splitext(audio_file)[0] + ".txt"

    # Initialize the speech recognizer
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    audio_input = speechsdk.AudioConfig(filename=audio_file)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    # Enable continuous recognition
    done = False

    def handle_final_result(evt):
        nonlocal done
        result = evt.result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            with open(output_file, "a") as file:
                file.write(result.text + "\n")
                return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
        if result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized")

    speech_recognizer.recognized.connect(handle_final_result)

    # Start continuous recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        pass
        
    # Stop continuous recognition
    speech_recognizer.stop_continuous_recognition()
    

# Replace 'audio_file.wav' with the path to your audio file
audio_file = "" #Enter path of the wav file here

speech_to_text_continuous(audio_file)
