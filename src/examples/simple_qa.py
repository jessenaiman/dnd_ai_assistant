from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def answer_question(question, corpus):
    """
    A simplified example of question answering using TF-IDF. 

    Args:
        question (str): The user's question.
        corpus (list): A list of text passages (e.g., rules sections).

    Returns:
        str: The most relevant text passage from the corpus.
    """
    vectorizer = TfidfVectorizer()
    corpus_vectors = vectorizer.fit_transform(corpus)
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(question_vector, corpus_vectors)
    most_similar_index = similarities.argmax()
    return corpus[most_similar_index]

# Example Usage
corpus = [
    "A longsword is a versatile weapon.",
    "To hit, you must roll a 20-sided die and add your attack bonus.",
    "A critical hit occurs when you roll a natural 20."
]
user_question = "What is a critical hit?"
answer = answer_question(user_question, corpus)
print(f"Answer: {answer}")
