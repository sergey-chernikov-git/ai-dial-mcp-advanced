from typing import Any

from mcp_server.models.user_info import UserSearchRequest
from mcp_server.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "search_users"

    @property
    def description(self) -> str:
        return ("Search for users based on provided criteria. You can search by name, surname, email, or gender. "
                "All parameters are optional, but at least one should be provided for a meaningful search.")

    @property
    def input_schema(self) -> dict[str, Any]:
        return UserSearchRequest.model_json_schema()

    async def execute(self, arguments: dict[str, Any]) -> str:
        return await self._user_client.search_users(**arguments)