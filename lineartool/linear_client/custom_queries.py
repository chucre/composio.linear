from typing import Any, Dict, Optional

from . import PaginationOrderBy, SendStrategy
from .custom_fields import (
    ApiKeyConnectionFields,
    ApplicationFields,
    AttachmentConnectionFields,
    AttachmentFields,
    AttachmentSourcesPayloadFields,
    AuditEntryConnectionFields,
    AuditEntryTypeFields,
    AuthenticationSessionResponseFields,
    AuthorizedApplicationFields,
    AuthResolverResponseFields,
    CommentConnectionFields,
    CommentFields,
    CustomerConnectionFields,
    CustomerFields,
    CustomerNeedConnectionFields,
    CustomerNeedFields,
    CustomerStatusConnectionFields,
    CustomerStatusFields,
    CustomViewConnectionFields,
    CustomViewFields,
    CustomViewHasSubscribersPayloadFields,
    CustomViewSuggestionPayloadFields,
    CycleConnectionFields,
    CycleFields,
    DiaryEntryFields,
    DocumentConnectionFields,
    DocumentContentHistoryPayloadFields,
    DocumentFields,
    DocumentSearchPayloadFields,
    EmojiConnectionFields,
    EmojiFields,
    EntityExternalLinkFields,
    ExternalUserConnectionFields,
    ExternalUserFields,
    FavoriteConnectionFields,
    FavoriteFields,
    GitHubEnterpriseServerInstallVerificationPayloadFields,
    InitiativeConnectionFields,
    InitiativeFields,
    InitiativeToProjectConnectionFields,
    InitiativeToProjectFields,
    IntegrationConnectionFields,
    IntegrationFields,
    IntegrationHasScopesPayloadFields,
    IntegrationsSettingsFields,
    IntegrationTemplateConnectionFields,
    IntegrationTemplateFields,
    IssueConnectionFields,
    IssueFields,
    IssueFilterSuggestionPayloadFields,
    IssueImportCheckPayloadFields,
    IssueImportSyncCheckPayloadFields,
    IssueLabelConnectionFields,
    IssueLabelFields,
    IssuePriorityValueFields,
    IssueRelationConnectionFields,
    IssueRelationFields,
    IssueSearchPayloadFields,
    NotificationConnectionFields,
    NotificationInterface,
    NotificationSubscriptionConnectionFields,
    NotificationSubscriptionInterface,
    OrganizationDomainClaimPayloadFields,
    OrganizationExistsPayloadFields,
    OrganizationFields,
    OrganizationInviteConnectionFields,
    OrganizationInviteFields,
    OrganizationMetaFields,
    ProjectConnectionFields,
    ProjectFields,
    ProjectFilterSuggestionPayloadFields,
    ProjectLinkConnectionFields,
    ProjectLinkFields,
    ProjectMilestoneConnectionFields,
    ProjectMilestoneFields,
    ProjectRelationConnectionFields,
    ProjectRelationFields,
    ProjectSearchPayloadFields,
    ProjectUpdateConnectionFields,
    ProjectUpdateFields,
    ProjectUpdateInteractionConnectionFields,
    ProjectUpdateInteractionFields,
    PushSubscriptionTestPayloadFields,
    RateLimitPayloadFields,
    RoadmapConnectionFields,
    RoadmapFields,
    RoadmapToProjectConnectionFields,
    RoadmapToProjectFields,
    SsoUrlFromEmailResponseFields,
    SummaryPayloadFields,
    TeamConnectionFields,
    TeamFields,
    TeamMembershipConnectionFields,
    TeamMembershipFields,
    TemplateFields,
    TimeScheduleConnectionFields,
    TimeScheduleFields,
    TriageResponsibilityConnectionFields,
    TriageResponsibilityFields,
    UserAuthorizedApplicationFields,
    UserConnectionFields,
    UserFields,
    UserSettingsFields,
    WebhookConnectionFields,
    WebhookFields,
    WorkflowStateConnectionFields,
    WorkflowStateFields,
    WorkspaceAuthorizedApplicationFields,
)
from .custom_typing_fields import GraphQLField, OrganizationInviteDetailsPayloadUnion
from .input_types import (
    AttachmentFilter,
    AuditEntryFilter,
    CommentFilter,
    CustomerFilter,
    CustomerNeedFilter,
    CycleFilter,
    DocumentFilter,
    IssueFilter,
    IssueLabelFilter,
    IssueSortInput,
    NotificationFilter,
    ProjectFilter,
    ProjectMilestoneFilter,
    ProjectUpdateFilter,
    TeamFilter,
    UserFilter,
    WorkflowStateFilter,
)


