from transformers import pipeline

ner = pipeline("ner", model="51la5/roberta-large-NER", tokenizer="51la5/roberta-large-NER", grouped_entities=True)

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

results = ner(text)

print("Identificētās vienības:")
for result in results:
    word = result["word"].replace("▁", "").replace("##", "").strip()
    print(f"Teksts: {word}, Vienība: {result['entity_group']}, Skala: {result['score']:.2f}")
