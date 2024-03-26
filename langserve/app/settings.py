from enum import Enum

from pydantic import Field, BaseModel, validator
from pydantic_settings import BaseSettings

from typing import Optional


class LLMProviders(str, Enum):
    AZURE = 'azure'
    OLLAMA = 'ollama'
    VERTEX_AI = 'vertexai'


class AzureSettings(BaseModel):
    azure_deployment: Optional[str] = Optional[Field(..., env="AZURE_DEPLOYMENT")]
    azure_api_version: Optional[str] = Optional[Field(..., env="AZURE_API_VERSION")]
    azure_embedding_deployment: Optional[str] = Optional[Field(..., env="AZURE_EMBEDDING_DEPLOYMENT")]
    azure_embedding_db_path: str = Field(..., env="AZURE_EMBEDDING_DB_PATH")


class VertexAiSettings(BaseModel):
    embedding_model: Optional[str] = Optional[Field(..., env="EMBEDDING_MODEL")]
    model: Optional[str] = Optional[Field(..., env="MODEL")]
    model_output_tokens: Optional[str] = Optional[Field(..., env="MODEL_OUTPUT_TOKENS")]
    embedding_db_path: str = Field(..., env="EMBEDDING_DB_PATH")


class AppSettings(BaseSettings):
    """Application settings (nested: see https://docs.pydantic.dev/1.10/usage/settings/)"""
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    openai_api_type: str = Field(..., env="OPENAI_API_TYPE") 
    openai_api_base: str = Field(..., env="OPENAI_API_BASE")
    openai_api_version: str = Field(..., env="OPENAI_API_VERSION")

    path_repository: str = Field(..., env="PATH_REPOSITORY")
    # path_embeddings: str = Field(..., env="PATH_EMBEDDINGS")

    file_types: list[str]
    llm_provider: LLMProviders = Field(..., env="LLM_PROVIDER")
    
    azure_settings: AzureSettings
    vertex_ai_settings: VertexAiSettings

    class Config:
        env_nested_delimiter = '__'
