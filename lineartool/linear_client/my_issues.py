from typing import List, Optional

from .base_model import BaseModel


class MyIssues(BaseModel):
    issues: "MyIssuesIssues"


class MyIssuesIssues(BaseModel):
    nodes: List["MyIssuesIssuesNodes"]


class MyIssuesIssuesNodes(BaseModel):
    id: str
    assignee: Optional["MyIssuesIssuesNodesAssignee"]
    identifier: str
    parent: Optional["MyIssuesIssuesNodesParent"]
    title: str


class MyIssuesIssuesNodesAssignee(BaseModel):
    id: str


class MyIssuesIssuesNodesParent(BaseModel):
    id: str


MyIssues.model_rebuild()
MyIssuesIssues.model_rebuild()
MyIssuesIssuesNodes.model_rebuild()
