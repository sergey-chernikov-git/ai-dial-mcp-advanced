from typing import Any, Required

from mcp_server.tools.users.base import BaseUserServiceTool


class GetUserByIdTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "get_user_by_id"

    @property
    def description(self) -> str:
        return "Get user by id"

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "id": {
                "type": "number",
                "description": "User ID that should be updated",
                "required": True
            }
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        user_id = arguments['id']
        return await self._user_client.get_user(user_id)
