"""**Embedding models**  are wrappers around embedding models
from different APIs and services.

**Embedding models** can be LLMs or not.

**Class hierarchy:**

.. code-block::

    Embeddings --> <name>Embeddings  # Examples: OpenAIEmbeddings, HuggingFaceEmbeddings
"""


import importlib
import logging
from typing import Any

_module_lookup = {
    "AlephAlphaAsymmetricSemanticEmbedding": "vectorcraft.embeddings.aleph_alpha",  # noqa: E501
    "AlephAlphaSymmetricSemanticEmbedding": "vectorcraft.embeddings.aleph_alpha",  # noqa: E501
    "AwaEmbeddings": "vectorcraft.embeddings.awa",
    "AzureOpenAIEmbeddings": "vectorcraft.embeddings.azure_openai",
    "BaichuanTextEmbeddings": "vectorcraft.embeddings.baichuan",
    "BedrockEmbeddings": "vectorcraft.embeddings.bedrock",
    "BookendEmbeddings": "vectorcraft.embeddings.bookend",
    "ClarifaiEmbeddings": "vectorcraft.embeddings.clarifai",
    "CohereEmbeddings": "vectorcraft.embeddings.cohere",
    "DashScopeEmbeddings": "vectorcraft.embeddings.dashscope",
    "DatabricksEmbeddings": "vectorcraft.embeddings.databricks",
    "DeepInfraEmbeddings": "vectorcraft.embeddings.deepinfra",
    "DeterministicFakeEmbedding": "vectorcraft.embeddings.fake",
    "EdenAiEmbeddings": "vectorcraft.embeddings.edenai",
    "ElasticsearchEmbeddings": "vectorcraft.embeddings.elasticsearch",
    "EmbaasEmbeddings": "vectorcraft.embeddings.embaas",
    "ErnieEmbeddings": "vectorcraft.embeddings.ernie",
    "FakeEmbeddings": "vectorcraft.embeddings.fake",
    "FastEmbedEmbeddings": "vectorcraft.embeddings.fastembed",
    "GPT4AllEmbeddings": "vectorcraft.embeddings.gpt4all",
    "GooglePalmEmbeddings": "vectorcraft.embeddings.google_palm",
    "GradientEmbeddings": "vectorcraft.embeddings.gradient_ai",
    "HuggingFaceBgeEmbeddings": "vectorcraft.embeddings.huggingface",
    "HuggingFaceEmbeddings": "vectorcraft.embeddings.huggingface",
    "HuggingFaceHubEmbeddings": "vectorcraft.embeddings.huggingface_hub",
    "HuggingFaceInferenceAPIEmbeddings": "vectorcraft.embeddings.huggingface",
    "HuggingFaceInstructEmbeddings": "vectorcraft.embeddings.huggingface",
    "InfinityEmbeddings": "vectorcraft.embeddings.infinity",
    "InfinityEmbeddingsLocal": "vectorcraft.embeddings.infinity_local",
    "JavelinAIGatewayEmbeddings": "vectorcraft.embeddings.javelin_ai_gateway",
    "JinaEmbeddings": "vectorcraft.embeddings.jina",
    "JohnSnowLabsEmbeddings": "vectorcraft.embeddings.johnsnowlabs",
    "LLMRailsEmbeddings": "vectorcraft.embeddings.llm_rails",
    "LaserEmbeddings": "vectorcraft.embeddings.laser",
    "LlamaCppEmbeddings": "vectorcraft.embeddings.llamacpp",
    "LlamafileEmbeddings": "vectorcraft.embeddings.llamafile",
    "LocalAIEmbeddings": "vectorcraft.embeddings.localai",
    "MiniMaxEmbeddings": "vectorcraft.embeddings.minimax",
    "MlflowAIGatewayEmbeddings": "vectorcraft.embeddings.mlflow_gateway",
    "MlflowCohereEmbeddings": "vectorcraft.embeddings.mlflow",
    "MlflowEmbeddings": "vectorcraft.embeddings.mlflow",
    "ModelScopeEmbeddings": "vectorcraft.embeddings.modelscope_hub",
    "MosaicMLInstructorEmbeddings": "vectorcraft.embeddings.mosaicml",
    "NLPCloudEmbeddings": "vectorcraft.embeddings.nlpcloud",
    "NeMoEmbeddings": "vectorcraft.embeddings.nemo",
    "OCIGenAIEmbeddings": "vectorcraft.embeddings.oci_generative_ai",
    "OctoAIEmbeddings": "vectorcraft.embeddings.octoai_embeddings",
    "OllamaEmbeddings": "vectorcraft.embeddings.ollama",
    "OpenAIEmbeddings": "vectorcraft.embeddings.openai",
    "QianfanEmbeddingsEndpoint": "vectorcraft.embeddings.baidu_qianfan_endpoint",  # noqa: E501
    "QuantizedBiEncoderEmbeddings": "vectorcraft.embeddings.optimum_intel",
    "SagemakerEndpointEmbeddings": "vectorcraft.embeddings.sagemaker_endpoint",
    "SelfHostedEmbeddings": "vectorcraft.embeddings.self_hosted",
    "SelfHostedHuggingFaceEmbeddings": "vectorcraft.embeddings.self_hosted_hugging_face",  # noqa: E501
    "SelfHostedHuggingFaceInstructEmbeddings": "vectorcraft.embeddings.self_hosted_hugging_face",  # noqa: E501
    "SentenceTransformerEmbeddings": "vectorcraft.embeddings.sentence_transformer",  # noqa: E501
    "SpacyEmbeddings": "vectorcraft.embeddings.spacy_embeddings",
    "SparkLLMTextEmbeddings": "vectorcraft.embeddings.sparkllm",
    "TensorflowHubEmbeddings": "vectorcraft.embeddings.tensorflow_hub",
    "VertexAIEmbeddings": "vectorcraft.embeddings.vertexai",
    "VolcanoEmbeddings": "vectorcraft.embeddings.volcengine",
    "VoyageEmbeddings": "vectorcraft.embeddings.voyageai",
    "XinferenceEmbeddings": "vectorcraft.embeddings.xinference",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())

logger = logging.getLogger(__name__)


# TODO: this is in here to maintain backwards compatibility
class HypotheticalDocumentEmbedder:
    def __init__(self, *args: Any, **kwargs: Any):
        logger.warning(
            "Using a deprecated class. Please use "
            "`from langchain.chains import HypotheticalDocumentEmbedder` instead"
        )
        from langchain.chains.hyde.base import HypotheticalDocumentEmbedder as H

        return H(*args, **kwargs)  # type: ignore

    @classmethod
    def from_llm(cls, *args: Any, **kwargs: Any) -> Any:
        logger.warning(
            "Using a deprecated class. Please use "
            "`from langchain.chains import HypotheticalDocumentEmbedder` instead"
        )
        from langchain.chains.hyde.base import HypotheticalDocumentEmbedder as H

        return H.from_llm(*args, **kwargs)
