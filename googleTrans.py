from googletrans import Translator

def text_to_translate(text,dest='en'):
    translator = Translator()
    result = translator.translate(text, dest).text
    return result



#if __name__ == '__main__':
 #   result = text_to_translate( text = "hello", dest = 'zh-tw' )
  #  print(result)

#輸出
#Tonight I want to order McDonald’s spicy chicken drumstick with French fries coke