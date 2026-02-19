from typing import List, Optional, Union
from letta.schemas.message import Message
from letta.schemas.letta_message import LettaMessage
from letta.constants import DEFAULT_MESSAGE_TOOL, DEFAULT_MESSAGE_TOOL_KWARG

class MessageConverter:
    """Service to handle message format conversions."""

    @staticmethod
    def to_letta_messages(
        messages: List[Message],
        use_assistant_message: bool = True,
        assistant_message_tool_name: str = DEFAULT_MESSAGE_TOOL,
        assistant_message_tool_kwarg: str = DEFAULT_MESSAGE_TOOL_KWARG,
        reverse: bool = True,
        include_err: Optional[bool] = None,
        text_is_assistant_message: bool = False,
    ) -> List[LettaMessage]:
        """
        Convert a list of internal Message objects to LettaMessage objects.

        This method currently proxies to `Message.to_letta_messages_from_list` but is intended to be the
        future home for all message conversion logic to separate schema definitions from business logic.

        Args:
            messages (List[Message]): The list of internal message objects to convert.
            use_assistant_message (bool): Whether to use the assistant message format. Defaults to True.
            assistant_message_tool_name (str): The name of the tool used for assistant messages.
            assistant_message_tool_kwarg (str): The keyword argument for the assistant message tool.
            reverse (bool): Whether to reverse the order of messages. Defaults to True.
            include_err (Optional[bool]): Whether to include error messages.
            text_is_assistant_message (bool): Whether to treat text as an assistant message.

        Returns:
            List[LettaMessage]: The converted list of LettaMessage objects.
        """
        if not messages:
            return []

        # Logic will be migrated here
        # For now, we proxy back to the original method until refactor is complete
        # to ensure we don't break existing calls during the transition
        return Message.to_letta_messages_from_list(
            messages,
            use_assistant_message,
            assistant_message_tool_name,
            assistant_message_tool_kwarg,
            reverse,
            include_err,
            text_is_assistant_message
        )
