import importlib
from typing import Any

_module_lookup = {
    "AzureAIDocumentIntelligenceParser": "vectorcraft.document_loaders.parsers.doc_intelligence",  # noqa: E501
    "BS4HTMLParser": "vectorcraft.document_loaders.parsers.html",
    "DocAIParser": "vectorcraft.document_loaders.parsers.docai",
    "GrobidParser": "vectorcraft.document_loaders.parsers.grobid",
    "LanguageParser": "vectorcraft.document_loaders.parsers.language",
    "OpenAIWhisperParser": "vectorcraft.document_loaders.parsers.audio",
    "PDFMinerParser": "vectorcraft.document_loaders.parsers.pdf",
    "PDFPlumberParser": "vectorcraft.document_loaders.parsers.pdf",
    "PyMuPDFParser": "vectorcraft.document_loaders.parsers.pdf",
    "PyPDFParser": "vectorcraft.document_loaders.parsers.pdf",
    "PyPDFium2Parser": "vectorcraft.document_loaders.parsers.pdf",
    "VsdxParser": "vectorcraft.document_loaders.parsers.vsdx",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
