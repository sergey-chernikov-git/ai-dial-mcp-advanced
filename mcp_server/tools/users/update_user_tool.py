from typing import Any

from mcp_server.models.user_info import UserUpdate
from mcp_server.tools.users.base import BaseUserServiceTool


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "update_user"

    @property
    def description(self) -> str:
        return "Updates an existing user in the system. Requires user ID and new information to update."

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "id": {
                "type": "number",
                "description": "User ID that should be updated",
                "required": True
            },
            "new_info": UserUpdate.model_json_schema()
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        user_id = int(arguments["id"])
        new_info = int(arguments["new_info"])
        new_user_info = UserUpdate.model_validate(new_info)
        return await self._user_client.update_user(user_id, new_user_info)

