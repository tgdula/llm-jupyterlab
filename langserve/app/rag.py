from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationSummaryMemory

from app.embedding import load_or_create_embeddings
from app.llm import LLMFactory
from app.settings import AppSettings, LLMProviders


# HINT: some langchain issues to be cleant later - for now, just ignore
import warnings
warnings.filterwarnings('ignore')

settings = AppSettings()

repository_path = settings.path_repository
file_extensions = settings.file_types

llm, embedding_model, embedding_path = None, None, None

if settings.llm_provider == LLMProviders.AZURE:
    llm, embedding_model, embedding_path = LLMFactory.from_azure_settings(settings.azure_settings)

elif settings.llm_provider == LLMProviders.VERTEX_AI:
    llm, embedding_model, embedding_path = LLMFactory.from_vertex_settings(settings.vertex_ai_settings)
    
else:
    raise ValueError(f"Unsupported settings provider: {settings.llm_provider}")

    
db = load_or_create_embeddings(
    embedding_model=embedding_model,
    persist_directory=embedding_path, 
    repository_path=repository_path,
    file_extensions=file_extensions,
    )

retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 8},
)

print(f' ** db collection counts:  {db._collection.count()}')

memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)