import requests,json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    request = requests.post(url = url, headers = headers, json = data)
    req_json = json.loads(request.text)
    anger_score = req_json["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = req_json["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = req_json["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = req_json["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = req_json["emotionPredictions"][0]["emotion"]["sadness"]
    emo_list=[anger_score,disgust_score,fear_score,joy_score,sadness_score]
    dominant_emotion = max(enumerate(emo_list), key=lambda x: x[1])[0]
    dom_emo_name = ["anger","disgust","fear","joy","sadness"][dominant_emotion]
    return {"anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion":  dom_emo_name
            }