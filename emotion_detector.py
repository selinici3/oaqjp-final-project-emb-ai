import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Replace 'YOUR_API_KEY' and 'YOUR_URL' with your Watson NLU credentials
authenticator = IAMAuthenticator('YOUR_API_KEY')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('YOUR_URL')

def detect_emotion(text):
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    return json.dumps(response, indent=2)

if __name__ == "__main__":
    text_to_analyze = "I am so happy today!"
    print(detect_emotion(text_to_analyze))
