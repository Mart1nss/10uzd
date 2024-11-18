from transformers import BertTokenizer, BertModel
import torch
from scipy.spatial.distance import cosine

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained('bert-base-multilingual-cased')

def get_word_vector(word):
    inputs = tokenizer(word, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    word_vector = outputs.last_hidden_state.mean(dim=1).squeeze()
    return word_vector

words = ["māja", "dzīvoklis", "jūra"]

vectors = {word: get_word_vector(word) for word in words}

similarities = {}
for word1 in words:
    for word2 in words:
        if word1 != word2:
            sim = 1 - cosine(vectors[word1].numpy(), vectors[word2].numpy()) 
            similarities[(word1, word2)] = sim

for pair, similarity in similarities.items():
    print(f"Līdzība starp '{pair[0]}' un '{pair[1]}': {similarity:.4f}")
