from typing import List

from vectorcraft.agent_toolkits.base import BaseToolkit
from vectorcraft.tools import BaseTool
from vectorcraft.tools.polygon import (
    PolygonAggregates,
    PolygonFinancials,
    PolygonLastQuote,
    PolygonTickerNews,
)
from vectorcraft.utilities.polygon import PolygonAPIWrapper


class PolygonToolkit(BaseToolkit):
    """Polygon Toolkit."""

    tools: List[BaseTool] = []

    @classmethod
    def from_polygon_api_wrapper(
        cls, polygon_api_wrapper: PolygonAPIWrapper
    ) -> "PolygonToolkit":
        tools = [
            PolygonAggregates(
                api_wrapper=polygon_api_wrapper,
            ),
            PolygonLastQuote(
                api_wrapper=polygon_api_wrapper,
            ),
            PolygonTickerNews(
                api_wrapper=polygon_api_wrapper,
            ),
            PolygonFinancials(
                api_wrapper=polygon_api_wrapper,
            ),
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
