from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContextViewType,
    CustomerStatusType,
    DateResolutionType,
    Day,
    GitAutomationStates,
    GithubOrgType,
    InitiativeStatus,
    InitiativeTab,
    IssueRelationType,
    PaginationNulls,
    PaginationSortOrder,
    ProjectTab,
    ProjectUpdateHealthType,
    PushSubscriptionType,
    SlackChannelType,
    SLADayCountType,
    SlaStatus,
    UserContextViewType,
    UserRoleType,
    ViewPreferencesType,
    ViewType,
)


class BooleanComparator(BaseModel):
    eq: Optional[bool] = None
    neq: Optional[bool] = None


class ContentComparator(BaseModel):
    contains: Optional[str] = None
    not_contains: Optional[str] = Field(alias="notContains", default=None)


class DateComparator(BaseModel):
    eq: Optional[Any] = None
    neq: Optional[Any] = None
    in_: Optional[List[Any]] = Field(alias="in", default=None)
    nin: Optional[List[Any]] = None
    lt: Optional[Any] = None
    lte: Optional[Any] = None
    gt: Optional[Any] = None
    gte: Optional[Any] = None


class NullableDateComparator(BaseModel):
    eq: Optional[Any] = None
    neq: Optional[Any] = None
    in_: Optional[List[Any]] = Field(alias="in", default=None)
    nin: Optional[List[Any]] = None
    null: Optional[bool] = None
    lt: Optional[Any] = None
    lte: Optional[Any] = None
    gt: Optional[Any] = None
    gte: Optional[Any] = None


class EstimateComparator(BaseModel):
    eq: Optional[float] = None
    neq: Optional[float] = None
    in_: Optional[List[float]] = Field(alias="in", default=None)
    nin: Optional[List[float]] = None
    null: Optional[bool] = None
    lt: Optional[float] = None
    lte: Optional[float] = None
    gt: Optional[float] = None
    gte: Optional[float] = None
    or_: Optional[List["NullableNumberComparator"]] = Field(alias="or", default=None)
    and_: Optional[List["NullableNumberComparator"]] = Field(alias="and", default=None)


class RelationExistsComparator(BaseModel):
    eq: Optional[bool] = None
    neq: Optional[bool] = None


class IDComparator(BaseModel):
    eq: Optional[str] = None
    neq: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    nin: Optional[List[str]] = None


class NumberComparator(BaseModel):
    eq: Optional[float] = None
    neq: Optional[float] = None
    in_: Optional[List[float]] = Field(alias="in", default=None)
    nin: Optional[List[float]] = None
    lt: Optional[float] = None
    lte: Optional[float] = None
    gt: Optional[float] = None
    gte: Optional[float] = None


class NullableNumberComparator(BaseModel):
    eq: Optional[float] = None
    neq: Optional[float] = None
    in_: Optional[List[float]] = Field(alias="in", default=None)
    nin: Optional[List[float]] = None
    null: Optional[bool] = None
    lt: Optional[float] = None
    lte: Optional[float] = None
    gt: Optional[float] = None
    gte: Optional[float] = None


class StringComparator(BaseModel):
    eq: Optional[str] = None
    neq: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    nin: Optional[List[str]] = None
    eq_ignore_case: Optional[str] = Field(alias="eqIgnoreCase", default=None)
    neq_ignore_case: Optional[str] = Field(alias="neqIgnoreCase", default=None)
    starts_with: Optional[str] = Field(alias="startsWith", default=None)
    starts_with_ignore_case: Optional[str] = Field(
        alias="startsWithIgnoreCase", default=None
    )
    not_starts_with: Optional[str] = Field(alias="notStartsWith", default=None)
    ends_with: Optional[str] = Field(alias="endsWith", default=None)
    not_ends_with: Optional[str] = Field(alias="notEndsWith", default=None)
    contains: Optional[str] = None
    contains_ignore_case: Optional[str] = Field(
        alias="containsIgnoreCase", default=None
    )
    not_contains: Optional[str] = Field(alias="notContains", default=None)
    not_contains_ignore_case: Optional[str] = Field(
        alias="notContainsIgnoreCase", default=None
    )


class NullableStringComparator(BaseModel):
    eq: Optional[str] = None
    neq: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    nin: Optional[List[str]] = None
    null: Optional[bool] = None
    eq_ignore_case: Optional[str] = Field(alias="eqIgnoreCase", default=None)
    neq_ignore_case: Optional[str] = Field(alias="neqIgnoreCase", default=None)
    starts_with: Optional[str] = Field(alias="startsWith", default=None)
    starts_with_ignore_case: Optional[str] = Field(
        alias="startsWithIgnoreCase", default=None
    )
    not_starts_with: Optional[str] = Field(alias="notStartsWith", default=None)
    ends_with: Optional[str] = Field(alias="endsWith", default=None)
    not_ends_with: Optional[str] = Field(alias="notEndsWith", default=None)
    contains: Optional[str] = None
    contains_ignore_case: Optional[str] = Field(
        alias="containsIgnoreCase", default=None
    )
    not_contains: Optional[str] = Field(alias="notContains", default=None)
    not_contains_ignore_case: Optional[str] = Field(
        alias="notContainsIgnoreCase", default=None
    )


class SourceTypeComparator(BaseModel):
    eq: Optional[str] = None
    neq: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    nin: Optional[List[str]] = None
    eq_ignore_case: Optional[str] = Field(alias="eqIgnoreCase", default=None)
    neq_ignore_case: Optional[str] = Field(alias="neqIgnoreCase", default=None)
    starts_with: Optional[str] = Field(alias="startsWith", default=None)
    starts_with_ignore_case: Optional[str] = Field(
        alias="startsWithIgnoreCase", default=None
    )
    not_starts_with: Optional[str] = Field(alias="notStartsWith", default=None)
    ends_with: Optional[str] = Field(alias="endsWith", default=None)
    not_ends_with: Optional[str] = Field(alias="notEndsWith", default=None)
    contains: Optional[str] = None
    contains_ignore_case: Optional[str] = Field(
        alias="containsIgnoreCase", default=None
    )
    not_contains: Optional[str] = Field(alias="notContains", default=None)
    not_contains_ignore_case: Optional[str] = Field(
        alias="notContainsIgnoreCase", default=None
    )


class TimelessDateComparator(BaseModel):
    eq: Optional[Any] = None
    neq: Optional[Any] = None
    in_: Optional[List[Any]] = Field(alias="in", default=None)
    nin: Optional[List[Any]] = None
    lt: Optional[Any] = None
    lte: Optional[Any] = None
    gt: Optional[Any] = None
    gte: Optional[Any] = None


class NullableTimelessDateComparator(BaseModel):
    eq: Optional[Any] = None
    neq: Optional[Any] = None
    in_: Optional[List[Any]] = Field(alias="in", default=None)
    nin: Optional[List[Any]] = None
    null: Optional[bool] = None
    lt: Optional[Any] = None
    lte: Optional[Any] = None
    gt: Optional[Any] = None
    gte: Optional[Any] = None


class SubTypeComparator(BaseModel):
    eq: Optional[str] = None
    neq: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    nin: Optional[List[str]] = None
    null: Optional[bool] = None


class SourceMetadataComparator(BaseModel):
    eq: Optional[str] = None
    neq: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    nin: Optional[List[str]] = None
    null: Optional[bool] = None
    sub_type: Optional["SubTypeComparator"] = Field(alias="subType", default=None)


class OrganizationIpRestrictionInput(BaseModel):
    range: str
    type: str
    description: Optional[str] = None
    enabled: bool


class SlackAsksTeamSettingsInput(BaseModel):
    id: str
    has_default_ask: bool = Field(alias="hasDefaultAsk")


class SlackChannelNameMappingInput(BaseModel):
    id: str
    name: str
    is_private: Optional[bool] = Field(alias="isPrivate", default=None)
    is_shared: Optional[bool] = Field(alias="isShared", default=None)
    bot_added: Optional[bool] = Field(alias="botAdded", default=None)
    teams: List["SlackAsksTeamSettingsInput"]
    auto_create_on_message: Optional[bool] = Field(
        alias="autoCreateOnMessage", default=None
    )
    auto_create_on_emoji: Optional[bool] = Field(
        alias="autoCreateOnEmoji", default=None
    )
    auto_create_on_bot_mention: Optional[bool] = Field(
        alias="autoCreateOnBotMention", default=None
    )
    auto_create_template_id: Optional[str] = Field(
        alias="autoCreateTemplateId", default=None
    )
    post_cancellation_updates: Optional[bool] = Field(
        alias="postCancellationUpdates", default=None
    )


class SharedSlackSettingsInput(BaseModel):
    team_name: Optional[str] = Field(alias="teamName", default=None)
    team_id: Optional[str] = Field(alias="teamId", default=None)
    enterprise_name: Optional[str] = Field(alias="enterpriseName", default=None)
    enterprise_id: Optional[str] = Field(alias="enterpriseId", default=None)
    should_unfurl: Optional[bool] = Field(alias="shouldUnfurl", default=None)


class SlackAsksSettingsInput(BaseModel):
    team_name: Optional[str] = Field(alias="teamName", default=None)
    team_id: Optional[str] = Field(alias="teamId", default=None)
    enterprise_name: Optional[str] = Field(alias="enterpriseName", default=None)
    enterprise_id: Optional[str] = Field(alias="enterpriseId", default=None)
    should_unfurl: Optional[bool] = Field(alias="shouldUnfurl", default=None)
    slack_channel_mapping: Optional[List["SlackChannelNameMappingInput"]] = Field(
        alias="slackChannelMapping", default=None
    )
    can_administrate: UserRoleType = Field(alias="canAdministrate")


class IntercomSettingsInput(BaseModel):
    send_note_on_status_change: Optional[bool] = Field(
        alias="sendNoteOnStatusChange", default=None
    )
    send_note_on_comment: Optional[bool] = Field(
        alias="sendNoteOnComment", default=None
    )
    automate_ticket_reopening_on_completion: Optional[bool] = Field(
        alias="automateTicketReopeningOnCompletion", default=None
    )
    automate_ticket_reopening_on_cancellation: Optional[bool] = Field(
        alias="automateTicketReopeningOnCancellation", default=None
    )
    automate_ticket_reopening_on_comment: Optional[bool] = Field(
        alias="automateTicketReopeningOnComment", default=None
    )


class FrontSettingsInput(BaseModel):
    send_note_on_status_change: Optional[bool] = Field(
        alias="sendNoteOnStatusChange", default=None
    )
    send_note_on_comment: Optional[bool] = Field(
        alias="sendNoteOnComment", default=None
    )
    automate_ticket_reopening_on_completion: Optional[bool] = Field(
        alias="automateTicketReopeningOnCompletion", default=None
    )
    automate_ticket_reopening_on_cancellation: Optional[bool] = Field(
        alias="automateTicketReopeningOnCancellation", default=None
    )
    automate_ticket_reopening_on_comment: Optional[bool] = Field(
        alias="automateTicketReopeningOnComment", default=None
    )


class SlackSettingsInput(BaseModel):
    team_name: Optional[str] = Field(alias="teamName", default=None)
    team_id: Optional[str] = Field(alias="teamId", default=None)
    enterprise_name: Optional[str] = Field(alias="enterpriseName", default=None)
    enterprise_id: Optional[str] = Field(alias="enterpriseId", default=None)
    should_unfurl: Optional[bool] = Field(alias="shouldUnfurl", default=None)
    link_on_issue_id_mention: bool = Field(alias="linkOnIssueIdMention")


class SlackPostSettingsInput(BaseModel):
    channel: str
    channel_id: str = Field(alias="channelId")
    configuration_url: str = Field(alias="configurationUrl")
    channel_type: Optional[SlackChannelType] = Field(alias="channelType", default=None)


class GitHubSettingsInput(BaseModel):
    org_avatar_url: Optional[str] = Field(alias="orgAvatarUrl", default=None)
    org_login: str = Field(alias="orgLogin")
    repositories: Optional[List["GitHubRepoInput"]] = None
    repositories_mapping: Optional[List["TeamRepoMappingInput"]] = Field(
        alias="repositoriesMapping", default=None
    )
    org_type: Optional[GithubOrgType] = Field(alias="orgType", default=None)


class GitHubImportSettingsInput(BaseModel):
    org_login: str = Field(alias="orgLogin")
    org_avatar_url: str = Field(alias="orgAvatarUrl")
    repositories: List["GitHubRepoInput"]
    org_type: GithubOrgType = Field(alias="orgType")


class GitHubPersonalSettingsInput(BaseModel):
    login: str


class GitHubRepoInput(BaseModel):
    full_name: str = Field(alias="fullName")
    id: float


class TeamRepoMappingInput(BaseModel):
    linear_team_id: str = Field(alias="linearTeamId")
    git_hub_repo_id: float = Field(alias="gitHubRepoId")
    bidirectional: Optional[bool] = None
    default: Optional[bool] = None


