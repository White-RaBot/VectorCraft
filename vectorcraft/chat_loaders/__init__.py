"""**Chat Loaders** load chat messages from common communications platforms.

Load chat messages from various
communications platforms such as Facebook Messenger, Telegram, and
WhatsApp. The loaded chat messages can be used for fine-tuning models.

**Class hierarchy:**

.. code-block::

    BaseChatLoader --> <name>ChatLoader  # Examples: WhatsAppChatLoader, IMessageChatLoader

**Main helpers:**

.. code-block::

    ChatSession

"""  # noqa: E501

import importlib
from typing import Any

_module_lookup = {
    "BaseChatLoader": "vectorcraft.chat_loaders.base",
    "FolderFacebookMessengerChatLoader": "vectorcraft.chat_loaders.facebook_messenger",  # noqa: E501
    "GMailLoader": "vectorcraft.chat_loaders.gmail",
    "IMessageChatLoader": "vectorcraft.chat_loaders.imessage",
    "LangSmithDatasetChatLoader": "vectorcraft.chat_loaders.langsmith",
    "LangSmithRunChatLoader": "vectorcraft.chat_loaders.langsmith",
    "SingleFileFacebookMessengerChatLoader": "vectorcraft.chat_loaders.facebook_messenger",  # noqa: E501
    "SlackChatLoader": "vectorcraft.chat_loaders.slack",
    "TelegramChatLoader": "vectorcraft.chat_loaders.telegram",
    "WhatsAppChatLoader": "vectorcraft.chat_loaders.whatsapp",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
