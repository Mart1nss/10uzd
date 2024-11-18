import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

cleaned_text = re.sub(r"@\s?|http\S+|[^a-zA-Zā-žĀ-Ž\s:\?]", "", text).strip().lower()

print(cleaned_text)

