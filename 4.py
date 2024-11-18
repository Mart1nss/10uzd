from textblob import TextBlob
from googletrans import Translator

translator = Translator()

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

for sentence in sentences:
    translated = translator.translate(sentence, src='lv', dest='en').text
    blob = TextBlob(translated)
    sentiment = "pozitīvs" if blob.sentiment.polarity > 0 else "negatīvs" if blob.sentiment.polarity < 0 else "neitrāls"
    print(f"Teikums: '{sentence}' (tulkots: '{translated}') ir {sentiment}")