class GitLabSettingsInput(BaseModel):
    url: Optional[str] = None
    readonly: Optional[bool] = None
    expires_at: Optional[str] = Field(alias="expiresAt", default=None)


class GoogleSheetsSettingsInput(BaseModel):
    spreadsheet_id: str = Field(alias="spreadsheetId")
    spreadsheet_url: str = Field(alias="spreadsheetUrl")
    sheet_id: float = Field(alias="sheetId")
    updated_issues_at: Optional[Any] = Field(alias="updatedIssuesAt", default=None)


class JiraProjectDataInput(BaseModel):
    id: str
    key: str
    name: str


class JiraLinearMappingInput(BaseModel):
    jira_project_id: str = Field(alias="jiraProjectId")
    linear_team_id: str = Field(alias="linearTeamId")
    bidirectional: Optional[bool] = None
    default: Optional[bool] = None


class JiraSettingsInput(BaseModel):
    project_mapping: Optional[List["JiraLinearMappingInput"]] = Field(
        alias="projectMapping", default=None
    )
    projects: List["JiraProjectDataInput"]
    is_jira_server: Optional[bool] = Field(alias="isJiraServer", default=False)
    setup_pending: Optional[bool] = Field(alias="setupPending", default=None)
    manual_setup: Optional[bool] = Field(alias="manualSetup", default=None)


class LaunchDarklySettingsInput(BaseModel):
    project_key: str = Field(alias="projectKey")
    environment: str


class JiraPersonalSettingsInput(BaseModel):
    site_name: Optional[str] = Field(alias="siteName", default=None)


class NotionSettingsInput(BaseModel):
    workspace_id: str = Field(alias="workspaceId")
    workspace_name: str = Field(alias="workspaceName")


class OpsgenieInput(BaseModel):
    api_failed_with_unauthorized_error_at: Optional[Any] = Field(
        alias="apiFailedWithUnauthorizedErrorAt", default=None
    )


class PagerDutyInput(BaseModel):
    api_failed_with_unauthorized_error_at: Optional[Any] = Field(
        alias="apiFailedWithUnauthorizedErrorAt", default=None
    )


class SentrySettingsInput(BaseModel):
    organization_slug: str = Field(alias="organizationSlug")


class ZendeskSettingsInput(BaseModel):
    send_note_on_status_change: Optional[bool] = Field(
        alias="sendNoteOnStatusChange", default=None
    )
    send_note_on_comment: Optional[bool] = Field(
        alias="sendNoteOnComment", default=None
    )
    automate_ticket_reopening_on_completion: Optional[bool] = Field(
        alias="automateTicketReopeningOnCompletion", default=None
    )
    automate_ticket_reopening_on_cancellation: Optional[bool] = Field(
        alias="automateTicketReopeningOnCancellation", default=None
    )
    automate_ticket_reopening_on_comment: Optional[bool] = Field(
        alias="automateTicketReopeningOnComment", default=None
    )
    subdomain: str
    url: str
    bot_user_id: Optional[str] = Field(alias="botUserId", default=None)


class IntegrationSettingsInput(BaseModel):
    slack: Optional["SlackSettingsInput"] = None
    slack_asks: Optional["SlackAsksSettingsInput"] = Field(
        alias="slackAsks", default=None
    )
    slack_post: Optional["SlackPostSettingsInput"] = Field(
        alias="slackPost", default=None
    )
    slack_project_post: Optional["SlackPostSettingsInput"] = Field(
        alias="slackProjectPost", default=None
    )
    slack_custom_view_notifications: Optional["SlackPostSettingsInput"] = Field(
        alias="slackCustomViewNotifications", default=None
    )
    slack_org_project_updates_post: Optional["SlackPostSettingsInput"] = Field(
        alias="slackOrgProjectUpdatesPost", default=None
    )
    google_sheets: Optional["GoogleSheetsSettingsInput"] = Field(
        alias="googleSheets", default=None
    )
    git_hub: Optional["GitHubSettingsInput"] = Field(alias="gitHub", default=None)
    git_hub_import: Optional["GitHubImportSettingsInput"] = Field(
        alias="gitHubImport", default=None
    )
    git_hub_personal: Optional["GitHubPersonalSettingsInput"] = Field(
        alias="gitHubPersonal", default=None
    )
    git_lab: Optional["GitLabSettingsInput"] = Field(alias="gitLab", default=None)
    sentry: Optional["SentrySettingsInput"] = None
    zendesk: Optional["ZendeskSettingsInput"] = None
    intercom: Optional["IntercomSettingsInput"] = None
    front: Optional["FrontSettingsInput"] = None
    jira: Optional["JiraSettingsInput"] = None
    notion: Optional["NotionSettingsInput"] = None
    opsgenie: Optional["OpsgenieInput"] = None
    pager_duty: Optional["PagerDutyInput"] = Field(alias="pagerDuty", default=None)
    launch_darkly: Optional["LaunchDarklySettingsInput"] = Field(
        alias="launchDarkly", default=None
    )
    jira_personal: Optional["JiraPersonalSettingsInput"] = Field(
        alias="jiraPersonal", default=None
    )


class AttachmentFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    title: Optional["StringComparator"] = None
    subtitle: Optional["NullableStringComparator"] = None
    url: Optional["StringComparator"] = None
    creator: Optional["NullableUserFilter"] = None
    source_type: Optional["SourceTypeComparator"] = Field(
        alias="sourceType", default=None
    )
    and_: Optional[List["AttachmentFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["AttachmentFilter"]] = Field(alias="or", default=None)


class AttachmentCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    title: Optional["StringComparator"] = None
    subtitle: Optional["NullableStringComparator"] = None
    url: Optional["StringComparator"] = None
    creator: Optional["NullableUserFilter"] = None
    source_type: Optional["SourceTypeComparator"] = Field(
        alias="sourceType", default=None
    )
    and_: Optional[List["AttachmentCollectionFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["AttachmentCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["AttachmentFilter"] = None
    every: Optional["AttachmentFilter"] = None
    length: Optional["NumberComparator"] = None


class AuditEntryFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    type: Optional["StringComparator"] = None
    ip: Optional["StringComparator"] = None
    country_code: Optional["StringComparator"] = Field(
        alias="countryCode", default=None
    )
    actor: Optional["NullableUserFilter"] = None


class StringItemComparator(BaseModel):
    eq: Optional[str] = None
    neq: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    nin: Optional[List[str]] = None
    eq_ignore_case: Optional[str] = Field(alias="eqIgnoreCase", default=None)
    neq_ignore_case: Optional[str] = Field(alias="neqIgnoreCase", default=None)
    starts_with: Optional[str] = Field(alias="startsWith", default=None)
    starts_with_ignore_case: Optional[str] = Field(
        alias="startsWithIgnoreCase", default=None
    )
    not_starts_with: Optional[str] = Field(alias="notStartsWith", default=None)
    ends_with: Optional[str] = Field(alias="endsWith", default=None)
    not_ends_with: Optional[str] = Field(alias="notEndsWith", default=None)
    contains: Optional[str] = None
    contains_ignore_case: Optional[str] = Field(
        alias="containsIgnoreCase", default=None
    )
    not_contains: Optional[str] = Field(alias="notContains", default=None)
    not_contains_ignore_case: Optional[str] = Field(
        alias="notContainsIgnoreCase", default=None
    )


class StringArrayComparator(BaseModel):
    length: Optional["NumberComparator"] = None
    every: Optional[List["StringItemComparator"]] = None
    some: Optional[List["StringItemComparator"]] = None


class CustomerFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slack_channel_id: Optional["StringComparator"] = Field(
        alias="slackChannelId", default=None
    )
    domains: Optional["StringArrayComparator"] = None
    external_ids: Optional["StringArrayComparator"] = Field(
        alias="externalIds", default=None
    )
    owner: Optional["UserFilter"] = None
    needs: Optional["CustomerNeedCollectionFilter"] = None
    and_: Optional[List["CustomerFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["CustomerFilter"]] = Field(alias="or", default=None)


class CustomerCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slack_channel_id: Optional["StringComparator"] = Field(
        alias="slackChannelId", default=None
    )
    domains: Optional["StringArrayComparator"] = None
    external_ids: Optional["StringArrayComparator"] = Field(
        alias="externalIds", default=None
    )
    owner: Optional["UserFilter"] = None
    needs: Optional["CustomerNeedCollectionFilter"] = None
    and_: Optional[List["CustomerCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["CustomerCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["CustomerFilter"] = None
    every: Optional["CustomerFilter"] = None
    length: Optional["NumberComparator"] = None


class CustomerNeedFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    priority: Optional["NumberComparator"] = None
    project: Optional["NullableProjectFilter"] = None
    issue: Optional["NullableIssueFilter"] = None
    comment: Optional["NullableCommentFilter"] = None
    customer: Optional["CustomerFilter"] = None
    and_: Optional[List["CustomerNeedFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["CustomerNeedFilter"]] = Field(alias="or", default=None)


class CustomerNeedCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    priority: Optional["NumberComparator"] = None
    project: Optional["NullableProjectFilter"] = None
    issue: Optional["NullableIssueFilter"] = None
    comment: Optional["NullableCommentFilter"] = None
    customer: Optional["CustomerFilter"] = None
    and_: Optional[List["CustomerNeedCollectionFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["CustomerNeedCollectionFilter"]] = Field(
        alias="or", default=None
    )
    some: Optional["CustomerNeedFilter"] = None
    every: Optional["CustomerNeedFilter"] = None
    length: Optional["NumberComparator"] = None


class CommentFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    body: Optional["StringComparator"] = None
    user: Optional["UserFilter"] = None
    issue: Optional["NullableIssueFilter"] = None
    project_update: Optional["ProjectUpdateFilter"] = Field(
        alias="projectUpdate", default=None
    )
    parent: Optional["NullableCommentFilter"] = None
    document_content: Optional["DocumentContentFilter"] = Field(
        alias="documentContent", default=None
    )
    reactions: Optional["ReactionCollectionFilter"] = None
    needs: Optional["CustomerNeedCollectionFilter"] = None
    and_: Optional[List["CommentFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["CommentFilter"]] = Field(alias="or", default=None)


class NullableCommentFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    body: Optional["StringComparator"] = None
    user: Optional["UserFilter"] = None
    issue: Optional["NullableIssueFilter"] = None
    project_update: Optional["ProjectUpdateFilter"] = Field(
        alias="projectUpdate", default=None
    )
    parent: Optional["NullableCommentFilter"] = None
    document_content: Optional["DocumentContentFilter"] = Field(
        alias="documentContent", default=None
    )
    reactions: Optional["ReactionCollectionFilter"] = None
    needs: Optional["CustomerNeedCollectionFilter"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableCommentFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableCommentFilter"]] = Field(alias="or", default=None)


class CommentCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    body: Optional["StringComparator"] = None
    user: Optional["UserFilter"] = None
    issue: Optional["NullableIssueFilter"] = None
    project_update: Optional["ProjectUpdateFilter"] = Field(
        alias="projectUpdate", default=None
    )
    parent: Optional["NullableCommentFilter"] = None
    document_content: Optional["DocumentContentFilter"] = Field(
        alias="documentContent", default=None
    )
    reactions: Optional["ReactionCollectionFilter"] = None
    needs: Optional["CustomerNeedCollectionFilter"] = None
    and_: Optional[List["CommentCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["CommentCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["CommentFilter"] = None
    every: Optional["CommentFilter"] = None
    length: Optional["NumberComparator"] = None


class CycleFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    number: Optional["NumberComparator"] = None
    name: Optional["StringComparator"] = None
    starts_at: Optional["DateComparator"] = Field(alias="startsAt", default=None)
    ends_at: Optional["DateComparator"] = Field(alias="endsAt", default=None)
    completed_at: Optional["DateComparator"] = Field(alias="completedAt", default=None)
    is_active: Optional["BooleanComparator"] = Field(alias="isActive", default=None)
    is_in_cooldown: Optional["BooleanComparator"] = Field(
        alias="isInCooldown", default=None
    )
    is_next: Optional["BooleanComparator"] = Field(alias="isNext", default=None)
    is_previous: Optional["BooleanComparator"] = Field(alias="isPrevious", default=None)
    is_future: Optional["BooleanComparator"] = Field(alias="isFuture", default=None)
    is_past: Optional["BooleanComparator"] = Field(alias="isPast", default=None)
    team: Optional["TeamFilter"] = None
    issues: Optional["IssueCollectionFilter"] = None
    and_: Optional[List["CycleFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["CycleFilter"]] = Field(alias="or", default=None)


class NullableCycleFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    number: Optional["NumberComparator"] = None
    name: Optional["StringComparator"] = None
    starts_at: Optional["DateComparator"] = Field(alias="startsAt", default=None)
    ends_at: Optional["DateComparator"] = Field(alias="endsAt", default=None)
    completed_at: Optional["DateComparator"] = Field(alias="completedAt", default=None)
    is_active: Optional["BooleanComparator"] = Field(alias="isActive", default=None)
    is_in_cooldown: Optional["BooleanComparator"] = Field(
        alias="isInCooldown", default=None
    )
    is_next: Optional["BooleanComparator"] = Field(alias="isNext", default=None)
    is_previous: Optional["BooleanComparator"] = Field(alias="isPrevious", default=None)
    is_future: Optional["BooleanComparator"] = Field(alias="isFuture", default=None)
    is_past: Optional["BooleanComparator"] = Field(alias="isPast", default=None)
    team: Optional["TeamFilter"] = None
    issues: Optional["IssueCollectionFilter"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableCycleFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableCycleFilter"]] = Field(alias="or", default=None)


class ProjectStatusFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    description: Optional["StringComparator"] = None
    position: Optional["NumberComparator"] = None
    type: Optional["StringComparator"] = None
    projects: Optional["ProjectCollectionFilter"] = None
    and_: Optional[List["ProjectStatusFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ProjectStatusFilter"]] = Field(alias="or", default=None)


class SlaStatusComparator(BaseModel):
    eq: Optional[SlaStatus] = None
    neq: Optional[SlaStatus] = None
    in_: Optional[List[SlaStatus]] = Field(alias="in", default=None)
    nin: Optional[List[SlaStatus]] = None
    null: Optional[bool] = None


class NullableIssueFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    number: Optional["NumberComparator"] = None
    title: Optional["StringComparator"] = None
    description: Optional["NullableStringComparator"] = None
    priority: Optional["NullableNumberComparator"] = None
    estimate: Optional["EstimateComparator"] = None
    started_at: Optional["NullableDateComparator"] = Field(
        alias="startedAt", default=None
    )
    triaged_at: Optional["NullableDateComparator"] = Field(
        alias="triagedAt", default=None
    )
    completed_at: Optional["NullableDateComparator"] = Field(
        alias="completedAt", default=None
    )
    canceled_at: Optional["NullableDateComparator"] = Field(
        alias="canceledAt", default=None
    )
    auto_closed_at: Optional["NullableDateComparator"] = Field(
        alias="autoClosedAt", default=None
    )
    auto_archived_at: Optional["NullableDateComparator"] = Field(
        alias="autoArchivedAt", default=None
    )
    due_date: Optional["NullableTimelessDateComparator"] = Field(
        alias="dueDate", default=None
    )
    snoozed_until_at: Optional["NullableDateComparator"] = Field(
        alias="snoozedUntilAt", default=None
    )
    assignee: Optional["NullableUserFilter"] = None
    last_applied_template: Optional["NullableTemplateFilter"] = Field(
        alias="lastAppliedTemplate", default=None
    )
    source_metadata: Optional["SourceMetadataComparator"] = Field(
        alias="sourceMetadata", default=None
    )
    creator: Optional["NullableUserFilter"] = None
    parent: Optional["NullableIssueFilter"] = None
    snoozed_by: Optional["NullableUserFilter"] = Field(alias="snoozedBy", default=None)
    labels: Optional["IssueLabelCollectionFilter"] = None
    subscribers: Optional["UserCollectionFilter"] = None
    team: Optional["TeamFilter"] = None
    project_milestone: Optional["NullableProjectMilestoneFilter"] = Field(
        alias="projectMilestone", default=None
    )
    comments: Optional["CommentCollectionFilter"] = None
    cycle: Optional["NullableCycleFilter"] = None
    project: Optional["NullableProjectFilter"] = None
    state: Optional["WorkflowStateFilter"] = None
    children: Optional["IssueCollectionFilter"] = None
    attachments: Optional["AttachmentCollectionFilter"] = None
    searchable_content: Optional["ContentComparator"] = Field(
        alias="searchableContent", default=None
    )
    has_related_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasRelatedRelations", default=None
    )
    has_duplicate_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDuplicateRelations", default=None
    )
    has_blocked_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockedByRelations", default=None
    )
    has_blocking_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockingRelations", default=None
    )
    sla_status: Optional["SlaStatusComparator"] = Field(alias="slaStatus", default=None)
    reactions: Optional["ReactionCollectionFilter"] = None
    needs: Optional["CustomerNeedFilter"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableIssueFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableIssueFilter"]] = Field(alias="or", default=None)


class IssueFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    number: Optional["NumberComparator"] = None
    title: Optional["StringComparator"] = None
    description: Optional["NullableStringComparator"] = None
    priority: Optional["NullableNumberComparator"] = None
    estimate: Optional["EstimateComparator"] = None
    started_at: Optional["NullableDateComparator"] = Field(
        alias="startedAt", default=None
    )
    triaged_at: Optional["NullableDateComparator"] = Field(
        alias="triagedAt", default=None
    )
    completed_at: Optional["NullableDateComparator"] = Field(
        alias="completedAt", default=None
    )
    canceled_at: Optional["NullableDateComparator"] = Field(
        alias="canceledAt", default=None
    )
    auto_closed_at: Optional["NullableDateComparator"] = Field(
        alias="autoClosedAt", default=None
    )
    auto_archived_at: Optional["NullableDateComparator"] = Field(
        alias="autoArchivedAt", default=None
    )
    due_date: Optional["NullableTimelessDateComparator"] = Field(
        alias="dueDate", default=None
    )
    snoozed_until_at: Optional["NullableDateComparator"] = Field(
        alias="snoozedUntilAt", default=None
    )
    assignee: Optional["NullableUserFilter"] = None
    last_applied_template: Optional["NullableTemplateFilter"] = Field(
        alias="lastAppliedTemplate", default=None
    )
    source_metadata: Optional["SourceMetadataComparator"] = Field(
        alias="sourceMetadata", default=None
    )
    creator: Optional["NullableUserFilter"] = None
    parent: Optional["NullableIssueFilter"] = None
    snoozed_by: Optional["NullableUserFilter"] = Field(alias="snoozedBy", default=None)
    labels: Optional["IssueLabelCollectionFilter"] = None
    subscribers: Optional["UserCollectionFilter"] = None
    team: Optional["TeamFilter"] = None
    project_milestone: Optional["NullableProjectMilestoneFilter"] = Field(
        alias="projectMilestone", default=None
    )
    comments: Optional["CommentCollectionFilter"] = None
    cycle: Optional["NullableCycleFilter"] = None
    project: Optional["NullableProjectFilter"] = None
    state: Optional["WorkflowStateFilter"] = None
    children: Optional["IssueCollectionFilter"] = None
    attachments: Optional["AttachmentCollectionFilter"] = None
    searchable_content: Optional["ContentComparator"] = Field(
        alias="searchableContent", default=None
    )
    has_related_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasRelatedRelations", default=None
    )
    has_duplicate_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDuplicateRelations", default=None
    )
    has_blocked_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockedByRelations", default=None
    )
    has_blocking_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockingRelations", default=None
    )
    sla_status: Optional["SlaStatusComparator"] = Field(alias="slaStatus", default=None)
    reactions: Optional["ReactionCollectionFilter"] = None
    needs: Optional["CustomerNeedFilter"] = None
    and_: Optional[List["IssueFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["IssueFilter"]] = Field(alias="or", default=None)


class IssueCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    number: Optional["NumberComparator"] = None
    title: Optional["StringComparator"] = None
    description: Optional["NullableStringComparator"] = None
    priority: Optional["NullableNumberComparator"] = None
    estimate: Optional["EstimateComparator"] = None
    started_at: Optional["NullableDateComparator"] = Field(
        alias="startedAt", default=None
    )
    triaged_at: Optional["NullableDateComparator"] = Field(
        alias="triagedAt", default=None
    )
    completed_at: Optional["NullableDateComparator"] = Field(
        alias="completedAt", default=None
    )
    canceled_at: Optional["NullableDateComparator"] = Field(
        alias="canceledAt", default=None
    )
    auto_closed_at: Optional["NullableDateComparator"] = Field(
        alias="autoClosedAt", default=None
    )
    auto_archived_at: Optional["NullableDateComparator"] = Field(
        alias="autoArchivedAt", default=None
    )
    due_date: Optional["NullableTimelessDateComparator"] = Field(
        alias="dueDate", default=None
    )
    snoozed_until_at: Optional["NullableDateComparator"] = Field(
        alias="snoozedUntilAt", default=None
    )
    assignee: Optional["NullableUserFilter"] = None
    last_applied_template: Optional["NullableTemplateFilter"] = Field(
        alias="lastAppliedTemplate", default=None
    )
    source_metadata: Optional["SourceMetadataComparator"] = Field(
        alias="sourceMetadata", default=None
    )
    creator: Optional["NullableUserFilter"] = None
    parent: Optional["NullableIssueFilter"] = None
    snoozed_by: Optional["NullableUserFilter"] = Field(alias="snoozedBy", default=None)
    labels: Optional["IssueLabelCollectionFilter"] = None
    subscribers: Optional["UserCollectionFilter"] = None
    team: Optional["TeamFilter"] = None
    project_milestone: Optional["NullableProjectMilestoneFilter"] = Field(
        alias="projectMilestone", default=None
    )
    comments: Optional["CommentCollectionFilter"] = None
    cycle: Optional["NullableCycleFilter"] = None
    project: Optional["NullableProjectFilter"] = None
    state: Optional["WorkflowStateFilter"] = None
    children: Optional["IssueCollectionFilter"] = None
    attachments: Optional["AttachmentCollectionFilter"] = None
    searchable_content: Optional["ContentComparator"] = Field(
        alias="searchableContent", default=None
    )
    has_related_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasRelatedRelations", default=None
    )
    has_duplicate_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDuplicateRelations", default=None
    )
    has_blocked_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockedByRelations", default=None
    )
    has_blocking_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockingRelations", default=None
    )
    sla_status: Optional["SlaStatusComparator"] = Field(alias="slaStatus", default=None)
    reactions: Optional["ReactionCollectionFilter"] = None
    needs: Optional["CustomerNeedFilter"] = None
    and_: Optional[List["IssueCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["IssueCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["IssueFilter"] = None
    every: Optional["IssueFilter"] = None
    length: Optional["NumberComparator"] = None


class NullableTemplateFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableTemplateFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableTemplateFilter"]] = Field(alias="or", default=None)


class UserFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    display_name: Optional["StringComparator"] = Field(
        alias="displayName", default=None
    )
    email: Optional["StringComparator"] = None
    active: Optional["BooleanComparator"] = None
    assigned_issues: Optional["IssueCollectionFilter"] = Field(
        alias="assignedIssues", default=None
    )
    admin: Optional["BooleanComparator"] = None
    is_me: Optional["BooleanComparator"] = Field(alias="isMe", default=None)
    and_: Optional[List["UserFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["UserFilter"]] = Field(alias="or", default=None)


class NullableUserFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    display_name: Optional["StringComparator"] = Field(
        alias="displayName", default=None
    )
    email: Optional["StringComparator"] = None
    active: Optional["BooleanComparator"] = None
    assigned_issues: Optional["IssueCollectionFilter"] = Field(
        alias="assignedIssues", default=None
    )
    admin: Optional["BooleanComparator"] = None
    is_me: Optional["BooleanComparator"] = Field(alias="isMe", default=None)
    null: Optional[bool] = None
    and_: Optional[List["NullableUserFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableUserFilter"]] = Field(alias="or", default=None)


class UserCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    display_name: Optional["StringComparator"] = Field(
        alias="displayName", default=None
    )
    email: Optional["StringComparator"] = None
    active: Optional["BooleanComparator"] = None
    assigned_issues: Optional["IssueCollectionFilter"] = Field(
        alias="assignedIssues", default=None
    )
    admin: Optional["BooleanComparator"] = None
    is_me: Optional["BooleanComparator"] = Field(alias="isMe", default=None)
    and_: Optional[List["UserCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["UserCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["UserFilter"] = None
    every: Optional["UserFilter"] = None
    length: Optional["NumberComparator"] = None


class InitiativeFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    status: Optional["StringComparator"] = None
    creator: Optional["UserFilter"] = None
    and_: Optional[List["InitiativeFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["InitiativeFilter"]] = Field(alias="or", default=None)


class InitiativeCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    status: Optional["StringComparator"] = None
    creator: Optional["UserFilter"] = None
    and_: Optional[List["InitiativeCollectionFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["InitiativeCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["InitiativeFilter"] = None
    every: Optional["InitiativeFilter"] = None
    length: Optional["NumberComparator"] = None


class ProjectUpdatesFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    health: Optional["StringComparator"] = None
    and_: Optional[List["ProjectUpdatesFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ProjectUpdatesFilter"]] = Field(alias="or", default=None)


class NullableProjectUpdatesFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    health: Optional["StringComparator"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableProjectUpdatesFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["NullableProjectUpdatesFilter"]] = Field(
        alias="or", default=None
    )


class ProjectUpdatesCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    health: Optional["StringComparator"] = None
    and_: Optional[List["ProjectUpdatesCollectionFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["ProjectUpdatesCollectionFilter"]] = Field(
        alias="or", default=None
    )
    some: Optional["ProjectUpdatesFilter"] = None
    every: Optional["ProjectUpdatesFilter"] = None
    length: Optional["NumberComparator"] = None


class ProjectFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    state: Optional["StringComparator"] = None
    status: Optional["ProjectStatusFilter"] = None
    priority: Optional["NullableNumberComparator"] = None
    searchable_content: Optional["ContentComparator"] = Field(
        alias="searchableContent", default=None
    )
    completed_at: Optional["NullableDateComparator"] = Field(
        alias="completedAt", default=None
    )
    start_date: Optional["NullableDateComparator"] = Field(
        alias="startDate", default=None
    )
    target_date: Optional["NullableDateComparator"] = Field(
        alias="targetDate", default=None
    )
    health: Optional["StringComparator"] = None
    has_related_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasRelatedRelations", default=None
    )
    has_depended_on_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDependedOnByRelations", default=None
    )
    has_depends_on_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDependsOnRelations", default=None
    )
    has_blocked_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockedByRelations", default=None
    )
    has_blocking_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockingRelations", default=None
    )
    project_updates: Optional["ProjectUpdatesCollectionFilter"] = Field(
        alias="projectUpdates", default=None
    )
    creator: Optional["UserFilter"] = None
    lead: Optional["NullableUserFilter"] = None
    members: Optional["UserCollectionFilter"] = None
    issues: Optional["IssueCollectionFilter"] = None
    roadmaps: Optional["RoadmapCollectionFilter"] = None
    initiatives: Optional["InitiativeCollectionFilter"] = None
    project_milestones: Optional["ProjectMilestoneCollectionFilter"] = Field(
        alias="projectMilestones", default=None
    )
    completed_project_milestones: Optional["ProjectMilestoneCollectionFilter"] = Field(
        alias="completedProjectMilestones", default=None
    )
    next_project_milestone: Optional["ProjectMilestoneFilter"] = Field(
        alias="nextProjectMilestone", default=None
    )
    accessible_teams: Optional["TeamCollectionFilter"] = Field(
        alias="accessibleTeams", default=None
    )
    last_applied_template: Optional["NullableTemplateFilter"] = Field(
        alias="lastAppliedTemplate", default=None
    )
    needs: Optional["CustomerNeedCollectionFilter"] = None
    and_: Optional[List["ProjectFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ProjectFilter"]] = Field(alias="or", default=None)


class NullableProjectFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    state: Optional["StringComparator"] = None
    status: Optional["ProjectStatusFilter"] = None
    priority: Optional["NullableNumberComparator"] = None
    searchable_content: Optional["ContentComparator"] = Field(
        alias="searchableContent", default=None
    )
    completed_at: Optional["NullableDateComparator"] = Field(
        alias="completedAt", default=None
    )
    start_date: Optional["NullableDateComparator"] = Field(
        alias="startDate", default=None
    )
    target_date: Optional["NullableDateComparator"] = Field(
        alias="targetDate", default=None
    )
    health: Optional["StringComparator"] = None
    has_related_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasRelatedRelations", default=None
    )
    has_depended_on_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDependedOnByRelations", default=None
    )
    has_depends_on_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDependsOnRelations", default=None
    )
    has_blocked_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockedByRelations", default=None
    )
    has_blocking_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockingRelations", default=None
    )
    project_updates: Optional["ProjectUpdatesCollectionFilter"] = Field(
        alias="projectUpdates", default=None
    )
    creator: Optional["UserFilter"] = None
    lead: Optional["NullableUserFilter"] = None
    members: Optional["UserCollectionFilter"] = None
    issues: Optional["IssueCollectionFilter"] = None
    roadmaps: Optional["RoadmapCollectionFilter"] = None
    initiatives: Optional["InitiativeCollectionFilter"] = None
    project_milestones: Optional["ProjectMilestoneCollectionFilter"] = Field(
        alias="projectMilestones", default=None
    )
    completed_project_milestones: Optional["ProjectMilestoneCollectionFilter"] = Field(
        alias="completedProjectMilestones", default=None
    )
    next_project_milestone: Optional["ProjectMilestoneFilter"] = Field(
        alias="nextProjectMilestone", default=None
    )
    accessible_teams: Optional["TeamCollectionFilter"] = Field(
        alias="accessibleTeams", default=None
    )
    last_applied_template: Optional["NullableTemplateFilter"] = Field(
        alias="lastAppliedTemplate", default=None
    )
    needs: Optional["CustomerNeedCollectionFilter"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableProjectFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableProjectFilter"]] = Field(alias="or", default=None)


class ProjectCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    state: Optional["StringComparator"] = None
    status: Optional["ProjectStatusFilter"] = None
    priority: Optional["NullableNumberComparator"] = None
    searchable_content: Optional["ContentComparator"] = Field(
        alias="searchableContent", default=None
    )
    completed_at: Optional["NullableDateComparator"] = Field(
        alias="completedAt", default=None
    )
    start_date: Optional["NullableDateComparator"] = Field(
        alias="startDate", default=None
    )
    target_date: Optional["NullableDateComparator"] = Field(
        alias="targetDate", default=None
    )
    health: Optional["StringComparator"] = None
    has_related_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasRelatedRelations", default=None
    )
    has_depended_on_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDependedOnByRelations", default=None
    )
    has_depends_on_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasDependsOnRelations", default=None
    )
    has_blocked_by_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockedByRelations", default=None
    )
    has_blocking_relations: Optional["RelationExistsComparator"] = Field(
        alias="hasBlockingRelations", default=None
    )
    project_updates: Optional["ProjectUpdatesCollectionFilter"] = Field(
        alias="projectUpdates", default=None
    )
    creator: Optional["UserFilter"] = None
    lead: Optional["NullableUserFilter"] = None
    members: Optional["UserCollectionFilter"] = None
    issues: Optional["IssueCollectionFilter"] = None
    roadmaps: Optional["RoadmapCollectionFilter"] = None
    initiatives: Optional["InitiativeCollectionFilter"] = None
    project_milestones: Optional["ProjectMilestoneCollectionFilter"] = Field(
        alias="projectMilestones", default=None
    )
    completed_project_milestones: Optional["ProjectMilestoneCollectionFilter"] = Field(
        alias="completedProjectMilestones", default=None
    )
    next_project_milestone: Optional["ProjectMilestoneFilter"] = Field(
        alias="nextProjectMilestone", default=None
    )
    accessible_teams: Optional["TeamCollectionFilter"] = Field(
        alias="accessibleTeams", default=None
    )
    last_applied_template: Optional["NullableTemplateFilter"] = Field(
        alias="lastAppliedTemplate", default=None
    )
    needs: Optional["CustomerNeedCollectionFilter"] = None
    and_: Optional[List["ProjectCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ProjectCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["ProjectFilter"] = None
    every: Optional["ProjectFilter"] = None
    length: Optional["NumberComparator"] = None


class ProjectMilestoneFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    target_date: Optional["NullableDateComparator"] = Field(
        alias="targetDate", default=None
    )
    and_: Optional[List["ProjectMilestoneFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ProjectMilestoneFilter"]] = Field(alias="or", default=None)


class NullableProjectMilestoneFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    target_date: Optional["NullableDateComparator"] = Field(
        alias="targetDate", default=None
    )
    null: Optional[bool] = None
    and_: Optional[List["NullableProjectMilestoneFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["NullableProjectMilestoneFilter"]] = Field(
        alias="or", default=None
    )


class ProjectMilestoneCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    target_date: Optional["NullableDateComparator"] = Field(
        alias="targetDate", default=None
    )
    and_: Optional[List["ProjectMilestoneCollectionFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["ProjectMilestoneCollectionFilter"]] = Field(
        alias="or", default=None
    )
    some: Optional["ProjectMilestoneFilter"] = None
    every: Optional["ProjectMilestoneFilter"] = None
    length: Optional["NumberComparator"] = None


class RoadmapFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    creator: Optional["UserFilter"] = None
    and_: Optional[List["RoadmapFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["RoadmapFilter"]] = Field(alias="or", default=None)


class RoadmapCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    creator: Optional["UserFilter"] = None
    and_: Optional[List["RoadmapCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["RoadmapCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["RoadmapFilter"] = None
    every: Optional["RoadmapFilter"] = None
    length: Optional["NumberComparator"] = None


class TeamFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    key: Optional["StringComparator"] = None
    description: Optional["NullableStringComparator"] = None
    issues: Optional["IssueCollectionFilter"] = None
    and_: Optional[List["TeamFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["TeamFilter"]] = Field(alias="or", default=None)


class NullableTeamFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    key: Optional["StringComparator"] = None
    description: Optional["NullableStringComparator"] = None
    issues: Optional["IssueCollectionFilter"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableTeamFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableTeamFilter"]] = Field(alias="or", default=None)


class TeamCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    and_: Optional[List["TeamCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["TeamCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["TeamFilter"] = None
    every: Optional["TeamFilter"] = None
    length: Optional["NumberComparator"] = None


class WorkflowStateFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    description: Optional["StringComparator"] = None
    position: Optional["NumberComparator"] = None
    type: Optional["StringComparator"] = None
    team: Optional["TeamFilter"] = None
    issues: Optional["IssueCollectionFilter"] = None
    and_: Optional[List["WorkflowStateFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["WorkflowStateFilter"]] = Field(alias="or", default=None)


class NullableDocumentContentFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    project: Optional["ProjectFilter"] = None
    document: Optional["DocumentFilter"] = None


class DocumentContentFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    project: Optional["ProjectFilter"] = None
    document: Optional["DocumentFilter"] = None


class IssueLabelFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    creator: Optional["NullableUserFilter"] = None
    team: Optional["NullableTeamFilter"] = None
    parent: Optional["IssueLabelFilter"] = None
    and_: Optional[List["IssueLabelFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["IssueLabelFilter"]] = Field(alias="or", default=None)


class IssueLabelCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    name: Optional["StringComparator"] = None
    creator: Optional["NullableUserFilter"] = None
    team: Optional["NullableTeamFilter"] = None
    parent: Optional["IssueLabelFilter"] = None
    and_: Optional[List["IssueLabelCollectionFilter"]] = Field(
        alias="and", default=None
    )
    or_: Optional[List["IssueLabelCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["IssueLabelFilter"] = None
    every: Optional["IssueLabelFilter"] = None
    length: Optional["NumberComparator"] = None


class ProjectUpdateFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    user: Optional["UserFilter"] = None
    project: Optional["ProjectFilter"] = None
    reactions: Optional["ReactionCollectionFilter"] = None
    and_: Optional[List["ProjectUpdateFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ProjectUpdateFilter"]] = Field(alias="or", default=None)


class DocumentFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    title: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    creator: Optional["UserFilter"] = None
    project: Optional["ProjectFilter"] = None
    initiative: Optional["InitiativeFilter"] = None
    and_: Optional[List["DocumentFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["DocumentFilter"]] = Field(alias="or", default=None)


class NullableDocumentFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    title: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    creator: Optional["UserFilter"] = None
    project: Optional["ProjectFilter"] = None
    initiative: Optional["InitiativeFilter"] = None
    null: Optional[bool] = None
    and_: Optional[List["NullableDocumentFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableDocumentFilter"]] = Field(alias="or", default=None)


class DocumentCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    title: Optional["StringComparator"] = None
    slug_id: Optional["StringComparator"] = Field(alias="slugId", default=None)
    creator: Optional["UserFilter"] = None
    project: Optional["ProjectFilter"] = None
    initiative: Optional["InitiativeFilter"] = None
    and_: Optional[List["DocumentCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["DocumentCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["DocumentFilter"] = None
    every: Optional["DocumentFilter"] = None
    length: Optional["NumberComparator"] = None


class ReactionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    emoji: Optional["StringComparator"] = None
    custom_emoji_id: Optional["IDComparator"] = Field(
        alias="customEmojiId", default=None
    )
    and_: Optional[List["ReactionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ReactionFilter"]] = Field(alias="or", default=None)


class NullableReactionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    emoji: Optional["StringComparator"] = None
    custom_emoji_id: Optional["IDComparator"] = Field(
        alias="customEmojiId", default=None
    )
    null: Optional[bool] = None
    and_: Optional[List["NullableReactionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NullableReactionFilter"]] = Field(alias="or", default=None)


class ReactionCollectionFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    emoji: Optional["StringComparator"] = None
    custom_emoji_id: Optional["IDComparator"] = Field(
        alias="customEmojiId", default=None
    )
    and_: Optional[List["ReactionCollectionFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["ReactionCollectionFilter"]] = Field(alias="or", default=None)
    some: Optional["ReactionFilter"] = None
    every: Optional["ReactionFilter"] = None
    length: Optional["NumberComparator"] = None


class NotificationFilter(BaseModel):
    id: Optional["IDComparator"] = None
    created_at: Optional["DateComparator"] = Field(alias="createdAt", default=None)
    updated_at: Optional["DateComparator"] = Field(alias="updatedAt", default=None)
    type: Optional["StringComparator"] = None
    archived_at: Optional["DateComparator"] = Field(alias="archivedAt", default=None)
    and_: Optional[List["NotificationFilter"]] = Field(alias="and", default=None)
    or_: Optional[List["NotificationFilter"]] = Field(alias="or", default=None)


class TimeScheduleEntryInput(BaseModel):
    starts_at: Any = Field(alias="startsAt")
    ends_at: Any = Field(alias="endsAt")
    user_id: Optional[str] = Field(alias="userId", default=None)
    user_email: Optional[str] = Field(alias="userEmail", default=None)


class TriageResponsibilityManualSelectionInput(BaseModel):
    user_ids: List[str] = Field(alias="userIds")
    assignment_index: Optional[int] = Field(alias="assignmentIndex", default=None)


class NotificationDeliveryPreferencesDayInput(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None


class NotificationDeliveryPreferencesScheduleInput(BaseModel):
    disabled: Optional[bool] = None
    sunday: "NotificationDeliveryPreferencesDayInput"
    monday: "NotificationDeliveryPreferencesDayInput"
    tuesday: "NotificationDeliveryPreferencesDayInput"
    wednesday: "NotificationDeliveryPreferencesDayInput"
    thursday: "NotificationDeliveryPreferencesDayInput"
    friday: "NotificationDeliveryPreferencesDayInput"
    saturday: "NotificationDeliveryPreferencesDayInput"


class NotificationDeliveryPreferencesChannelInput(BaseModel):
    notifications_disabled: Optional[bool] = Field(
        alias="notificationsDisabled", default=None
    )
    schedule: Optional["NotificationDeliveryPreferencesScheduleInput"] = None


class NotificationDeliveryPreferencesInput(BaseModel):
    mobile: Optional["NotificationDeliveryPreferencesChannelInput"] = None


class WorkflowCondition(BaseModel):
    issue_filter: Optional["IssueFilter"] = Field(alias="issueFilter", default=None)
    project_filter: Optional["ProjectFilter"] = Field(
        alias="projectFilter", default=None
    )


class IssueCreateInput(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    description_data: Optional[Any] = Field(alias="descriptionData", default=None)
    assignee_id: Optional[str] = Field(alias="assigneeId", default=None)
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    priority: Optional[int] = None
    estimate: Optional[int] = None
    subscriber_ids: Optional[List[str]] = Field(alias="subscriberIds", default=None)
    label_ids: Optional[List[str]] = Field(alias="labelIds", default=None)
    team_id: str = Field(alias="teamId")
    cycle_id: Optional[str] = Field(alias="cycleId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    project_milestone_id: Optional[str] = Field(
        alias="projectMilestoneId", default=None
    )
    last_applied_template_id: Optional[str] = Field(
        alias="lastAppliedTemplateId", default=None
    )
    state_id: Optional[str] = Field(alias="stateId", default=None)
    reference_comment_id: Optional[str] = Field(
        alias="referenceCommentId", default=None
    )
    source_comment_id: Optional[str] = Field(alias="sourceCommentId", default=None)
    board_order: Optional[float] = Field(alias="boardOrder", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    priority_sort_order: Optional[float] = Field(
        alias="prioritySortOrder", default=None
    )
    sub_issue_sort_order: Optional[float] = Field(
        alias="subIssueSortOrder", default=None
    )
    due_date: Optional[Any] = Field(alias="dueDate", default=None)
    create_as_user: Optional[str] = Field(alias="createAsUser", default=None)
    display_icon_url: Optional[str] = Field(alias="displayIconUrl", default=None)
    preserve_sort_order_on_create: Optional[bool] = Field(
        alias="preserveSortOrderOnCreate", default=None
    )
    created_at: Optional[Any] = Field(alias="createdAt", default=None)
    sla_breaches_at: Optional[Any] = Field(alias="slaBreachesAt", default=None)
    template_id: Optional[str] = Field(alias="templateId", default=None)


class IssueUpdateInput(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    description_data: Optional[Any] = Field(alias="descriptionData", default=None)
    assignee_id: Optional[str] = Field(alias="assigneeId", default=None)
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    priority: Optional[int] = None
    estimate: Optional[int] = None
    subscriber_ids: Optional[List[str]] = Field(alias="subscriberIds", default=None)
    label_ids: Optional[List[str]] = Field(alias="labelIds", default=None)
    team_id: Optional[str] = Field(alias="teamId", default=None)
    cycle_id: Optional[str] = Field(alias="cycleId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    project_milestone_id: Optional[str] = Field(
        alias="projectMilestoneId", default=None
    )
    last_applied_template_id: Optional[str] = Field(
        alias="lastAppliedTemplateId", default=None
    )
    state_id: Optional[str] = Field(alias="stateId", default=None)
    board_order: Optional[float] = Field(alias="boardOrder", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    priority_sort_order: Optional[float] = Field(
        alias="prioritySortOrder", default=None
    )
    sub_issue_sort_order: Optional[float] = Field(
        alias="subIssueSortOrder", default=None
    )
    due_date: Optional[Any] = Field(alias="dueDate", default=None)
    trashed: Optional[bool] = None
    sla_breaches_at: Optional[Any] = Field(alias="slaBreachesAt", default=None)
    snoozed_until_at: Optional[Any] = Field(alias="snoozedUntilAt", default=None)
    snoozed_by_id: Optional[str] = Field(alias="snoozedById", default=None)


class AuthApiKeyCreateInput(BaseModel):
    id: Optional[str] = None
    label: str
    key: str


class ApiKeyCreateInput(BaseModel):
    id: Optional[str] = None
    label: str
    key: str


class AttachmentCreateInput(BaseModel):
    id: Optional[str] = None
    title: str
    subtitle: Optional[str] = None
    url: str
    issue_id: str = Field(alias="issueId")
    icon_url: Optional[str] = Field(alias="iconUrl", default=None)
    metadata: Optional[Any] = None
    group_by_source: Optional[bool] = Field(alias="groupBySource", default=None)
    comment_body: Optional[str] = Field(alias="commentBody", default=None)
    comment_body_data: Optional[Any] = Field(alias="commentBodyData", default=None)
    create_as_user: Optional[str] = Field(alias="createAsUser", default=None)


class AttachmentUpdateInput(BaseModel):
    title: str
    subtitle: Optional[str] = None
    metadata: Optional[Any] = None
    icon_url: Optional[str] = Field(alias="iconUrl", default=None)


class OnboardingCustomerSurvey(BaseModel):
    company_role: Optional[str] = Field(alias="companyRole", default=None)
    company_size: Optional[str] = Field(alias="companySize", default=None)


class CreateOrganizationInput(BaseModel):
    name: str
    url_key: str = Field(alias="urlKey")
    domain_access: Optional[bool] = Field(alias="domainAccess", default=None)
    timezone: Optional[str] = None
    utm: Optional[str] = None


class JoinOrganizationInput(BaseModel):
    organization_id: str = Field(alias="organizationId")
    invite_link: Optional[str] = Field(alias="inviteLink", default=None)


class EmailUserAccountAuthChallengeInput(BaseModel):
    email: str
    is_desktop: Optional[bool] = Field(alias="isDesktop", default=None)
    client_auth_code: Optional[str] = Field(alias="clientAuthCode", default=None)
    signup_code: Optional[str] = Field(alias="signupCode", default=None)
    invite_link: Optional[str] = Field(alias="inviteLink", default=None)
    login_code_only: Optional[bool] = Field(alias="loginCodeOnly", default=None)


class TokenUserAccountAuthInput(BaseModel):
    email: str
    token: str
    timezone: str
    team_ids_to_join: Optional[List[str]] = Field(alias="teamIdsToJoin", default=None)
    invite_link: Optional[str] = Field(alias="inviteLink", default=None)


class GoogleUserAccountAuthInput(BaseModel):
    code: str
    redirect_uri: Optional[str] = Field(alias="redirectUri", default=None)
    timezone: str
    team_ids_to_join: Optional[List[str]] = Field(alias="teamIdsToJoin", default=None)
    signup_code: Optional[str] = Field(alias="signupCode", default=None)
    invite_link: Optional[str] = Field(alias="inviteLink", default=None)
    disallow_signup: Optional[bool] = Field(alias="disallowSignup", default=None)


class CommentCreateInput(BaseModel):
    id: Optional[str] = None
    body: Optional[str] = None
    body_data: Optional[Any] = Field(alias="bodyData", default=None)
    issue_id: Optional[str] = Field(alias="issueId", default=None)
    project_update_id: Optional[str] = Field(alias="projectUpdateId", default=None)
    document_content_id: Optional[str] = Field(alias="documentContentId", default=None)
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    create_as_user: Optional[str] = Field(alias="createAsUser", default=None)
    display_icon_url: Optional[str] = Field(alias="displayIconUrl", default=None)
    created_at: Optional[Any] = Field(alias="createdAt", default=None)
    do_not_subscribe_to_issue: Optional[bool] = Field(
        alias="doNotSubscribeToIssue", default=None
    )
    create_on_synced_slack_thread: Optional[bool] = Field(
        alias="createOnSyncedSlackThread", default=None
    )
    quoted_text: Optional[str] = Field(alias="quotedText", default=None)
    subscriber_ids: Optional[List[str]] = Field(alias="subscriberIds", default=None)


class CommentUpdateInput(BaseModel):
    body: Optional[str] = None
    body_data: Optional[Any] = Field(alias="bodyData", default=None)
    resolving_user_id: Optional[str] = Field(alias="resolvingUserId", default=None)
    resolving_comment_id: Optional[str] = Field(
        alias="resolvingCommentId", default=None
    )
    quoted_text: Optional[str] = Field(alias="quotedText", default=None)
    subscriber_ids: Optional[List[str]] = Field(alias="subscriberIds", default=None)
    do_not_subscribe_to_issue: Optional[bool] = Field(
        alias="doNotSubscribeToIssue", default=None
    )


class ContactCreateInput(BaseModel):
    type: str
    message: str
    operating_system: Optional[str] = Field(alias="operatingSystem", default=None)
    browser: Optional[str] = None
    device: Optional[str] = None
    client_version: Optional[str] = Field(alias="clientVersion", default=None)
    disappointment_rating: Optional[int] = Field(
        alias="disappointmentRating", default=None
    )


class ContactSalesCreateInput(BaseModel):
    name: str
    email: str
    company_size: Optional[str] = Field(alias="companySize", default=None)
    message: Optional[str] = None


class CustomerNeedCreateInput(BaseModel):
    id: Optional[str] = None
    customer_id: str = Field(alias="customerId")
    issue_id: Optional[str] = Field(alias="issueId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    comment_id: Optional[str] = Field(alias="commentId", default=None)
    priority: Optional[float] = None


class CustomerNeedUpdateInput(BaseModel):
    id: Optional[str] = None
    priority: Optional[float] = None


class CustomerCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    domains: Optional[List[str]] = Field(default_factory=lambda: [])
    external_ids: Optional[List[str]] = Field(
        alias="externalIds", default_factory=lambda: []
    )
    slack_channel_id: Optional[str] = Field(alias="slackChannelId", default=None)
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    status_id: Optional[str] = Field(alias="statusId", default=None)


class CustomerUpdateInput(BaseModel):
    name: Optional[str] = None
    domains: Optional[List[str]] = None
    external_ids: Optional[List[str]] = Field(alias="externalIds", default=None)
    slack_channel_id: Optional[str] = Field(alias="slackChannelId", default=None)
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    status_id: Optional[str] = Field(alias="statusId", default=None)


class CustomerStatusCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    color: str
    description: Optional[str] = None
    position: float
    type: CustomerStatusType


class CustomerStatusUpdateInput(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    description: Optional[str] = None
    position: Optional[float] = None
    type: Optional[CustomerStatusType] = None


class PrioritySort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None
    no_priority_first: Optional[bool] = Field(alias="noPriorityFirst", default=False)


class EstimateSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class TitleSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class LabelSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class SlaStatusSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class CreatedAtSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class CycleSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None
    current_cycle_first: Optional[bool] = Field(
        alias="currentCycleFirst", default=False
    )


class UpdatedAtSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class MilestoneSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class CompletedAtSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class AssigneeSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class DueDateSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class ProjectSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class TeamSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class WorkflowStateSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class ManualSort(BaseModel):
    nulls: Optional[PaginationNulls] = PaginationNulls.last
    order: Optional[PaginationSortOrder] = None


class IssueSortInput(BaseModel):
    priority: Optional["PrioritySort"] = None
    estimate: Optional["EstimateSort"] = None
    title: Optional["TitleSort"] = None
    label: Optional["LabelSort"] = None
    sla_status: Optional["SlaStatusSort"] = Field(alias="slaStatus", default=None)
    created_at: Optional["CreatedAtSort"] = Field(alias="createdAt", default=None)
    updated_at: Optional["UpdatedAtSort"] = Field(alias="updatedAt", default=None)
    completed_at: Optional["CompletedAtSort"] = Field(alias="completedAt", default=None)
    due_date: Optional["DueDateSort"] = Field(alias="dueDate", default=None)
    cycle: Optional["CycleSort"] = None
    milestone: Optional["MilestoneSort"] = None
    assignee: Optional["AssigneeSort"] = None
    project: Optional["ProjectSort"] = None
    team: Optional["TeamSort"] = None
    manual: Optional["ManualSort"] = None
    workflow_state: Optional["WorkflowStateSort"] = Field(
        alias="workflowState", default=None
    )


class CustomViewCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    team_id: Optional[str] = Field(alias="teamId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    filters: Optional[Any] = None
    filter_data: Optional["IssueFilter"] = Field(alias="filterData", default=None)
    project_filter_data: Optional["ProjectFilter"] = Field(
        alias="projectFilterData", default=None
    )
    shared: Optional[bool] = None


class CustomViewUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    team_id: Optional[str] = Field(alias="teamId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    filters: Optional[Any] = None
    filter_data: Optional["IssueFilter"] = Field(alias="filterData", default=None)
    project_filter_data: Optional["ProjectFilter"] = Field(
        alias="projectFilterData", default=None
    )
    shared: Optional[bool] = None


class CycleCreateInput(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    team_id: str = Field(alias="teamId")
    starts_at: Any = Field(alias="startsAt")
    ends_at: Any = Field(alias="endsAt")
    completed_at: Optional[Any] = Field(alias="completedAt", default=None)


class CycleUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    starts_at: Optional[Any] = Field(alias="startsAt", default=None)
    ends_at: Optional[Any] = Field(alias="endsAt", default=None)
    completed_at: Optional[Any] = Field(alias="completedAt", default=None)


class CycleShiftAllInput(BaseModel):
    id: str
    days_to_shift: float = Field(alias="daysToShift")


class DiaryEntryCreateInput(BaseModel):
    id: Optional[str] = None
    date: Any
    body_data: Optional[Any] = Field(alias="bodyData", default=None)


class DiaryEntryUpdateInput(BaseModel):
    body_data: Optional[Any] = Field(alias="bodyData", default=None)
    date: Optional[Any] = None


class DocumentCreateInput(BaseModel):
    id: Optional[str] = None
    title: str
    icon: Optional[str] = None
    color: Optional[str] = None
    content_data: Optional[Any] = Field(alias="contentData", default=None)
    content: Optional[str] = None
    project_id: Optional[str] = Field(alias="projectId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    last_applied_template_id: Optional[str] = Field(
        alias="lastAppliedTemplateId", default=None
    )
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    subscriber_ids: Optional[List[str]] = Field(alias="subscriberIds", default=None)


class DocumentUpdateInput(BaseModel):
    title: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    content_data: Optional[Any] = Field(alias="contentData", default=None)
    content: Optional[str] = None
    project_id: Optional[str] = Field(alias="projectId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    last_applied_template_id: Optional[str] = Field(
        alias="lastAppliedTemplateId", default=None
    )
    hidden_at: Optional[Any] = Field(alias="hiddenAt", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    trashed: Optional[bool] = None
    subscriber_ids: Optional[List[str]] = Field(alias="subscriberIds", default=None)


class EmailIntakeAddressCreateInput(BaseModel):
    id: Optional[str] = None
    team_id: Optional[str] = Field(alias="teamId", default=None)
    template_id: Optional[str] = Field(alias="templateId", default=None)


class EmailIntakeAddressUpdateInput(BaseModel):
    enabled: bool


class EmailUnsubscribeInput(BaseModel):
    type: str
    token: str
    user_id: str = Field(alias="userId")


class EmojiCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    url: str


class EntityExternalLinkCreateInput(BaseModel):
    id: Optional[str] = None
    url: str
    label: str
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class EntityExternalLinkUpdateInput(BaseModel):
    url: Optional[str] = None
    label: Optional[str] = None
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class InitiativeToProjectCreateInput(BaseModel):
    id: Optional[str] = None
    project_id: str = Field(alias="projectId")
    initiative_id: str = Field(alias="initiativeId")
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class InitiativeToProjectUpdateInput(BaseModel):
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class InitiativeCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    color: Optional[str] = None
    icon: Optional[str] = None
    status: Optional[InitiativeStatus] = None
    target_date: Optional[Any] = Field(alias="targetDate", default=None)
    target_date_resolution: Optional[DateResolutionType] = Field(
        alias="targetDateResolution", default=None
    )


class InitiativeUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    color: Optional[str] = None
    icon: Optional[str] = None
    target_date: Optional[Any] = Field(alias="targetDate", default=None)
    status: Optional[InitiativeStatus] = None
    target_date_resolution: Optional[DateResolutionType] = Field(
        alias="targetDateResolution", default=None
    )
    trashed: Optional[bool] = None


class FavoriteCreateInput(BaseModel):
    id: Optional[str] = None
    folder_name: Optional[str] = Field(alias="folderName", default=None)
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    issue_id: Optional[str] = Field(alias="issueId", default=None)
    facet_id: Optional[str] = Field(alias="facetId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    project_tab: Optional[ProjectTab] = Field(alias="projectTab", default=None)
    predefined_view_type: Optional[str] = Field(
        alias="predefinedViewType", default=None
    )
    predefined_view_team_id: Optional[str] = Field(
        alias="predefinedViewTeamId", default=None
    )
    cycle_id: Optional[str] = Field(alias="cycleId", default=None)
    custom_view_id: Optional[str] = Field(alias="customViewId", default=None)
    document_id: Optional[str] = Field(alias="documentId", default=None)
    roadmap_id: Optional[str] = Field(alias="roadmapId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    initiative_tab: Optional[InitiativeTab] = Field(alias="initiativeTab", default=None)
    label_id: Optional[str] = Field(alias="labelId", default=None)
    user_id: Optional[str] = Field(alias="userId", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class FavoriteUpdateInput(BaseModel):
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    folder_name: Optional[str] = Field(alias="folderName", default=None)


class GitAutomationStateCreateInput(BaseModel):
    id: Optional[str] = None
    team_id: str = Field(alias="teamId")
    state_id: Optional[str] = Field(alias="stateId", default=None)
    branch_pattern: Optional[str] = Field(alias="branchPattern", default=None)
    target_branch_id: Optional[str] = Field(alias="targetBranchId", default=None)
    event: GitAutomationStates


class GitAutomationStateUpdateInput(BaseModel):
    state_id: Optional[str] = Field(alias="stateId", default=None)
    branch_pattern: Optional[str] = Field(alias="branchPattern", default=None)
    target_branch_id: Optional[str] = Field(alias="targetBranchId", default=None)
    event: Optional[GitAutomationStates] = None


class GitAutomationTargetBranchCreateInput(BaseModel):
    id: Optional[str] = None
    team_id: str = Field(alias="teamId")
    branch_pattern: str = Field(alias="branchPattern")
    is_regex: Optional[bool] = Field(alias="isRegex", default=False)


class GitAutomationTargetBranchUpdateInput(BaseModel):
    branch_pattern: Optional[str] = Field(alias="branchPattern", default=None)
    is_regex: Optional[bool] = Field(alias="isRegex", default=None)


class IntegrationRequestInput(BaseModel):
    email: Optional[str] = None
    name: str


class JiraConfigurationInput(BaseModel):
    access_token: str = Field(alias="accessToken")
    email: str
    hostname: str
    project: Optional[str] = None
    manual_setup: Optional[bool] = Field(alias="manualSetup", default=None)


class JiraUpdateInput(BaseModel):
    id: str
    update_projects: Optional[bool] = Field(alias="updateProjects", default=None)
    update_metadata: Optional[bool] = Field(alias="updateMetadata", default=None)
    delete_webhook: Optional[bool] = Field(alias="deleteWebhook", default=None)
    webhook_secret: Optional[str] = Field(alias="webhookSecret", default=None)


class AirbyteConfigurationInput(BaseModel):
    api_key: str = Field(alias="apiKey")


class IntegrationsSettingsCreateInput(BaseModel):
    slack_issue_created: Optional[bool] = Field(alias="slackIssueCreated", default=None)
    slack_issue_added_to_view: Optional[bool] = Field(
        alias="slackIssueAddedToView", default=None
    )
    slack_issue_new_comment: Optional[bool] = Field(
        alias="slackIssueNewComment", default=None
    )
    slack_issue_status_changed_done: Optional[bool] = Field(
        alias="slackIssueStatusChangedDone", default=None
    )
    slack_issue_status_changed_all: Optional[bool] = Field(
        alias="slackIssueStatusChangedAll", default=None
    )
    slack_project_update_created: Optional[bool] = Field(
        alias="slackProjectUpdateCreated", default=None
    )
    slack_project_update_created_to_team: Optional[bool] = Field(
        alias="slackProjectUpdateCreatedToTeam", default=None
    )
    slack_project_update_created_to_workspace: Optional[bool] = Field(
        alias="slackProjectUpdateCreatedToWorkspace", default=None
    )
    slack_issue_added_to_triage: Optional[bool] = Field(
        alias="slackIssueAddedToTriage", default=None
    )
    slack_issue_sla_high_risk: Optional[bool] = Field(
        alias="slackIssueSlaHighRisk", default=None
    )
    slack_issue_sla_breached: Optional[bool] = Field(
        alias="slackIssueSlaBreached", default=None
    )
    id: Optional[str] = None
    team_id: Optional[str] = Field(alias="teamId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)


class IntegrationsSettingsUpdateInput(BaseModel):
    slack_issue_created: Optional[bool] = Field(alias="slackIssueCreated", default=None)
    slack_issue_added_to_view: Optional[bool] = Field(
        alias="slackIssueAddedToView", default=None
    )
    slack_issue_new_comment: Optional[bool] = Field(
        alias="slackIssueNewComment", default=None
    )
    slack_issue_status_changed_done: Optional[bool] = Field(
        alias="slackIssueStatusChangedDone", default=None
    )
    slack_issue_status_changed_all: Optional[bool] = Field(
        alias="slackIssueStatusChangedAll", default=None
    )
    slack_project_update_created: Optional[bool] = Field(
        alias="slackProjectUpdateCreated", default=None
    )
    slack_project_update_created_to_team: Optional[bool] = Field(
        alias="slackProjectUpdateCreatedToTeam", default=None
    )
    slack_project_update_created_to_workspace: Optional[bool] = Field(
        alias="slackProjectUpdateCreatedToWorkspace", default=None
    )
    slack_issue_added_to_triage: Optional[bool] = Field(
        alias="slackIssueAddedToTriage", default=None
    )
    slack_issue_sla_high_risk: Optional[bool] = Field(
        alias="slackIssueSlaHighRisk", default=None
    )
    slack_issue_sla_breached: Optional[bool] = Field(
        alias="slackIssueSlaBreached", default=None
    )


class IntegrationTemplateCreateInput(BaseModel):
    id: Optional[str] = None
    integration_id: str = Field(alias="integrationId")
    template_id: str = Field(alias="templateId")
    foreign_entity_id: Optional[str] = Field(alias="foreignEntityId", default=None)


class IssueImportMappingInput(BaseModel):
    users: Optional[Any] = None
    workflow_states: Optional[Any] = Field(alias="workflowStates", default=None)
    epics: Optional[Any] = None


class IssueImportUpdateInput(BaseModel):
    mapping: Any


class IssueLabelCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    color: Optional[str] = None
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    team_id: Optional[str] = Field(alias="teamId", default=None)


class IssueLabelUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    color: Optional[str] = None


class IssueRelationCreateInput(BaseModel):
    id: Optional[str] = None
    type: IssueRelationType
    issue_id: str = Field(alias="issueId")
    related_issue_id: str = Field(alias="relatedIssueId")


class IssueRelationUpdateInput(BaseModel):
    type: Optional[str] = None
    issue_id: Optional[str] = Field(alias="issueId", default=None)
    related_issue_id: Optional[str] = Field(alias="relatedIssueId", default=None)


class NotificationUpdateInput(BaseModel):
    read_at: Optional[Any] = Field(alias="readAt", default=None)
    snoozed_until_at: Optional[Any] = Field(alias="snoozedUntilAt", default=None)
    project_update_id: Optional[str] = Field(alias="projectUpdateId", default=None)


class NotificationEntityInput(BaseModel):
    issue_id: Optional[str] = Field(alias="issueId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    project_update_id: Optional[str] = Field(alias="projectUpdateId", default=None)
    oauth_client_approval_id: Optional[str] = Field(
        alias="oauthClientApprovalId", default=None
    )
    id: Optional[str] = None


class NotificationSubscriptionCreateInput(BaseModel):
    id: Optional[str] = None
    custom_view_id: Optional[str] = Field(alias="customViewId", default=None)
    cycle_id: Optional[str] = Field(alias="cycleId", default=None)
    label_id: Optional[str] = Field(alias="labelId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    team_id: Optional[str] = Field(alias="teamId", default=None)
    user_id: Optional[str] = Field(alias="userId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    context_view_type: Optional[ContextViewType] = Field(
        alias="contextViewType", default=None
    )
    user_context_view_type: Optional[UserContextViewType] = Field(
        alias="userContextViewType", default=None
    )
    notification_subscription_types: Optional[List[str]] = Field(
        alias="notificationSubscriptionTypes", default=None
    )
    active: Optional[bool] = None


class NotificationSubscriptionUpdateInput(BaseModel):
    notification_subscription_types: Optional[List[str]] = Field(
        alias="notificationSubscriptionTypes", default=None
    )
    active: Optional[bool] = None


class OrganizationDomainCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    verification_email: Optional[str] = Field(alias="verificationEmail", default=None)
    auth_type: Optional[str] = Field(alias="authType", default="general")


class OrganizationDomainUpdateInput(BaseModel):
    disable_organization_creation: Optional[bool] = Field(
        alias="disableOrganizationCreation", default=None
    )


class OrganizationDomainVerificationInput(BaseModel):
    organization_domain_id: str = Field(alias="organizationDomainId")
    verification_code: str = Field(alias="verificationCode")


class OrganizationInviteCreateInput(BaseModel):
    id: Optional[str] = None
    email: str
    role: Optional[UserRoleType] = UserRoleType.user
    message: Optional[str] = None
    team_ids: Optional[List[str]] = Field(alias="teamIds", default=None)
    metadata: Optional[Any] = None


class OrganizationInviteUpdateInput(BaseModel):
    team_ids: List[str] = Field(alias="teamIds")


class AuthOrganizationUpdateInput(BaseModel):
    url_key: Optional[str] = Field(alias="urlKey", default=None)
    invite_hash: Optional[str] = Field(alias="inviteHash", default=None)


class OrganizationUpdateInput(BaseModel):
    name: Optional[str] = None
    logo_url: Optional[str] = Field(alias="logoUrl", default=None)
    url_key: Optional[str] = Field(alias="urlKey", default=None)
    git_branch_format: Optional[str] = Field(alias="gitBranchFormat", default=None)
    git_linkback_messages_enabled: Optional[bool] = Field(
        alias="gitLinkbackMessagesEnabled", default=None
    )
    git_public_linkback_messages_enabled: Optional[bool] = Field(
        alias="gitPublicLinkbackMessagesEnabled", default=None
    )
    roadmap_enabled: Optional[bool] = Field(alias="roadmapEnabled", default=None)
    project_update_reminder_frequency_in_weeks: Optional[float] = Field(
        alias="projectUpdateReminderFrequencyInWeeks", default=None
    )
    project_update_reminders_day: Optional[Day] = Field(
        alias="projectUpdateRemindersDay", default=None
    )
    project_update_reminders_hour: Optional[float] = Field(
        alias="projectUpdateRemindersHour", default=None
    )
    fiscal_year_start_month: Optional[float] = Field(
        alias="fiscalYearStartMonth", default=None
    )
    reduced_personal_information: Optional[bool] = Field(
        alias="reducedPersonalInformation", default=None
    )
    oauth_app_review: Optional[bool] = Field(alias="oauthAppReview", default=None)
    allowed_auth_services: Optional[List[str]] = Field(
        alias="allowedAuthServices", default=None
    )
    sla_enabled: Optional[bool] = Field(alias="slaEnabled", default=None)
    sla_day_count: Optional[SLADayCountType] = Field(alias="slaDayCount", default=None)
    allow_members_to_invite: Optional[bool] = Field(
        alias="allowMembersToInvite", default=None
    )
    ip_restrictions: Optional[List["OrganizationIpRestrictionInput"]] = Field(
        alias="ipRestrictions", default=None
    )
    theme_settings: Optional[Any] = Field(alias="themeSettings", default=None)


class DeleteOrganizationInput(BaseModel):
    deletion_code: str = Field(alias="deletionCode")


class ProjectLinkCreateInput(BaseModel):
    id: Optional[str] = None
    url: str
    label: str
    project_id: str = Field(alias="projectId")
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class ProjectLinkUpdateInput(BaseModel):
    url: Optional[str] = None
    label: Optional[str] = None
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class ProjectMilestoneCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    description_data: Optional[Any] = Field(alias="descriptionData", default=None)
    target_date: Optional[Any] = Field(alias="targetDate", default=None)
    project_id: str = Field(alias="projectId")
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class ProjectMilestoneUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    description_data: Optional[Any] = Field(alias="descriptionData", default=None)
    target_date: Optional[Any] = Field(alias="targetDate", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class ProjectRelationCreateInput(BaseModel):
    id: Optional[str] = None
    type: str
    project_id: str = Field(alias="projectId")
    project_milestone_id: Optional[str] = Field(
        alias="projectMilestoneId", default=None
    )
    anchor_type: str = Field(alias="anchorType")
    related_project_id: str = Field(alias="relatedProjectId")
    related_project_milestone_id: Optional[str] = Field(
        alias="relatedProjectMilestoneId", default=None
    )
    related_anchor_type: str = Field(alias="relatedAnchorType")


class ProjectRelationUpdateInput(BaseModel):
    type: Optional[str] = None
    project_id: Optional[str] = Field(alias="projectId", default=None)
    project_milestone_id: Optional[str] = Field(
        alias="projectMilestoneId", default=None
    )
    anchor_type: Optional[str] = Field(alias="anchorType", default=None)
    related_project_id: Optional[str] = Field(alias="relatedProjectId", default=None)
    related_project_milestone_id: Optional[str] = Field(
        alias="relatedProjectMilestoneId", default=None
    )
    related_anchor_type: Optional[str] = Field(alias="relatedAnchorType", default=None)


class ProjectCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    icon: Optional[str] = None
    color: Optional[str] = None
    state: Optional[str] = None
    status_id: Optional[str] = Field(alias="statusId", default=None)
    description: Optional[str] = None
    team_ids: List[str] = Field(alias="teamIds")
    converted_from_issue_id: Optional[str] = Field(
        alias="convertedFromIssueId", default=None
    )
    last_applied_template_id: Optional[str] = Field(
        alias="lastAppliedTemplateId", default=None
    )
    lead_id: Optional[str] = Field(alias="leadId", default=None)
    member_ids: Optional[List[str]] = Field(alias="memberIds", default=None)
    start_date: Optional[Any] = Field(alias="startDate", default=None)
    start_date_resolution: Optional[DateResolutionType] = Field(
        alias="startDateResolution", default=None
    )
    target_date: Optional[Any] = Field(alias="targetDate", default=None)
    target_date_resolution: Optional[DateResolutionType] = Field(
        alias="targetDateResolution", default=None
    )
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    priority_sort_order: Optional[float] = Field(
        alias="prioritySortOrder", default=None
    )
    priority: Optional[int] = None


class ProjectUpdateInput(BaseModel):
    state: Optional[str] = None
    status_id: Optional[str] = Field(alias="statusId", default=None)
    name: Optional[str] = None
    description: Optional[str] = None
    converted_from_issue_id: Optional[str] = Field(
        alias="convertedFromIssueId", default=None
    )
    last_applied_template_id: Optional[str] = Field(
        alias="lastAppliedTemplateId", default=None
    )
    icon: Optional[str] = None
    color: Optional[str] = None
    team_ids: Optional[List[str]] = Field(alias="teamIds", default=None)
    project_update_reminders_paused_until_at: Optional[Any] = Field(
        alias="projectUpdateRemindersPausedUntilAt", default=None
    )
    lead_id: Optional[str] = Field(alias="leadId", default=None)
    member_ids: Optional[List[str]] = Field(alias="memberIds", default=None)
    start_date: Optional[Any] = Field(alias="startDate", default=None)
    start_date_resolution: Optional[DateResolutionType] = Field(
        alias="startDateResolution", default=None
    )
    target_date: Optional[Any] = Field(alias="targetDate", default=None)
    target_date_resolution: Optional[DateResolutionType] = Field(
        alias="targetDateResolution", default=None
    )
    completed_at: Optional[Any] = Field(alias="completedAt", default=None)
    canceled_at: Optional[Any] = Field(alias="canceledAt", default=None)
    slack_new_issue: Optional[bool] = Field(alias="slackNewIssue", default=None)
    slack_issue_comments: Optional[bool] = Field(
        alias="slackIssueComments", default=None
    )
    slack_issue_statuses: Optional[bool] = Field(
        alias="slackIssueStatuses", default=None
    )
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    priority_sort_order: Optional[float] = Field(
        alias="prioritySortOrder", default=None
    )
    trashed: Optional[bool] = None
    priority: Optional[int] = None


class ProjectUpdateInteractionCreateInput(BaseModel):
    id: Optional[str] = None
    project_update_id: str = Field(alias="projectUpdateId")
    read_at: Any = Field(alias="readAt")


class ProjectUpdateCreateInput(BaseModel):
    id: Optional[str] = None
    body: Optional[str] = None
    body_data: Optional[Any] = Field(alias="bodyData", default=None)
    project_id: str = Field(alias="projectId")
    health: Optional[ProjectUpdateHealthType] = None
    is_diff_hidden: Optional[bool] = Field(alias="isDiffHidden", default=None)


class ProjectUpdateUpdateInput(BaseModel):
    body: Optional[str] = None
    body_data: Optional[Any] = Field(alias="bodyData", default=None)
    health: Optional[ProjectUpdateHealthType] = None
    is_diff_hidden: Optional[bool] = Field(alias="isDiffHidden", default=None)


class PushSubscriptionCreateInput(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = Field(alias="userId", default=None)
    data: str
    type: Optional[PushSubscriptionType] = PushSubscriptionType.web


class ReactionCreateInput(BaseModel):
    id: Optional[str] = None
    emoji: str
    comment_id: Optional[str] = Field(alias="commentId", default=None)
    project_update_id: Optional[str] = Field(alias="projectUpdateId", default=None)
    issue_id: Optional[str] = Field(alias="issueId", default=None)


class RoadmapCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    color: Optional[str] = None


class RoadmapUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[str] = Field(alias="ownerId", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)
    color: Optional[str] = None


class RoadmapToProjectCreateInput(BaseModel):
    id: Optional[str] = None
    project_id: str = Field(alias="projectId")
    roadmap_id: str = Field(alias="roadmapId")
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class RoadmapToProjectUpdateInput(BaseModel):
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class TeamMembershipCreateInput(BaseModel):
    id: Optional[str] = None
    user_id: str = Field(alias="userId")
    team_id: str = Field(alias="teamId")
    owner: Optional[bool] = None
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class TeamMembershipUpdateInput(BaseModel):
    owner: Optional[bool] = None
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class TeamCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    key: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    organization_id: Optional[str] = Field(alias="organizationId", default=None)
    cycles_enabled: Optional[bool] = Field(alias="cyclesEnabled", default=None)
    cycle_start_day: Optional[float] = Field(alias="cycleStartDay", default=None)
    cycle_duration: Optional[int] = Field(alias="cycleDuration", default=None)
    cycle_cooldown_time: Optional[int] = Field(alias="cycleCooldownTime", default=None)
    cycle_issue_auto_assign_started: Optional[bool] = Field(
        alias="cycleIssueAutoAssignStarted", default=None
    )
    cycle_issue_auto_assign_completed: Optional[bool] = Field(
        alias="cycleIssueAutoAssignCompleted", default=None
    )
    cycle_lock_to_active: Optional[bool] = Field(
        alias="cycleLockToActive", default=None
    )
    upcoming_cycle_count: Optional[float] = Field(
        alias="upcomingCycleCount", default=None
    )
    triage_enabled: Optional[bool] = Field(alias="triageEnabled", default=None)
    require_priority_to_leave_triage: Optional[bool] = Field(
        alias="requirePriorityToLeaveTriage", default=None
    )
    timezone: Optional[str] = None
    issue_ordering_no_priority_first: Optional[bool] = Field(
        alias="issueOrderingNoPriorityFirst", default=None
    )
    issue_estimation_type: Optional[str] = Field(
        alias="issueEstimationType", default=None
    )
    issue_estimation_allow_zero: Optional[bool] = Field(
        alias="issueEstimationAllowZero", default=None
    )
    set_issue_sort_order_on_state_change: Optional[str] = Field(
        alias="setIssueSortOrderOnStateChange", default=None
    )
    issue_estimation_extended: Optional[bool] = Field(
        alias="issueEstimationExtended", default=None
    )
    default_issue_estimate: Optional[float] = Field(
        alias="defaultIssueEstimate", default=None
    )
    group_issue_history: Optional[bool] = Field(alias="groupIssueHistory", default=None)
    default_template_for_members_id: Optional[str] = Field(
        alias="defaultTemplateForMembersId", default=None
    )
    default_template_for_non_members_id: Optional[str] = Field(
        alias="defaultTemplateForNonMembersId", default=None
    )
    default_project_template_id: Optional[str] = Field(
        alias="defaultProjectTemplateId", default=None
    )
    private: Optional[bool] = None
    auto_close_period: Optional[float] = Field(alias="autoClosePeriod", default=None)
    auto_close_state_id: Optional[str] = Field(alias="autoCloseStateId", default=None)
    auto_archive_period: Optional[float] = Field(
        alias="autoArchivePeriod", default=None
    )
    marked_as_duplicate_workflow_state_id: Optional[str] = Field(
        alias="markedAsDuplicateWorkflowStateId", default=None
    )


class TeamUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    key: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    cycles_enabled: Optional[bool] = Field(alias="cyclesEnabled", default=None)
    cycle_start_day: Optional[float] = Field(alias="cycleStartDay", default=None)
    cycle_duration: Optional[int] = Field(alias="cycleDuration", default=None)
    cycle_cooldown_time: Optional[int] = Field(alias="cycleCooldownTime", default=None)
    cycle_issue_auto_assign_started: Optional[bool] = Field(
        alias="cycleIssueAutoAssignStarted", default=None
    )
    cycle_issue_auto_assign_completed: Optional[bool] = Field(
        alias="cycleIssueAutoAssignCompleted", default=None
    )
    cycle_lock_to_active: Optional[bool] = Field(
        alias="cycleLockToActive", default=None
    )
    cycle_enabled_start_week: Optional[str] = Field(
        alias="cycleEnabledStartWeek", default=None
    )
    cycle_enabled_start_date: Optional[Any] = Field(
        alias="cycleEnabledStartDate", default=None
    )
    upcoming_cycle_count: Optional[float] = Field(
        alias="upcomingCycleCount", default=None
    )
    timezone: Optional[str] = None
    issue_ordering_no_priority_first: Optional[bool] = Field(
        alias="issueOrderingNoPriorityFirst", default=None
    )
    issue_estimation_type: Optional[str] = Field(
        alias="issueEstimationType", default=None
    )
    issue_estimation_allow_zero: Optional[bool] = Field(
        alias="issueEstimationAllowZero", default=None
    )
    set_issue_sort_order_on_state_change: Optional[str] = Field(
        alias="setIssueSortOrderOnStateChange", default=None
    )
    issue_estimation_extended: Optional[bool] = Field(
        alias="issueEstimationExtended", default=None
    )
    default_issue_estimate: Optional[float] = Field(
        alias="defaultIssueEstimate", default=None
    )
    draft_workflow_state_id: Optional[str] = Field(
        alias="draftWorkflowStateId", default=None
    )
    start_workflow_state_id: Optional[str] = Field(
        alias="startWorkflowStateId", default=None
    )
    review_workflow_state_id: Optional[str] = Field(
        alias="reviewWorkflowStateId", default=None
    )
    mergeable_workflow_state_id: Optional[str] = Field(
        alias="mergeableWorkflowStateId", default=None
    )
    merge_workflow_state_id: Optional[str] = Field(
        alias="mergeWorkflowStateId", default=None
    )
    slack_new_issue: Optional[bool] = Field(alias="slackNewIssue", default=None)
    slack_issue_comments: Optional[bool] = Field(
        alias="slackIssueComments", default=None
    )
    slack_issue_statuses: Optional[bool] = Field(
        alias="slackIssueStatuses", default=None
    )
    group_issue_history: Optional[bool] = Field(alias="groupIssueHistory", default=None)
    default_template_for_members_id: Optional[str] = Field(
        alias="defaultTemplateForMembersId", default=None
    )
    default_template_for_non_members_id: Optional[str] = Field(
        alias="defaultTemplateForNonMembersId", default=None
    )
    default_project_template_id: Optional[str] = Field(
        alias="defaultProjectTemplateId", default=None
    )
    private: Optional[bool] = None
    triage_enabled: Optional[bool] = Field(alias="triageEnabled", default=None)
    require_priority_to_leave_triage: Optional[bool] = Field(
        alias="requirePriorityToLeaveTriage", default=None
    )
    default_issue_state_id: Optional[str] = Field(
        alias="defaultIssueStateId", default=None
    )
    auto_close_period: Optional[float] = Field(alias="autoClosePeriod", default=None)
    auto_close_state_id: Optional[str] = Field(alias="autoCloseStateId", default=None)
    auto_archive_period: Optional[float] = Field(
        alias="autoArchivePeriod", default=None
    )
    marked_as_duplicate_workflow_state_id: Optional[str] = Field(
        alias="markedAsDuplicateWorkflowStateId", default=None
    )
    join_by_default: Optional[bool] = Field(alias="joinByDefault", default=None)
    scim_managed: Optional[bool] = Field(alias="scimManaged", default=None)


class TemplateCreateInput(BaseModel):
    id: Optional[str] = None
    type: str
    team_id: Optional[str] = Field(alias="teamId", default=None)
    name: str
    description: Optional[str] = None
    template_data: Any = Field(alias="templateData")
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class TemplateUpdateInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    team_id: Optional[str] = Field(alias="teamId", default=None)
    template_data: Optional[Any] = Field(alias="templateData", default=None)
    sort_order: Optional[float] = Field(alias="sortOrder", default=None)


class TimeScheduleCreateInput(BaseModel):
    id: Optional[str] = None
    name: str
    entries: List["TimeScheduleEntryInput"]
    external_id: Optional[str] = Field(alias="externalId", default=None)
    external_url: Optional[str] = Field(alias="externalUrl", default=None)


class TimeScheduleUpdateInput(BaseModel):
    name: Optional[str] = None
    entries: Optional[List["TimeScheduleEntryInput"]] = None
    external_id: Optional[str] = Field(alias="externalId", default=None)
    external_url: Optional[str] = Field(alias="externalUrl", default=None)


class TriageResponsibilityCreateInput(BaseModel):
    id: Optional[str] = None
    team_id: str = Field(alias="teamId")
    action: str
    manual_selection: Optional["TriageResponsibilityManualSelectionInput"] = Field(
        alias="manualSelection", default=None
    )
    time_schedule_id: Optional[str] = Field(alias="timeScheduleId", default=None)


class TriageResponsibilityUpdateInput(BaseModel):
    action: Optional[str] = None
    manual_selection: Optional["TriageResponsibilityManualSelectionInput"] = Field(
        alias="manualSelection", default=None
    )
    time_schedule_id: Optional[str] = Field(alias="timeScheduleId", default=None)


class UserUpdateInput(BaseModel):
    name: Optional[str] = None
    display_name: Optional[str] = Field(alias="displayName", default=None)
    avatar_url: Optional[str] = Field(alias="avatarUrl", default=None)
    active: Optional[bool] = None
    disable_reason: Optional[str] = Field(alias="disableReason", default=None)
    admin: Optional[bool] = None
    description: Optional[str] = None
    status_emoji: Optional[str] = Field(alias="statusEmoji", default=None)
    status_label: Optional[str] = Field(alias="statusLabel", default=None)
    status_until_at: Optional[Any] = Field(alias="statusUntilAt", default=None)
    timezone: Optional[str] = None


class UserSettingsUpdateInput(BaseModel):
    settings: Optional[Any] = None
    unsubscribed_from: Optional[List[str]] = Field(
        alias="unsubscribedFrom", default=None
    )
    subscribed_to_changelog: Optional[bool] = Field(
        alias="subscribedToChangelog", default=None
    )
    subscribed_to_dpa: Optional[bool] = Field(alias="subscribedToDPA", default=None)
    subscribed_to_invite_accepted: Optional[bool] = Field(
        alias="subscribedToInviteAccepted", default=None
    )
    subscribed_to_privacy_legal_updates: Optional[bool] = Field(
        alias="subscribedToPrivacyLegalUpdates", default=None
    )
    subscribed_to_unread_notifications_reminder: Optional[bool] = Field(
        alias="subscribedToUnreadNotificationsReminder", default=None
    )
    notification_preferences: Optional[Any] = Field(
        alias="notificationPreferences", default=None
    )
    notification_delivery_preferences: Optional[
        "NotificationDeliveryPreferencesInput"
    ] = Field(alias="notificationDeliveryPreferences", default=None)
    usage_warning_history: Optional[Any] = Field(
        alias="usageWarningHistory", default=None
    )


class ViewPreferencesCreateInput(BaseModel):
    id: Optional[str] = None
    type: ViewPreferencesType
    view_type: ViewType = Field(alias="viewType")
    preferences: Any
    insights: Optional[Any] = None
    team_id: Optional[str] = Field(alias="teamId", default=None)
    project_id: Optional[str] = Field(alias="projectId", default=None)
    roadmap_id: Optional[str] = Field(alias="roadmapId", default=None)
    initiative_id: Optional[str] = Field(alias="initiativeId", default=None)
    label_id: Optional[str] = Field(alias="labelId", default=None)
    cycle_id: Optional[str] = Field(alias="cycleId", default=None)
    custom_view_id: Optional[str] = Field(alias="customViewId", default=None)
    user_id: Optional[str] = Field(alias="userId", default=None)


class ViewPreferencesUpdateInput(BaseModel):
    preferences: Optional[Any] = None
    insights: Optional[Any] = None


class WebhookCreateInput(BaseModel):
    label: Optional[str] = None
    id: Optional[str] = None
    enabled: Optional[bool] = True
    secret: Optional[str] = None
    url: str
    resource_types: List[str] = Field(alias="resourceTypes")
    team_id: Optional[str] = Field(alias="teamId", default=None)
    all_public_teams: Optional[bool] = Field(alias="allPublicTeams", default=None)


class WebhookUpdateInput(BaseModel):
    label: Optional[str] = None
    secret: Optional[str] = None
    enabled: Optional[bool] = None
    url: Optional[str] = None
    resource_types: Optional[List[str]] = Field(alias="resourceTypes", default=None)


class WorkflowStateCreateInput(BaseModel):
    id: Optional[str] = None
    type: str
    name: str
    color: str
    description: Optional[str] = None
    position: Optional[float] = None
    team_id: str = Field(alias="teamId")


class WorkflowStateUpdateInput(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    description: Optional[str] = None
    position: Optional[float] = None


EstimateComparator.model_rebuild()
SourceMetadataComparator.model_rebuild()
SlackChannelNameMappingInput.model_rebuild()
SlackAsksSettingsInput.model_rebuild()
GitHubSettingsInput.model_rebuild()
GitHubImportSettingsInput.model_rebuild()
JiraSettingsInput.model_rebuild()
IntegrationSettingsInput.model_rebuild()
AttachmentFilter.model_rebuild()
AttachmentCollectionFilter.model_rebuild()
AuditEntryFilter.model_rebuild()
StringArrayComparator.model_rebuild()
CustomerFilter.model_rebuild()
CustomerCollectionFilter.model_rebuild()
CustomerNeedFilter.model_rebuild()
CustomerNeedCollectionFilter.model_rebuild()
CommentFilter.model_rebuild()
NullableCommentFilter.model_rebuild()
CommentCollectionFilter.model_rebuild()
CycleFilter.model_rebuild()
NullableCycleFilter.model_rebuild()
ProjectStatusFilter.model_rebuild()
NullableIssueFilter.model_rebuild()
IssueFilter.model_rebuild()
IssueCollectionFilter.model_rebuild()
NullableTemplateFilter.model_rebuild()
UserFilter.model_rebuild()
NullableUserFilter.model_rebuild()
UserCollectionFilter.model_rebuild()
InitiativeFilter.model_rebuild()
InitiativeCollectionFilter.model_rebuild()
ProjectUpdatesFilter.model_rebuild()
NullableProjectUpdatesFilter.model_rebuild()
ProjectUpdatesCollectionFilter.model_rebuild()
ProjectFilter.model_rebuild()
NullableProjectFilter.model_rebuild()
ProjectCollectionFilter.model_rebuild()
ProjectMilestoneFilter.model_rebuild()
NullableProjectMilestoneFilter.model_rebuild()
ProjectMilestoneCollectionFilter.model_rebuild()
RoadmapFilter.model_rebuild()
RoadmapCollectionFilter.model_rebuild()
TeamFilter.model_rebuild()
NullableTeamFilter.model_rebuild()
TeamCollectionFilter.model_rebuild()
WorkflowStateFilter.model_rebuild()
NullableDocumentContentFilter.model_rebuild()
DocumentContentFilter.model_rebuild()
IssueLabelFilter.model_rebuild()
IssueLabelCollectionFilter.model_rebuild()
ProjectUpdateFilter.model_rebuild()
DocumentFilter.model_rebuild()
NullableDocumentFilter.model_rebuild()
DocumentCollectionFilter.model_rebuild()
ReactionFilter.model_rebuild()
NullableReactionFilter.model_rebuild()
ReactionCollectionFilter.model_rebuild()
NotificationFilter.model_rebuild()
NotificationDeliveryPreferencesScheduleInput.model_rebuild()
NotificationDeliveryPreferencesChannelInput.model_rebuild()
NotificationDeliveryPreferencesInput.model_rebuild()
WorkflowCondition.model_rebuild()
IssueSortInput.model_rebuild()
CustomViewCreateInput.model_rebuild()
CustomViewUpdateInput.model_rebuild()
OrganizationUpdateInput.model_rebuild()
TimeScheduleCreateInput.model_rebuild()
TimeScheduleUpdateInput.model_rebuild()
TriageResponsibilityCreateInput.model_rebuild()
TriageResponsibilityUpdateInput.model_rebuild()
UserSettingsUpdateInput.model_rebuild()
