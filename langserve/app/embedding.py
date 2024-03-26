from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter


def load_split_documents(repo_path:str, file_extensions:list[str], exclude_files:list[str]=[]):
    """Splits all text files (of given extension) into chunks to calculate embeddings"""
    def load_documents(repo_path:str, file_extensions:list[str], exclude_files:list[str]=[]):
    
        loader = GenericLoader.from_filesystem(
            repo_path,
            glob="**/*",
            suffixes=file_extensions,
            exclude=exclude_files,
            parser=LanguageParser(language=Language.CSHARP, parser_threshold=500),
        )
        documents = loader.load()
        print(f' ** loaded files:  {len(documents)}')
        return documents

    # HINT: split code files to some arbitrary size. Use overlap
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.CSHARP, chunk_size=2000, chunk_overlap=200
    )
    documents = load_documents(repo_path, file_extensions)
    texts = python_splitter.split_documents(documents)
    print(f' ** loaded documents: {len(documents)}; splitted into code files:  {len(texts)}')
    return texts

    
def load_or_create_embeddings(embedding_model, persist_directory:str, repository_path:str, file_extensions:list[str]) -> Chroma:
    # HINT: try loading existing embeddings from ChromaDB
    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )

    if db._collection.count() > 0:
        print(f"Embeddings' database was already initializede: {persist_directory}")
    else:
        # when collection's empty, re-create it
        print(f"Embeddings' database is empty - restoring")
        texts = load_split_documents(repository_path, file_extensions)
        db = Chroma.from_documents(
            documents=texts, 
            embedding=embedding_model,
            persist_directory=persist_directory
        )
        db.persist()
    
    return db