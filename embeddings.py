from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    Responsible for converting text chunks
    into vector embeddings.
    """

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def get_embedding_model(self):
        return self.embedding_model