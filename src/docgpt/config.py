from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "docGPT"
    ALLOWED_HOSTS: list = ["*"]
    DOCUMENT_STORE: str = "FAISS"
    LLM_MODEL: str = "meta.llama3-8b-instruct-v1:0"
    EMBEDDING_MODEL: str = "amazon.titan-embed-text-v2:0`"
    UPLOAD_DIR: str = "uploads"

    class Config:
        env_file = ".env"


settings = Settings()
