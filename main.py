from transformers import pipeline

print("Loading GPT-2 model...")

generator = pipeline("text-generation", model="gpt2")

print("Model loaded successfully!\n")

prompts = [
    "Artificial Intelligence is",
    "The future of education will",
    "Technology helps humans by",
    "A student went to college and"
]

for i, prompt in enumerate(prompts, start=1):

    print("=" * 50)
    print(f"Input {i}: {prompt}")

    result = generator(
        prompt,
        max_length=50,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )

    print("\nGenerated Output:")
    print(result[0]["generated_text"])
    print()

print("Experiment completed successfully!")
