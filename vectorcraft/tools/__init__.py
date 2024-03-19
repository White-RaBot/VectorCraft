"""**Tools** are classes that an Agent uses to interact with the world.

Each tool has a **description**. Agent uses the description to choose the right
tool for the job.

**Class hierarchy:**

.. code-block::

    ToolMetaclass --> BaseTool --> <name>Tool  # Examples: AIPluginTool, BaseGraphQLTool
                                   <name>      # Examples: BraveSearch, HumanInputRun

**Main helpers:**

.. code-block::

    CallbackManagerForToolRun, AsyncCallbackManagerForToolRun
"""
import importlib
from typing import Any

# Used for internal purposes
_DEPRECATED_TOOLS = {"PythonAstREPLTool", "PythonREPLTool"}

_module_lookup = {
    "AINAppOps": "vectorcraft.tools.ainetwork.app",
    "AINOwnerOps": "vectorcraft.tools.ainetwork.owner",
    "AINRuleOps": "vectorcraft.tools.ainetwork.rule",
    "AINTransfer": "vectorcraft.tools.ainetwork.transfer",
    "AINValueOps": "vectorcraft.tools.ainetwork.value",
    "AIPluginTool": "vectorcraft.tools.plugin",
    "APIOperation": "vectorcraft.tools.openapi.utils.api_models",
    "ArxivQueryRun": "vectorcraft.tools.arxiv.tool",
    "AzureCogsFormRecognizerTool": "vectorcraft.tools.azure_cognitive_services",
    "AzureCogsImageAnalysisTool": "vectorcraft.tools.azure_cognitive_services",
    "AzureCogsSpeech2TextTool": "vectorcraft.tools.azure_cognitive_services",
    "AzureCogsText2SpeechTool": "vectorcraft.tools.azure_cognitive_services",
    "AzureCogsTextAnalyticsHealthTool": "vectorcraft.tools.azure_cognitive_services",  # noqa: E501
    "BaseGraphQLTool": "vectorcraft.tools.graphql.tool",
    "BaseRequestsTool": "vectorcraft.tools.requests.tool",
    "BaseSQLDatabaseTool": "vectorcraft.tools.sql_database.tool",
    "BaseSparkSQLTool": "vectorcraft.tools.spark_sql.tool",
    "BaseTool": "langchain_core.tools",
    "BearlyInterpreterTool": "vectorcraft.tools.bearly.tool",
    "BingSearchResults": "vectorcraft.tools.bing_search.tool",
    "BingSearchRun": "vectorcraft.tools.bing_search.tool",
    "BraveSearch": "vectorcraft.tools.brave_search.tool",
    "ClickTool": "vectorcraft.tools.playwright",
    "CogniswitchKnowledgeRequest": "vectorcraft.tools.cogniswitch.tool",
    "CogniswitchKnowledgeSourceFile": "vectorcraft.tools.cogniswitch.tool",
    "CogniswitchKnowledgeSourceURL": "vectorcraft.tools.cogniswitch.tool",
    "CogniswitchKnowledgeStatus": "vectorcraft.tools.cogniswitch.tool",
    "ConneryAction": "vectorcraft.tools.connery",
    "CopyFileTool": "vectorcraft.tools.file_management",
    "CurrentWebPageTool": "vectorcraft.tools.playwright",
    "DeleteFileTool": "vectorcraft.tools.file_management",
    "DuckDuckGoSearchResults": "vectorcraft.tools.ddg_search.tool",
    "DuckDuckGoSearchRun": "vectorcraft.tools.ddg_search.tool",
    "E2BDataAnalysisTool": "vectorcraft.tools.e2b_data_analysis.tool",
    "EdenAiExplicitImageTool": "vectorcraft.tools.edenai",
    "EdenAiObjectDetectionTool": "vectorcraft.tools.edenai",
    "EdenAiParsingIDTool": "vectorcraft.tools.edenai",
    "EdenAiParsingInvoiceTool": "vectorcraft.tools.edenai",
    "EdenAiSpeechToTextTool": "vectorcraft.tools.edenai",
    "EdenAiTextModerationTool": "vectorcraft.tools.edenai",
    "EdenAiTextToSpeechTool": "vectorcraft.tools.edenai",
    "EdenaiTool": "vectorcraft.tools.edenai",
    "ElevenLabsText2SpeechTool": "vectorcraft.tools.eleven_labs.text2speech",
    "ExtractHyperlinksTool": "vectorcraft.tools.playwright",
    "ExtractTextTool": "vectorcraft.tools.playwright",
    "FileSearchTool": "vectorcraft.tools.file_management",
    "GetElementsTool": "vectorcraft.tools.playwright",
    "GmailCreateDraft": "vectorcraft.tools.gmail",
    "GmailGetMessage": "vectorcraft.tools.gmail",
    "GmailGetThread": "vectorcraft.tools.gmail",
    "GmailSearch": "vectorcraft.tools.gmail",
    "GmailSendMessage": "vectorcraft.tools.gmail",
    "GoogleCloudTextToSpeechTool": "vectorcraft.tools.google_cloud.texttospeech",  # noqa: E501
    "GooglePlacesTool": "vectorcraft.tools.google_places.tool",
    "GoogleSearchResults": "vectorcraft.tools.google_search.tool",
    "GoogleSearchRun": "vectorcraft.tools.google_search.tool",
    "GoogleSerperResults": "vectorcraft.tools.google_serper.tool",
    "GoogleSerperRun": "vectorcraft.tools.google_serper.tool",
    "HumanInputRun": "vectorcraft.tools.human.tool",
    "IFTTTWebhook": "vectorcraft.tools.ifttt",
    "InfoPowerBITool": "vectorcraft.tools.powerbi.tool",
    "InfoSQLDatabaseTool": "vectorcraft.tools.sql_database.tool",
    "InfoSparkSQLTool": "vectorcraft.tools.spark_sql.tool",
    "JiraAction": "vectorcraft.tools.jira.tool",
    "JsonGetValueTool": "vectorcraft.tools.json.tool",
    "JsonListKeysTool": "vectorcraft.tools.json.tool",
    "ListDirectoryTool": "vectorcraft.tools.file_management",
    "ListPowerBITool": "vectorcraft.tools.powerbi.tool",
    "ListSQLDatabaseTool": "vectorcraft.tools.sql_database.tool",
    "ListSparkSQLTool": "vectorcraft.tools.spark_sql.tool",
    "MerriamWebsterQueryRun": "vectorcraft.tools.merriam_webster.tool",
    "MetaphorSearchResults": "vectorcraft.tools.metaphor_search",
    "MoveFileTool": "vectorcraft.tools.file_management",
    "NasaAction": "vectorcraft.tools.nasa.tool",
    "NavigateBackTool": "vectorcraft.tools.playwright",
    "NavigateTool": "vectorcraft.tools.playwright",
    "O365CreateDraftMessage": "vectorcraft.tools.office365.create_draft_message",  # noqa: E501
    "O365SearchEmails": "vectorcraft.tools.office365.messages_search",
    "O365SearchEvents": "vectorcraft.tools.office365.events_search",
    "O365SendEvent": "vectorcraft.tools.office365.send_event",
    "O365SendMessage": "vectorcraft.tools.office365.send_message",
    "OpenAPISpec": "vectorcraft.tools.openapi.utils.openapi_utils",
    "OpenWeatherMapQueryRun": "vectorcraft.tools.openweathermap.tool",
    "PolygonAggregates": "vectorcraft.tools.polygon.aggregates",
    "PolygonFinancials": "vectorcraft.tools.polygon.financials",
    "PolygonLastQuote": "vectorcraft.tools.polygon.last_quote",
    "PolygonTickerNews": "vectorcraft.tools.polygon.ticker_news",
    "PubmedQueryRun": "vectorcraft.tools.pubmed.tool",
    "QueryCheckerTool": "vectorcraft.tools.spark_sql.tool",
    "QueryPowerBITool": "vectorcraft.tools.powerbi.tool",
    "QuerySQLCheckerTool": "vectorcraft.tools.sql_database.tool",
    "QuerySQLDataBaseTool": "vectorcraft.tools.sql_database.tool",
    "QuerySparkSQLTool": "vectorcraft.tools.spark_sql.tool",
    "ReadFileTool": "vectorcraft.tools.file_management",
    "RedditSearchRun": "vectorcraft.tools.reddit_search.tool",
    "RedditSearchSchema": "vectorcraft.tools.reddit_search.tool",
    "RequestsDeleteTool": "vectorcraft.tools.requests.tool",
    "RequestsGetTool": "vectorcraft.tools.requests.tool",
    "RequestsPatchTool": "vectorcraft.tools.requests.tool",
    "RequestsPostTool": "vectorcraft.tools.requests.tool",
    "RequestsPutTool": "vectorcraft.tools.requests.tool",
    "SceneXplainTool": "vectorcraft.tools.scenexplain.tool",
    "SearchAPIResults": "vectorcraft.tools.searchapi.tool",
    "SearchAPIRun": "vectorcraft.tools.searchapi.tool",
    "SearxSearchResults": "vectorcraft.tools.searx_search.tool",
    "SearxSearchRun": "vectorcraft.tools.searx_search.tool",
    "ShellTool": "vectorcraft.tools.shell.tool",
    "SlackGetChannel": "vectorcraft.tools.slack.get_channel",
    "SlackGetMessage": "vectorcraft.tools.slack.get_message",
    "SlackScheduleMessage": "vectorcraft.tools.slack.schedule_message",
    "SlackSendMessage": "vectorcraft.tools.slack.send_message",
    "SleepTool": "vectorcraft.tools.sleep.tool",
    "StackExchangeTool": "vectorcraft.tools.stackexchange.tool",
    "StdInInquireTool": "vectorcraft.tools.interaction.tool",
    "SteamWebAPIQueryRun": "vectorcraft.tools.steam.tool",
    "SteamshipImageGenerationTool": "vectorcraft.tools.steamship_image_generation",  # noqa: E501
    "StructuredTool": "langchain_core.tools",
    "Tool": "langchain_core.tools",
    "VectorStoreQATool": "vectorcraft.tools.vectorstore.tool",
    "VectorStoreQAWithSourcesTool": "vectorcraft.tools.vectorstore.tool",
    "WikipediaQueryRun": "vectorcraft.tools.wikipedia.tool",
    "WolframAlphaQueryRun": "vectorcraft.tools.wolfram_alpha.tool",
    "WriteFileTool": "vectorcraft.tools.file_management",
    "YahooFinanceNewsTool": "vectorcraft.tools.yahoo_finance_news",
    "YouSearchTool": "vectorcraft.tools.you.tool",
    "YouTubeSearchTool": "vectorcraft.tools.youtube.search",
    "ZapierNLAListActions": "vectorcraft.tools.zapier.tool",
    "ZapierNLARunAction": "vectorcraft.tools.zapier.tool",
    "authenticate": "vectorcraft.tools.office365.utils",
    "format_tool_to_openai_function": "vectorcraft.tools.convert_to_openai",
    "tool": "langchain_core.tools",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
