from google_trans_new import google_translator

def text_to_translate(text):
    tran = ''
    for txt in text:
        tran += txt + ''

    translator = google_translator()
    translate_text = translator.translate(tran, lang_tgt='zh-tw')
    return translate_text



