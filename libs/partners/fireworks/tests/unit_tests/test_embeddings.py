"""Test embedding model integration."""

from langchain_fireworks.embeddings import FireworksEmbeddings

from langchain_standard_tests.unit_tests import EmbeddingsUnitTests
from typing import Type

class TestOllamaEmbeddings(EmbeddingsUnitTests):
    @property
    def embeddings_class(self) -> Type[FireworksEmbeddings]:
        return FireworksEmbeddings

    @property
    def embedding_model_params(self) -> dict:
        return {"model": "nomic-ai/nomic-embed-text-v1.5"}
