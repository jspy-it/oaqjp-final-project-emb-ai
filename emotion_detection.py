import requests
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    response = requests.post(url, json = { "raw_document": { "text": text_to_analyze } }, headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"})
    return response.text