from langdetect import detect

texts = [
    "Šodien ir saulaina diena.",
    "Today is a very sunny day.",
    "Сегодня солнечный день."
]

for text in texts:
    language = detect(text)
    print(f"Teksts: '{text}' ir valodā: {language}")
