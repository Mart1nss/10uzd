from googletrans import Translator

translator = Translator()

texts_lv = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translations = [translator.translate(text, src='lv', dest='en').text for text in texts_lv]

for i, translation in enumerate(translations):
    print(f"Latviski: {texts_lv[i]}")
    print(f"Angliski: {translation}")
    print()
