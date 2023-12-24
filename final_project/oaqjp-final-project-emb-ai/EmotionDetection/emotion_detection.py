import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=myobj,headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code ==200:
        anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        var = ['anger','disgust','fear','joy','sadness']
        val = [anger,disgust,fear,joy,sadness]
        mydict = dict(zip(var,val))
        revdict = dict(zip(val,var))
        dominant_emotion = revdict.get((max([v for k,v in mydict.items()])))
        newvar = ['anger','disgust','fear','joy','sadness','dominant_emotion']
        newval = [anger,disgust,fear,joy,sadness,dominant_emotion]
        return dict(zip(newvar,newval))
    elif response.status_code == 500:
        return None