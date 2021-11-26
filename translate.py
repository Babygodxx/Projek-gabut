from googletrans import Translator
Translator = Translator()
Translation = Translator.translate("aku sangat benci paddamu anjing", dest = 'zh-cn')
print(Translation.text)