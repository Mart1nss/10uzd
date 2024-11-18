from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

start_phrase = "Reiz kādā tālā zemē..."

story = generator(start_phrase, max_length=50, num_return_sequences=1)[0]['generated_text']

print("Īss stāsts:")
print(story)
