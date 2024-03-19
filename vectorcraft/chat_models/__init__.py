"""**Chat Models** are a variation on language models.

While Chat Models use language models under the hood, the interface they expose
is a bit different. Rather than expose a "text in, text out" API, they expose
an interface where "chat messages" are the inputs and outputs.

**Class hierarchy:**

.. code-block::

    BaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm

**Main helpers:**

.. code-block::

    AIMessage, BaseMessage, HumanMessage
"""  # noqa: E501

import importlib
from typing import Any

_module_lookup = {
    "AzureChatOpenAI": "vectorcraft.chat_models.azure_openai",
    "BedrockChat": "vectorcraft.chat_models.bedrock",
    "ChatAnthropic": "vectorcraft.chat_models.anthropic",
    "ChatAnyscale": "vectorcraft.chat_models.anyscale",
    "ChatBaichuan": "vectorcraft.chat_models.baichuan",
    "ChatCohere": "vectorcraft.chat_models.cohere",
    "ChatDatabricks": "vectorcraft.chat_models.databricks",
    "ChatDeepInfra": "vectorcraft.chat_models.deepinfra",
    "ChatEverlyAI": "vectorcraft.chat_models.everlyai",
    "ChatFireworks": "vectorcraft.chat_models.fireworks",
    "ChatFriendli": "vectorcraft.chat_models.friendli",
    "ChatGooglePalm": "vectorcraft.chat_models.google_palm",
    "ChatHuggingFace": "vectorcraft.chat_models.huggingface",
    "ChatHunyuan": "vectorcraft.chat_models.hunyuan",
    "ChatJavelinAIGateway": "vectorcraft.chat_models.javelin_ai_gateway",
    "ChatKinetica": "vectorcraft.chat_models.kinetica",
    "ChatKonko": "vectorcraft.chat_models.konko",
    "ChatLiteLLM": "vectorcraft.chat_models.litellm",
    "ChatLiteLLMRouter": "vectorcraft.chat_models.litellm_router",
    "ChatMLflowAIGateway": "vectorcraft.chat_models.mlflow_ai_gateway",
    "ChatMaritalk": "vectorcraft.chat_models.maritalk",
    "ChatMlflow": "vectorcraft.chat_models.mlflow",
    "ChatOllama": "vectorcraft.chat_models.ollama",
    "ChatOpenAI": "vectorcraft.chat_models.openai",
    "ChatPerplexity": "vectorcraft.chat_models.perplexity",
    "ChatSparkLLM": "vectorcraft.chat_models.sparkllm",
    "ChatTongyi": "vectorcraft.chat_models.tongyi",
    "ChatVertexAI": "vectorcraft.chat_models.vertexai",
    "ChatYandexGPT": "vectorcraft.chat_models.yandex",
    "ChatYuan2": "vectorcraft.chat_models.yuan2",
    "ChatZhipuAI": "vectorcraft.chat_models.zhipuai",
    "ErnieBotChat": "vectorcraft.chat_models.ernie",
    "FakeListChatModel": "vectorcraft.chat_models.fake",
    "GPTRouter": "vectorcraft.chat_models.gpt_router",
    "GigaChat": "vectorcraft.chat_models.gigachat",
    "HumanInputChatModel": "vectorcraft.chat_models.human",
    "JinaChat": "vectorcraft.chat_models.jinachat",
    "LlamaEdgeChatService": "vectorcraft.chat_models.llama_edge",
    "MiniMaxChat": "vectorcraft.chat_models.minimax",
    "PaiEasChatEndpoint": "vectorcraft.chat_models.pai_eas_endpoint",
    "PromptLayerChatOpenAI": "vectorcraft.chat_models.promptlayer_openai",
    "QianfanChatEndpoint": "vectorcraft.chat_models.baidu_qianfan_endpoint",
    "VolcEngineMaasChat": "vectorcraft.chat_models.volcengine_maas",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
