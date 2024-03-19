"""**Retriever** class returns Documents given a text **query**.

It is more general than a vector store. A retriever does not need to be able to
store documents, only to return (or retrieve) it. Vector stores can be used as
the backbone of a retriever, but there are other types of retrievers as well.

**Class hierarchy:**

.. code-block::

    BaseRetriever --> <name>Retriever  # Examples: ArxivRetriever, MergerRetriever

**Main helpers:**

.. code-block::

    Document, Serializable, Callbacks,
    CallbackManagerForRetrieverRun, AsyncCallbackManagerForRetrieverRun
"""

import importlib
from typing import Any

_module_lookup = {
    "AmazonKendraRetriever": "vectorcraft.retrievers.kendra",
    "AmazonKnowledgeBasesRetriever": "vectorcraft.retrievers.bedrock",
    "ArceeRetriever": "vectorcraft.retrievers.arcee",
    "ArxivRetriever": "vectorcraft.retrievers.arxiv",
    "AzureCognitiveSearchRetriever": "vectorcraft.retrievers.azure_cognitive_search",  # noqa: E501
    "BM25Retriever": "vectorcraft.retrievers.bm25",
    "BreebsRetriever": "vectorcraft.retrievers.breebs",
    "ChaindeskRetriever": "vectorcraft.retrievers.chaindesk",
    "ChatGPTPluginRetriever": "vectorcraft.retrievers.chatgpt_plugin_retriever",
    "CohereRagRetriever": "vectorcraft.retrievers.cohere_rag_retriever",
    "DocArrayRetriever": "vectorcraft.retrievers.docarray",
    "ElasticSearchBM25Retriever": "vectorcraft.retrievers.elastic_search_bm25",
    "EmbedchainRetriever": "vectorcraft.retrievers.embedchain",
    "GoogleCloudEnterpriseSearchRetriever": "vectorcraft.retrievers.google_vertex_ai_search",  # noqa: E501
    "GoogleDocumentAIWarehouseRetriever": "vectorcraft.retrievers.google_cloud_documentai_warehouse",  # noqa: E501
    "GoogleVertexAIMultiTurnSearchRetriever": "vectorcraft.retrievers.google_vertex_ai_search",  # noqa: E501
    "GoogleVertexAISearchRetriever": "vectorcraft.retrievers.google_vertex_ai_search",  # noqa: E501
    "KNNRetriever": "vectorcraft.retrievers.knn",
    "KayAiRetriever": "vectorcraft.retrievers.kay",
    "LlamaIndexGraphRetriever": "vectorcraft.retrievers.llama_index",
    "LlamaIndexRetriever": "vectorcraft.retrievers.llama_index",
    "MetalRetriever": "vectorcraft.retrievers.metal",
    "MilvusRetriever": "vectorcraft.retrievers.milvus",
    "OutlineRetriever": "vectorcraft.retrievers.outline",
    "PineconeHybridSearchRetriever": "vectorcraft.retrievers.pinecone_hybrid_search",  # noqa: E501
    "PubMedRetriever": "vectorcraft.retrievers.pubmed",
    "QdrantSparseVectorRetriever": "vectorcraft.retrievers.qdrant_sparse_vector_retriever",  # noqa: E501
    "RemoteLangChainRetriever": "vectorcraft.retrievers.remote_retriever",
    "SVMRetriever": "vectorcraft.retrievers.svm",
    "TFIDFRetriever": "vectorcraft.retrievers.tfidf",
    "TavilySearchAPIRetriever": "vectorcraft.retrievers.tavily_search_api",
    "VespaRetriever": "vectorcraft.retrievers.vespa_retriever",
    "WeaviateHybridSearchRetriever": "vectorcraft.retrievers.weaviate_hybrid_search",  # noqa: E501
    "WikipediaRetriever": "vectorcraft.retrievers.wikipedia",
    "YouRetriever": "vectorcraft.retrievers.you",
    "ZepRetriever": "vectorcraft.retrievers.zep",
    "ZillizRetriever": "vectorcraft.retrievers.zilliz",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
