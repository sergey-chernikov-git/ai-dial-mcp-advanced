from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class DeleteUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "delete_user"

    @property
    def description(self) -> str:
        return "Delete user by id"

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
        return await self._user_client.delete_user(user_id)