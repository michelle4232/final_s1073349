from google_trans_new import google_translator

def text_to_translate(text):
    translator = google_translator()
    translate_text = translator.translate(text, lang_tgt='zh-tw')
    return translate_text



