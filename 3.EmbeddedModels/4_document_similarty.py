from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv  

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", dimension=300,)

documents= [
    "India is a country in South Asia.",
    "The capital of India is New Delhi.",
    "The currency of India is Indian Rupee.",
    "The capital of France is Paris.",
    "The currency of France is Euro."
]

query = "What is the currency of france?"

doc_embbedings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embbedings)[0]

index, scores =sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print("Query: ", query)
print("Most similar document: ")
print(documents[index])

print("Similarity Score: ", np.round(scores, 2))