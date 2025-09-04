from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Initialize HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

# Wrap in LangChain Chat
model = ChatHuggingFace(llm=llm)

# Ask a question
result = model.invoke("Explain the theory of relativity in simple terms?")

print(result.content)
