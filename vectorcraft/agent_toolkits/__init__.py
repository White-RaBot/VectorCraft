"""**Toolkits** are sets of tools that can be used to interact with
various services and APIs.
"""
import importlib
from typing import Any

_module_lookup = {
    "AINetworkToolkit": "vectorcraft.agent_toolkits.ainetwork.toolkit",
    "AmadeusToolkit": "vectorcraft.agent_toolkits.amadeus.toolkit",
    "AzureCognitiveServicesToolkit": "vectorcraft.agent_toolkits.azure_cognitive_services",  # noqa: E501
    "CogniswitchToolkit": "vectorcraft.agent_toolkits.cogniswitch.toolkit",
    "ConneryToolkit": "vectorcraft.agent_toolkits.connery",
    "FileManagementToolkit": "vectorcraft.agent_toolkits.file_management.toolkit",  # noqa: E501
    "GmailToolkit": "vectorcraft.agent_toolkits.gmail.toolkit",
    "JiraToolkit": "vectorcraft.agent_toolkits.jira.toolkit",
    "JsonToolkit": "vectorcraft.agent_toolkits.json.toolkit",
    "MultionToolkit": "vectorcraft.agent_toolkits.multion.toolkit",
    "NLAToolkit": "vectorcraft.agent_toolkits.nla.toolkit",
    "NasaToolkit": "vectorcraft.agent_toolkits.nasa.toolkit",
    "O365Toolkit": "vectorcraft.agent_toolkits.office365.toolkit",
    "OpenAPIToolkit": "vectorcraft.agent_toolkits.openapi.toolkit",
    "PlayWrightBrowserToolkit": "vectorcraft.agent_toolkits.playwright.toolkit",
    "PolygonToolkit": "vectorcraft.agent_toolkits.polygon.toolkit",
    "PowerBIToolkit": "vectorcraft.agent_toolkits.powerbi.toolkit",
    "SQLDatabaseToolkit": "vectorcraft.agent_toolkits.sql.toolkit",
    "SlackToolkit": "vectorcraft.agent_toolkits.slack.toolkit",
    "SparkSQLToolkit": "vectorcraft.agent_toolkits.spark_sql.toolkit",
    "SteamToolkit": "vectorcraft.agent_toolkits.steam.toolkit",
    "ZapierToolkit": "vectorcraft.agent_toolkits.zapier.toolkit",
    "create_json_agent": "vectorcraft.agent_toolkits.json.base",
    "create_openapi_agent": "vectorcraft.agent_toolkits.openapi.base",
    "create_pbi_agent": "vectorcraft.agent_toolkits.powerbi.base",
    "create_pbi_chat_agent": "vectorcraft.agent_toolkits.powerbi.chat_base",
    "create_spark_sql_agent": "vectorcraft.agent_toolkits.spark_sql.base",
    "create_sql_agent": "vectorcraft.agent_toolkits.sql.base",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
