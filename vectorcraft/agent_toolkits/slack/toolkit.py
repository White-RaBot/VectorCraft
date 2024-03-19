from __future__ import annotations

from typing import TYPE_CHECKING, List

from langchain_core.pydantic_v1 import Field

from vectorcraft.agent_toolkits.base import BaseToolkit
from vectorcraft.tools import BaseTool
from vectorcraft.tools.slack.get_channel import SlackGetChannel
from vectorcraft.tools.slack.get_message import SlackGetMessage
from vectorcraft.tools.slack.schedule_message import SlackScheduleMessage
from vectorcraft.tools.slack.send_message import SlackSendMessage
from vectorcraft.tools.slack.utils import login

if TYPE_CHECKING:
    from slack_sdk import WebClient


class SlackToolkit(BaseToolkit):
    """Toolkit for interacting with Slack."""

    client: WebClient = Field(default_factory=login)

    class Config:
        """Pydantic config."""

        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [
            SlackGetChannel(),
            SlackGetMessage(),
            SlackScheduleMessage(),
            SlackSendMessage(),
        ]
