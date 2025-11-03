from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from scipy.spatial.distance import cosine
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# OpenAI埋め込みモデルを設定
embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# 文書データの設定
documents = [
    Document(page_content="今日は天気が良いですね。公園に行きますか？"),
    Document(page_content="AI技術は近年急速に発展しています。"),
    Document(page_content="コーヒーはとても人気があります。"),
    Document(page_content="pythonはとても便利だ"),
]

# Chromaデータベースを作成
db = Chroma.from_documents(documents=documents, embedding=embeddings_model)

query = "AIの発展について教えて"

query_embedding = embeddings_model.embed_query(query)

result = db.similarity_search_by_vector(query_embedding)

for doc in result:
    doc_embedding = embeddings_model.embed_query(doc.page_content)
    similarity = 1 - cosine(query_embedding, doc_embedding)
    print(f"類似度({doc.page_content}):{similarity}") 
