from langchain_core.language_models.llms import BaseLLM
from langchain_core.embeddings import Embeddings

from app.settings import AzureSettings, VertexAiSettings


class LLMFactory:
    

    @classmethod
    def from_vertex_settings(settings: VertexAiSettings) -> tuple[BaseLLM, Embeddings, str]:
        from langchain_google_vertexai import VertexAIEmbeddings
        from langchain_google_vertexai import VertexAI

        llm = VertexAI(
            model_name=settings.model, 
            max_output_tokens=settings.model_output_tokens, 
            temperature=0.2)
        
        embedding_model = VertexAIEmbeddings(
            model_name=settings.embedding_model)

        embedding_path = settings.embedding_db_path

        return llm, embedding_model, embedding_path


    def from_azure_settings(settings: AzureSettings) -> tuple[BaseLLM, Embeddings, str]:
        from langchain_community.embeddings import AzureOpenAIEmbeddings
        from langchain.chat_models.azure_openai import AzureChatOpenAI
        
        llm = AzureChatOpenAI(
            deployment_name=settings.azure_deployment,
            openai_api_version=settings.azure_api_version,
        )

        embedding_model = AzureOpenAIEmbeddings(
            azure_deployment=settings.azure_embedding_deployment,
        )

        embedding_path = settings.azure_embedding_db_path

        return llm, embedding_model, embedding_path
