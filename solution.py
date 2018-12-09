import requests


def translate_it(source_file, target_file, source_lang, target_lang = 'ru'):

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    langs = f'{source_lang}-{target_lang}'

    with open(source_file) as text:

        params = {
            'key': key,
            'lang': langs,
            'text': text,
        }
        response = requests.post(url, params=params).json()
        translated_text = ' '.join(response.get('text', []))

    with open(target_file, 'w', encoding='utf8') as text:
        text.write(translated_text)


if __name__ == "__main__":
    translate_it('DE.txt', 'DE_tran.txt', 'de', 'en')
    translate_it('ES.txt', 'ES_tran.txt', 'es')
    translate_it('FR.txt', 'FR_tran.txt', 'fr', 'es')
