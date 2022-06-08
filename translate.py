def translate(word, lang):

    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    return translate_client.translate(word, target_language=lang)
