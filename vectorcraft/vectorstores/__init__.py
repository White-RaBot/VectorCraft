"""**Vector store** stores embedded data and performs vector search.

One of the most common ways to store and search over unstructured data is to
embed it and store the resulting embedding vectors, and then query the store
and retrieve the data that are 'most similar' to the embedded query.

**Class hierarchy:**

.. code-block::

    VectorStore --> <name>  # Examples: Annoy, FAISS, Milvus

    BaseRetriever --> VectorStoreRetriever --> <name>Retriever  # Example: VespaRetriever

**Main helpers:**

.. code-block::

    Embeddings, Document
"""  # noqa: E501

import importlib
from typing import Any

_module_lookup = {
    "AlibabaCloudOpenSearch": "vectorcraft.vectorstores.alibabacloud_opensearch",  # noqa: E501
    "AlibabaCloudOpenSearchSettings": "vectorcraft.vectorstores.alibabacloud_opensearch",  # noqa: E501
    "AnalyticDB": "vectorcraft.vectorstores.analyticdb",
    "Annoy": "vectorcraft.vectorstores.annoy",
    "ApacheDoris": "vectorcraft.vectorstores.apache_doris",
    "AstraDB": "vectorcraft.vectorstores.astradb",
    "AtlasDB": "vectorcraft.vectorstores.atlas",
    "AwaDB": "vectorcraft.vectorstores.awadb",
    "AzureCosmosDBVectorSearch": "vectorcraft.vectorstores.azure_cosmos_db",
    "AzureSearch": "vectorcraft.vectorstores.azuresearch",
    "BaiduVectorDB": "vectorcraft.vectorstores.baiduvectordb",
    "BESVectorStore": "vectorcraft.vectorstores.baiducloud_vector_search",
    "Bagel": "vectorcraft.vectorstores.bageldb",
    "BigQueryVectorSearch": "vectorcraft.vectorstores.bigquery_vector_search",
    "Cassandra": "vectorcraft.vectorstores.cassandra",
    "Chroma": "vectorcraft.vectorstores.chroma",
    "Clarifai": "vectorcraft.vectorstores.clarifai",
    "Clickhouse": "vectorcraft.vectorstores.clickhouse",
    "ClickhouseSettings": "vectorcraft.vectorstores.clickhouse",
    "DashVector": "vectorcraft.vectorstores.dashvector",
    "DatabricksVectorSearch": "vectorcraft.vectorstores.databricks_vector_search",  # noqa: E501
    "DeepLake": "vectorcraft.vectorstores.deeplake",
    "Dingo": "vectorcraft.vectorstores.dingo",
    "DistanceStrategy": "vectorcraft.vectorstores.kinetica",
    "DocArrayHnswSearch": "vectorcraft.vectorstores.docarray",
    "DocArrayInMemorySearch": "vectorcraft.vectorstores.docarray",
    "DocumentDBVectorSearch": "vectorcraft.vectorstores.documentdb",
    "ElasticKnnSearch": "vectorcraft.vectorstores.elastic_vector_search",
    "ElasticVectorSearch": "vectorcraft.vectorstores.elastic_vector_search",
    "ElasticsearchStore": "vectorcraft.vectorstores.elasticsearch",
    "Epsilla": "vectorcraft.vectorstores.epsilla",
    "FAISS": "vectorcraft.vectorstores.faiss",
    "HanaDB": "vectorcraft.vectorstores.hanavector",
    "Hologres": "vectorcraft.vectorstores.hologres",
    "InfinispanVS": "vectorcraft.vectorstores.infinispanvs",
    "KDBAI": "vectorcraft.vectorstores.kdbai",
    "Kinetica": "vectorcraft.vectorstores.kinetica",
    "KineticaSettings": "vectorcraft.vectorstores.kinetica",
    "LLMRails": "vectorcraft.vectorstores.llm_rails",
    "LanceDB": "vectorcraft.vectorstores.lancedb",
    "Lantern": "vectorcraft.vectorstores.lantern",
    "Marqo": "vectorcraft.vectorstores.marqo",
    "MatchingEngine": "vectorcraft.vectorstores.matching_engine",
    "Meilisearch": "vectorcraft.vectorstores.meilisearch",
    "Milvus": "vectorcraft.vectorstores.milvus",
    "MomentoVectorIndex": "vectorcraft.vectorstores.momento_vector_index",
    "MongoDBAtlasVectorSearch": "vectorcraft.vectorstores.mongodb_atlas",
    "MyScale": "vectorcraft.vectorstores.myscale",
    "MyScaleSettings": "vectorcraft.vectorstores.myscale",
    "Neo4jVector": "vectorcraft.vectorstores.neo4j_vector",
    "NeuralDBVectorStore": "vectorcraft.vectorstores.thirdai_neuraldb",
    "OpenSearchVectorSearch": "vectorcraft.vectorstores.opensearch_vector_search",  # noqa: E501
    "PGEmbedding": "vectorcraft.vectorstores.pgembedding",
    "PGVector": "vectorcraft.vectorstores.pgvector",
    "Pinecone": "vectorcraft.vectorstores.pinecone",
    "Qdrant": "vectorcraft.vectorstores.qdrant",
    "Redis": "vectorcraft.vectorstores.redis",
    "Rockset": "vectorcraft.vectorstores.rocksetdb",
    "SKLearnVectorStore": "vectorcraft.vectorstores.sklearn",
    "SQLiteVSS": "vectorcraft.vectorstores.sqlitevss",
    "ScaNN": "vectorcraft.vectorstores.scann",
    "SemaDB": "vectorcraft.vectorstores.semadb",
    "SingleStoreDB": "vectorcraft.vectorstores.singlestoredb",
    "StarRocks": "vectorcraft.vectorstores.starrocks",
    "SupabaseVectorStore": "vectorcraft.vectorstores.supabase",
    "SurrealDBStore": "vectorcraft.vectorstores.surrealdb",
    "Tair": "vectorcraft.vectorstores.tair",
    "TencentVectorDB": "vectorcraft.vectorstores.tencentvectordb",
    "TiDBVectorStore": "vectorcraft.vectorstores.tidb_vector",
    "Tigris": "vectorcraft.vectorstores.tigris",
    "TileDB": "vectorcraft.vectorstores.tiledb",
    "TimescaleVector": "vectorcraft.vectorstores.timescalevector",
    "Typesense": "vectorcraft.vectorstores.typesense",
    "USearch": "vectorcraft.vectorstores.usearch",
    "Vald": "vectorcraft.vectorstores.vald",
    "Vearch": "vectorcraft.vectorstores.vearch",
    "Vectara": "vectorcraft.vectorstores.vectara",
    "VectorStore": "langchain_core.vectorstores",
    "VespaStore": "vectorcraft.vectorstores.vespa",
    "Weaviate": "vectorcraft.vectorstores.weaviate",
    "Yellowbrick": "vectorcraft.vectorstores.yellowbrick",
    "ZepVectorStore": "vectorcraft.vectorstores.zep",
    "Zilliz": "vectorcraft.vectorstores.zilliz",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
