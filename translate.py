import json
import requests
from flask import current_app
from flask_babel import _ 

# TODO: may be request languages are many
def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    
    headers = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Content-type': 'application/json'
    }
    content = [{'text': text}]
    if source_language == "":
        http_url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={}'.format(dest_language)
    else:
        http_url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(source_language,dest_language)
    
    request = requests.post(http_url, headers=headers, json=content)

    if request.status_code != 200:
        return _('Error: the translation service failed.')

    response = request.json()

    return response[0]['translations'][0]['text']
