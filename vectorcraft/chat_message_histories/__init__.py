"""**Chat message history** stores a history of the message interactions in a chat.


**Class hierarchy:**

.. code-block::

    BaseChatMessageHistory --> <name>ChatMessageHistory  # Examples: FileChatMessageHistory, PostgresChatMessageHistory

**Main helpers:**

.. code-block::

    AIMessage, HumanMessage, BaseMessage

"""  # noqa: E501

import importlib
from typing import Any

_module_lookup = {
    "AstraDBChatMessageHistory": "vectorcraft.chat_message_histories.astradb",
    "CassandraChatMessageHistory": "vectorcraft.chat_message_histories.cassandra",  # noqa: E501
    "ChatMessageHistory": "vectorcraft.chat_message_histories.in_memory",
    "CosmosDBChatMessageHistory": "vectorcraft.chat_message_histories.cosmos_db",  # noqa: E501
    "DynamoDBChatMessageHistory": "vectorcraft.chat_message_histories.dynamodb",
    "ElasticsearchChatMessageHistory": "vectorcraft.chat_message_histories.elasticsearch",  # noqa: E501
    "FileChatMessageHistory": "vectorcraft.chat_message_histories.file",
    "FirestoreChatMessageHistory": "vectorcraft.chat_message_histories.firestore",  # noqa: E501
    "MomentoChatMessageHistory": "vectorcraft.chat_message_histories.momento",
    "MongoDBChatMessageHistory": "vectorcraft.chat_message_histories.mongodb",
    "Neo4jChatMessageHistory": "vectorcraft.chat_message_histories.neo4j",
    "PostgresChatMessageHistory": "vectorcraft.chat_message_histories.postgres",
    "RedisChatMessageHistory": "vectorcraft.chat_message_histories.redis",
    "RocksetChatMessageHistory": "vectorcraft.chat_message_histories.rocksetdb",
    "SQLChatMessageHistory": "vectorcraft.chat_message_histories.sql",
    "SingleStoreDBChatMessageHistory": "vectorcraft.chat_message_histories.singlestoredb",  # noqa: E501
    "StreamlitChatMessageHistory": "vectorcraft.chat_message_histories.streamlit",  # noqa: E501
    "TiDBChatMessageHistory": "vectorcraft.chat_message_histories.tidb",
    "UpstashRedisChatMessageHistory": "vectorcraft.chat_message_histories.upstash_redis",  # noqa: E501
    "XataChatMessageHistory": "vectorcraft.chat_message_histories.xata",
    "ZepChatMessageHistory": "vectorcraft.chat_message_histories.zep",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
