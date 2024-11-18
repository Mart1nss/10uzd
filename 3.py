text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

set1 = set(text1.lower().replace(".", "").split())
set2 = set(text2.lower().replace(".", "").split())

common_words = set1 & set2
similarity = len(common_words) / len(set1 | set2) * 100

print(f"Sakritīgie vārdi: {common_words}")
print(f"Sakritības līmenis: {similarity:.2f}%")
