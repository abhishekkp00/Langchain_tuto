from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv  

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", dimension=30,)

documents= [
    "India is a country in South Asia.",
    "The capital of India is New Delhi.",
    "The currency of India is Indian Rupee."
]

result = embeddings.embed_documents(documents)
print(str(result))