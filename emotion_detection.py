
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": I love this new technology. } }
import json

# Example: Converting a dictionary to a JSON string
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert dictionary to JSON string
json_string = json.dumps(data)
print(json_string)

# Example: Converting a JSON string to a dictionary
json_data = '{"name": "Jane Doe", "age": 25, "city": "Los Angeles"}'
data_dict = json.loads(json_data)
print(data_dict)
{
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': '<name of the dominant emotion>'
}
