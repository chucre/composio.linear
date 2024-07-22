import asyncio
from composio_tools.lib import Action
from pydantic import BaseModel, Field
from ..linear_client.client import Client
from ..linear_client.my_issues import MyIssuesIssuesNodes
from typing import List

class GetMyIssuesRequest(BaseModel): {}

class GetMyIssuesResponseSingleItem(BaseModel):
    id: str = Field(..., description="ID of the issue")
    name: str = Field(..., description="Name of the issue")
    # ... Add other relevant fields

class GetMyIssues(Action):
    """
    Get subtasks for a specific task.
    """
    _display_name = "Get My Issues"
    _request_schema = GetMyIssuesRequest
    _response_schema = List["MyIssuesIssuesNodes"]

    def _execute_async(self, authorisation_data: dict):
        client = Client(authorisation_data["base_url"], authorisation_data["headers"]);
        response = client.my_issues();
        return response.issues.nodes;

    def execute(self, req: _request_schema, authorisation_data: dict):
        try:
            response_data = self._execute_async(authorisation_data);
            execution_details = {"executed": True}
        except Exception as e:
            execution_details = {"executed": False}
            response_data = {"error": str(e)}
        
        return {
            "execution_details": execution_details,
            "response_data": response_data
        }