class Query:
    @classmethod
    def api_keys(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ApiKeyConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ApiKeyConnectionFields(field_name="apiKeys", arguments=cleared_arguments)

    @classmethod
    def application_info(cls, client_id: str) -> ApplicationFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "clientId": {"type": "String!", "value": client_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ApplicationFields(
            field_name="applicationInfo", arguments=cleared_arguments
        )

    @classmethod
    def application_info_by_ids(cls, ids: str) -> ApplicationFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "String!", "value": ids}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ApplicationFields(
            field_name="applicationInfoByIds", arguments=cleared_arguments
        )

    @classmethod
    def application_info_with_memberships_by_ids(
        cls, client_ids: str
    ) -> WorkspaceAuthorizedApplicationFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "clientIds": {"type": "String!", "value": client_ids}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkspaceAuthorizedApplicationFields(
            field_name="applicationInfoWithMembershipsByIds",
            arguments=cleared_arguments,
        )

    @classmethod
    def application_with_authorization(
        cls,
        scope: str,
        client_id: str,
        *,
        actor: Optional[str] = None,
        redirect_uri: Optional[str] = None
    ) -> UserAuthorizedApplicationFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "actor": {"type": "String", "value": actor},
            "redirectUri": {"type": "String", "value": redirect_uri},
            "scope": {"type": "String!", "value": scope},
            "clientId": {"type": "String!", "value": client_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserAuthorizedApplicationFields(
            field_name="applicationWithAuthorization", arguments=cleared_arguments
        )

    @classmethod
    def authorized_applications(cls) -> AuthorizedApplicationFields:
        return AuthorizedApplicationFields(field_name="authorizedApplications")

    @classmethod
    def workspace_authorized_applications(cls) -> WorkspaceAuthorizedApplicationFields:
        return WorkspaceAuthorizedApplicationFields(
            field_name="workspaceAuthorizedApplications"
        )

    @classmethod
    def attachments(
        cls,
        *,
        filter: Optional[AttachmentFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> AttachmentConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "AttachmentFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentConnectionFields(
            field_name="attachments", arguments=cleared_arguments
        )

    @classmethod
    def attachment(cls, id: str) -> AttachmentFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentFields(field_name="attachment", arguments=cleared_arguments)

    @classmethod
    def attachments_for_url(
        cls,
        url: str,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> AttachmentConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
            "url": {"type": "String!", "value": url},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentConnectionFields(
            field_name="attachmentsForURL", arguments=cleared_arguments
        )

    @classmethod
    def attachment_issue(cls, id: str) -> IssueFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueFields(field_name="attachmentIssue", arguments=cleared_arguments)

    @classmethod
    def attachment_sources(
        cls, *, team_id: Optional[str] = None
    ) -> AttachmentSourcesPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "teamId": {"type": "String", "value": team_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentSourcesPayloadFields(
            field_name="attachmentSources", arguments=cleared_arguments
        )

    @classmethod
    def audit_entry_types(cls) -> AuditEntryTypeFields:
        return AuditEntryTypeFields(field_name="auditEntryTypes")

    @classmethod
    def audit_entries(
        cls,
        *,
        filter: Optional[AuditEntryFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> AuditEntryConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "AuditEntryFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AuditEntryConnectionFields(
            field_name="auditEntries", arguments=cleared_arguments
        )

    @classmethod
    def available_users(cls) -> AuthResolverResponseFields:
        return AuthResolverResponseFields(field_name="availableUsers")

    @classmethod
    def authentication_sessions(cls) -> AuthenticationSessionResponseFields:
        return AuthenticationSessionResponseFields(field_name="authenticationSessions")

    @classmethod
    def sso_url_from_email(
        cls, email: str, *, is_desktop: Optional[bool] = None
    ) -> SsoUrlFromEmailResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "isDesktop": {"type": "Boolean", "value": is_desktop},
            "email": {"type": "String!", "value": email},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SsoUrlFromEmailResponseFields(
            field_name="ssoUrlFromEmail", arguments=cleared_arguments
        )

    @classmethod
    def comments(
        cls,
        *,
        filter: Optional[CommentFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> CommentConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "CommentFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CommentConnectionFields(
            field_name="comments", arguments=cleared_arguments
        )

    @classmethod
    def comment(
        cls,
        *,
        id: Optional[str] = None,
        issue_id: Optional[str] = None,
        hash: Optional[str] = None
    ) -> CommentFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "id": {"type": "String", "value": id},
            "issueId": {"type": "String", "value": issue_id},
            "hash": {"type": "String", "value": hash},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CommentFields(field_name="comment", arguments=cleared_arguments)

    @classmethod
    def customer_needs(
        cls,
        *,
        filter: Optional[CustomerNeedFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> CustomerNeedConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "CustomerNeedFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerNeedConnectionFields(
            field_name="customerNeeds", arguments=cleared_arguments
        )

    @classmethod
    def customer_need(cls, id: str) -> CustomerNeedFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerNeedFields(
            field_name="customerNeed", arguments=cleared_arguments
        )

    @classmethod
    def customers(
        cls,
        *,
        filter: Optional[CustomerFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> CustomerConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "CustomerFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerConnectionFields(
            field_name="customers", arguments=cleared_arguments
        )

    @classmethod
    def customer(cls, id: str) -> CustomerFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerFields(field_name="customer", arguments=cleared_arguments)

    @classmethod
    def customer_statuses(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> CustomerStatusConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerStatusConnectionFields(
            field_name="customerStatuses", arguments=cleared_arguments
        )

    @classmethod
    def customer_status(cls, id: str) -> CustomerStatusFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerStatusFields(
            field_name="customerStatus", arguments=cleared_arguments
        )

    @classmethod
    def custom_views(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> CustomViewConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomViewConnectionFields(
            field_name="customViews", arguments=cleared_arguments
        )

    @classmethod
    def custom_view(cls, id: str) -> CustomViewFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomViewFields(field_name="customView", arguments=cleared_arguments)

    @classmethod
    def custom_view_details_suggestion(
        cls, filter: Any, *, model_name: Optional[str] = None
    ) -> CustomViewSuggestionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "modelName": {"type": "String", "value": model_name},
            "filter": {"type": "JSONObject!", "value": filter},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomViewSuggestionPayloadFields(
            field_name="customViewDetailsSuggestion", arguments=cleared_arguments
        )

    @classmethod
    def custom_view_has_subscribers(
        cls, id: str
    ) -> CustomViewHasSubscribersPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomViewHasSubscribersPayloadFields(
            field_name="customViewHasSubscribers", arguments=cleared_arguments
        )

    @classmethod
    def cycles(
        cls,
        *,
        filter: Optional[CycleFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> CycleConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "CycleFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CycleConnectionFields(field_name="cycles", arguments=cleared_arguments)

    @classmethod
    def cycle(cls, id: str) -> CycleFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CycleFields(field_name="cycle", arguments=cleared_arguments)

    @classmethod
    def diary_entry(cls, id: str) -> DiaryEntryFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DiaryEntryFields(field_name="diaryEntry", arguments=cleared_arguments)

    @classmethod
    def document_content_history(cls, id: str) -> DocumentContentHistoryPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentContentHistoryPayloadFields(
            field_name="documentContentHistory", arguments=cleared_arguments
        )

    @classmethod
    def documents(
        cls,
        *,
        filter: Optional[DocumentFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> DocumentConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "DocumentFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentConnectionFields(
            field_name="documents", arguments=cleared_arguments
        )

    @classmethod
    def document(cls, id: str) -> DocumentFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentFields(field_name="document", arguments=cleared_arguments)

    @classmethod
    def emojis(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> EmojiConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmojiConnectionFields(field_name="emojis", arguments=cleared_arguments)

    @classmethod
    def emoji(cls, id: str) -> EmojiFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmojiFields(field_name="emoji", arguments=cleared_arguments)

    @classmethod
    def entity_external_link(cls, id: str) -> EntityExternalLinkFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EntityExternalLinkFields(
            field_name="entityExternalLink", arguments=cleared_arguments
        )

    @classmethod
    def external_users(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ExternalUserConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ExternalUserConnectionFields(
            field_name="externalUsers", arguments=cleared_arguments
        )

    @classmethod
    def external_user(cls, id: str) -> ExternalUserFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ExternalUserFields(
            field_name="externalUser", arguments=cleared_arguments
        )

    @classmethod
    def initiative_to_projects(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> InitiativeToProjectConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeToProjectConnectionFields(
            field_name="initiativeToProjects", arguments=cleared_arguments
        )

    @classmethod
    def initiative_to_project(cls, id: str) -> InitiativeToProjectFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeToProjectFields(
            field_name="initiativeToProject", arguments=cleared_arguments
        )

    @classmethod
    def initiatives(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> InitiativeConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeConnectionFields(
            field_name="initiatives", arguments=cleared_arguments
        )

    @classmethod
    def initiative(cls, id: str) -> InitiativeFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeFields(field_name="initiative", arguments=cleared_arguments)

    @classmethod
    def favorites(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> FavoriteConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FavoriteConnectionFields(
            field_name="favorites", arguments=cleared_arguments
        )

    @classmethod
    def favorite(cls, id: str) -> FavoriteFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FavoriteFields(field_name="favorite", arguments=cleared_arguments)

    @classmethod
    def integrations(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> IntegrationConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationConnectionFields(
            field_name="integrations", arguments=cleared_arguments
        )

    @classmethod
    def integration(cls, id: str) -> IntegrationFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationFields(field_name="integration", arguments=cleared_arguments)

    @classmethod
    def verify_git_hub_enterprise_server_installation(
        cls,
    ) -> GitHubEnterpriseServerInstallVerificationPayloadFields:
        return GitHubEnterpriseServerInstallVerificationPayloadFields(
            field_name="verifyGitHubEnterpriseServerInstallation"
        )

    @classmethod
    def integration_has_scopes(
        cls, scopes: str, integration_id: str
    ) -> IntegrationHasScopesPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "scopes": {"type": "String!", "value": scopes},
            "integrationId": {"type": "String!", "value": integration_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationHasScopesPayloadFields(
            field_name="integrationHasScopes", arguments=cleared_arguments
        )

    @classmethod
    def project_updates(
        cls,
        *,
        filter: Optional[ProjectUpdateFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ProjectUpdateConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "ProjectUpdateFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdateConnectionFields(
            field_name="projectUpdates", arguments=cleared_arguments
        )

    @classmethod
    def integrations_settings(cls, id: str) -> IntegrationsSettingsFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationsSettingsFields(
            field_name="integrationsSettings", arguments=cleared_arguments
        )

    @classmethod
    def integration_templates(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> IntegrationTemplateConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationTemplateConnectionFields(
            field_name="integrationTemplates", arguments=cleared_arguments
        )

    @classmethod
    def integration_template(cls, id: str) -> IntegrationTemplateFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationTemplateFields(
            field_name="integrationTemplate", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_check_csv(
        cls, csv_url: str, service: str
    ) -> IssueImportCheckPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "csvUrl": {"type": "String!", "value": csv_url},
            "service": {"type": "String!", "value": service},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportCheckPayloadFields(
            field_name="issueImportCheckCSV", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_check_sync(
        cls, issue_import_id: str
    ) -> IssueImportSyncCheckPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "issueImportId": {"type": "String!", "value": issue_import_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportSyncCheckPayloadFields(
            field_name="issueImportCheckSync", arguments=cleared_arguments
        )

    @classmethod
    def issue_labels(
        cls,
        *,
        filter: Optional[IssueLabelFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> IssueLabelConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueLabelFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueLabelConnectionFields(
            field_name="issueLabels", arguments=cleared_arguments
        )

    @classmethod
    def issue_label(cls, id: str) -> IssueLabelFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueLabelFields(field_name="issueLabel", arguments=cleared_arguments)

    @classmethod
    def issue_relations(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> IssueRelationConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueRelationConnectionFields(
            field_name="issueRelations", arguments=cleared_arguments
        )

    @classmethod
    def issue_relation(cls, id: str) -> IssueRelationFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueRelationFields(
            field_name="issueRelation", arguments=cleared_arguments
        )

    @classmethod
    def issues(
        cls,
        *,
        filter: Optional[IssueFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None,
        sort: Optional[IssueSortInput] = None
    ) -> IssueConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
            "sort": {"type": "IssueSortInput", "value": sort},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueConnectionFields(field_name="issues", arguments=cleared_arguments)

    @classmethod
    def issue(cls, id: str) -> IssueFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueFields(field_name="issue", arguments=cleared_arguments)

    @classmethod
    def issue_search(
        cls,
        *,
        filter: Optional[IssueFilter] = None,
        query: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> IssueConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
            "query": {"type": "String", "value": query},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueConnectionFields(
            field_name="issueSearch", arguments=cleared_arguments
        )

    @classmethod
    def issue_vcs_branch_search(cls, branch_name: str) -> IssueFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "branchName": {"type": "String!", "value": branch_name}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueFields(
            field_name="issueVcsBranchSearch", arguments=cleared_arguments
        )

    @classmethod
    def issue_figma_file_key_search(
        cls,
        file_key: str,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> IssueConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
            "fileKey": {"type": "String!", "value": file_key},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueConnectionFields(
            field_name="issueFigmaFileKeySearch", arguments=cleared_arguments
        )

    @classmethod
    def issue_priority_values(cls) -> IssuePriorityValueFields:
        return IssuePriorityValueFields(field_name="issuePriorityValues")

    @classmethod
    def issue_filter_suggestion(
        cls, prompt: str, *, project_id: Optional[str] = None
    ) -> IssueFilterSuggestionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "projectId": {"type": "String", "value": project_id},
            "prompt": {"type": "String!", "value": prompt},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueFilterSuggestionPayloadFields(
            field_name="issueFilterSuggestion", arguments=cleared_arguments
        )

    @classmethod
    def notifications(
        cls,
        *,
        filter: Optional[NotificationFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> NotificationConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "NotificationFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationConnectionFields(
            field_name="notifications", arguments=cleared_arguments
        )

    @classmethod
    def notifications_unread_count(cls) -> GraphQLField:
        return GraphQLField(field_name="notificationsUnreadCount")

    @classmethod
    def notification(cls, id: str) -> NotificationInterface:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationInterface(
            field_name="notification", arguments=cleared_arguments
        )

    @classmethod
    def notification_subscriptions(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> NotificationSubscriptionConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationSubscriptionConnectionFields(
            field_name="notificationSubscriptions", arguments=cleared_arguments
        )

    @classmethod
    def notification_subscription(cls, id: str) -> NotificationSubscriptionInterface:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationSubscriptionInterface(
            field_name="notificationSubscription", arguments=cleared_arguments
        )

    @classmethod
    def organization_domain_claim_request(
        cls, id: str
    ) -> OrganizationDomainClaimPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationDomainClaimPayloadFields(
            field_name="organizationDomainClaimRequest", arguments=cleared_arguments
        )

    @classmethod
    def organization_invites(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> OrganizationInviteConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationInviteConnectionFields(
            field_name="organizationInvites", arguments=cleared_arguments
        )

    @classmethod
    def organization_invite(cls, id: str) -> OrganizationInviteFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationInviteFields(
            field_name="organizationInvite", arguments=cleared_arguments
        )

    @classmethod
    def organization_invite_details(
        cls, id: str
    ) -> OrganizationInviteDetailsPayloadUnion:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationInviteDetailsPayloadUnion(
            field_name="organizationInviteDetails", arguments=cleared_arguments
        )

    @classmethod
    def organization(cls) -> OrganizationFields:
        return OrganizationFields(field_name="organization")

    @classmethod
    def organization_exists(cls, url_key: str) -> OrganizationExistsPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "urlKey": {"type": "String!", "value": url_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationExistsPayloadFields(
            field_name="organizationExists", arguments=cleared_arguments
        )

    @classmethod
    def archived_teams(cls) -> TeamFields:
        return TeamFields(field_name="archivedTeams")

    @classmethod
    def organization_meta(cls, url_key: str) -> OrganizationMetaFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "urlKey": {"type": "String!", "value": url_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationMetaFields(
            field_name="organizationMeta", arguments=cleared_arguments
        )

    @classmethod
    def project_links(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ProjectLinkConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectLinkConnectionFields(
            field_name="projectLinks", arguments=cleared_arguments
        )

    @classmethod
    def project_link(cls, id: str) -> ProjectLinkFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectLinkFields(field_name="projectLink", arguments=cleared_arguments)

    @classmethod
    def project_milestones(
        cls,
        *,
        filter: Optional[ProjectMilestoneFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ProjectMilestoneConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "ProjectMilestoneFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectMilestoneConnectionFields(
            field_name="projectMilestones", arguments=cleared_arguments
        )

    @classmethod
    def project_milestone(cls, id: str) -> ProjectMilestoneFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectMilestoneFields(
            field_name="projectMilestone", arguments=cleared_arguments
        )

    @classmethod
    def project_relations(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ProjectRelationConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectRelationConnectionFields(
            field_name="projectRelations", arguments=cleared_arguments
        )

    @classmethod
    def project_relation(cls, id: str) -> ProjectRelationFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectRelationFields(
            field_name="projectRelation", arguments=cleared_arguments
        )

    @classmethod
    def projects(
        cls,
        *,
        filter: Optional[ProjectFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ProjectConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "ProjectFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectConnectionFields(
            field_name="projects", arguments=cleared_arguments
        )

    @classmethod
    def project(cls, id: str) -> ProjectFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectFields(field_name="project", arguments=cleared_arguments)

    @classmethod
    def project_filter_suggestion(
        cls, prompt: str
    ) -> ProjectFilterSuggestionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "prompt": {"type": "String!", "value": prompt}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectFilterSuggestionPayloadFields(
            field_name="projectFilterSuggestion", arguments=cleared_arguments
        )

    @classmethod
    def project_update_interactions(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> ProjectUpdateInteractionConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdateInteractionConnectionFields(
            field_name="projectUpdateInteractions", arguments=cleared_arguments
        )

    @classmethod
    def project_update_interaction(cls, id: str) -> ProjectUpdateInteractionFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdateInteractionFields(
            field_name="projectUpdateInteraction", arguments=cleared_arguments
        )

    @classmethod
    def project_update(cls, id: str) -> ProjectUpdateFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdateFields(
            field_name="projectUpdate", arguments=cleared_arguments
        )

    @classmethod
    def summarize_project_updates(cls, ids: str) -> SummaryPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "ids": {"type": "String!", "value": ids}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SummaryPayloadFields(
            field_name="summarizeProjectUpdates", arguments=cleared_arguments
        )

    @classmethod
    def push_subscription_test(
        cls,
        *,
        target_mobile: Optional[bool] = None,
        send_strategy: Optional[SendStrategy] = None
    ) -> PushSubscriptionTestPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "targetMobile": {"type": "Boolean", "value": target_mobile},
            "sendStrategy": {"type": "SendStrategy", "value": send_strategy},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PushSubscriptionTestPayloadFields(
            field_name="pushSubscriptionTest", arguments=cleared_arguments
        )

    @classmethod
    def rate_limit_status(cls) -> RateLimitPayloadFields:
        return RateLimitPayloadFields(field_name="rateLimitStatus")

    @classmethod
    def roadmaps(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> RoadmapConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapConnectionFields(
            field_name="roadmaps", arguments=cleared_arguments
        )

    @classmethod
    def roadmap(cls, id: str) -> RoadmapFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapFields(field_name="roadmap", arguments=cleared_arguments)

    @classmethod
    def roadmap_to_projects(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> RoadmapToProjectConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapToProjectConnectionFields(
            field_name="roadmapToProjects", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_to_project(cls, id: str) -> RoadmapToProjectFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapToProjectFields(
            field_name="roadmapToProject", arguments=cleared_arguments
        )

    @classmethod
    def search_documents(
        cls,
        term: str,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None,
        snippet_size: Optional[float] = None,
        include_comments: Optional[bool] = None,
        team_id: Optional[str] = None
    ) -> DocumentSearchPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
            "term": {"type": "String!", "value": term},
            "snippetSize": {"type": "Float", "value": snippet_size},
            "includeComments": {"type": "Boolean", "value": include_comments},
            "teamId": {"type": "String", "value": team_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentSearchPayloadFields(
            field_name="searchDocuments", arguments=cleared_arguments
        )

    @classmethod
    def search_projects(
        cls,
        term: str,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None,
        snippet_size: Optional[float] = None,
        include_comments: Optional[bool] = None,
        team_id: Optional[str] = None
    ) -> ProjectSearchPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
            "term": {"type": "String!", "value": term},
            "snippetSize": {"type": "Float", "value": snippet_size},
            "includeComments": {"type": "Boolean", "value": include_comments},
            "teamId": {"type": "String", "value": team_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectSearchPayloadFields(
            field_name="searchProjects", arguments=cleared_arguments
        )

    @classmethod
    def search_issues(
        cls,
        term: str,
        *,
        filter: Optional[IssueFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None,
        snippet_size: Optional[float] = None,
        include_comments: Optional[bool] = None,
        team_id: Optional[str] = None
    ) -> IssueSearchPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
            "term": {"type": "String!", "value": term},
            "snippetSize": {"type": "Float", "value": snippet_size},
            "includeComments": {"type": "Boolean", "value": include_comments},
            "teamId": {"type": "String", "value": team_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueSearchPayloadFields(
            field_name="searchIssues", arguments=cleared_arguments
        )

    @classmethod
    def team_memberships(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> TeamMembershipConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamMembershipConnectionFields(
            field_name="teamMemberships", arguments=cleared_arguments
        )

    @classmethod
    def team_membership(cls, id: str) -> TeamMembershipFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamMembershipFields(
            field_name="teamMembership", arguments=cleared_arguments
        )

    @classmethod
    def teams(
        cls,
        *,
        filter: Optional[TeamFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> TeamConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "TeamFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamConnectionFields(field_name="teams", arguments=cleared_arguments)

    @classmethod
    def administrable_teams(
        cls,
        *,
        filter: Optional[TeamFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> TeamConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "TeamFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamConnectionFields(
            field_name="administrableTeams", arguments=cleared_arguments
        )

    @classmethod
    def team(cls, id: str) -> TeamFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamFields(field_name="team", arguments=cleared_arguments)

    @classmethod
    def templates(cls) -> TemplateFields:
        return TemplateFields(field_name="templates")

    @classmethod
    def template(cls, id: str) -> TemplateFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TemplateFields(field_name="template", arguments=cleared_arguments)

    @classmethod
    def templates_for_integration(cls, integration_type: str) -> TemplateFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "integrationType": {"type": "String!", "value": integration_type}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TemplateFields(
            field_name="templatesForIntegration", arguments=cleared_arguments
        )

    @classmethod
    def time_schedules(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> TimeScheduleConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimeScheduleConnectionFields(
            field_name="timeSchedules", arguments=cleared_arguments
        )

    @classmethod
    def time_schedule(cls, id: str) -> TimeScheduleFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimeScheduleFields(
            field_name="timeSchedule", arguments=cleared_arguments
        )

    @classmethod
    def triage_responsibilities(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> TriageResponsibilityConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TriageResponsibilityConnectionFields(
            field_name="triageResponsibilities", arguments=cleared_arguments
        )

    @classmethod
    def triage_responsibility(cls, id: str) -> TriageResponsibilityFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TriageResponsibilityFields(
            field_name="triageResponsibility", arguments=cleared_arguments
        )

    @classmethod
    def users(
        cls,
        *,
        filter: Optional[UserFilter] = None,
        include_disabled: Optional[bool] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> UserConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "UserFilter", "value": filter},
            "includeDisabled": {"type": "Boolean", "value": include_disabled},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserConnectionFields(field_name="users", arguments=cleared_arguments)

    @classmethod
    def user(cls, id: str) -> UserFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserFields(field_name="user", arguments=cleared_arguments)

    @classmethod
    def viewer(cls) -> UserFields:
        return UserFields(field_name="viewer")

    @classmethod
    def user_settings(cls) -> UserSettingsFields:
        return UserSettingsFields(field_name="userSettings")

    @classmethod
    def webhooks(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> WebhookConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WebhookConnectionFields(
            field_name="webhooks", arguments=cleared_arguments
        )

    @classmethod
    def webhook(cls, id: str) -> WebhookFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WebhookFields(field_name="webhook", arguments=cleared_arguments)

    @classmethod
    def workflow_states(
        cls,
        *,
        filter: Optional[WorkflowStateFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> WorkflowStateConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "WorkflowStateFilter", "value": filter},
            "before": {"type": "String", "value": before},
            "after": {"type": "String", "value": after},
            "first": {"type": "Int", "value": first},
            "last": {"type": "Int", "value": last},
            "includeArchived": {"type": "Boolean", "value": include_archived},
            "orderBy": {"type": "PaginationOrderBy", "value": order_by},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkflowStateConnectionFields(
            field_name="workflowStates", arguments=cleared_arguments
        )

    @classmethod
    def workflow_state(cls, id: str) -> WorkflowStateFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkflowStateFields(
            field_name="workflowState", arguments=cleared_arguments
        )
