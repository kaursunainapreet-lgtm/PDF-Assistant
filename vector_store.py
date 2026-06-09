from langchain_chroma import Chroma


class VectorStoreManager:
    """
    Responsible for creating and managing
    the Chroma vector database.
    """

    def __init__(self, persist_directory="vector_store"):
        self.persist_directory = persist_directory

    def create_vector_store(
        self,
        documents,
        embedding_model
    ):
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embedding_model,
            persist_directory=self.persist_directory
        )

        return vector_store