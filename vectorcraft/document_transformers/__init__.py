"""**Document Transformers** are classes to transform Documents.

**Document Transformers** usually used to transform a lot of Documents in a single run.

**Class hierarchy:**

.. code-block::

    BaseDocumentTransformer --> <name>  # Examples: DoctranQATransformer, DoctranTextTranslator

**Main helpers:**

.. code-block::

    Document
"""  # noqa: E501

import importlib
from typing import Any

_module_lookup = {
    "BeautifulSoupTransformer": "vectorcraft.document_transformers.beautiful_soup_transformer",  # noqa: E501
    "DoctranPropertyExtractor": "vectorcraft.document_transformers.doctran_text_extract",  # noqa: E501
    "DoctranQATransformer": "vectorcraft.document_transformers.doctran_text_qa",
    "DoctranTextTranslator": "vectorcraft.document_transformers.doctran_text_translate",  # noqa: E501
    "EmbeddingsClusteringFilter": "vectorcraft.document_transformers.embeddings_redundant_filter",  # noqa: E501
    "EmbeddingsRedundantFilter": "vectorcraft.document_transformers.embeddings_redundant_filter",  # noqa: E501
    "GoogleTranslateTransformer": "vectorcraft.document_transformers.google_translate",  # noqa: E501
    "Html2TextTransformer": "vectorcraft.document_transformers.html2text",
    "LongContextReorder": "vectorcraft.document_transformers.long_context_reorder",  # noqa: E501
    "NucliaTextTransformer": "vectorcraft.document_transformers.nuclia_text_transform",  # noqa: E501
    "OpenAIMetadataTagger": "vectorcraft.document_transformers.openai_functions",  # noqa: E501
    "get_stateful_documents": "vectorcraft.document_transformers.embeddings_redundant_filter",  # noqa: E501
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
