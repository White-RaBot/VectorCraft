"""**Callback handlers** allow listening to events in LangChain.

**Class hierarchy:**

.. code-block::

    BaseCallbackHandler --> <name>CallbackHandler  # Example: AimCallbackHandler
"""
import importlib
from typing import Any

_module_lookup = {
    "AimCallbackHandler": "vectorcraft.callbacks.aim_callback",
    "ArgillaCallbackHandler": "vectorcraft.callbacks.argilla_callback",
    "ArizeCallbackHandler": "vectorcraft.callbacks.arize_callback",
    "ArthurCallbackHandler": "vectorcraft.callbacks.arthur_callback",
    "ClearMLCallbackHandler": "vectorcraft.callbacks.clearml_callback",
    "CometCallbackHandler": "vectorcraft.callbacks.comet_ml_callback",
    "ContextCallbackHandler": "vectorcraft.callbacks.context_callback",
    "FiddlerCallbackHandler": "vectorcraft.callbacks.fiddler_callback",
    "FlyteCallbackHandler": "vectorcraft.callbacks.flyte_callback",
    "HumanApprovalCallbackHandler": "vectorcraft.callbacks.human",
    "InfinoCallbackHandler": "vectorcraft.callbacks.infino_callback",
    "LLMThoughtLabeler": "vectorcraft.callbacks.streamlit",
    "LLMonitorCallbackHandler": "vectorcraft.callbacks.llmonitor_callback",
    "LabelStudioCallbackHandler": "vectorcraft.callbacks.labelstudio_callback",
    "MlflowCallbackHandler": "vectorcraft.callbacks.mlflow_callback",
    "OpenAICallbackHandler": "vectorcraft.callbacks.openai_info",
    "PromptLayerCallbackHandler": "vectorcraft.callbacks.promptlayer_callback",
    "SageMakerCallbackHandler": "vectorcraft.callbacks.sagemaker_callback",
    "StreamlitCallbackHandler": "vectorcraft.callbacks.streamlit",
    "TrubricsCallbackHandler": "vectorcraft.callbacks.trubrics_callback",
    "WandbCallbackHandler": "vectorcraft.callbacks.wandb_callback",
    "WhyLabsCallbackHandler": "vectorcraft.callbacks.whylabs_callback",
    "get_openai_callback": "vectorcraft.callbacks.manager",
    "wandb_tracing_enabled": "vectorcraft.callbacks.manager",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
