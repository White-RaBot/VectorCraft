from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from langchain_core.language_models import BaseLanguageModel
from langchain_core.pydantic_v1 import Field

from vectorcraft.agent_toolkits.base import BaseToolkit
from vectorcraft.tools import BaseTool
from vectorcraft.tools.amadeus.closest_airport import AmadeusClosestAirport
from vectorcraft.tools.amadeus.flight_search import AmadeusFlightSearch
from vectorcraft.tools.amadeus.utils import authenticate

if TYPE_CHECKING:
    from amadeus import Client


class AmadeusToolkit(BaseToolkit):
    """Toolkit for interacting with Amadeus which offers APIs for travel."""

    client: Client = Field(default_factory=authenticate)
    llm: Optional[BaseLanguageModel] = Field(default=None)

    class Config:
        """Pydantic config."""

        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [
            AmadeusClosestAirport(llm=self.llm),
            AmadeusFlightSearch(),
        ]
