import typing as t
from lineartool.actions.my_issues import GetMyIssues
from .actions import GetMyIssues 
from composio_tools.lib import Tool, Action

class LinearTool(Tool):
    """
    Tool to help teams plan, track, and manage their software projects.
    """

    def actions(self) -> list[t.Type[Action]]:
        return [GetMyIssues]

    def triggers(self) -> list:
        return []  # If applicable, define triggers here

    """
    Connect to Linear to manage issues, projects, subtasks, and more.
    """
    def actions(self) -> list:
        return [
            GetMyIssues,
        ]

    def triggers(self) -> list:
        return []
    
__all__ = ["LinearTool"]