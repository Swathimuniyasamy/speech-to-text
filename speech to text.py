
 pip install ibm-watson
pip install python-dotenvfrom ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Replace with your API key and URL
api_key = "sQUzQK5PCKeIlLi4U3Qdmp7rHOVS85S_K3ekn4n_3ypA"
url = "https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/099c6131-ed84-45a0-9dda-c7fe00860c3e"

# Set up authenticator and Speech to Text service
authenticator = IAMAuthenticator(api_key)
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url(url)

# Function to convert audio file to text
def transcribe_audio(audio_file_path):
    try:
        with open(audio_file_path, 'rb') as audio_file:
            response = speech_to_text.recognize(
                audio=audio_file,
                content_type='audio/mpeg',  # Ensure this matches your file format
                model='en-US_BroadbandModel'
            ).get_result()
            
            # Check if there are results and alternatives in the response
            if response['results'] and response['results'][0]['alternatives']:
                transcript = response['results'][0]['alternatives'][0]['transcript']
                return transcript
            else:
                return "No speech detected or empty response."

    except Exception as e:
        print("Error transcribing audio:", e)
        return None

# Example usage
audio_file_path ='gd.mp3.mp3'  # File path after uploading

transcript = transcribe_audio(audio_file_path)
print("Transcript:", transcript)