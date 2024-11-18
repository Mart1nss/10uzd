from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
text = text.lower().replace(",", "").replace(".", "")
words = text.split()
word_counts = Counter(words)

print(word_counts)