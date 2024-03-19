"""**Utilities** are the integrations with third-part systems and packages.

Other LangChain classes use **Utilities** to interact with third-part systems
and packages.
"""
import importlib
from typing import Any

_module_lookup = {
    "AlphaVantageAPIWrapper": "vectorcraft.utilities.alpha_vantage",
    "ApifyWrapper": "vectorcraft.utilities.apify",
    "ArceeWrapper": "vectorcraft.utilities.arcee",
    "ArxivAPIWrapper": "vectorcraft.utilities.arxiv",
    "AudioStream": "vectorcraft.utilities.nvidia_riva",
    "BibtexparserWrapper": "vectorcraft.utilities.bibtex",
    "BingSearchAPIWrapper": "vectorcraft.utilities.bing_search",
    "BraveSearchWrapper": "vectorcraft.utilities.brave_search",
    "DuckDuckGoSearchAPIWrapper": "vectorcraft.utilities.duckduckgo_search",
    "GoldenQueryAPIWrapper": "vectorcraft.utilities.golden_query",
    "GoogleFinanceAPIWrapper": "vectorcraft.utilities.google_finance",
    "GoogleJobsAPIWrapper": "vectorcraft.utilities.google_jobs",
    "GoogleLensAPIWrapper": "vectorcraft.utilities.google_lens",
    "GooglePlacesAPIWrapper": "vectorcraft.utilities.google_places_api",
    "GoogleScholarAPIWrapper": "vectorcraft.utilities.google_scholar",
    "GoogleSearchAPIWrapper": "vectorcraft.utilities.google_search",
    "GoogleSerperAPIWrapper": "vectorcraft.utilities.google_serper",
    "GoogleTrendsAPIWrapper": "vectorcraft.utilities.google_trends",
    "GraphQLAPIWrapper": "vectorcraft.utilities.graphql",
    "JiraAPIWrapper": "vectorcraft.utilities.jira",
    "LambdaWrapper": "vectorcraft.utilities.awslambda",
    "MaxComputeAPIWrapper": "vectorcraft.utilities.max_compute",
    "MerriamWebsterAPIWrapper": "vectorcraft.utilities.merriam_webster",
    "MetaphorSearchAPIWrapper": "vectorcraft.utilities.metaphor_search",
    "NVIDIARivaASR": "vectorcraft.utilities.nvidia_riva",
    "NVIDIARivaStream": "vectorcraft.utilities.nvidia_riva",
    "NVIDIARivaTTS": "vectorcraft.utilities.nvidia_riva",
    "NasaAPIWrapper": "vectorcraft.utilities.nasa",
    "NutritionAIAPI": "vectorcraft.utilities.passio_nutrition_ai",
    "OpenWeatherMapAPIWrapper": "vectorcraft.utilities.openweathermap",
    "OutlineAPIWrapper": "vectorcraft.utilities.outline",
    "Portkey": "vectorcraft.utilities.portkey",
    "PowerBIDataset": "vectorcraft.utilities.powerbi",
    "PubMedAPIWrapper": "vectorcraft.utilities.pubmed",
    "PythonREPL": "vectorcraft.utilities.python",
    "Requests": "vectorcraft.utilities.requests",
    "RequestsWrapper": "vectorcraft.utilities.requests",
    "RivaASR": "vectorcraft.utilities.nvidia_riva",
    "RivaTTS": "vectorcraft.utilities.nvidia_riva",
    "SQLDatabase": "vectorcraft.utilities.sql_database",
    "SceneXplainAPIWrapper": "vectorcraft.utilities.scenexplain",
    "SearchApiAPIWrapper": "vectorcraft.utilities.searchapi",
    "SearxSearchWrapper": "vectorcraft.utilities.searx_search",
    "SerpAPIWrapper": "vectorcraft.utilities.serpapi",
    "SparkSQL": "vectorcraft.utilities.spark_sql",
    "StackExchangeAPIWrapper": "vectorcraft.utilities.stackexchange",
    "SteamWebAPIWrapper": "vectorcraft.utilities.steam",
    "TensorflowDatasets": "vectorcraft.utilities.tensorflow_datasets",
    "TextRequestsWrapper": "vectorcraft.utilities.requests",
    "TwilioAPIWrapper": "vectorcraft.utilities.twilio",
    "WikipediaAPIWrapper": "vectorcraft.utilities.wikipedia",
    "WolframAlphaAPIWrapper": "vectorcraft.utilities.wolfram_alpha",
    "YouSearchAPIWrapper": "vectorcraft.utilities.you",
    "ZapierNLAWrapper": "vectorcraft.utilities.zapier",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = list(_module_lookup.keys())
