from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents= [
    "India is a country in South Asia.",
    "The capital of India is New Delhi.",
    "The currency of India is Indian Rupee."
]

vector= embedding.embed_documents(documents)

print(str(vector))
