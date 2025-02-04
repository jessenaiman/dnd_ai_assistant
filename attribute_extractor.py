import pandas as pd

# Define Q&A pairs
qa_pairs = [
    ("What are the six attributes in D&D?", 
     "The six attributes are Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma."),
    ("How do you roll ability scores in D&D?", 
     "Players roll 3d6 for each attribute. Some groups use the '4d6 drop the lowest' method.")
]

# Convert to DataFrame and save to CSV
df = pd.DataFrame(qa_pairs, columns=["question", "answer"])
df.to_csv("attribute_faq.csv", index=False)

print("Dataset saved to attribute_faq.csv")