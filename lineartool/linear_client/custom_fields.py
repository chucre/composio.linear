from typing import Any, Dict, Optional, Union

from . import PaginationOrderBy
from .base_operation import GraphQLField
from .custom_typing_fields import (
    ActorBotGraphQLField,
    ApiKeyConnectionGraphQLField,
    ApiKeyEdgeGraphQLField,
    ApiKeyGraphQLField,
    ApiKeyPayloadGraphQLField,
    ApplicationGraphQLField,
    ArchivePayloadGraphQLField,
    ArchiveResponseGraphQLField,
    AsksChannelConnectPayloadGraphQLField,
    AttachmentArchivePayloadGraphQLField,
    AttachmentConnectionGraphQLField,
    AttachmentEdgeGraphQLField,
    AttachmentGraphQLField,
    AttachmentPayloadGraphQLField,
    AttachmentSourcesPayloadGraphQLField,
    AuditEntryConnectionGraphQLField,
    AuditEntryEdgeGraphQLField,
    AuditEntryGraphQLField,
    AuditEntryTypeGraphQLField,
    AuthenticationSessionResponseGraphQLField,
    AuthMembershipGraphQLField,
    AuthOrganizationGraphQLField,
    AuthorizedApplicationGraphQLField,
    AuthResolverResponseGraphQLField,
    AuthUserGraphQLField,
    CommentConnectionGraphQLField,
    CommentEdgeGraphQLField,
    CommentGraphQLField,
    CommentPayloadGraphQLField,
    ContactPayloadGraphQLField,
    CreateCsvExportReportPayloadGraphQLField,
    CreateOrJoinOrganizationResponseGraphQLField,
    CustomerConnectionGraphQLField,
    CustomerEdgeGraphQLField,
    CustomerGraphQLField,
    CustomerNeedConnectionGraphQLField,
    CustomerNeedEdgeGraphQLField,
    CustomerNeedGraphQLField,
    CustomerNeedPayloadGraphQLField,
    CustomerPayloadGraphQLField,
    CustomerStatusConnectionGraphQLField,
    CustomerStatusEdgeGraphQLField,
    CustomerStatusGraphQLField,
    CustomerStatusPayloadGraphQLField,
    CustomViewConnectionGraphQLField,
    CustomViewEdgeGraphQLField,
    CustomViewGraphQLField,
    CustomViewHasSubscribersPayloadGraphQLField,
    CustomViewPayloadGraphQLField,
    CustomViewSuggestionPayloadGraphQLField,
    CycleArchivePayloadGraphQLField,
    CycleConnectionGraphQLField,
    CycleEdgeGraphQLField,
    CycleGraphQLField,
    CyclePayloadGraphQLField,
    DeletePayloadGraphQLField,
    DiaryEntryGraphQLField,
    DiaryEntryPayloadGraphQLField,
    DocumentArchivePayloadGraphQLField,
    DocumentConnectionGraphQLField,
    DocumentContentGraphQLField,
    DocumentContentHistoryPayloadGraphQLField,
    DocumentContentHistoryTypeGraphQLField,
    DocumentEdgeGraphQLField,
    DocumentGraphQLField,
    DocumentPayloadGraphQLField,
    DocumentSearchPayloadGraphQLField,
    DocumentSearchResultEdgeGraphQLField,
    DocumentSearchResultGraphQLField,
    EmailIntakeAddressGraphQLField,
    EmailIntakeAddressPayloadGraphQLField,
    EmailUnsubscribePayloadGraphQLField,
    EmailUserAccountAuthChallengeResponseGraphQLField,
    EmojiConnectionGraphQLField,
    EmojiEdgeGraphQLField,
    EmojiGraphQLField,
    EmojiPayloadGraphQLField,
    EntityExternalLinkConnectionGraphQLField,
    EntityExternalLinkEdgeGraphQLField,
    EntityExternalLinkGraphQLField,
    EntityExternalLinkPayloadGraphQLField,
    EntityGraphQLField,
    ExternalUserConnectionGraphQLField,
    ExternalUserEdgeGraphQLField,
    ExternalUserGraphQLField,
    FacetGraphQLField,
    FavoriteConnectionGraphQLField,
    FavoriteEdgeGraphQLField,
    FavoriteGraphQLField,
    FavoritePayloadGraphQLField,
    FrontAttachmentPayloadGraphQLField,
    GitAutomationStateConnectionGraphQLField,
    GitAutomationStateEdgeGraphQLField,
    GitAutomationStateGraphQLField,
    GitAutomationStatePayloadGraphQLField,
    GitAutomationTargetBranchGraphQLField,
    GitAutomationTargetBranchPayloadGraphQLField,
    GitHubCommitIntegrationPayloadGraphQLField,
    GitHubEnterpriseServerInstallVerificationPayloadGraphQLField,
    GitHubEnterpriseServerPayloadGraphQLField,
    ImageUploadFromUrlPayloadGraphQLField,
    InitiativeArchivePayloadGraphQLField,
    InitiativeConnectionGraphQLField,
    InitiativeEdgeGraphQLField,
    InitiativeGraphQLField,
    InitiativePayloadGraphQLField,
    InitiativeToProjectConnectionGraphQLField,
    InitiativeToProjectEdgeGraphQLField,
    InitiativeToProjectGraphQLField,
    InitiativeToProjectPayloadGraphQLField,
    IntegrationConnectionGraphQLField,
    IntegrationEdgeGraphQLField,
    IntegrationGraphQLField,
    IntegrationHasScopesPayloadGraphQLField,
    IntegrationPayloadGraphQLField,
    IntegrationRequestPayloadGraphQLField,
    IntegrationsSettingsGraphQLField,
    IntegrationsSettingsPayloadGraphQLField,
    IntegrationTemplateConnectionGraphQLField,
    IntegrationTemplateEdgeGraphQLField,
    IntegrationTemplateGraphQLField,
    IntegrationTemplatePayloadGraphQLField,
    IssueArchivePayloadGraphQLField,
    IssueBatchPayloadGraphQLField,
    IssueConnectionGraphQLField,
    IssueEdgeGraphQLField,
    IssueFilterSuggestionPayloadGraphQLField,
    IssueGraphQLField,
    IssueHistoryConnectionGraphQLField,
    IssueHistoryEdgeGraphQLField,
    IssueHistoryGraphQLField,
    IssueImportCheckPayloadGraphQLField,
    IssueImportDeletePayloadGraphQLField,
    IssueImportGraphQLField,
    IssueImportPayloadGraphQLField,
    IssueImportSyncCheckPayloadGraphQLField,
    IssueLabelConnectionGraphQLField,
    IssueLabelEdgeGraphQLField,
    IssueLabelGraphQLField,
    IssueLabelPayloadGraphQLField,
    IssuePayloadGraphQLField,
    IssuePriorityValueGraphQLField,
    IssueRelationConnectionGraphQLField,
    IssueRelationEdgeGraphQLField,
    IssueRelationGraphQLField,
    IssueRelationHistoryPayloadGraphQLField,
    IssueRelationPayloadGraphQLField,
    IssueSearchPayloadGraphQLField,
    IssueSearchResultEdgeGraphQLField,
    IssueSearchResultGraphQLField,
    LogoutResponseGraphQLField,
    NodeGraphQLField,
    NotificationArchivePayloadGraphQLField,
    NotificationBatchActionPayloadGraphQLField,
    NotificationConnectionGraphQLField,
    NotificationDeliveryPreferencesChannelGraphQLField,
    NotificationDeliveryPreferencesDayGraphQLField,
    NotificationDeliveryPreferencesGraphQLField,
    NotificationDeliveryPreferencesScheduleGraphQLField,
    NotificationEdgeGraphQLField,
    NotificationGraphQLField,
    NotificationPayloadGraphQLField,
    NotificationSubscriptionConnectionGraphQLField,
    NotificationSubscriptionEdgeGraphQLField,
    NotificationSubscriptionGraphQLField,
    NotificationSubscriptionPayloadGraphQLField,
    OrganizationAcceptedOrExpiredInviteDetailsPayloadGraphQLField,
    OrganizationCancelDeletePayloadGraphQLField,
    OrganizationDeletePayloadGraphQLField,
    OrganizationDomainClaimPayloadGraphQLField,
    OrganizationDomainGraphQLField,
    OrganizationDomainPayloadGraphQLField,
    OrganizationDomainSimplePayloadGraphQLField,
    OrganizationExistsPayloadGraphQLField,
    OrganizationGraphQLField,
    OrganizationInviteConnectionGraphQLField,
    OrganizationInviteEdgeGraphQLField,
    OrganizationInviteFullDetailsPayloadGraphQLField,
    OrganizationInviteGraphQLField,
    OrganizationInvitePayloadGraphQLField,
    OrganizationIpRestrictionGraphQLField,
    OrganizationMetaGraphQLField,
    OrganizationPayloadGraphQLField,
    OrganizationStartTrialPayloadGraphQLField,
    PageInfoGraphQLField,
    PaidSubscriptionGraphQLField,
    PasskeyLoginStartResponseGraphQLField,
    ProjectArchivePayloadGraphQLField,
    ProjectConnectionGraphQLField,
    ProjectEdgeGraphQLField,
    ProjectFilterSuggestionPayloadGraphQLField,
    ProjectGraphQLField,
    ProjectLinkConnectionGraphQLField,
    ProjectLinkEdgeGraphQLField,
    ProjectLinkGraphQLField,
    ProjectLinkPayloadGraphQLField,
    ProjectMilestoneConnectionGraphQLField,
    ProjectMilestoneEdgeGraphQLField,
    ProjectMilestoneGraphQLField,
    ProjectMilestonePayloadGraphQLField,
    ProjectPayloadGraphQLField,
    ProjectRelationConnectionGraphQLField,
    ProjectRelationEdgeGraphQLField,
    ProjectRelationGraphQLField,
    ProjectRelationPayloadGraphQLField,
    ProjectSearchPayloadGraphQLField,
    ProjectSearchResultEdgeGraphQLField,
    ProjectSearchResultGraphQLField,
    ProjectStatusGraphQLField,
    ProjectUpdateConnectionGraphQLField,
    ProjectUpdateEdgeGraphQLField,
    ProjectUpdateGraphQLField,
    ProjectUpdateInteractionConnectionGraphQLField,
    ProjectUpdateInteractionEdgeGraphQLField,
    ProjectUpdateInteractionGraphQLField,
    ProjectUpdateInteractionPayloadGraphQLField,
    ProjectUpdatePayloadGraphQLField,
    ProjectUpdateReminderPayloadGraphQLField,
    ProjectUpdateWithInteractionPayloadGraphQLField,
    PushSubscriptionGraphQLField,
    PushSubscriptionPayloadGraphQLField,
    PushSubscriptionTestPayloadGraphQLField,
    RateLimitPayloadGraphQLField,
    RateLimitResultPayloadGraphQLField,
    ReactionGraphQLField,
    ReactionPayloadGraphQLField,
    RoadmapArchivePayloadGraphQLField,
    RoadmapConnectionGraphQLField,
    RoadmapEdgeGraphQLField,
    RoadmapGraphQLField,
    RoadmapPayloadGraphQLField,
    RoadmapToProjectConnectionGraphQLField,
    RoadmapToProjectEdgeGraphQLField,
    RoadmapToProjectGraphQLField,
    RoadmapToProjectPayloadGraphQLField,
    SlackAsksTeamSettingsGraphQLField,
    SlackChannelConnectPayloadGraphQLField,
    SlackChannelNameMappingGraphQLField,
    SsoUrlFromEmailResponseGraphQLField,
    SuccessPayloadGraphQLField,
    SummaryPayloadGraphQLField,
    TeamArchivePayloadGraphQLField,
    TeamConnectionGraphQLField,
    TeamEdgeGraphQLField,
    TeamGraphQLField,
    TeamMembershipConnectionGraphQLField,
    TeamMembershipEdgeGraphQLField,
    TeamMembershipGraphQLField,
    TeamMembershipPayloadGraphQLField,
    TeamPayloadGraphQLField,
    TemplateConnectionGraphQLField,
    TemplateEdgeGraphQLField,
    TemplateGraphQLField,
    TemplatePayloadGraphQLField,
    TextDraftGraphQLField,
    TimeScheduleConnectionGraphQLField,
    TimeScheduleEdgeGraphQLField,
    TimeScheduleEntryGraphQLField,
    TimeScheduleGraphQLField,
    TimeSchedulePayloadGraphQLField,
    TriageResponsibilityConnectionGraphQLField,
    TriageResponsibilityEdgeGraphQLField,
    TriageResponsibilityGraphQLField,
    TriageResponsibilityManualSelectionGraphQLField,
    TriageResponsibilityPayloadGraphQLField,
    UploadFileGraphQLField,
    UploadFileHeaderGraphQLField,
    UploadPayloadGraphQLField,
    UserAdminPayloadGraphQLField,
    UserAuthorizedApplicationGraphQLField,
    UserConnectionGraphQLField,
    UserEdgeGraphQLField,
    UserGraphQLField,
    UserPayloadGraphQLField,
    UserSettingsFlagPayloadGraphQLField,
    UserSettingsFlagsResetPayloadGraphQLField,
    UserSettingsGraphQLField,
    UserSettingsPayloadGraphQLField,
    ViewPreferencesGraphQLField,
    ViewPreferencesPayloadGraphQLField,
    ViewPreferencesValuesGraphQLField,
    WebhookConnectionGraphQLField,
    WebhookEdgeGraphQLField,
    WebhookGraphQLField,
    WebhookPayloadGraphQLField,
    WorkflowStateArchivePayloadGraphQLField,
    WorkflowStateConnectionGraphQLField,
    WorkflowStateEdgeGraphQLField,
    WorkflowStateGraphQLField,
    WorkflowStatePayloadGraphQLField,
    WorkspaceAuthorizedApplicationGraphQLField,
)
from .input_types import (
    AttachmentFilter,
    CommentFilter,
    CycleFilter,
    DocumentFilter,
    IssueFilter,
    IssueLabelFilter,
    IssueSortInput,
    ProjectFilter,
    ProjectMilestoneFilter,
    TeamFilter,
    UserFilter,
    WorkflowStateFilter,
)


class ActorBotFields(GraphQLField):
    id: "ActorBotGraphQLField" = ActorBotGraphQLField("id")
    type: "ActorBotGraphQLField" = ActorBotGraphQLField("type")
    sub_type: "ActorBotGraphQLField" = ActorBotGraphQLField("subType")
    name: "ActorBotGraphQLField" = ActorBotGraphQLField("name")
    user_display_name: "ActorBotGraphQLField" = ActorBotGraphQLField("userDisplayName")
    avatar_url: "ActorBotGraphQLField" = ActorBotGraphQLField("avatarUrl")

    def fields(self, *subfields: ActorBotGraphQLField) -> "ActorBotFields":
        """Subfields should come from the ActorBotFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ActorBotFields":
        self._alias = alias
        return self


class ApiKeyFields(GraphQLField):
    id: "ApiKeyGraphQLField" = ApiKeyGraphQLField("id")
    created_at: "ApiKeyGraphQLField" = ApiKeyGraphQLField("createdAt")
    updated_at: "ApiKeyGraphQLField" = ApiKeyGraphQLField("updatedAt")
    archived_at: "ApiKeyGraphQLField" = ApiKeyGraphQLField("archivedAt")
    label: "ApiKeyGraphQLField" = ApiKeyGraphQLField("label")

    def fields(self, *subfields: ApiKeyGraphQLField) -> "ApiKeyFields":
        """Subfields should come from the ApiKeyFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ApiKeyFields":
        self._alias = alias
        return self


class ApiKeyConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ApiKeyEdgeFields":
        return ApiKeyEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ApiKeyFields":
        return ApiKeyFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ApiKeyConnectionGraphQLField,
            "ApiKeyEdgeFields",
            "ApiKeyFields",
            "PageInfoFields",
        ]
    ) -> "ApiKeyConnectionFields":
        """Subfields should come from the ApiKeyConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ApiKeyConnectionFields":
        self._alias = alias
        return self


class ApiKeyEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ApiKeyFields":
        return ApiKeyFields("node")

    cursor: "ApiKeyEdgeGraphQLField" = ApiKeyEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[ApiKeyEdgeGraphQLField, "ApiKeyFields"]
    ) -> "ApiKeyEdgeFields":
        """Subfields should come from the ApiKeyEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ApiKeyEdgeFields":
        self._alias = alias
        return self


class ApiKeyPayloadFields(GraphQLField):
    last_sync_id: "ApiKeyPayloadGraphQLField" = ApiKeyPayloadGraphQLField("lastSyncId")

    @classmethod
    def api_key(cls) -> "ApiKeyFields":
        return ApiKeyFields("api_key")

    success: "ApiKeyPayloadGraphQLField" = ApiKeyPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[ApiKeyPayloadGraphQLField, "ApiKeyFields"]
    ) -> "ApiKeyPayloadFields":
        """Subfields should come from the ApiKeyPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ApiKeyPayloadFields":
        self._alias = alias
        return self


class ApplicationFields(GraphQLField):
    id: "ApplicationGraphQLField" = ApplicationGraphQLField("id")
    client_id: "ApplicationGraphQLField" = ApplicationGraphQLField("clientId")
    name: "ApplicationGraphQLField" = ApplicationGraphQLField("name")
    description: "ApplicationGraphQLField" = ApplicationGraphQLField("description")
    developer: "ApplicationGraphQLField" = ApplicationGraphQLField("developer")
    developer_url: "ApplicationGraphQLField" = ApplicationGraphQLField("developerUrl")
    image_url: "ApplicationGraphQLField" = ApplicationGraphQLField("imageUrl")

    def fields(self, *subfields: ApplicationGraphQLField) -> "ApplicationFields":
        """Subfields should come from the ApplicationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ApplicationFields":
        self._alias = alias
        return self


class ArchivePayloadInterface(GraphQLField):
    last_sync_id: "ArchivePayloadGraphQLField" = ArchivePayloadGraphQLField(
        "lastSyncId"
    )
    success: "ArchivePayloadGraphQLField" = ArchivePayloadGraphQLField("success")

    def fields(
        self, *subfields: ArchivePayloadGraphQLField
    ) -> "ArchivePayloadInterface":
        """Subfields should come from the ArchivePayloadInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ArchivePayloadInterface":
        self._alias = alias
        return self

    def on(self, type_name: str, *subfields: GraphQLField) -> "ArchivePayloadInterface":
        self._inline_fragments[type_name] = subfields
        return self


class ArchiveResponseFields(GraphQLField):
    archive: "ArchiveResponseGraphQLField" = ArchiveResponseGraphQLField("archive")
    total_count: "ArchiveResponseGraphQLField" = ArchiveResponseGraphQLField(
        "totalCount"
    )
    database_version: "ArchiveResponseGraphQLField" = ArchiveResponseGraphQLField(
        "databaseVersion"
    )
    includes_dependencies: "ArchiveResponseGraphQLField" = ArchiveResponseGraphQLField(
        "includesDependencies"
    )

    def fields(
        self, *subfields: ArchiveResponseGraphQLField
    ) -> "ArchiveResponseFields":
        """Subfields should come from the ArchiveResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ArchiveResponseFields":
        self._alias = alias
        return self


class AsksChannelConnectPayloadFields(GraphQLField):
    last_sync_id: "AsksChannelConnectPayloadGraphQLField" = (
        AsksChannelConnectPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def integration(cls) -> "IntegrationFields":
        return IntegrationFields("integration")

    success: "AsksChannelConnectPayloadGraphQLField" = (
        AsksChannelConnectPayloadGraphQLField("success")
    )

    @classmethod
    def mapping(cls) -> "SlackChannelNameMappingFields":
        return SlackChannelNameMappingFields("mapping")

    add_bot: "AsksChannelConnectPayloadGraphQLField" = (
        AsksChannelConnectPayloadGraphQLField("addBot")
    )

    def fields(
        self,
        *subfields: Union[
            AsksChannelConnectPayloadGraphQLField,
            "IntegrationFields",
            "SlackChannelNameMappingFields",
        ]
    ) -> "AsksChannelConnectPayloadFields":
        """Subfields should come from the AsksChannelConnectPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AsksChannelConnectPayloadFields":
        self._alias = alias
        return self


class AttachmentFields(GraphQLField):
    id: "AttachmentGraphQLField" = AttachmentGraphQLField("id")
    created_at: "AttachmentGraphQLField" = AttachmentGraphQLField("createdAt")
    updated_at: "AttachmentGraphQLField" = AttachmentGraphQLField("updatedAt")
    archived_at: "AttachmentGraphQLField" = AttachmentGraphQLField("archivedAt")
    title: "AttachmentGraphQLField" = AttachmentGraphQLField("title")
    subtitle: "AttachmentGraphQLField" = AttachmentGraphQLField("subtitle")
    url: "AttachmentGraphQLField" = AttachmentGraphQLField("url")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def external_user_creator(cls) -> "ExternalUserFields":
        return ExternalUserFields("external_user_creator")

    metadata: "AttachmentGraphQLField" = AttachmentGraphQLField("metadata")
    source: "AttachmentGraphQLField" = AttachmentGraphQLField("source")
    source_type: "AttachmentGraphQLField" = AttachmentGraphQLField("sourceType")
    group_by_source: "AttachmentGraphQLField" = AttachmentGraphQLField("groupBySource")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    def fields(
        self,
        *subfields: Union[
            AttachmentGraphQLField, "ExternalUserFields", "IssueFields", "UserFields"
        ]
    ) -> "AttachmentFields":
        """Subfields should come from the AttachmentFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AttachmentFields":
        self._alias = alias
        return self


class AttachmentArchivePayloadFields(GraphQLField):
    last_sync_id: "AttachmentArchivePayloadGraphQLField" = (
        AttachmentArchivePayloadGraphQLField("lastSyncId")
    )
    success: "AttachmentArchivePayloadGraphQLField" = (
        AttachmentArchivePayloadGraphQLField("success")
    )

    @classmethod
    def entity(cls) -> "AttachmentFields":
        return AttachmentFields("entity")

    def fields(
        self,
        *subfields: Union[AttachmentArchivePayloadGraphQLField, "AttachmentFields"]
    ) -> "AttachmentArchivePayloadFields":
        """Subfields should come from the AttachmentArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AttachmentArchivePayloadFields":
        self._alias = alias
        return self


class AttachmentConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "AttachmentEdgeFields":
        return AttachmentEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "AttachmentFields":
        return AttachmentFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            AttachmentConnectionGraphQLField,
            "AttachmentEdgeFields",
            "AttachmentFields",
            "PageInfoFields",
        ]
    ) -> "AttachmentConnectionFields":
        """Subfields should come from the AttachmentConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AttachmentConnectionFields":
        self._alias = alias
        return self


class AttachmentEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "AttachmentFields":
        return AttachmentFields("node")

    cursor: "AttachmentEdgeGraphQLField" = AttachmentEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[AttachmentEdgeGraphQLField, "AttachmentFields"]
    ) -> "AttachmentEdgeFields":
        """Subfields should come from the AttachmentEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AttachmentEdgeFields":
        self._alias = alias
        return self


class AttachmentPayloadFields(GraphQLField):
    last_sync_id: "AttachmentPayloadGraphQLField" = AttachmentPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def attachment(cls) -> "AttachmentFields":
        return AttachmentFields("attachment")

    success: "AttachmentPayloadGraphQLField" = AttachmentPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[AttachmentPayloadGraphQLField, "AttachmentFields"]
    ) -> "AttachmentPayloadFields":
        """Subfields should come from the AttachmentPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AttachmentPayloadFields":
        self._alias = alias
        return self


class AttachmentSourcesPayloadFields(GraphQLField):
    sources: "AttachmentSourcesPayloadGraphQLField" = (
        AttachmentSourcesPayloadGraphQLField("sources")
    )

    def fields(
        self, *subfields: AttachmentSourcesPayloadGraphQLField
    ) -> "AttachmentSourcesPayloadFields":
        """Subfields should come from the AttachmentSourcesPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AttachmentSourcesPayloadFields":
        self._alias = alias
        return self


class AuditEntryFields(GraphQLField):
    id: "AuditEntryGraphQLField" = AuditEntryGraphQLField("id")
    created_at: "AuditEntryGraphQLField" = AuditEntryGraphQLField("createdAt")
    updated_at: "AuditEntryGraphQLField" = AuditEntryGraphQLField("updatedAt")
    archived_at: "AuditEntryGraphQLField" = AuditEntryGraphQLField("archivedAt")
    type: "AuditEntryGraphQLField" = AuditEntryGraphQLField("type")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def actor(cls) -> "UserFields":
        return UserFields("actor")

    actor_id: "AuditEntryGraphQLField" = AuditEntryGraphQLField("actorId")
    ip: "AuditEntryGraphQLField" = AuditEntryGraphQLField("ip")
    country_code: "AuditEntryGraphQLField" = AuditEntryGraphQLField("countryCode")
    metadata: "AuditEntryGraphQLField" = AuditEntryGraphQLField("metadata")
    request_information: "AuditEntryGraphQLField" = AuditEntryGraphQLField(
        "requestInformation"
    )

    def fields(
        self,
        *subfields: Union[AuditEntryGraphQLField, "OrganizationFields", "UserFields"]
    ) -> "AuditEntryFields":
        """Subfields should come from the AuditEntryFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuditEntryFields":
        self._alias = alias
        return self


class AuditEntryConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "AuditEntryEdgeFields":
        return AuditEntryEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "AuditEntryFields":
        return AuditEntryFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            AuditEntryConnectionGraphQLField,
            "AuditEntryEdgeFields",
            "AuditEntryFields",
            "PageInfoFields",
        ]
    ) -> "AuditEntryConnectionFields":
        """Subfields should come from the AuditEntryConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuditEntryConnectionFields":
        self._alias = alias
        return self


class AuditEntryEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "AuditEntryFields":
        return AuditEntryFields("node")

    cursor: "AuditEntryEdgeGraphQLField" = AuditEntryEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[AuditEntryEdgeGraphQLField, "AuditEntryFields"]
    ) -> "AuditEntryEdgeFields":
        """Subfields should come from the AuditEntryEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuditEntryEdgeFields":
        self._alias = alias
        return self


class AuditEntryTypeFields(GraphQLField):
    type: "AuditEntryTypeGraphQLField" = AuditEntryTypeGraphQLField("type")
    description: "AuditEntryTypeGraphQLField" = AuditEntryTypeGraphQLField(
        "description"
    )

    def fields(self, *subfields: AuditEntryTypeGraphQLField) -> "AuditEntryTypeFields":
        """Subfields should come from the AuditEntryTypeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuditEntryTypeFields":
        self._alias = alias
        return self


class AuthMembershipFields(GraphQLField):
    user_id: "AuthMembershipGraphQLField" = AuthMembershipGraphQLField("userId")
    created_at: "AuthMembershipGraphQLField" = AuthMembershipGraphQLField("createdAt")

    def fields(self, *subfields: AuthMembershipGraphQLField) -> "AuthMembershipFields":
        """Subfields should come from the AuthMembershipFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuthMembershipFields":
        self._alias = alias
        return self


class AuthOrganizationFields(GraphQLField):
    id: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField("id")
    name: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField("name")
    enabled: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField("enabled")
    url_key: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField("urlKey")
    previous_url_keys: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField(
        "previousUrlKeys"
    )
    logo_url: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField("logoUrl")
    deletion_requested_at: "AuthOrganizationGraphQLField" = (
        AuthOrganizationGraphQLField("deletionRequestedAt")
    )
    release_channel: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField(
        "releaseChannel"
    )
    saml_enabled: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField(
        "samlEnabled"
    )
    saml_settings: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField(
        "samlSettings"
    )
    allowed_auth_services: "AuthOrganizationGraphQLField" = (
        AuthOrganizationGraphQLField("allowedAuthServices")
    )
    scim_enabled: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField(
        "scimEnabled"
    )
    service_id: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField(
        "serviceId"
    )
    region: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField("region")
    user_count: "AuthOrganizationGraphQLField" = AuthOrganizationGraphQLField(
        "userCount"
    )

    def fields(
        self, *subfields: AuthOrganizationGraphQLField
    ) -> "AuthOrganizationFields":
        """Subfields should come from the AuthOrganizationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuthOrganizationFields":
        self._alias = alias
        return self


class AuthResolverResponseFields(GraphQLField):
    id: "AuthResolverResponseGraphQLField" = AuthResolverResponseGraphQLField("id")
    email: "AuthResolverResponseGraphQLField" = AuthResolverResponseGraphQLField(
        "email"
    )
    allow_domain_access: "AuthResolverResponseGraphQLField" = (
        AuthResolverResponseGraphQLField("allowDomainAccess")
    )

    @classmethod
    def users(cls) -> "AuthUserFields":
        return AuthUserFields("users")

    @classmethod
    def locked_users(cls) -> "AuthUserFields":
        return AuthUserFields("locked_users")

    @classmethod
    def available_organizations(cls) -> "AuthOrganizationFields":
        return AuthOrganizationFields("available_organizations")

    @classmethod
    def locked_organizations(cls) -> "AuthOrganizationFields":
        return AuthOrganizationFields("locked_organizations")

    last_used_organization_id: "AuthResolverResponseGraphQLField" = (
        AuthResolverResponseGraphQLField("lastUsedOrganizationId")
    )
    token: "AuthResolverResponseGraphQLField" = AuthResolverResponseGraphQLField(
        "token"
    )

    def fields(
        self,
        *subfields: Union[
            AuthResolverResponseGraphQLField, "AuthOrganizationFields", "AuthUserFields"
        ]
    ) -> "AuthResolverResponseFields":
        """Subfields should come from the AuthResolverResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuthResolverResponseFields":
        self._alias = alias
        return self


class AuthUserFields(GraphQLField):
    id: "AuthUserGraphQLField" = AuthUserGraphQLField("id")
    name: "AuthUserGraphQLField" = AuthUserGraphQLField("name")
    display_name: "AuthUserGraphQLField" = AuthUserGraphQLField("displayName")
    email: "AuthUserGraphQLField" = AuthUserGraphQLField("email")
    avatar_url: "AuthUserGraphQLField" = AuthUserGraphQLField("avatarUrl")
    role: "AuthUserGraphQLField" = AuthUserGraphQLField("role")
    active: "AuthUserGraphQLField" = AuthUserGraphQLField("active")
    user_account_id: "AuthUserGraphQLField" = AuthUserGraphQLField("userAccountId")

    @classmethod
    def organization(cls) -> "AuthOrganizationFields":
        return AuthOrganizationFields("organization")

    def fields(
        self, *subfields: Union[AuthUserGraphQLField, "AuthOrganizationFields"]
    ) -> "AuthUserFields":
        """Subfields should come from the AuthUserFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuthUserFields":
        self._alias = alias
        return self


class AuthenticationSessionResponseFields(GraphQLField):
    id: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("id")
    )
    type: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("type")
    )
    ip: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("ip")
    )
    location_country: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("locationCountry")
    )
    location_country_code: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("locationCountryCode")
    )
    country_codes: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("countryCodes")
    )
    location_region_code: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("locationRegionCode")
    )
    location_city: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("locationCity")
    )
    user_agent: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("userAgent")
    )
    browser_type: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("browserType")
    )
    last_active_at: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("lastActiveAt")
    )
    created_at: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("createdAt")
    )
    updated_at: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("updatedAt")
    )
    location: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("location")
    )
    operating_system: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("operatingSystem")
    )
    client: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("client")
    )
    name: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("name")
    )
    is_current_session: "AuthenticationSessionResponseGraphQLField" = (
        AuthenticationSessionResponseGraphQLField("isCurrentSession")
    )

    def fields(
        self, *subfields: AuthenticationSessionResponseGraphQLField
    ) -> "AuthenticationSessionResponseFields":
        """Subfields should come from the AuthenticationSessionResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuthenticationSessionResponseFields":
        self._alias = alias
        return self


class AuthorizedApplicationFields(GraphQLField):
    name: "AuthorizedApplicationGraphQLField" = AuthorizedApplicationGraphQLField(
        "name"
    )
    image_url: "AuthorizedApplicationGraphQLField" = AuthorizedApplicationGraphQLField(
        "imageUrl"
    )
    scope: "AuthorizedApplicationGraphQLField" = AuthorizedApplicationGraphQLField(
        "scope"
    )
    app_id: "AuthorizedApplicationGraphQLField" = AuthorizedApplicationGraphQLField(
        "appId"
    )
    client_id: "AuthorizedApplicationGraphQLField" = AuthorizedApplicationGraphQLField(
        "clientId"
    )
    webhooks_enabled: "AuthorizedApplicationGraphQLField" = (
        AuthorizedApplicationGraphQLField("webhooksEnabled")
    )

    def fields(
        self, *subfields: AuthorizedApplicationGraphQLField
    ) -> "AuthorizedApplicationFields":
        """Subfields should come from the AuthorizedApplicationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "AuthorizedApplicationFields":
        self._alias = alias
        return self


class CommentFields(GraphQLField):
    id: "CommentGraphQLField" = CommentGraphQLField("id")
    created_at: "CommentGraphQLField" = CommentGraphQLField("createdAt")
    updated_at: "CommentGraphQLField" = CommentGraphQLField("updatedAt")
    archived_at: "CommentGraphQLField" = CommentGraphQLField("archivedAt")
    body: "CommentGraphQLField" = CommentGraphQLField("body")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    @classmethod
    def document_content(cls) -> "DocumentContentFields":
        return DocumentContentFields("document_content")

    @classmethod
    def project_update(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("project_update")

    @classmethod
    def parent(cls) -> "CommentFields":
        return CommentFields("parent")

    @classmethod
    def resolving_user(cls) -> "UserFields":
        return UserFields("resolving_user")

    resolved_at: "CommentGraphQLField" = CommentGraphQLField("resolvedAt")

    @classmethod
    def resolving_comment(cls) -> "CommentFields":
        return CommentFields("resolving_comment")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    @classmethod
    def external_user(cls) -> "ExternalUserFields":
        return ExternalUserFields("external_user")

    edited_at: "CommentGraphQLField" = CommentGraphQLField("editedAt")
    body_data: "CommentGraphQLField" = CommentGraphQLField("bodyData")
    quoted_text: "CommentGraphQLField" = CommentGraphQLField("quotedText")
    summary_text: "CommentGraphQLField" = CommentGraphQLField("summaryText")
    reaction_data: "CommentGraphQLField" = CommentGraphQLField("reactionData")
    url: "CommentGraphQLField" = CommentGraphQLField("url")

    @classmethod
    def children(
        cls,
        *,
        filter: Optional[CommentFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "CommentConnectionFields":
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
        return CommentConnectionFields("children", arguments=cleared_arguments)

    @classmethod
    def bot_actor(cls) -> "ActorBotFields":
        return ActorBotFields("bot_actor")

    @classmethod
    def reactions(cls) -> "ReactionFields":
        return ReactionFields("reactions")

    def fields(
        self,
        *subfields: Union[
            CommentGraphQLField,
            "ActorBotFields",
            "CommentConnectionFields",
            "CommentFields",
            "DocumentContentFields",
            "ExternalUserFields",
            "IssueFields",
            "ProjectUpdateFields",
            "ReactionFields",
            "UserFields",
        ]
    ) -> "CommentFields":
        """Subfields should come from the CommentFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CommentFields":
        self._alias = alias
        return self


class CommentConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "CommentEdgeFields":
        return CommentEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "CommentFields":
        return CommentFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            CommentConnectionGraphQLField,
            "CommentEdgeFields",
            "CommentFields",
            "PageInfoFields",
        ]
    ) -> "CommentConnectionFields":
        """Subfields should come from the CommentConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CommentConnectionFields":
        self._alias = alias
        return self


class CommentEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "CommentFields":
        return CommentFields("node")

    cursor: "CommentEdgeGraphQLField" = CommentEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[CommentEdgeGraphQLField, "CommentFields"]
    ) -> "CommentEdgeFields":
        """Subfields should come from the CommentEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CommentEdgeFields":
        self._alias = alias
        return self


class CommentPayloadFields(GraphQLField):
    last_sync_id: "CommentPayloadGraphQLField" = CommentPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def comment(cls) -> "CommentFields":
        return CommentFields("comment")

    success: "CommentPayloadGraphQLField" = CommentPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[CommentPayloadGraphQLField, "CommentFields"]
    ) -> "CommentPayloadFields":
        """Subfields should come from the CommentPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CommentPayloadFields":
        self._alias = alias
        return self


class ContactPayloadFields(GraphQLField):
    success: "ContactPayloadGraphQLField" = ContactPayloadGraphQLField("success")

    def fields(self, *subfields: ContactPayloadGraphQLField) -> "ContactPayloadFields":
        """Subfields should come from the ContactPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ContactPayloadFields":
        self._alias = alias
        return self


class CreateCsvExportReportPayloadFields(GraphQLField):
    success: "CreateCsvExportReportPayloadGraphQLField" = (
        CreateCsvExportReportPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: CreateCsvExportReportPayloadGraphQLField
    ) -> "CreateCsvExportReportPayloadFields":
        """Subfields should come from the CreateCsvExportReportPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CreateCsvExportReportPayloadFields":
        self._alias = alias
        return self


class CreateOrJoinOrganizationResponseFields(GraphQLField):
    @classmethod
    def organization(cls) -> "AuthOrganizationFields":
        return AuthOrganizationFields("organization")

    @classmethod
    def user(cls) -> "AuthUserFields":
        return AuthUserFields("user")

    def fields(
        self,
        *subfields: Union[
            CreateOrJoinOrganizationResponseGraphQLField,
            "AuthOrganizationFields",
            "AuthUserFields",
        ]
    ) -> "CreateOrJoinOrganizationResponseFields":
        """Subfields should come from the CreateOrJoinOrganizationResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CreateOrJoinOrganizationResponseFields":
        self._alias = alias
        return self


class CustomViewFields(GraphQLField):
    id: "CustomViewGraphQLField" = CustomViewGraphQLField("id")
    created_at: "CustomViewGraphQLField" = CustomViewGraphQLField("createdAt")
    updated_at: "CustomViewGraphQLField" = CustomViewGraphQLField("updatedAt")
    archived_at: "CustomViewGraphQLField" = CustomViewGraphQLField("archivedAt")
    name: "CustomViewGraphQLField" = CustomViewGraphQLField("name")
    description: "CustomViewGraphQLField" = CustomViewGraphQLField("description")
    icon: "CustomViewGraphQLField" = CustomViewGraphQLField("icon")
    color: "CustomViewGraphQLField" = CustomViewGraphQLField("color")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def owner(cls) -> "UserFields":
        return UserFields("owner")

    @classmethod
    def updated_by(cls) -> "UserFields":
        return UserFields("updated_by")

    filters: "CustomViewGraphQLField" = CustomViewGraphQLField("filters")
    filter_data: "CustomViewGraphQLField" = CustomViewGraphQLField("filterData")
    project_filter_data: "CustomViewGraphQLField" = CustomViewGraphQLField(
        "projectFilterData"
    )
    shared: "CustomViewGraphQLField" = CustomViewGraphQLField("shared")
    model_name: "CustomViewGraphQLField" = CustomViewGraphQLField("modelName")

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
    ) -> "ProjectConnectionFields":
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
        return ProjectConnectionFields("projects", arguments=cleared_arguments)

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
    ) -> "IssueConnectionFields":
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    @classmethod
    def user_view_preferences(cls) -> "ViewPreferencesFields":
        return ViewPreferencesFields("user_view_preferences")

    @classmethod
    def organization_view_preferences(cls) -> "ViewPreferencesFields":
        return ViewPreferencesFields("organization_view_preferences")

    @classmethod
    def view_preferences_values(cls) -> "ViewPreferencesValuesFields":
        return ViewPreferencesValuesFields("view_preferences_values")

    def fields(
        self,
        *subfields: Union[
            CustomViewGraphQLField,
            "IssueConnectionFields",
            "OrganizationFields",
            "ProjectConnectionFields",
            "TeamFields",
            "UserFields",
            "ViewPreferencesFields",
            "ViewPreferencesValuesFields",
        ]
    ) -> "CustomViewFields":
        """Subfields should come from the CustomViewFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomViewFields":
        self._alias = alias
        return self


class CustomViewConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "CustomViewEdgeFields":
        return CustomViewEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "CustomViewFields":
        return CustomViewFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            CustomViewConnectionGraphQLField,
            "CustomViewEdgeFields",
            "CustomViewFields",
            "PageInfoFields",
        ]
    ) -> "CustomViewConnectionFields":
        """Subfields should come from the CustomViewConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomViewConnectionFields":
        self._alias = alias
        return self


class CustomViewEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "CustomViewFields":
        return CustomViewFields("node")

    cursor: "CustomViewEdgeGraphQLField" = CustomViewEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[CustomViewEdgeGraphQLField, "CustomViewFields"]
    ) -> "CustomViewEdgeFields":
        """Subfields should come from the CustomViewEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomViewEdgeFields":
        self._alias = alias
        return self


class CustomViewHasSubscribersPayloadFields(GraphQLField):
    has_subscribers: "CustomViewHasSubscribersPayloadGraphQLField" = (
        CustomViewHasSubscribersPayloadGraphQLField("hasSubscribers")
    )

    def fields(
        self, *subfields: CustomViewHasSubscribersPayloadGraphQLField
    ) -> "CustomViewHasSubscribersPayloadFields":
        """Subfields should come from the CustomViewHasSubscribersPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomViewHasSubscribersPayloadFields":
        self._alias = alias
        return self


class CustomViewPayloadFields(GraphQLField):
    last_sync_id: "CustomViewPayloadGraphQLField" = CustomViewPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def custom_view(cls) -> "CustomViewFields":
        return CustomViewFields("custom_view")

    success: "CustomViewPayloadGraphQLField" = CustomViewPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[CustomViewPayloadGraphQLField, "CustomViewFields"]
    ) -> "CustomViewPayloadFields":
        """Subfields should come from the CustomViewPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomViewPayloadFields":
        self._alias = alias
        return self


class CustomViewSuggestionPayloadFields(GraphQLField):
    name: "CustomViewSuggestionPayloadGraphQLField" = (
        CustomViewSuggestionPayloadGraphQLField("name")
    )
    description: "CustomViewSuggestionPayloadGraphQLField" = (
        CustomViewSuggestionPayloadGraphQLField("description")
    )
    icon: "CustomViewSuggestionPayloadGraphQLField" = (
        CustomViewSuggestionPayloadGraphQLField("icon")
    )

    def fields(
        self, *subfields: CustomViewSuggestionPayloadGraphQLField
    ) -> "CustomViewSuggestionPayloadFields":
        """Subfields should come from the CustomViewSuggestionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomViewSuggestionPayloadFields":
        self._alias = alias
        return self


class CustomerFields(GraphQLField):
    id: "CustomerGraphQLField" = CustomerGraphQLField("id")
    created_at: "CustomerGraphQLField" = CustomerGraphQLField("createdAt")
    updated_at: "CustomerGraphQLField" = CustomerGraphQLField("updatedAt")
    archived_at: "CustomerGraphQLField" = CustomerGraphQLField("archivedAt")
    name: "CustomerGraphQLField" = CustomerGraphQLField("name")
    logo_url: "CustomerGraphQLField" = CustomerGraphQLField("logoUrl")
    domains: "CustomerGraphQLField" = CustomerGraphQLField("domains")
    external_ids: "CustomerGraphQLField" = CustomerGraphQLField("externalIds")
    slack_channel_id: "CustomerGraphQLField" = CustomerGraphQLField("slackChannelId")

    @classmethod
    def owner(cls) -> "UserFields":
        return UserFields("owner")

    @classmethod
    def status(cls) -> "CustomerStatusFields":
        return CustomerStatusFields("status")

    def fields(
        self,
        *subfields: Union[CustomerGraphQLField, "CustomerStatusFields", "UserFields"]
    ) -> "CustomerFields":
        """Subfields should come from the CustomerFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerFields":
        self._alias = alias
        return self


class CustomerConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "CustomerEdgeFields":
        return CustomerEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "CustomerFields":
        return CustomerFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            CustomerConnectionGraphQLField,
            "CustomerEdgeFields",
            "CustomerFields",
            "PageInfoFields",
        ]
    ) -> "CustomerConnectionFields":
        """Subfields should come from the CustomerConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerConnectionFields":
        self._alias = alias
        return self


class CustomerEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "CustomerFields":
        return CustomerFields("node")

    cursor: "CustomerEdgeGraphQLField" = CustomerEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[CustomerEdgeGraphQLField, "CustomerFields"]
    ) -> "CustomerEdgeFields":
        """Subfields should come from the CustomerEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerEdgeFields":
        self._alias = alias
        return self


class CustomerNeedFields(GraphQLField):
    id: "CustomerNeedGraphQLField" = CustomerNeedGraphQLField("id")
    created_at: "CustomerNeedGraphQLField" = CustomerNeedGraphQLField("createdAt")
    updated_at: "CustomerNeedGraphQLField" = CustomerNeedGraphQLField("updatedAt")
    archived_at: "CustomerNeedGraphQLField" = CustomerNeedGraphQLField("archivedAt")

    @classmethod
    def customer(cls) -> "CustomerFields":
        return CustomerFields("customer")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def comment(cls) -> "CommentFields":
        return CommentFields("comment")

    priority: "CustomerNeedGraphQLField" = CustomerNeedGraphQLField("priority")

    def fields(
        self,
        *subfields: Union[
            CustomerNeedGraphQLField,
            "CommentFields",
            "CustomerFields",
            "IssueFields",
            "ProjectFields",
        ]
    ) -> "CustomerNeedFields":
        """Subfields should come from the CustomerNeedFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerNeedFields":
        self._alias = alias
        return self


class CustomerNeedConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "CustomerNeedEdgeFields":
        return CustomerNeedEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "CustomerNeedFields":
        return CustomerNeedFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            CustomerNeedConnectionGraphQLField,
            "CustomerNeedEdgeFields",
            "CustomerNeedFields",
            "PageInfoFields",
        ]
    ) -> "CustomerNeedConnectionFields":
        """Subfields should come from the CustomerNeedConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerNeedConnectionFields":
        self._alias = alias
        return self


class CustomerNeedEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "CustomerNeedFields":
        return CustomerNeedFields("node")

    cursor: "CustomerNeedEdgeGraphQLField" = CustomerNeedEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[CustomerNeedEdgeGraphQLField, "CustomerNeedFields"]
    ) -> "CustomerNeedEdgeFields":
        """Subfields should come from the CustomerNeedEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerNeedEdgeFields":
        self._alias = alias
        return self


class CustomerNeedPayloadFields(GraphQLField):
    last_sync_id: "CustomerNeedPayloadGraphQLField" = CustomerNeedPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def need(cls) -> "CustomerNeedFields":
        return CustomerNeedFields("need")

    success: "CustomerNeedPayloadGraphQLField" = CustomerNeedPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[CustomerNeedPayloadGraphQLField, "CustomerNeedFields"]
    ) -> "CustomerNeedPayloadFields":
        """Subfields should come from the CustomerNeedPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerNeedPayloadFields":
        self._alias = alias
        return self


class CustomerPayloadFields(GraphQLField):
    last_sync_id: "CustomerPayloadGraphQLField" = CustomerPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def customer(cls) -> "CustomerFields":
        return CustomerFields("customer")

    success: "CustomerPayloadGraphQLField" = CustomerPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[CustomerPayloadGraphQLField, "CustomerFields"]
    ) -> "CustomerPayloadFields":
        """Subfields should come from the CustomerPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerPayloadFields":
        self._alias = alias
        return self


class CustomerStatusFields(GraphQLField):
    id: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("id")
    created_at: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("createdAt")
    updated_at: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("updatedAt")
    archived_at: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("archivedAt")
    name: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("name")
    color: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("color")
    type: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("type")
    description: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField(
        "description"
    )
    position: "CustomerStatusGraphQLField" = CustomerStatusGraphQLField("position")

    def fields(self, *subfields: CustomerStatusGraphQLField) -> "CustomerStatusFields":
        """Subfields should come from the CustomerStatusFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerStatusFields":
        self._alias = alias
        return self


class CustomerStatusConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "CustomerStatusEdgeFields":
        return CustomerStatusEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "CustomerStatusFields":
        return CustomerStatusFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            CustomerStatusConnectionGraphQLField,
            "CustomerStatusEdgeFields",
            "CustomerStatusFields",
            "PageInfoFields",
        ]
    ) -> "CustomerStatusConnectionFields":
        """Subfields should come from the CustomerStatusConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerStatusConnectionFields":
        self._alias = alias
        return self


class CustomerStatusEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "CustomerStatusFields":
        return CustomerStatusFields("node")

    cursor: "CustomerStatusEdgeGraphQLField" = CustomerStatusEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[CustomerStatusEdgeGraphQLField, "CustomerStatusFields"]
    ) -> "CustomerStatusEdgeFields":
        """Subfields should come from the CustomerStatusEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerStatusEdgeFields":
        self._alias = alias
        return self


class CustomerStatusPayloadFields(GraphQLField):
    last_sync_id: "CustomerStatusPayloadGraphQLField" = (
        CustomerStatusPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def status(cls) -> "CustomerStatusFields":
        return CustomerStatusFields("status")

    success: "CustomerStatusPayloadGraphQLField" = CustomerStatusPayloadGraphQLField(
        "success"
    )

    def fields(
        self,
        *subfields: Union[CustomerStatusPayloadGraphQLField, "CustomerStatusFields"]
    ) -> "CustomerStatusPayloadFields":
        """Subfields should come from the CustomerStatusPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CustomerStatusPayloadFields":
        self._alias = alias
        return self


class CycleFields(GraphQLField):
    id: "CycleGraphQLField" = CycleGraphQLField("id")
    created_at: "CycleGraphQLField" = CycleGraphQLField("createdAt")
    updated_at: "CycleGraphQLField" = CycleGraphQLField("updatedAt")
    archived_at: "CycleGraphQLField" = CycleGraphQLField("archivedAt")
    number: "CycleGraphQLField" = CycleGraphQLField("number")
    name: "CycleGraphQLField" = CycleGraphQLField("name")
    description: "CycleGraphQLField" = CycleGraphQLField("description")
    starts_at: "CycleGraphQLField" = CycleGraphQLField("startsAt")
    ends_at: "CycleGraphQLField" = CycleGraphQLField("endsAt")
    completed_at: "CycleGraphQLField" = CycleGraphQLField("completedAt")
    auto_archived_at: "CycleGraphQLField" = CycleGraphQLField("autoArchivedAt")
    issue_count_history: "CycleGraphQLField" = CycleGraphQLField("issueCountHistory")
    completed_issue_count_history: "CycleGraphQLField" = CycleGraphQLField(
        "completedIssueCountHistory"
    )
    scope_history: "CycleGraphQLField" = CycleGraphQLField("scopeHistory")
    completed_scope_history: "CycleGraphQLField" = CycleGraphQLField(
        "completedScopeHistory"
    )
    in_progress_scope_history: "CycleGraphQLField" = CycleGraphQLField(
        "inProgressScopeHistory"
    )

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    progress_history: "CycleGraphQLField" = CycleGraphQLField("progressHistory")

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
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    @classmethod
    def uncompleted_issues_upon_close(
        cls,
        *,
        filter: Optional[IssueFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
            "uncompleted_issues_upon_close", arguments=cleared_arguments
        )

    progress: "CycleGraphQLField" = CycleGraphQLField("progress")

    def fields(
        self,
        *subfields: Union[CycleGraphQLField, "IssueConnectionFields", "TeamFields"]
    ) -> "CycleFields":
        """Subfields should come from the CycleFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CycleFields":
        self._alias = alias
        return self


class CycleArchivePayloadFields(GraphQLField):
    last_sync_id: "CycleArchivePayloadGraphQLField" = CycleArchivePayloadGraphQLField(
        "lastSyncId"
    )
    success: "CycleArchivePayloadGraphQLField" = CycleArchivePayloadGraphQLField(
        "success"
    )

    @classmethod
    def entity(cls) -> "CycleFields":
        return CycleFields("entity")

    def fields(
        self, *subfields: Union[CycleArchivePayloadGraphQLField, "CycleFields"]
    ) -> "CycleArchivePayloadFields":
        """Subfields should come from the CycleArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CycleArchivePayloadFields":
        self._alias = alias
        return self


class CycleConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "CycleEdgeFields":
        return CycleEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "CycleFields":
        return CycleFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            CycleConnectionGraphQLField,
            "CycleEdgeFields",
            "CycleFields",
            "PageInfoFields",
        ]
    ) -> "CycleConnectionFields":
        """Subfields should come from the CycleConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CycleConnectionFields":
        self._alias = alias
        return self


class CycleEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "CycleFields":
        return CycleFields("node")

    cursor: "CycleEdgeGraphQLField" = CycleEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[CycleEdgeGraphQLField, "CycleFields"]
    ) -> "CycleEdgeFields":
        """Subfields should come from the CycleEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CycleEdgeFields":
        self._alias = alias
        return self


class CyclePayloadFields(GraphQLField):
    last_sync_id: "CyclePayloadGraphQLField" = CyclePayloadGraphQLField("lastSyncId")

    @classmethod
    def cycle(cls) -> "CycleFields":
        return CycleFields("cycle")

    success: "CyclePayloadGraphQLField" = CyclePayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[CyclePayloadGraphQLField, "CycleFields"]
    ) -> "CyclePayloadFields":
        """Subfields should come from the CyclePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "CyclePayloadFields":
        self._alias = alias
        return self


class DeletePayloadFields(GraphQLField):
    last_sync_id: "DeletePayloadGraphQLField" = DeletePayloadGraphQLField("lastSyncId")
    success: "DeletePayloadGraphQLField" = DeletePayloadGraphQLField("success")
    entity_id: "DeletePayloadGraphQLField" = DeletePayloadGraphQLField("entityId")

    def fields(self, *subfields: DeletePayloadGraphQLField) -> "DeletePayloadFields":
        """Subfields should come from the DeletePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DeletePayloadFields":
        self._alias = alias
        return self


class DiaryEntryFields(GraphQLField):
    id: "DiaryEntryGraphQLField" = DiaryEntryGraphQLField("id")
    created_at: "DiaryEntryGraphQLField" = DiaryEntryGraphQLField("createdAt")
    updated_at: "DiaryEntryGraphQLField" = DiaryEntryGraphQLField("updatedAt")
    archived_at: "DiaryEntryGraphQLField" = DiaryEntryGraphQLField("archivedAt")
    body_data: "DiaryEntryGraphQLField" = DiaryEntryGraphQLField("bodyData")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    date: "DiaryEntryGraphQLField" = DiaryEntryGraphQLField("date")
    url: "DiaryEntryGraphQLField" = DiaryEntryGraphQLField("url")

    def fields(
        self, *subfields: Union[DiaryEntryGraphQLField, "UserFields"]
    ) -> "DiaryEntryFields":
        """Subfields should come from the DiaryEntryFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DiaryEntryFields":
        self._alias = alias
        return self


class DiaryEntryPayloadFields(GraphQLField):
    last_sync_id: "DiaryEntryPayloadGraphQLField" = DiaryEntryPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def diary_entry(cls) -> "DiaryEntryFields":
        return DiaryEntryFields("diary_entry")

    success: "DiaryEntryPayloadGraphQLField" = DiaryEntryPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[DiaryEntryPayloadGraphQLField, "DiaryEntryFields"]
    ) -> "DiaryEntryPayloadFields":
        """Subfields should come from the DiaryEntryPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DiaryEntryPayloadFields":
        self._alias = alias
        return self


class DocumentFields(GraphQLField):
    id: "DocumentGraphQLField" = DocumentGraphQLField("id")
    created_at: "DocumentGraphQLField" = DocumentGraphQLField("createdAt")
    updated_at: "DocumentGraphQLField" = DocumentGraphQLField("updatedAt")
    archived_at: "DocumentGraphQLField" = DocumentGraphQLField("archivedAt")
    title: "DocumentGraphQLField" = DocumentGraphQLField("title")
    icon: "DocumentGraphQLField" = DocumentGraphQLField("icon")
    color: "DocumentGraphQLField" = DocumentGraphQLField("color")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def updated_by(cls) -> "UserFields":
        return UserFields("updated_by")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    slug_id: "DocumentGraphQLField" = DocumentGraphQLField("slugId")

    @classmethod
    def last_applied_template(cls) -> "TemplateFields":
        return TemplateFields("last_applied_template")

    hidden_at: "DocumentGraphQLField" = DocumentGraphQLField("hiddenAt")
    trashed: "DocumentGraphQLField" = DocumentGraphQLField("trashed")
    sort_order: "DocumentGraphQLField" = DocumentGraphQLField("sortOrder")
    content: "DocumentGraphQLField" = DocumentGraphQLField("content")
    content_state: "DocumentGraphQLField" = DocumentGraphQLField("contentState")
    url: "DocumentGraphQLField" = DocumentGraphQLField("url")
    content_data: "DocumentGraphQLField" = DocumentGraphQLField("contentData")

    def fields(
        self,
        *subfields: Union[
            DocumentGraphQLField,
            "InitiativeFields",
            "ProjectFields",
            "TemplateFields",
            "UserFields",
        ]
    ) -> "DocumentFields":
        """Subfields should come from the DocumentFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentFields":
        self._alias = alias
        return self


class DocumentArchivePayloadFields(GraphQLField):
    last_sync_id: "DocumentArchivePayloadGraphQLField" = (
        DocumentArchivePayloadGraphQLField("lastSyncId")
    )
    success: "DocumentArchivePayloadGraphQLField" = DocumentArchivePayloadGraphQLField(
        "success"
    )

    @classmethod
    def entity(cls) -> "DocumentFields":
        return DocumentFields("entity")

    def fields(
        self, *subfields: Union[DocumentArchivePayloadGraphQLField, "DocumentFields"]
    ) -> "DocumentArchivePayloadFields":
        """Subfields should come from the DocumentArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentArchivePayloadFields":
        self._alias = alias
        return self


class DocumentConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "DocumentEdgeFields":
        return DocumentEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "DocumentFields":
        return DocumentFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            DocumentConnectionGraphQLField,
            "DocumentEdgeFields",
            "DocumentFields",
            "PageInfoFields",
        ]
    ) -> "DocumentConnectionFields":
        """Subfields should come from the DocumentConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentConnectionFields":
        self._alias = alias
        return self


class DocumentContentFields(GraphQLField):
    id: "DocumentContentGraphQLField" = DocumentContentGraphQLField("id")
    created_at: "DocumentContentGraphQLField" = DocumentContentGraphQLField("createdAt")
    updated_at: "DocumentContentGraphQLField" = DocumentContentGraphQLField("updatedAt")
    archived_at: "DocumentContentGraphQLField" = DocumentContentGraphQLField(
        "archivedAt"
    )
    content: "DocumentContentGraphQLField" = DocumentContentGraphQLField("content")
    content_data: "DocumentContentGraphQLField" = DocumentContentGraphQLField(
        "contentData"
    )
    content_state: "DocumentContentGraphQLField" = DocumentContentGraphQLField(
        "contentState"
    )

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    @classmethod
    def project_milestone(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("project_milestone")

    @classmethod
    def document(cls) -> "DocumentFields":
        return DocumentFields("document")

    restored_at: "DocumentContentGraphQLField" = DocumentContentGraphQLField(
        "restoredAt"
    )

    def fields(
        self,
        *subfields: Union[
            DocumentContentGraphQLField,
            "DocumentFields",
            "InitiativeFields",
            "IssueFields",
            "ProjectFields",
            "ProjectMilestoneFields",
        ]
    ) -> "DocumentContentFields":
        """Subfields should come from the DocumentContentFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentContentFields":
        self._alias = alias
        return self


class DocumentContentHistoryPayloadFields(GraphQLField):
    @classmethod
    def history(cls) -> "DocumentContentHistoryTypeFields":
        return DocumentContentHistoryTypeFields("history")

    success: "DocumentContentHistoryPayloadGraphQLField" = (
        DocumentContentHistoryPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            DocumentContentHistoryPayloadGraphQLField,
            "DocumentContentHistoryTypeFields",
        ]
    ) -> "DocumentContentHistoryPayloadFields":
        """Subfields should come from the DocumentContentHistoryPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentContentHistoryPayloadFields":
        self._alias = alias
        return self


class DocumentContentHistoryTypeFields(GraphQLField):
    id: "DocumentContentHistoryTypeGraphQLField" = (
        DocumentContentHistoryTypeGraphQLField("id")
    )
    created_at: "DocumentContentHistoryTypeGraphQLField" = (
        DocumentContentHistoryTypeGraphQLField("createdAt")
    )
    content_data_snapshot_at: "DocumentContentHistoryTypeGraphQLField" = (
        DocumentContentHistoryTypeGraphQLField("contentDataSnapshotAt")
    )
    content_data: "DocumentContentHistoryTypeGraphQLField" = (
        DocumentContentHistoryTypeGraphQLField("contentData")
    )
    actor_ids: "DocumentContentHistoryTypeGraphQLField" = (
        DocumentContentHistoryTypeGraphQLField("actorIds")
    )

    def fields(
        self, *subfields: DocumentContentHistoryTypeGraphQLField
    ) -> "DocumentContentHistoryTypeFields":
        """Subfields should come from the DocumentContentHistoryTypeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentContentHistoryTypeFields":
        self._alias = alias
        return self


class DocumentEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "DocumentFields":
        return DocumentFields("node")

    cursor: "DocumentEdgeGraphQLField" = DocumentEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[DocumentEdgeGraphQLField, "DocumentFields"]
    ) -> "DocumentEdgeFields":
        """Subfields should come from the DocumentEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentEdgeFields":
        self._alias = alias
        return self


class DocumentPayloadFields(GraphQLField):
    last_sync_id: "DocumentPayloadGraphQLField" = DocumentPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def document(cls) -> "DocumentFields":
        return DocumentFields("document")

    success: "DocumentPayloadGraphQLField" = DocumentPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[DocumentPayloadGraphQLField, "DocumentFields"]
    ) -> "DocumentPayloadFields":
        """Subfields should come from the DocumentPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentPayloadFields":
        self._alias = alias
        return self


class DocumentSearchPayloadFields(GraphQLField):
    @classmethod
    def edges(cls) -> "DocumentSearchResultEdgeFields":
        return DocumentSearchResultEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "DocumentSearchResultFields":
        return DocumentSearchResultFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    @classmethod
    def archive_payload(cls) -> "ArchiveResponseFields":
        return ArchiveResponseFields("archive_payload")

    total_count: "DocumentSearchPayloadGraphQLField" = (
        DocumentSearchPayloadGraphQLField("totalCount")
    )

    def fields(
        self,
        *subfields: Union[
            DocumentSearchPayloadGraphQLField,
            "ArchiveResponseFields",
            "DocumentSearchResultEdgeFields",
            "DocumentSearchResultFields",
            "PageInfoFields",
        ]
    ) -> "DocumentSearchPayloadFields":
        """Subfields should come from the DocumentSearchPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentSearchPayloadFields":
        self._alias = alias
        return self


class DocumentSearchResultFields(GraphQLField):
    id: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField("id")
    created_at: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "createdAt"
    )
    updated_at: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "updatedAt"
    )
    archived_at: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "archivedAt"
    )
    title: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "title"
    )
    icon: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField("icon")
    color: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "color"
    )

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def updated_by(cls) -> "UserFields":
        return UserFields("updated_by")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    slug_id: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "slugId"
    )

    @classmethod
    def last_applied_template(cls) -> "TemplateFields":
        return TemplateFields("last_applied_template")

    hidden_at: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "hiddenAt"
    )
    trashed: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "trashed"
    )
    sort_order: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "sortOrder"
    )
    content: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "content"
    )
    content_state: "DocumentSearchResultGraphQLField" = (
        DocumentSearchResultGraphQLField("contentState")
    )
    url: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField("url")
    content_data: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "contentData"
    )
    metadata: "DocumentSearchResultGraphQLField" = DocumentSearchResultGraphQLField(
        "metadata"
    )

    def fields(
        self,
        *subfields: Union[
            DocumentSearchResultGraphQLField,
            "InitiativeFields",
            "ProjectFields",
            "TemplateFields",
            "UserFields",
        ]
    ) -> "DocumentSearchResultFields":
        """Subfields should come from the DocumentSearchResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentSearchResultFields":
        self._alias = alias
        return self


class DocumentSearchResultEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "DocumentSearchResultFields":
        return DocumentSearchResultFields("node")

    cursor: "DocumentSearchResultEdgeGraphQLField" = (
        DocumentSearchResultEdgeGraphQLField("cursor")
    )

    def fields(
        self,
        *subfields: Union[
            DocumentSearchResultEdgeGraphQLField, "DocumentSearchResultFields"
        ]
    ) -> "DocumentSearchResultEdgeFields":
        """Subfields should come from the DocumentSearchResultEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "DocumentSearchResultEdgeFields":
        self._alias = alias
        return self


class EmailIntakeAddressFields(GraphQLField):
    id: "EmailIntakeAddressGraphQLField" = EmailIntakeAddressGraphQLField("id")
    created_at: "EmailIntakeAddressGraphQLField" = EmailIntakeAddressGraphQLField(
        "createdAt"
    )
    updated_at: "EmailIntakeAddressGraphQLField" = EmailIntakeAddressGraphQLField(
        "updatedAt"
    )
    archived_at: "EmailIntakeAddressGraphQLField" = EmailIntakeAddressGraphQLField(
        "archivedAt"
    )
    address: "EmailIntakeAddressGraphQLField" = EmailIntakeAddressGraphQLField(
        "address"
    )
    enabled: "EmailIntakeAddressGraphQLField" = EmailIntakeAddressGraphQLField(
        "enabled"
    )

    @classmethod
    def template(cls) -> "TemplateFields":
        return TemplateFields("template")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    def fields(
        self,
        *subfields: Union[
            EmailIntakeAddressGraphQLField,
            "OrganizationFields",
            "TeamFields",
            "TemplateFields",
            "UserFields",
        ]
    ) -> "EmailIntakeAddressFields":
        """Subfields should come from the EmailIntakeAddressFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmailIntakeAddressFields":
        self._alias = alias
        return self


class EmailIntakeAddressPayloadFields(GraphQLField):
    last_sync_id: "EmailIntakeAddressPayloadGraphQLField" = (
        EmailIntakeAddressPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def email_intake_address(cls) -> "EmailIntakeAddressFields":
        return EmailIntakeAddressFields("email_intake_address")

    success: "EmailIntakeAddressPayloadGraphQLField" = (
        EmailIntakeAddressPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            EmailIntakeAddressPayloadGraphQLField, "EmailIntakeAddressFields"
        ]
    ) -> "EmailIntakeAddressPayloadFields":
        """Subfields should come from the EmailIntakeAddressPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmailIntakeAddressPayloadFields":
        self._alias = alias
        return self


class EmailUnsubscribePayloadFields(GraphQLField):
    success: "EmailUnsubscribePayloadGraphQLField" = (
        EmailUnsubscribePayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: EmailUnsubscribePayloadGraphQLField
    ) -> "EmailUnsubscribePayloadFields":
        """Subfields should come from the EmailUnsubscribePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmailUnsubscribePayloadFields":
        self._alias = alias
        return self


class EmailUserAccountAuthChallengeResponseFields(GraphQLField):
    success: "EmailUserAccountAuthChallengeResponseGraphQLField" = (
        EmailUserAccountAuthChallengeResponseGraphQLField("success")
    )
    auth_type: "EmailUserAccountAuthChallengeResponseGraphQLField" = (
        EmailUserAccountAuthChallengeResponseGraphQLField("authType")
    )

    def fields(
        self, *subfields: EmailUserAccountAuthChallengeResponseGraphQLField
    ) -> "EmailUserAccountAuthChallengeResponseFields":
        """Subfields should come from the EmailUserAccountAuthChallengeResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmailUserAccountAuthChallengeResponseFields":
        self._alias = alias
        return self


class EmojiFields(GraphQLField):
    id: "EmojiGraphQLField" = EmojiGraphQLField("id")
    created_at: "EmojiGraphQLField" = EmojiGraphQLField("createdAt")
    updated_at: "EmojiGraphQLField" = EmojiGraphQLField("updatedAt")
    archived_at: "EmojiGraphQLField" = EmojiGraphQLField("archivedAt")
    name: "EmojiGraphQLField" = EmojiGraphQLField("name")
    url: "EmojiGraphQLField" = EmojiGraphQLField("url")
    source: "EmojiGraphQLField" = EmojiGraphQLField("source")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    def fields(
        self, *subfields: Union[EmojiGraphQLField, "OrganizationFields", "UserFields"]
    ) -> "EmojiFields":
        """Subfields should come from the EmojiFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmojiFields":
        self._alias = alias
        return self


class EmojiConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "EmojiEdgeFields":
        return EmojiEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "EmojiFields":
        return EmojiFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            EmojiConnectionGraphQLField,
            "EmojiEdgeFields",
            "EmojiFields",
            "PageInfoFields",
        ]
    ) -> "EmojiConnectionFields":
        """Subfields should come from the EmojiConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmojiConnectionFields":
        self._alias = alias
        return self


class EmojiEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "EmojiFields":
        return EmojiFields("node")

    cursor: "EmojiEdgeGraphQLField" = EmojiEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[EmojiEdgeGraphQLField, "EmojiFields"]
    ) -> "EmojiEdgeFields":
        """Subfields should come from the EmojiEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmojiEdgeFields":
        self._alias = alias
        return self


class EmojiPayloadFields(GraphQLField):
    last_sync_id: "EmojiPayloadGraphQLField" = EmojiPayloadGraphQLField("lastSyncId")

    @classmethod
    def emoji(cls) -> "EmojiFields":
        return EmojiFields("emoji")

    success: "EmojiPayloadGraphQLField" = EmojiPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[EmojiPayloadGraphQLField, "EmojiFields"]
    ) -> "EmojiPayloadFields":
        """Subfields should come from the EmojiPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EmojiPayloadFields":
        self._alias = alias
        return self


class EntityInterface(GraphQLField):
    id: "EntityGraphQLField" = EntityGraphQLField("id")
    created_at: "EntityGraphQLField" = EntityGraphQLField("createdAt")
    updated_at: "EntityGraphQLField" = EntityGraphQLField("updatedAt")
    archived_at: "EntityGraphQLField" = EntityGraphQLField("archivedAt")

    def fields(self, *subfields: EntityGraphQLField) -> "EntityInterface":
        """Subfields should come from the EntityInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EntityInterface":
        self._alias = alias
        return self

    def on(self, type_name: str, *subfields: GraphQLField) -> "EntityInterface":
        self._inline_fragments[type_name] = subfields
        return self


class EntityExternalLinkFields(GraphQLField):
    id: "EntityExternalLinkGraphQLField" = EntityExternalLinkGraphQLField("id")
    created_at: "EntityExternalLinkGraphQLField" = EntityExternalLinkGraphQLField(
        "createdAt"
    )
    updated_at: "EntityExternalLinkGraphQLField" = EntityExternalLinkGraphQLField(
        "updatedAt"
    )
    archived_at: "EntityExternalLinkGraphQLField" = EntityExternalLinkGraphQLField(
        "archivedAt"
    )
    url: "EntityExternalLinkGraphQLField" = EntityExternalLinkGraphQLField("url")
    label: "EntityExternalLinkGraphQLField" = EntityExternalLinkGraphQLField("label")
    sort_order: "EntityExternalLinkGraphQLField" = EntityExternalLinkGraphQLField(
        "sortOrder"
    )

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    def fields(
        self,
        *subfields: Union[
            EntityExternalLinkGraphQLField, "InitiativeFields", "UserFields"
        ]
    ) -> "EntityExternalLinkFields":
        """Subfields should come from the EntityExternalLinkFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EntityExternalLinkFields":
        self._alias = alias
        return self


class EntityExternalLinkConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "EntityExternalLinkEdgeFields":
        return EntityExternalLinkEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "EntityExternalLinkFields":
        return EntityExternalLinkFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            EntityExternalLinkConnectionGraphQLField,
            "EntityExternalLinkEdgeFields",
            "EntityExternalLinkFields",
            "PageInfoFields",
        ]
    ) -> "EntityExternalLinkConnectionFields":
        """Subfields should come from the EntityExternalLinkConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EntityExternalLinkConnectionFields":
        self._alias = alias
        return self


class EntityExternalLinkEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "EntityExternalLinkFields":
        return EntityExternalLinkFields("node")

    cursor: "EntityExternalLinkEdgeGraphQLField" = EntityExternalLinkEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[
            EntityExternalLinkEdgeGraphQLField, "EntityExternalLinkFields"
        ]
    ) -> "EntityExternalLinkEdgeFields":
        """Subfields should come from the EntityExternalLinkEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EntityExternalLinkEdgeFields":
        self._alias = alias
        return self


class EntityExternalLinkPayloadFields(GraphQLField):
    last_sync_id: "EntityExternalLinkPayloadGraphQLField" = (
        EntityExternalLinkPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def entity_external_link(cls) -> "EntityExternalLinkFields":
        return EntityExternalLinkFields("entity_external_link")

    success: "EntityExternalLinkPayloadGraphQLField" = (
        EntityExternalLinkPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            EntityExternalLinkPayloadGraphQLField, "EntityExternalLinkFields"
        ]
    ) -> "EntityExternalLinkPayloadFields":
        """Subfields should come from the EntityExternalLinkPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "EntityExternalLinkPayloadFields":
        self._alias = alias
        return self


class ExternalUserFields(GraphQLField):
    id: "ExternalUserGraphQLField" = ExternalUserGraphQLField("id")
    created_at: "ExternalUserGraphQLField" = ExternalUserGraphQLField("createdAt")
    updated_at: "ExternalUserGraphQLField" = ExternalUserGraphQLField("updatedAt")
    archived_at: "ExternalUserGraphQLField" = ExternalUserGraphQLField("archivedAt")
    name: "ExternalUserGraphQLField" = ExternalUserGraphQLField("name")
    display_name: "ExternalUserGraphQLField" = ExternalUserGraphQLField("displayName")
    email: "ExternalUserGraphQLField" = ExternalUserGraphQLField("email")
    avatar_url: "ExternalUserGraphQLField" = ExternalUserGraphQLField("avatarUrl")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    last_seen: "ExternalUserGraphQLField" = ExternalUserGraphQLField("lastSeen")

    def fields(
        self, *subfields: Union[ExternalUserGraphQLField, "OrganizationFields"]
    ) -> "ExternalUserFields":
        """Subfields should come from the ExternalUserFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ExternalUserFields":
        self._alias = alias
        return self


class ExternalUserConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ExternalUserEdgeFields":
        return ExternalUserEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ExternalUserFields":
        return ExternalUserFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ExternalUserConnectionGraphQLField,
            "ExternalUserEdgeFields",
            "ExternalUserFields",
            "PageInfoFields",
        ]
    ) -> "ExternalUserConnectionFields":
        """Subfields should come from the ExternalUserConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ExternalUserConnectionFields":
        self._alias = alias
        return self


class ExternalUserEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ExternalUserFields":
        return ExternalUserFields("node")

    cursor: "ExternalUserEdgeGraphQLField" = ExternalUserEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[ExternalUserEdgeGraphQLField, "ExternalUserFields"]
    ) -> "ExternalUserEdgeFields":
        """Subfields should come from the ExternalUserEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ExternalUserEdgeFields":
        self._alias = alias
        return self


class FacetFields(GraphQLField):
    id: "FacetGraphQLField" = FacetGraphQLField("id")
    created_at: "FacetGraphQLField" = FacetGraphQLField("createdAt")
    updated_at: "FacetGraphQLField" = FacetGraphQLField("updatedAt")
    archived_at: "FacetGraphQLField" = FacetGraphQLField("archivedAt")
    sort_order: "FacetGraphQLField" = FacetGraphQLField("sortOrder")

    @classmethod
    def source_organization(cls) -> "OrganizationFields":
        return OrganizationFields("source_organization")

    @classmethod
    def source_team(cls) -> "TeamFields":
        return TeamFields("source_team")

    @classmethod
    def source_project(cls) -> "ProjectFields":
        return ProjectFields("source_project")

    @classmethod
    def source_initiative(cls) -> "InitiativeFields":
        return InitiativeFields("source_initiative")

    source_page: "FacetGraphQLField" = FacetGraphQLField("sourcePage")

    @classmethod
    def target_custom_view(cls) -> "CustomViewFields":
        return CustomViewFields("target_custom_view")

    def fields(
        self,
        *subfields: Union[
            FacetGraphQLField,
            "CustomViewFields",
            "InitiativeFields",
            "OrganizationFields",
            "ProjectFields",
            "TeamFields",
        ]
    ) -> "FacetFields":
        """Subfields should come from the FacetFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FacetFields":
        self._alias = alias
        return self


class FavoriteFields(GraphQLField):
    id: "FavoriteGraphQLField" = FavoriteGraphQLField("id")
    created_at: "FavoriteGraphQLField" = FavoriteGraphQLField("createdAt")
    updated_at: "FavoriteGraphQLField" = FavoriteGraphQLField("updatedAt")
    archived_at: "FavoriteGraphQLField" = FavoriteGraphQLField("archivedAt")
    type: "FavoriteGraphQLField" = FavoriteGraphQLField("type")

    @classmethod
    def parent(cls) -> "FavoriteFields":
        return FavoriteFields("parent")

    folder_name: "FavoriteGraphQLField" = FavoriteGraphQLField("folderName")
    project_tab: "FavoriteGraphQLField" = FavoriteGraphQLField("projectTab")
    predefined_view_type: "FavoriteGraphQLField" = FavoriteGraphQLField(
        "predefinedViewType"
    )
    initiative_tab: "FavoriteGraphQLField" = FavoriteGraphQLField("initiativeTab")

    @classmethod
    def owner(cls) -> "UserFields":
        return UserFields("owner")

    sort_order: "FavoriteGraphQLField" = FavoriteGraphQLField("sortOrder")

    @classmethod
    def children(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "FavoriteConnectionFields":
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
        return FavoriteConnectionFields("children", arguments=cleared_arguments)

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def facet(cls) -> "FacetFields":
        return FacetFields("facet")

    @classmethod
    def project_team(cls) -> "TeamFields":
        return TeamFields("project_team")

    @classmethod
    def cycle(cls) -> "CycleFields":
        return CycleFields("cycle")

    @classmethod
    def custom_view(cls) -> "CustomViewFields":
        return CustomViewFields("custom_view")

    @classmethod
    def predefined_view_team(cls) -> "TeamFields":
        return TeamFields("predefined_view_team")

    @classmethod
    def document(cls) -> "DocumentFields":
        return DocumentFields("document")

    @classmethod
    def roadmap(cls) -> "RoadmapFields":
        return RoadmapFields("roadmap")

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    @classmethod
    def label(cls) -> "IssueLabelFields":
        return IssueLabelFields("label")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    url: "FavoriteGraphQLField" = FavoriteGraphQLField("url")

    def fields(
        self,
        *subfields: Union[
            FavoriteGraphQLField,
            "CustomViewFields",
            "CycleFields",
            "DocumentFields",
            "FacetFields",
            "FavoriteConnectionFields",
            "FavoriteFields",
            "InitiativeFields",
            "IssueFields",
            "IssueLabelFields",
            "ProjectFields",
            "RoadmapFields",
            "TeamFields",
            "UserFields",
        ]
    ) -> "FavoriteFields":
        """Subfields should come from the FavoriteFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FavoriteFields":
        self._alias = alias
        return self


class FavoriteConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "FavoriteEdgeFields":
        return FavoriteEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "FavoriteFields":
        return FavoriteFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            FavoriteConnectionGraphQLField,
            "FavoriteEdgeFields",
            "FavoriteFields",
            "PageInfoFields",
        ]
    ) -> "FavoriteConnectionFields":
        """Subfields should come from the FavoriteConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FavoriteConnectionFields":
        self._alias = alias
        return self


class FavoriteEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "FavoriteFields":
        return FavoriteFields("node")

    cursor: "FavoriteEdgeGraphQLField" = FavoriteEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[FavoriteEdgeGraphQLField, "FavoriteFields"]
    ) -> "FavoriteEdgeFields":
        """Subfields should come from the FavoriteEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FavoriteEdgeFields":
        self._alias = alias
        return self


class FavoritePayloadFields(GraphQLField):
    last_sync_id: "FavoritePayloadGraphQLField" = FavoritePayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def favorite(cls) -> "FavoriteFields":
        return FavoriteFields("favorite")

    success: "FavoritePayloadGraphQLField" = FavoritePayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[FavoritePayloadGraphQLField, "FavoriteFields"]
    ) -> "FavoritePayloadFields":
        """Subfields should come from the FavoritePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FavoritePayloadFields":
        self._alias = alias
        return self


class FrontAttachmentPayloadFields(GraphQLField):
    last_sync_id: "FrontAttachmentPayloadGraphQLField" = (
        FrontAttachmentPayloadGraphQLField("lastSyncId")
    )
    success: "FrontAttachmentPayloadGraphQLField" = FrontAttachmentPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: FrontAttachmentPayloadGraphQLField
    ) -> "FrontAttachmentPayloadFields":
        """Subfields should come from the FrontAttachmentPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "FrontAttachmentPayloadFields":
        self._alias = alias
        return self


class GitAutomationStateFields(GraphQLField):
    id: "GitAutomationStateGraphQLField" = GitAutomationStateGraphQLField("id")
    created_at: "GitAutomationStateGraphQLField" = GitAutomationStateGraphQLField(
        "createdAt"
    )
    updated_at: "GitAutomationStateGraphQLField" = GitAutomationStateGraphQLField(
        "updatedAt"
    )
    archived_at: "GitAutomationStateGraphQLField" = GitAutomationStateGraphQLField(
        "archivedAt"
    )

    @classmethod
    def state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("state")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def target_branch(cls) -> "GitAutomationTargetBranchFields":
        return GitAutomationTargetBranchFields("target_branch")

    event: "GitAutomationStateGraphQLField" = GitAutomationStateGraphQLField("event")
    branch_pattern: "GitAutomationStateGraphQLField" = GitAutomationStateGraphQLField(
        "branchPattern"
    )

    def fields(
        self,
        *subfields: Union[
            GitAutomationStateGraphQLField,
            "GitAutomationTargetBranchFields",
            "TeamFields",
            "WorkflowStateFields",
        ]
    ) -> "GitAutomationStateFields":
        """Subfields should come from the GitAutomationStateFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitAutomationStateFields":
        self._alias = alias
        return self


class GitAutomationStateConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "GitAutomationStateEdgeFields":
        return GitAutomationStateEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "GitAutomationStateFields":
        return GitAutomationStateFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            GitAutomationStateConnectionGraphQLField,
            "GitAutomationStateEdgeFields",
            "GitAutomationStateFields",
            "PageInfoFields",
        ]
    ) -> "GitAutomationStateConnectionFields":
        """Subfields should come from the GitAutomationStateConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitAutomationStateConnectionFields":
        self._alias = alias
        return self


class GitAutomationStateEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "GitAutomationStateFields":
        return GitAutomationStateFields("node")

    cursor: "GitAutomationStateEdgeGraphQLField" = GitAutomationStateEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[
            GitAutomationStateEdgeGraphQLField, "GitAutomationStateFields"
        ]
    ) -> "GitAutomationStateEdgeFields":
        """Subfields should come from the GitAutomationStateEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitAutomationStateEdgeFields":
        self._alias = alias
        return self


class GitAutomationStatePayloadFields(GraphQLField):
    last_sync_id: "GitAutomationStatePayloadGraphQLField" = (
        GitAutomationStatePayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def git_automation_state(cls) -> "GitAutomationStateFields":
        return GitAutomationStateFields("git_automation_state")

    success: "GitAutomationStatePayloadGraphQLField" = (
        GitAutomationStatePayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            GitAutomationStatePayloadGraphQLField, "GitAutomationStateFields"
        ]
    ) -> "GitAutomationStatePayloadFields":
        """Subfields should come from the GitAutomationStatePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitAutomationStatePayloadFields":
        self._alias = alias
        return self


class GitAutomationTargetBranchFields(GraphQLField):
    id: "GitAutomationTargetBranchGraphQLField" = GitAutomationTargetBranchGraphQLField(
        "id"
    )
    created_at: "GitAutomationTargetBranchGraphQLField" = (
        GitAutomationTargetBranchGraphQLField("createdAt")
    )
    updated_at: "GitAutomationTargetBranchGraphQLField" = (
        GitAutomationTargetBranchGraphQLField("updatedAt")
    )
    archived_at: "GitAutomationTargetBranchGraphQLField" = (
        GitAutomationTargetBranchGraphQLField("archivedAt")
    )

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    branch_pattern: "GitAutomationTargetBranchGraphQLField" = (
        GitAutomationTargetBranchGraphQLField("branchPattern")
    )
    is_regex: "GitAutomationTargetBranchGraphQLField" = (
        GitAutomationTargetBranchGraphQLField("isRegex")
    )

    @classmethod
    def automation_states(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "GitAutomationStateConnectionFields":
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
        return GitAutomationStateConnectionFields(
            "automation_states", arguments=cleared_arguments
        )

    def fields(
        self,
        *subfields: Union[
            GitAutomationTargetBranchGraphQLField,
            "GitAutomationStateConnectionFields",
            "TeamFields",
        ]
    ) -> "GitAutomationTargetBranchFields":
        """Subfields should come from the GitAutomationTargetBranchFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitAutomationTargetBranchFields":
        self._alias = alias
        return self


class GitAutomationTargetBranchPayloadFields(GraphQLField):
    last_sync_id: "GitAutomationTargetBranchPayloadGraphQLField" = (
        GitAutomationTargetBranchPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def target_branch(cls) -> "GitAutomationTargetBranchFields":
        return GitAutomationTargetBranchFields("target_branch")

    success: "GitAutomationTargetBranchPayloadGraphQLField" = (
        GitAutomationTargetBranchPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            GitAutomationTargetBranchPayloadGraphQLField,
            "GitAutomationTargetBranchFields",
        ]
    ) -> "GitAutomationTargetBranchPayloadFields":
        """Subfields should come from the GitAutomationTargetBranchPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitAutomationTargetBranchPayloadFields":
        self._alias = alias
        return self


class GitHubCommitIntegrationPayloadFields(GraphQLField):
    last_sync_id: "GitHubCommitIntegrationPayloadGraphQLField" = (
        GitHubCommitIntegrationPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def integration(cls) -> "IntegrationFields":
        return IntegrationFields("integration")

    success: "GitHubCommitIntegrationPayloadGraphQLField" = (
        GitHubCommitIntegrationPayloadGraphQLField("success")
    )
    webhook_secret: "GitHubCommitIntegrationPayloadGraphQLField" = (
        GitHubCommitIntegrationPayloadGraphQLField("webhookSecret")
    )

    def fields(
        self,
        *subfields: Union[
            GitHubCommitIntegrationPayloadGraphQLField, "IntegrationFields"
        ]
    ) -> "GitHubCommitIntegrationPayloadFields":
        """Subfields should come from the GitHubCommitIntegrationPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitHubCommitIntegrationPayloadFields":
        self._alias = alias
        return self


class GitHubEnterpriseServerInstallVerificationPayloadFields(GraphQLField):
    success: "GitHubEnterpriseServerInstallVerificationPayloadGraphQLField" = (
        GitHubEnterpriseServerInstallVerificationPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: GitHubEnterpriseServerInstallVerificationPayloadGraphQLField
    ) -> "GitHubEnterpriseServerInstallVerificationPayloadFields":
        """Subfields should come from the GitHubEnterpriseServerInstallVerificationPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(
        self, alias: str
    ) -> "GitHubEnterpriseServerInstallVerificationPayloadFields":
        self._alias = alias
        return self


class GitHubEnterpriseServerPayloadFields(GraphQLField):
    last_sync_id: "GitHubEnterpriseServerPayloadGraphQLField" = (
        GitHubEnterpriseServerPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def integration(cls) -> "IntegrationFields":
        return IntegrationFields("integration")

    success: "GitHubEnterpriseServerPayloadGraphQLField" = (
        GitHubEnterpriseServerPayloadGraphQLField("success")
    )
    setup_url: "GitHubEnterpriseServerPayloadGraphQLField" = (
        GitHubEnterpriseServerPayloadGraphQLField("setupUrl")
    )
    install_url: "GitHubEnterpriseServerPayloadGraphQLField" = (
        GitHubEnterpriseServerPayloadGraphQLField("installUrl")
    )
    webhook_secret: "GitHubEnterpriseServerPayloadGraphQLField" = (
        GitHubEnterpriseServerPayloadGraphQLField("webhookSecret")
    )

    def fields(
        self,
        *subfields: Union[
            GitHubEnterpriseServerPayloadGraphQLField, "IntegrationFields"
        ]
    ) -> "GitHubEnterpriseServerPayloadFields":
        """Subfields should come from the GitHubEnterpriseServerPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "GitHubEnterpriseServerPayloadFields":
        self._alias = alias
        return self


class ImageUploadFromUrlPayloadFields(GraphQLField):
    last_sync_id: "ImageUploadFromUrlPayloadGraphQLField" = (
        ImageUploadFromUrlPayloadGraphQLField("lastSyncId")
    )
    url: "ImageUploadFromUrlPayloadGraphQLField" = (
        ImageUploadFromUrlPayloadGraphQLField("url")
    )
    success: "ImageUploadFromUrlPayloadGraphQLField" = (
        ImageUploadFromUrlPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: ImageUploadFromUrlPayloadGraphQLField
    ) -> "ImageUploadFromUrlPayloadFields":
        """Subfields should come from the ImageUploadFromUrlPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ImageUploadFromUrlPayloadFields":
        self._alias = alias
        return self


class InitiativeFields(GraphQLField):
    id: "InitiativeGraphQLField" = InitiativeGraphQLField("id")
    created_at: "InitiativeGraphQLField" = InitiativeGraphQLField("createdAt")
    updated_at: "InitiativeGraphQLField" = InitiativeGraphQLField("updatedAt")
    archived_at: "InitiativeGraphQLField" = InitiativeGraphQLField("archivedAt")
    name: "InitiativeGraphQLField" = InitiativeGraphQLField("name")
    description: "InitiativeGraphQLField" = InitiativeGraphQLField("description")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def owner(cls) -> "UserFields":
        return UserFields("owner")

    slug_id: "InitiativeGraphQLField" = InitiativeGraphQLField("slugId")
    sort_order: "InitiativeGraphQLField" = InitiativeGraphQLField("sortOrder")
    color: "InitiativeGraphQLField" = InitiativeGraphQLField("color")
    icon: "InitiativeGraphQLField" = InitiativeGraphQLField("icon")
    trashed: "InitiativeGraphQLField" = InitiativeGraphQLField("trashed")
    target_date: "InitiativeGraphQLField" = InitiativeGraphQLField("targetDate")
    target_date_resolution: "InitiativeGraphQLField" = InitiativeGraphQLField(
        "targetDateResolution"
    )
    status: "InitiativeGraphQLField" = InitiativeGraphQLField("status")

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
    ) -> "ProjectConnectionFields":
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
        return ProjectConnectionFields("projects", arguments=cleared_arguments)

    @classmethod
    def links(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "EntityExternalLinkConnectionFields":
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
        return EntityExternalLinkConnectionFields("links", arguments=cleared_arguments)

    def fields(
        self,
        *subfields: Union[
            InitiativeGraphQLField,
            "EntityExternalLinkConnectionFields",
            "OrganizationFields",
            "ProjectConnectionFields",
            "UserFields",
        ]
    ) -> "InitiativeFields":
        """Subfields should come from the InitiativeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeFields":
        self._alias = alias
        return self


class InitiativeArchivePayloadFields(GraphQLField):
    last_sync_id: "InitiativeArchivePayloadGraphQLField" = (
        InitiativeArchivePayloadGraphQLField("lastSyncId")
    )
    success: "InitiativeArchivePayloadGraphQLField" = (
        InitiativeArchivePayloadGraphQLField("success")
    )

    @classmethod
    def entity(cls) -> "InitiativeFields":
        return InitiativeFields("entity")

    def fields(
        self,
        *subfields: Union[InitiativeArchivePayloadGraphQLField, "InitiativeFields"]
    ) -> "InitiativeArchivePayloadFields":
        """Subfields should come from the InitiativeArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeArchivePayloadFields":
        self._alias = alias
        return self


class InitiativeConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "InitiativeEdgeFields":
        return InitiativeEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "InitiativeFields":
        return InitiativeFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            InitiativeConnectionGraphQLField,
            "InitiativeEdgeFields",
            "InitiativeFields",
            "PageInfoFields",
        ]
    ) -> "InitiativeConnectionFields":
        """Subfields should come from the InitiativeConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeConnectionFields":
        self._alias = alias
        return self


class InitiativeEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "InitiativeFields":
        return InitiativeFields("node")

    cursor: "InitiativeEdgeGraphQLField" = InitiativeEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[InitiativeEdgeGraphQLField, "InitiativeFields"]
    ) -> "InitiativeEdgeFields":
        """Subfields should come from the InitiativeEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeEdgeFields":
        self._alias = alias
        return self


class InitiativePayloadFields(GraphQLField):
    last_sync_id: "InitiativePayloadGraphQLField" = InitiativePayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    success: "InitiativePayloadGraphQLField" = InitiativePayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[InitiativePayloadGraphQLField, "InitiativeFields"]
    ) -> "InitiativePayloadFields":
        """Subfields should come from the InitiativePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativePayloadFields":
        self._alias = alias
        return self


class InitiativeToProjectFields(GraphQLField):
    id: "InitiativeToProjectGraphQLField" = InitiativeToProjectGraphQLField("id")
    created_at: "InitiativeToProjectGraphQLField" = InitiativeToProjectGraphQLField(
        "createdAt"
    )
    updated_at: "InitiativeToProjectGraphQLField" = InitiativeToProjectGraphQLField(
        "updatedAt"
    )
    archived_at: "InitiativeToProjectGraphQLField" = InitiativeToProjectGraphQLField(
        "archivedAt"
    )

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    sort_order: "InitiativeToProjectGraphQLField" = InitiativeToProjectGraphQLField(
        "sortOrder"
    )

    def fields(
        self,
        *subfields: Union[
            InitiativeToProjectGraphQLField, "InitiativeFields", "ProjectFields"
        ]
    ) -> "InitiativeToProjectFields":
        """Subfields should come from the InitiativeToProjectFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeToProjectFields":
        self._alias = alias
        return self


class InitiativeToProjectConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "InitiativeToProjectEdgeFields":
        return InitiativeToProjectEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "InitiativeToProjectFields":
        return InitiativeToProjectFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            InitiativeToProjectConnectionGraphQLField,
            "InitiativeToProjectEdgeFields",
            "InitiativeToProjectFields",
            "PageInfoFields",
        ]
    ) -> "InitiativeToProjectConnectionFields":
        """Subfields should come from the InitiativeToProjectConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeToProjectConnectionFields":
        self._alias = alias
        return self


class InitiativeToProjectEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "InitiativeToProjectFields":
        return InitiativeToProjectFields("node")

    cursor: "InitiativeToProjectEdgeGraphQLField" = InitiativeToProjectEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[
            InitiativeToProjectEdgeGraphQLField, "InitiativeToProjectFields"
        ]
    ) -> "InitiativeToProjectEdgeFields":
        """Subfields should come from the InitiativeToProjectEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeToProjectEdgeFields":
        self._alias = alias
        return self


class InitiativeToProjectPayloadFields(GraphQLField):
    last_sync_id: "InitiativeToProjectPayloadGraphQLField" = (
        InitiativeToProjectPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def initiative_to_project(cls) -> "InitiativeToProjectFields":
        return InitiativeToProjectFields("initiative_to_project")

    success: "InitiativeToProjectPayloadGraphQLField" = (
        InitiativeToProjectPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            InitiativeToProjectPayloadGraphQLField, "InitiativeToProjectFields"
        ]
    ) -> "InitiativeToProjectPayloadFields":
        """Subfields should come from the InitiativeToProjectPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "InitiativeToProjectPayloadFields":
        self._alias = alias
        return self


class IntegrationFields(GraphQLField):
    id: "IntegrationGraphQLField" = IntegrationGraphQLField("id")
    created_at: "IntegrationGraphQLField" = IntegrationGraphQLField("createdAt")
    updated_at: "IntegrationGraphQLField" = IntegrationGraphQLField("updatedAt")
    archived_at: "IntegrationGraphQLField" = IntegrationGraphQLField("archivedAt")
    service: "IntegrationGraphQLField" = IntegrationGraphQLField("service")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    def fields(
        self,
        *subfields: Union[
            IntegrationGraphQLField, "OrganizationFields", "TeamFields", "UserFields"
        ]
    ) -> "IntegrationFields":
        """Subfields should come from the IntegrationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationFields":
        self._alias = alias
        return self


class IntegrationConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "IntegrationEdgeFields":
        return IntegrationEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "IntegrationFields":
        return IntegrationFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            IntegrationConnectionGraphQLField,
            "IntegrationEdgeFields",
            "IntegrationFields",
            "PageInfoFields",
        ]
    ) -> "IntegrationConnectionFields":
        """Subfields should come from the IntegrationConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationConnectionFields":
        self._alias = alias
        return self


class IntegrationEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "IntegrationFields":
        return IntegrationFields("node")

    cursor: "IntegrationEdgeGraphQLField" = IntegrationEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[IntegrationEdgeGraphQLField, "IntegrationFields"]
    ) -> "IntegrationEdgeFields":
        """Subfields should come from the IntegrationEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationEdgeFields":
        self._alias = alias
        return self


class IntegrationHasScopesPayloadFields(GraphQLField):
    has_all_scopes: "IntegrationHasScopesPayloadGraphQLField" = (
        IntegrationHasScopesPayloadGraphQLField("hasAllScopes")
    )
    missing_scopes: "IntegrationHasScopesPayloadGraphQLField" = (
        IntegrationHasScopesPayloadGraphQLField("missingScopes")
    )

    def fields(
        self, *subfields: IntegrationHasScopesPayloadGraphQLField
    ) -> "IntegrationHasScopesPayloadFields":
        """Subfields should come from the IntegrationHasScopesPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationHasScopesPayloadFields":
        self._alias = alias
        return self


class IntegrationPayloadFields(GraphQLField):
    last_sync_id: "IntegrationPayloadGraphQLField" = IntegrationPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def integration(cls) -> "IntegrationFields":
        return IntegrationFields("integration")

    success: "IntegrationPayloadGraphQLField" = IntegrationPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[IntegrationPayloadGraphQLField, "IntegrationFields"]
    ) -> "IntegrationPayloadFields":
        """Subfields should come from the IntegrationPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationPayloadFields":
        self._alias = alias
        return self


class IntegrationRequestPayloadFields(GraphQLField):
    success: "IntegrationRequestPayloadGraphQLField" = (
        IntegrationRequestPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: IntegrationRequestPayloadGraphQLField
    ) -> "IntegrationRequestPayloadFields":
        """Subfields should come from the IntegrationRequestPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationRequestPayloadFields":
        self._alias = alias
        return self


class IntegrationTemplateFields(GraphQLField):
    id: "IntegrationTemplateGraphQLField" = IntegrationTemplateGraphQLField("id")
    created_at: "IntegrationTemplateGraphQLField" = IntegrationTemplateGraphQLField(
        "createdAt"
    )
    updated_at: "IntegrationTemplateGraphQLField" = IntegrationTemplateGraphQLField(
        "updatedAt"
    )
    archived_at: "IntegrationTemplateGraphQLField" = IntegrationTemplateGraphQLField(
        "archivedAt"
    )

    @classmethod
    def template(cls) -> "TemplateFields":
        return TemplateFields("template")

    @classmethod
    def integration(cls) -> "IntegrationFields":
        return IntegrationFields("integration")

    foreign_entity_id: "IntegrationTemplateGraphQLField" = (
        IntegrationTemplateGraphQLField("foreignEntityId")
    )

    def fields(
        self,
        *subfields: Union[
            IntegrationTemplateGraphQLField, "IntegrationFields", "TemplateFields"
        ]
    ) -> "IntegrationTemplateFields":
        """Subfields should come from the IntegrationTemplateFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationTemplateFields":
        self._alias = alias
        return self


class IntegrationTemplateConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "IntegrationTemplateEdgeFields":
        return IntegrationTemplateEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "IntegrationTemplateFields":
        return IntegrationTemplateFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            IntegrationTemplateConnectionGraphQLField,
            "IntegrationTemplateEdgeFields",
            "IntegrationTemplateFields",
            "PageInfoFields",
        ]
    ) -> "IntegrationTemplateConnectionFields":
        """Subfields should come from the IntegrationTemplateConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationTemplateConnectionFields":
        self._alias = alias
        return self


class IntegrationTemplateEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "IntegrationTemplateFields":
        return IntegrationTemplateFields("node")

    cursor: "IntegrationTemplateEdgeGraphQLField" = IntegrationTemplateEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[
            IntegrationTemplateEdgeGraphQLField, "IntegrationTemplateFields"
        ]
    ) -> "IntegrationTemplateEdgeFields":
        """Subfields should come from the IntegrationTemplateEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationTemplateEdgeFields":
        self._alias = alias
        return self


class IntegrationTemplatePayloadFields(GraphQLField):
    last_sync_id: "IntegrationTemplatePayloadGraphQLField" = (
        IntegrationTemplatePayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def integration_template(cls) -> "IntegrationTemplateFields":
        return IntegrationTemplateFields("integration_template")

    success: "IntegrationTemplatePayloadGraphQLField" = (
        IntegrationTemplatePayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            IntegrationTemplatePayloadGraphQLField, "IntegrationTemplateFields"
        ]
    ) -> "IntegrationTemplatePayloadFields":
        """Subfields should come from the IntegrationTemplatePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationTemplatePayloadFields":
        self._alias = alias
        return self


class IntegrationsSettingsFields(GraphQLField):
    id: "IntegrationsSettingsGraphQLField" = IntegrationsSettingsGraphQLField("id")
    created_at: "IntegrationsSettingsGraphQLField" = IntegrationsSettingsGraphQLField(
        "createdAt"
    )
    updated_at: "IntegrationsSettingsGraphQLField" = IntegrationsSettingsGraphQLField(
        "updatedAt"
    )
    archived_at: "IntegrationsSettingsGraphQLField" = IntegrationsSettingsGraphQLField(
        "archivedAt"
    )
    slack_issue_created: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueCreated")
    )
    slack_issue_new_comment: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueNewComment")
    )
    slack_issue_status_changed_done: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueStatusChangedDone")
    )
    slack_issue_added_to_view: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueAddedToView")
    )
    slack_issue_status_changed_all: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueStatusChangedAll")
    )
    slack_project_update_created: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackProjectUpdateCreated")
    )
    slack_project_update_created_to_team: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackProjectUpdateCreatedToTeam")
    )
    slack_project_update_created_to_workspace: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackProjectUpdateCreatedToWorkspace")
    )
    slack_issue_added_to_triage: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueAddedToTriage")
    )
    slack_issue_sla_high_risk: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueSlaHighRisk")
    )
    slack_issue_sla_breached: "IntegrationsSettingsGraphQLField" = (
        IntegrationsSettingsGraphQLField("slackIssueSlaBreached")
    )

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    def fields(
        self,
        *subfields: Union[
            IntegrationsSettingsGraphQLField, "ProjectFields", "TeamFields"
        ]
    ) -> "IntegrationsSettingsFields":
        """Subfields should come from the IntegrationsSettingsFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationsSettingsFields":
        self._alias = alias
        return self


class IntegrationsSettingsPayloadFields(GraphQLField):
    last_sync_id: "IntegrationsSettingsPayloadGraphQLField" = (
        IntegrationsSettingsPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def integrations_settings(cls) -> "IntegrationsSettingsFields":
        return IntegrationsSettingsFields("integrations_settings")

    success: "IntegrationsSettingsPayloadGraphQLField" = (
        IntegrationsSettingsPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            IntegrationsSettingsPayloadGraphQLField, "IntegrationsSettingsFields"
        ]
    ) -> "IntegrationsSettingsPayloadFields":
        """Subfields should come from the IntegrationsSettingsPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IntegrationsSettingsPayloadFields":
        self._alias = alias
        return self


class IssueFields(GraphQLField):
    id: "IssueGraphQLField" = IssueGraphQLField("id")
    created_at: "IssueGraphQLField" = IssueGraphQLField("createdAt")
    updated_at: "IssueGraphQLField" = IssueGraphQLField("updatedAt")
    archived_at: "IssueGraphQLField" = IssueGraphQLField("archivedAt")
    number: "IssueGraphQLField" = IssueGraphQLField("number")
    title: "IssueGraphQLField" = IssueGraphQLField("title")
    priority: "IssueGraphQLField" = IssueGraphQLField("priority")
    estimate: "IssueGraphQLField" = IssueGraphQLField("estimate")
    board_order: "IssueGraphQLField" = IssueGraphQLField("boardOrder")
    sort_order: "IssueGraphQLField" = IssueGraphQLField("sortOrder")
    priority_sort_order: "IssueGraphQLField" = IssueGraphQLField("prioritySortOrder")
    started_at: "IssueGraphQLField" = IssueGraphQLField("startedAt")
    completed_at: "IssueGraphQLField" = IssueGraphQLField("completedAt")
    started_triage_at: "IssueGraphQLField" = IssueGraphQLField("startedTriageAt")
    triaged_at: "IssueGraphQLField" = IssueGraphQLField("triagedAt")
    canceled_at: "IssueGraphQLField" = IssueGraphQLField("canceledAt")
    auto_closed_at: "IssueGraphQLField" = IssueGraphQLField("autoClosedAt")
    auto_archived_at: "IssueGraphQLField" = IssueGraphQLField("autoArchivedAt")
    due_date: "IssueGraphQLField" = IssueGraphQLField("dueDate")
    sla_started_at: "IssueGraphQLField" = IssueGraphQLField("slaStartedAt")
    sla_breaches_at: "IssueGraphQLField" = IssueGraphQLField("slaBreachesAt")
    trashed: "IssueGraphQLField" = IssueGraphQLField("trashed")
    snoozed_until_at: "IssueGraphQLField" = IssueGraphQLField("snoozedUntilAt")
    label_ids: "IssueGraphQLField" = IssueGraphQLField("labelIds")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def cycle(cls) -> "CycleFields":
        return CycleFields("cycle")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def project_milestone(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("project_milestone")

    @classmethod
    def last_applied_template(cls) -> "TemplateFields":
        return TemplateFields("last_applied_template")

    previous_identifiers: "IssueGraphQLField" = IssueGraphQLField("previousIdentifiers")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def external_user_creator(cls) -> "ExternalUserFields":
        return ExternalUserFields("external_user_creator")

    @classmethod
    def assignee(cls) -> "UserFields":
        return UserFields("assignee")

    @classmethod
    def snoozed_by(cls) -> "UserFields":
        return UserFields("snoozed_by")

    @classmethod
    def state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("state")

    sub_issue_sort_order: "IssueGraphQLField" = IssueGraphQLField("subIssueSortOrder")
    reaction_data: "IssueGraphQLField" = IssueGraphQLField("reactionData")
    priority_label: "IssueGraphQLField" = IssueGraphQLField("priorityLabel")

    @classmethod
    def source_comment(cls) -> "CommentFields":
        return CommentFields("source_comment")

    integration_source_type: "IssueGraphQLField" = IssueGraphQLField(
        "integrationSourceType"
    )

    @classmethod
    def bot_actor(cls) -> "ActorBotFields":
        return ActorBotFields("bot_actor")

    @classmethod
    def favorite(cls) -> "FavoriteFields":
        return FavoriteFields("favorite")

    identifier: "IssueGraphQLField" = IssueGraphQLField("identifier")
    url: "IssueGraphQLField" = IssueGraphQLField("url")
    branch_name: "IssueGraphQLField" = IssueGraphQLField("branchName")
    customer_ticket_count: "IssueGraphQLField" = IssueGraphQLField(
        "customerTicketCount"
    )

    @classmethod
    def subscribers(
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
    ) -> "UserConnectionFields":
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
        return UserConnectionFields("subscribers", arguments=cleared_arguments)

    @classmethod
    def parent(cls) -> "IssueFields":
        return IssueFields("parent")

    @classmethod
    def children(
        cls,
        *,
        filter: Optional[IssueFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("children", arguments=cleared_arguments)

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
    ) -> "CommentConnectionFields":
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
        return CommentConnectionFields("comments", arguments=cleared_arguments)

    @classmethod
    def history(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueHistoryConnectionFields":
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
        return IssueHistoryConnectionFields("history", arguments=cleared_arguments)

    @classmethod
    def labels(
        cls,
        *,
        filter: Optional[IssueLabelFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueLabelConnectionFields":
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
        return IssueLabelConnectionFields("labels", arguments=cleared_arguments)

    @classmethod
    def relations(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueRelationConnectionFields":
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
        return IssueRelationConnectionFields("relations", arguments=cleared_arguments)

    @classmethod
    def inverse_relations(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueRelationConnectionFields":
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
            "inverse_relations", arguments=cleared_arguments
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
    ) -> "AttachmentConnectionFields":
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
        return AttachmentConnectionFields("attachments", arguments=cleared_arguments)

    description: "IssueGraphQLField" = IssueGraphQLField("description")
    description_data: "IssueGraphQLField" = IssueGraphQLField("descriptionData")
    description_state: "IssueGraphQLField" = IssueGraphQLField("descriptionState")

    @classmethod
    def reactions(cls) -> "ReactionFields":
        return ReactionFields("reactions")

    def fields(
        self,
        *subfields: Union[
            IssueGraphQLField,
            "ActorBotFields",
            "AttachmentConnectionFields",
            "CommentConnectionFields",
            "CommentFields",
            "CycleFields",
            "ExternalUserFields",
            "FavoriteFields",
            "IssueConnectionFields",
            "IssueFields",
            "IssueHistoryConnectionFields",
            "IssueLabelConnectionFields",
            "IssueRelationConnectionFields",
            "ProjectFields",
            "ProjectMilestoneFields",
            "ReactionFields",
            "TeamFields",
            "TemplateFields",
            "UserConnectionFields",
            "UserFields",
            "WorkflowStateFields",
        ]
    ) -> "IssueFields":
        """Subfields should come from the IssueFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueFields":
        self._alias = alias
        return self


class IssueArchivePayloadFields(GraphQLField):
    last_sync_id: "IssueArchivePayloadGraphQLField" = IssueArchivePayloadGraphQLField(
        "lastSyncId"
    )
    success: "IssueArchivePayloadGraphQLField" = IssueArchivePayloadGraphQLField(
        "success"
    )

    @classmethod
    def entity(cls) -> "IssueFields":
        return IssueFields("entity")

    def fields(
        self, *subfields: Union[IssueArchivePayloadGraphQLField, "IssueFields"]
    ) -> "IssueArchivePayloadFields":
        """Subfields should come from the IssueArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueArchivePayloadFields":
        self._alias = alias
        return self


class IssueBatchPayloadFields(GraphQLField):
    last_sync_id: "IssueBatchPayloadGraphQLField" = IssueBatchPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def issues(cls) -> "IssueFields":
        return IssueFields("issues")

    success: "IssueBatchPayloadGraphQLField" = IssueBatchPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[IssueBatchPayloadGraphQLField, "IssueFields"]
    ) -> "IssueBatchPayloadFields":
        """Subfields should come from the IssueBatchPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueBatchPayloadFields":
        self._alias = alias
        return self


class IssueConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "IssueEdgeFields":
        return IssueEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "IssueFields":
        return IssueFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            IssueConnectionGraphQLField,
            "IssueEdgeFields",
            "IssueFields",
            "PageInfoFields",
        ]
    ) -> "IssueConnectionFields":
        """Subfields should come from the IssueConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueConnectionFields":
        self._alias = alias
        return self


class IssueEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "IssueFields":
        return IssueFields("node")

    cursor: "IssueEdgeGraphQLField" = IssueEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[IssueEdgeGraphQLField, "IssueFields"]
    ) -> "IssueEdgeFields":
        """Subfields should come from the IssueEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueEdgeFields":
        self._alias = alias
        return self


class IssueFilterSuggestionPayloadFields(GraphQLField):
    filter: "IssueFilterSuggestionPayloadGraphQLField" = (
        IssueFilterSuggestionPayloadGraphQLField("filter")
    )

    def fields(
        self, *subfields: IssueFilterSuggestionPayloadGraphQLField
    ) -> "IssueFilterSuggestionPayloadFields":
        """Subfields should come from the IssueFilterSuggestionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueFilterSuggestionPayloadFields":
        self._alias = alias
        return self


class IssueHistoryFields(GraphQLField):
    id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("id")
    created_at: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("createdAt")
    updated_at: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("updatedAt")
    archived_at: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("archivedAt")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    actor_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("actorId")
    updated_description: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "updatedDescription"
    )
    from_title: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("fromTitle")
    to_title: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toTitle")
    from_assignee_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "fromAssigneeId"
    )
    to_assignee_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "toAssigneeId"
    )
    from_priority: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("fromPriority")
    to_priority: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toPriority")
    from_team_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("fromTeamId")
    to_team_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toTeamId")
    from_parent_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "fromParentId"
    )
    to_parent_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toParentId")
    from_state_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("fromStateId")
    to_state_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toStateId")
    from_cycle_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("fromCycleId")
    to_cycle_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toCycleId")
    to_converted_project_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "toConvertedProjectId"
    )
    from_project_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "fromProjectId"
    )
    to_project_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toProjectId")
    from_estimate: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("fromEstimate")
    to_estimate: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toEstimate")
    archived: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("archived")
    trashed: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("trashed")
    attachment_id: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("attachmentId")
    added_label_ids: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "addedLabelIds"
    )
    removed_label_ids: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField(
        "removedLabelIds"
    )

    @classmethod
    def relation_changes(cls) -> "IssueRelationHistoryPayloadFields":
        return IssueRelationHistoryPayloadFields("relation_changes")

    auto_closed: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("autoClosed")
    auto_archived: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("autoArchived")
    from_due_date: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("fromDueDate")
    to_due_date: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("toDueDate")
    changes: "IssueHistoryGraphQLField" = IssueHistoryGraphQLField("changes")

    @classmethod
    def actor(cls) -> "UserFields":
        return UserFields("actor")

    @classmethod
    def actors(cls) -> "UserFields":
        return UserFields("actors")

    @classmethod
    def from_assignee(cls) -> "UserFields":
        return UserFields("from_assignee")

    @classmethod
    def to_assignee(cls) -> "UserFields":
        return UserFields("to_assignee")

    @classmethod
    def from_cycle(cls) -> "CycleFields":
        return CycleFields("from_cycle")

    @classmethod
    def to_cycle(cls) -> "CycleFields":
        return CycleFields("to_cycle")

    @classmethod
    def to_converted_project(cls) -> "ProjectFields":
        return ProjectFields("to_converted_project")

    @classmethod
    def from_project(cls) -> "ProjectFields":
        return ProjectFields("from_project")

    @classmethod
    def to_project(cls) -> "ProjectFields":
        return ProjectFields("to_project")

    @classmethod
    def from_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("from_state")

    @classmethod
    def to_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("to_state")

    @classmethod
    def from_team(cls) -> "TeamFields":
        return TeamFields("from_team")

    @classmethod
    def to_team(cls) -> "TeamFields":
        return TeamFields("to_team")

    @classmethod
    def from_parent(cls) -> "IssueFields":
        return IssueFields("from_parent")

    @classmethod
    def to_parent(cls) -> "IssueFields":
        return IssueFields("to_parent")

    @classmethod
    def attachment(cls) -> "AttachmentFields":
        return AttachmentFields("attachment")

    @classmethod
    def issue_import(cls) -> "IssueImportFields":
        return IssueImportFields("issue_import")

    @classmethod
    def triage_responsibility_notified_users(cls) -> "UserFields":
        return UserFields("triage_responsibility_notified_users")

    @classmethod
    def bot_actor(cls) -> "ActorBotFields":
        return ActorBotFields("bot_actor")

    @classmethod
    def added_labels(cls) -> "IssueLabelFields":
        return IssueLabelFields("added_labels")

    @classmethod
    def removed_labels(cls) -> "IssueLabelFields":
        return IssueLabelFields("removed_labels")

    def fields(
        self,
        *subfields: Union[
            IssueHistoryGraphQLField,
            "ActorBotFields",
            "AttachmentFields",
            "CycleFields",
            "IssueFields",
            "IssueImportFields",
            "IssueLabelFields",
            "IssueRelationHistoryPayloadFields",
            "ProjectFields",
            "TeamFields",
            "UserFields",
            "WorkflowStateFields",
        ]
    ) -> "IssueHistoryFields":
        """Subfields should come from the IssueHistoryFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueHistoryFields":
        self._alias = alias
        return self


class IssueHistoryConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "IssueHistoryEdgeFields":
        return IssueHistoryEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "IssueHistoryFields":
        return IssueHistoryFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            IssueHistoryConnectionGraphQLField,
            "IssueHistoryEdgeFields",
            "IssueHistoryFields",
            "PageInfoFields",
        ]
    ) -> "IssueHistoryConnectionFields":
        """Subfields should come from the IssueHistoryConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueHistoryConnectionFields":
        self._alias = alias
        return self


class IssueHistoryEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "IssueHistoryFields":
        return IssueHistoryFields("node")

    cursor: "IssueHistoryEdgeGraphQLField" = IssueHistoryEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[IssueHistoryEdgeGraphQLField, "IssueHistoryFields"]
    ) -> "IssueHistoryEdgeFields":
        """Subfields should come from the IssueHistoryEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueHistoryEdgeFields":
        self._alias = alias
        return self


class IssueImportFields(GraphQLField):
    id: "IssueImportGraphQLField" = IssueImportGraphQLField("id")
    created_at: "IssueImportGraphQLField" = IssueImportGraphQLField("createdAt")
    updated_at: "IssueImportGraphQLField" = IssueImportGraphQLField("updatedAt")
    archived_at: "IssueImportGraphQLField" = IssueImportGraphQLField("archivedAt")
    team_name: "IssueImportGraphQLField" = IssueImportGraphQLField("teamName")
    creator_id: "IssueImportGraphQLField" = IssueImportGraphQLField("creatorId")
    service: "IssueImportGraphQLField" = IssueImportGraphQLField("service")
    status: "IssueImportGraphQLField" = IssueImportGraphQLField("status")
    mapping: "IssueImportGraphQLField" = IssueImportGraphQLField("mapping")
    error: "IssueImportGraphQLField" = IssueImportGraphQLField("error")
    progress: "IssueImportGraphQLField" = IssueImportGraphQLField("progress")
    csv_file_url: "IssueImportGraphQLField" = IssueImportGraphQLField("csvFileUrl")
    error_metadata: "IssueImportGraphQLField" = IssueImportGraphQLField("errorMetadata")
    service_metadata: "IssueImportGraphQLField" = IssueImportGraphQLField(
        "serviceMetadata"
    )
    display_name: "IssueImportGraphQLField" = IssueImportGraphQLField("displayName")

    def fields(self, *subfields: IssueImportGraphQLField) -> "IssueImportFields":
        """Subfields should come from the IssueImportFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueImportFields":
        self._alias = alias
        return self


class IssueImportCheckPayloadFields(GraphQLField):
    success: "IssueImportCheckPayloadGraphQLField" = (
        IssueImportCheckPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: IssueImportCheckPayloadGraphQLField
    ) -> "IssueImportCheckPayloadFields":
        """Subfields should come from the IssueImportCheckPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueImportCheckPayloadFields":
        self._alias = alias
        return self


class IssueImportDeletePayloadFields(GraphQLField):
    last_sync_id: "IssueImportDeletePayloadGraphQLField" = (
        IssueImportDeletePayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def issue_import(cls) -> "IssueImportFields":
        return IssueImportFields("issue_import")

    success: "IssueImportDeletePayloadGraphQLField" = (
        IssueImportDeletePayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[IssueImportDeletePayloadGraphQLField, "IssueImportFields"]
    ) -> "IssueImportDeletePayloadFields":
        """Subfields should come from the IssueImportDeletePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueImportDeletePayloadFields":
        self._alias = alias
        return self


class IssueImportPayloadFields(GraphQLField):
    last_sync_id: "IssueImportPayloadGraphQLField" = IssueImportPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def issue_import(cls) -> "IssueImportFields":
        return IssueImportFields("issue_import")

    success: "IssueImportPayloadGraphQLField" = IssueImportPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[IssueImportPayloadGraphQLField, "IssueImportFields"]
    ) -> "IssueImportPayloadFields":
        """Subfields should come from the IssueImportPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueImportPayloadFields":
        self._alias = alias
        return self


class IssueImportSyncCheckPayloadFields(GraphQLField):
    can_sync: "IssueImportSyncCheckPayloadGraphQLField" = (
        IssueImportSyncCheckPayloadGraphQLField("canSync")
    )
    error: "IssueImportSyncCheckPayloadGraphQLField" = (
        IssueImportSyncCheckPayloadGraphQLField("error")
    )

    def fields(
        self, *subfields: IssueImportSyncCheckPayloadGraphQLField
    ) -> "IssueImportSyncCheckPayloadFields":
        """Subfields should come from the IssueImportSyncCheckPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueImportSyncCheckPayloadFields":
        self._alias = alias
        return self


class IssueLabelFields(GraphQLField):
    id: "IssueLabelGraphQLField" = IssueLabelGraphQLField("id")
    created_at: "IssueLabelGraphQLField" = IssueLabelGraphQLField("createdAt")
    updated_at: "IssueLabelGraphQLField" = IssueLabelGraphQLField("updatedAt")
    archived_at: "IssueLabelGraphQLField" = IssueLabelGraphQLField("archivedAt")
    name: "IssueLabelGraphQLField" = IssueLabelGraphQLField("name")
    description: "IssueLabelGraphQLField" = IssueLabelGraphQLField("description")
    color: "IssueLabelGraphQLField" = IssueLabelGraphQLField("color")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def parent(cls) -> "IssueLabelFields":
        return IssueLabelFields("parent")

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
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    @classmethod
    def children(
        cls,
        *,
        filter: Optional[IssueLabelFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueLabelConnectionFields":
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
        return IssueLabelConnectionFields("children", arguments=cleared_arguments)

    is_group: "IssueLabelGraphQLField" = IssueLabelGraphQLField("isGroup")

    def fields(
        self,
        *subfields: Union[
            IssueLabelGraphQLField,
            "IssueConnectionFields",
            "IssueLabelConnectionFields",
            "IssueLabelFields",
            "OrganizationFields",
            "TeamFields",
            "UserFields",
        ]
    ) -> "IssueLabelFields":
        """Subfields should come from the IssueLabelFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueLabelFields":
        self._alias = alias
        return self


class IssueLabelConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "IssueLabelEdgeFields":
        return IssueLabelEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "IssueLabelFields":
        return IssueLabelFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            IssueLabelConnectionGraphQLField,
            "IssueLabelEdgeFields",
            "IssueLabelFields",
            "PageInfoFields",
        ]
    ) -> "IssueLabelConnectionFields":
        """Subfields should come from the IssueLabelConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueLabelConnectionFields":
        self._alias = alias
        return self


class IssueLabelEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "IssueLabelFields":
        return IssueLabelFields("node")

    cursor: "IssueLabelEdgeGraphQLField" = IssueLabelEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[IssueLabelEdgeGraphQLField, "IssueLabelFields"]
    ) -> "IssueLabelEdgeFields":
        """Subfields should come from the IssueLabelEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueLabelEdgeFields":
        self._alias = alias
        return self


class IssueLabelPayloadFields(GraphQLField):
    last_sync_id: "IssueLabelPayloadGraphQLField" = IssueLabelPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def issue_label(cls) -> "IssueLabelFields":
        return IssueLabelFields("issue_label")

    success: "IssueLabelPayloadGraphQLField" = IssueLabelPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[IssueLabelPayloadGraphQLField, "IssueLabelFields"]
    ) -> "IssueLabelPayloadFields":
        """Subfields should come from the IssueLabelPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueLabelPayloadFields":
        self._alias = alias
        return self


class IssuePayloadFields(GraphQLField):
    last_sync_id: "IssuePayloadGraphQLField" = IssuePayloadGraphQLField("lastSyncId")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    success: "IssuePayloadGraphQLField" = IssuePayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[IssuePayloadGraphQLField, "IssueFields"]
    ) -> "IssuePayloadFields":
        """Subfields should come from the IssuePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssuePayloadFields":
        self._alias = alias
        return self


class IssuePriorityValueFields(GraphQLField):
    priority: "IssuePriorityValueGraphQLField" = IssuePriorityValueGraphQLField(
        "priority"
    )
    label: "IssuePriorityValueGraphQLField" = IssuePriorityValueGraphQLField("label")

    def fields(
        self, *subfields: IssuePriorityValueGraphQLField
    ) -> "IssuePriorityValueFields":
        """Subfields should come from the IssuePriorityValueFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssuePriorityValueFields":
        self._alias = alias
        return self


class IssueRelationFields(GraphQLField):
    id: "IssueRelationGraphQLField" = IssueRelationGraphQLField("id")
    created_at: "IssueRelationGraphQLField" = IssueRelationGraphQLField("createdAt")
    updated_at: "IssueRelationGraphQLField" = IssueRelationGraphQLField("updatedAt")
    archived_at: "IssueRelationGraphQLField" = IssueRelationGraphQLField("archivedAt")
    type: "IssueRelationGraphQLField" = IssueRelationGraphQLField("type")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    @classmethod
    def related_issue(cls) -> "IssueFields":
        return IssueFields("related_issue")

    def fields(
        self, *subfields: Union[IssueRelationGraphQLField, "IssueFields"]
    ) -> "IssueRelationFields":
        """Subfields should come from the IssueRelationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueRelationFields":
        self._alias = alias
        return self


class IssueRelationConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "IssueRelationEdgeFields":
        return IssueRelationEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "IssueRelationFields":
        return IssueRelationFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            IssueRelationConnectionGraphQLField,
            "IssueRelationEdgeFields",
            "IssueRelationFields",
            "PageInfoFields",
        ]
    ) -> "IssueRelationConnectionFields":
        """Subfields should come from the IssueRelationConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueRelationConnectionFields":
        self._alias = alias
        return self


class IssueRelationEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "IssueRelationFields":
        return IssueRelationFields("node")

    cursor: "IssueRelationEdgeGraphQLField" = IssueRelationEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[IssueRelationEdgeGraphQLField, "IssueRelationFields"]
    ) -> "IssueRelationEdgeFields":
        """Subfields should come from the IssueRelationEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueRelationEdgeFields":
        self._alias = alias
        return self


class IssueRelationHistoryPayloadFields(GraphQLField):
    identifier: "IssueRelationHistoryPayloadGraphQLField" = (
        IssueRelationHistoryPayloadGraphQLField("identifier")
    )
    type: "IssueRelationHistoryPayloadGraphQLField" = (
        IssueRelationHistoryPayloadGraphQLField("type")
    )

    def fields(
        self, *subfields: IssueRelationHistoryPayloadGraphQLField
    ) -> "IssueRelationHistoryPayloadFields":
        """Subfields should come from the IssueRelationHistoryPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueRelationHistoryPayloadFields":
        self._alias = alias
        return self


class IssueRelationPayloadFields(GraphQLField):
    last_sync_id: "IssueRelationPayloadGraphQLField" = IssueRelationPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def issue_relation(cls) -> "IssueRelationFields":
        return IssueRelationFields("issue_relation")

    success: "IssueRelationPayloadGraphQLField" = IssueRelationPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[IssueRelationPayloadGraphQLField, "IssueRelationFields"]
    ) -> "IssueRelationPayloadFields":
        """Subfields should come from the IssueRelationPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueRelationPayloadFields":
        self._alias = alias
        return self


class IssueSearchPayloadFields(GraphQLField):
    @classmethod
    def edges(cls) -> "IssueSearchResultEdgeFields":
        return IssueSearchResultEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "IssueSearchResultFields":
        return IssueSearchResultFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    @classmethod
    def archive_payload(cls) -> "ArchiveResponseFields":
        return ArchiveResponseFields("archive_payload")

    total_count: "IssueSearchPayloadGraphQLField" = IssueSearchPayloadGraphQLField(
        "totalCount"
    )

    def fields(
        self,
        *subfields: Union[
            IssueSearchPayloadGraphQLField,
            "ArchiveResponseFields",
            "IssueSearchResultEdgeFields",
            "IssueSearchResultFields",
            "PageInfoFields",
        ]
    ) -> "IssueSearchPayloadFields":
        """Subfields should come from the IssueSearchPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueSearchPayloadFields":
        self._alias = alias
        return self


class IssueSearchResultFields(GraphQLField):
    id: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField("id")
    created_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "createdAt"
    )
    updated_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "updatedAt"
    )
    archived_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "archivedAt"
    )
    number: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField("number")
    title: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField("title")
    priority: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "priority"
    )
    estimate: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "estimate"
    )
    board_order: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "boardOrder"
    )
    sort_order: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "sortOrder"
    )
    priority_sort_order: "IssueSearchResultGraphQLField" = (
        IssueSearchResultGraphQLField("prioritySortOrder")
    )
    started_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "startedAt"
    )
    completed_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "completedAt"
    )
    started_triage_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "startedTriageAt"
    )
    triaged_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "triagedAt"
    )
    canceled_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "canceledAt"
    )
    auto_closed_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "autoClosedAt"
    )
    auto_archived_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "autoArchivedAt"
    )
    due_date: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField("dueDate")
    sla_started_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "slaStartedAt"
    )
    sla_breaches_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "slaBreachesAt"
    )
    trashed: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField("trashed")
    snoozed_until_at: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "snoozedUntilAt"
    )
    label_ids: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "labelIds"
    )

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def cycle(cls) -> "CycleFields":
        return CycleFields("cycle")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def project_milestone(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("project_milestone")

    @classmethod
    def last_applied_template(cls) -> "TemplateFields":
        return TemplateFields("last_applied_template")

    previous_identifiers: "IssueSearchResultGraphQLField" = (
        IssueSearchResultGraphQLField("previousIdentifiers")
    )

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def external_user_creator(cls) -> "ExternalUserFields":
        return ExternalUserFields("external_user_creator")

    @classmethod
    def assignee(cls) -> "UserFields":
        return UserFields("assignee")

    @classmethod
    def snoozed_by(cls) -> "UserFields":
        return UserFields("snoozed_by")

    @classmethod
    def state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("state")

    sub_issue_sort_order: "IssueSearchResultGraphQLField" = (
        IssueSearchResultGraphQLField("subIssueSortOrder")
    )
    reaction_data: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "reactionData"
    )
    priority_label: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "priorityLabel"
    )

    @classmethod
    def source_comment(cls) -> "CommentFields":
        return CommentFields("source_comment")

    integration_source_type: "IssueSearchResultGraphQLField" = (
        IssueSearchResultGraphQLField("integrationSourceType")
    )

    @classmethod
    def bot_actor(cls) -> "ActorBotFields":
        return ActorBotFields("bot_actor")

    @classmethod
    def favorite(cls) -> "FavoriteFields":
        return FavoriteFields("favorite")

    identifier: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "identifier"
    )
    url: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField("url")
    branch_name: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "branchName"
    )
    customer_ticket_count: "IssueSearchResultGraphQLField" = (
        IssueSearchResultGraphQLField("customerTicketCount")
    )

    @classmethod
    def subscribers(
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
    ) -> "UserConnectionFields":
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
        return UserConnectionFields("subscribers", arguments=cleared_arguments)

    @classmethod
    def parent(cls) -> "IssueFields":
        return IssueFields("parent")

    @classmethod
    def children(
        cls,
        *,
        filter: Optional[IssueFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("children", arguments=cleared_arguments)

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
    ) -> "CommentConnectionFields":
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
        return CommentConnectionFields("comments", arguments=cleared_arguments)

    @classmethod
    def history(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueHistoryConnectionFields":
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
        return IssueHistoryConnectionFields("history", arguments=cleared_arguments)

    @classmethod
    def labels(
        cls,
        *,
        filter: Optional[IssueLabelFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueLabelConnectionFields":
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
        return IssueLabelConnectionFields("labels", arguments=cleared_arguments)

    @classmethod
    def relations(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueRelationConnectionFields":
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
        return IssueRelationConnectionFields("relations", arguments=cleared_arguments)

    @classmethod
    def inverse_relations(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueRelationConnectionFields":
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
            "inverse_relations", arguments=cleared_arguments
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
    ) -> "AttachmentConnectionFields":
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
        return AttachmentConnectionFields("attachments", arguments=cleared_arguments)

    description: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "description"
    )
    description_data: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "descriptionData"
    )
    description_state: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "descriptionState"
    )

    @classmethod
    def reactions(cls) -> "ReactionFields":
        return ReactionFields("reactions")

    metadata: "IssueSearchResultGraphQLField" = IssueSearchResultGraphQLField(
        "metadata"
    )

    def fields(
        self,
        *subfields: Union[
            IssueSearchResultGraphQLField,
            "ActorBotFields",
            "AttachmentConnectionFields",
            "CommentConnectionFields",
            "CommentFields",
            "CycleFields",
            "ExternalUserFields",
            "FavoriteFields",
            "IssueConnectionFields",
            "IssueFields",
            "IssueHistoryConnectionFields",
            "IssueLabelConnectionFields",
            "IssueRelationConnectionFields",
            "ProjectFields",
            "ProjectMilestoneFields",
            "ReactionFields",
            "TeamFields",
            "TemplateFields",
            "UserConnectionFields",
            "UserFields",
            "WorkflowStateFields",
        ]
    ) -> "IssueSearchResultFields":
        """Subfields should come from the IssueSearchResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueSearchResultFields":
        self._alias = alias
        return self


class IssueSearchResultEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "IssueSearchResultFields":
        return IssueSearchResultFields("node")

    cursor: "IssueSearchResultEdgeGraphQLField" = IssueSearchResultEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[IssueSearchResultEdgeGraphQLField, "IssueSearchResultFields"]
    ) -> "IssueSearchResultEdgeFields":
        """Subfields should come from the IssueSearchResultEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "IssueSearchResultEdgeFields":
        self._alias = alias
        return self


class LogoutResponseFields(GraphQLField):
    success: "LogoutResponseGraphQLField" = LogoutResponseGraphQLField("success")

    def fields(self, *subfields: LogoutResponseGraphQLField) -> "LogoutResponseFields":
        """Subfields should come from the LogoutResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "LogoutResponseFields":
        self._alias = alias
        return self


class NodeInterface(GraphQLField):
    id: "NodeGraphQLField" = NodeGraphQLField("id")

    def fields(self, *subfields: NodeGraphQLField) -> "NodeInterface":
        """Subfields should come from the NodeInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NodeInterface":
        self._alias = alias
        return self

    def on(self, type_name: str, *subfields: GraphQLField) -> "NodeInterface":
        self._inline_fragments[type_name] = subfields
        return self


class NotificationInterface(GraphQLField):
    id: "NotificationGraphQLField" = NotificationGraphQLField("id")
    created_at: "NotificationGraphQLField" = NotificationGraphQLField("createdAt")
    updated_at: "NotificationGraphQLField" = NotificationGraphQLField("updatedAt")
    archived_at: "NotificationGraphQLField" = NotificationGraphQLField("archivedAt")
    type: "NotificationGraphQLField" = NotificationGraphQLField("type")

    @classmethod
    def actor(cls) -> "UserFields":
        return UserFields("actor")

    @classmethod
    def external_user_actor(cls) -> "ExternalUserFields":
        return ExternalUserFields("external_user_actor")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    read_at: "NotificationGraphQLField" = NotificationGraphQLField("readAt")
    emailed_at: "NotificationGraphQLField" = NotificationGraphQLField("emailedAt")
    snoozed_until_at: "NotificationGraphQLField" = NotificationGraphQLField(
        "snoozedUntilAt"
    )
    unsnoozed_at: "NotificationGraphQLField" = NotificationGraphQLField("unsnoozedAt")
    url: "NotificationGraphQLField" = NotificationGraphQLField("url")
    inbox_url: "NotificationGraphQLField" = NotificationGraphQLField("inboxUrl")
    title: "NotificationGraphQLField" = NotificationGraphQLField("title")
    subtitle: "NotificationGraphQLField" = NotificationGraphQLField("subtitle")
    is_linear_actor: "NotificationGraphQLField" = NotificationGraphQLField(
        "isLinearActor"
    )
    actor_avatar_url: "NotificationGraphQLField" = NotificationGraphQLField(
        "actorAvatarUrl"
    )
    actor_initials: "NotificationGraphQLField" = NotificationGraphQLField(
        "actorInitials"
    )
    actor_avatar_color: "NotificationGraphQLField" = NotificationGraphQLField(
        "actorAvatarColor"
    )
    issue_status_type: "NotificationGraphQLField" = NotificationGraphQLField(
        "issueStatusType"
    )
    project_update_health: "NotificationGraphQLField" = NotificationGraphQLField(
        "projectUpdateHealth"
    )
    grouping_key: "NotificationGraphQLField" = NotificationGraphQLField("groupingKey")

    @classmethod
    def bot_actor(cls) -> "ActorBotFields":
        return ActorBotFields("bot_actor")

    def fields(
        self,
        *subfields: Union[
            NotificationGraphQLField,
            "ActorBotFields",
            "ExternalUserFields",
            "UserFields",
        ]
    ) -> "NotificationInterface":
        """Subfields should come from the NotificationInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationInterface":
        self._alias = alias
        return self

    def on(self, type_name: str, *subfields: GraphQLField) -> "NotificationInterface":
        self._inline_fragments[type_name] = subfields
        return self


class NotificationArchivePayloadFields(GraphQLField):
    last_sync_id: "NotificationArchivePayloadGraphQLField" = (
        NotificationArchivePayloadGraphQLField("lastSyncId")
    )
    success: "NotificationArchivePayloadGraphQLField" = (
        NotificationArchivePayloadGraphQLField("success")
    )

    @classmethod
    def entity(cls) -> "NotificationInterface":
        return NotificationInterface("entity")

    def fields(
        self,
        *subfields: Union[
            NotificationArchivePayloadGraphQLField, "NotificationInterface"
        ]
    ) -> "NotificationArchivePayloadFields":
        """Subfields should come from the NotificationArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationArchivePayloadFields":
        self._alias = alias
        return self


class NotificationBatchActionPayloadFields(GraphQLField):
    last_sync_id: "NotificationBatchActionPayloadGraphQLField" = (
        NotificationBatchActionPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def notifications(cls) -> "NotificationInterface":
        return NotificationInterface("notifications")

    success: "NotificationBatchActionPayloadGraphQLField" = (
        NotificationBatchActionPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            NotificationBatchActionPayloadGraphQLField, "NotificationInterface"
        ]
    ) -> "NotificationBatchActionPayloadFields":
        """Subfields should come from the NotificationBatchActionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationBatchActionPayloadFields":
        self._alias = alias
        return self


class NotificationConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "NotificationEdgeFields":
        return NotificationEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "NotificationInterface":
        return NotificationInterface("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            NotificationConnectionGraphQLField,
            "NotificationEdgeFields",
            "NotificationInterface",
            "PageInfoFields",
        ]
    ) -> "NotificationConnectionFields":
        """Subfields should come from the NotificationConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationConnectionFields":
        self._alias = alias
        return self


class NotificationDeliveryPreferencesFields(GraphQLField):
    @classmethod
    def mobile(cls) -> "NotificationDeliveryPreferencesChannelFields":
        return NotificationDeliveryPreferencesChannelFields("mobile")

    def fields(
        self,
        *subfields: Union[
            NotificationDeliveryPreferencesGraphQLField,
            "NotificationDeliveryPreferencesChannelFields",
        ]
    ) -> "NotificationDeliveryPreferencesFields":
        """Subfields should come from the NotificationDeliveryPreferencesFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationDeliveryPreferencesFields":
        self._alias = alias
        return self


class NotificationDeliveryPreferencesChannelFields(GraphQLField):
    notifications_disabled: "NotificationDeliveryPreferencesChannelGraphQLField" = (
        NotificationDeliveryPreferencesChannelGraphQLField("notificationsDisabled")
    )

    @classmethod
    def schedule(cls) -> "NotificationDeliveryPreferencesScheduleFields":
        return NotificationDeliveryPreferencesScheduleFields("schedule")

    def fields(
        self,
        *subfields: Union[
            NotificationDeliveryPreferencesChannelGraphQLField,
            "NotificationDeliveryPreferencesScheduleFields",
        ]
    ) -> "NotificationDeliveryPreferencesChannelFields":
        """Subfields should come from the NotificationDeliveryPreferencesChannelFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationDeliveryPreferencesChannelFields":
        self._alias = alias
        return self


class NotificationDeliveryPreferencesDayFields(GraphQLField):
    start: "NotificationDeliveryPreferencesDayGraphQLField" = (
        NotificationDeliveryPreferencesDayGraphQLField("start")
    )
    end: "NotificationDeliveryPreferencesDayGraphQLField" = (
        NotificationDeliveryPreferencesDayGraphQLField("end")
    )

    def fields(
        self, *subfields: NotificationDeliveryPreferencesDayGraphQLField
    ) -> "NotificationDeliveryPreferencesDayFields":
        """Subfields should come from the NotificationDeliveryPreferencesDayFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationDeliveryPreferencesDayFields":
        self._alias = alias
        return self


class NotificationDeliveryPreferencesScheduleFields(GraphQLField):
    disabled: "NotificationDeliveryPreferencesScheduleGraphQLField" = (
        NotificationDeliveryPreferencesScheduleGraphQLField("disabled")
    )

    @classmethod
    def sunday(cls) -> "NotificationDeliveryPreferencesDayFields":
        return NotificationDeliveryPreferencesDayFields("sunday")

    @classmethod
    def monday(cls) -> "NotificationDeliveryPreferencesDayFields":
        return NotificationDeliveryPreferencesDayFields("monday")

    @classmethod
    def tuesday(cls) -> "NotificationDeliveryPreferencesDayFields":
        return NotificationDeliveryPreferencesDayFields("tuesday")

    @classmethod
    def wednesday(cls) -> "NotificationDeliveryPreferencesDayFields":
        return NotificationDeliveryPreferencesDayFields("wednesday")

    @classmethod
    def thursday(cls) -> "NotificationDeliveryPreferencesDayFields":
        return NotificationDeliveryPreferencesDayFields("thursday")

    @classmethod
    def friday(cls) -> "NotificationDeliveryPreferencesDayFields":
        return NotificationDeliveryPreferencesDayFields("friday")

    @classmethod
    def saturday(cls) -> "NotificationDeliveryPreferencesDayFields":
        return NotificationDeliveryPreferencesDayFields("saturday")

    def fields(
        self,
        *subfields: Union[
            NotificationDeliveryPreferencesScheduleGraphQLField,
            "NotificationDeliveryPreferencesDayFields",
        ]
    ) -> "NotificationDeliveryPreferencesScheduleFields":
        """Subfields should come from the NotificationDeliveryPreferencesScheduleFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationDeliveryPreferencesScheduleFields":
        self._alias = alias
        return self


class NotificationEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "NotificationInterface":
        return NotificationInterface("node")

    cursor: "NotificationEdgeGraphQLField" = NotificationEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[NotificationEdgeGraphQLField, "NotificationInterface"]
    ) -> "NotificationEdgeFields":
        """Subfields should come from the NotificationEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationEdgeFields":
        self._alias = alias
        return self


class NotificationPayloadFields(GraphQLField):
    last_sync_id: "NotificationPayloadGraphQLField" = NotificationPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def notification(cls) -> "NotificationInterface":
        return NotificationInterface("notification")

    success: "NotificationPayloadGraphQLField" = NotificationPayloadGraphQLField(
        "success"
    )

    def fields(
        self,
        *subfields: Union[NotificationPayloadGraphQLField, "NotificationInterface"]
    ) -> "NotificationPayloadFields":
        """Subfields should come from the NotificationPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationPayloadFields":
        self._alias = alias
        return self


class NotificationSubscriptionInterface(GraphQLField):
    id: "NotificationSubscriptionGraphQLField" = NotificationSubscriptionGraphQLField(
        "id"
    )
    created_at: "NotificationSubscriptionGraphQLField" = (
        NotificationSubscriptionGraphQLField("createdAt")
    )
    updated_at: "NotificationSubscriptionGraphQLField" = (
        NotificationSubscriptionGraphQLField("updatedAt")
    )
    archived_at: "NotificationSubscriptionGraphQLField" = (
        NotificationSubscriptionGraphQLField("archivedAt")
    )

    @classmethod
    def subscriber(cls) -> "UserFields":
        return UserFields("subscriber")

    @classmethod
    def custom_view(cls) -> "CustomViewFields":
        return CustomViewFields("custom_view")

    @classmethod
    def cycle(cls) -> "CycleFields":
        return CycleFields("cycle")

    @classmethod
    def label(cls) -> "IssueLabelFields":
        return IssueLabelFields("label")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def initiative(cls) -> "InitiativeFields":
        return InitiativeFields("initiative")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    context_view_type: "NotificationSubscriptionGraphQLField" = (
        NotificationSubscriptionGraphQLField("contextViewType")
    )
    user_context_view_type: "NotificationSubscriptionGraphQLField" = (
        NotificationSubscriptionGraphQLField("userContextViewType")
    )
    active: "NotificationSubscriptionGraphQLField" = (
        NotificationSubscriptionGraphQLField("active")
    )

    def fields(
        self,
        *subfields: Union[
            NotificationSubscriptionGraphQLField,
            "CustomViewFields",
            "CycleFields",
            "InitiativeFields",
            "IssueLabelFields",
            "ProjectFields",
            "TeamFields",
            "UserFields",
        ]
    ) -> "NotificationSubscriptionInterface":
        """Subfields should come from the NotificationSubscriptionInterface class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationSubscriptionInterface":
        self._alias = alias
        return self

    def on(
        self, type_name: str, *subfields: GraphQLField
    ) -> "NotificationSubscriptionInterface":
        self._inline_fragments[type_name] = subfields
        return self


class NotificationSubscriptionConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "NotificationSubscriptionEdgeFields":
        return NotificationSubscriptionEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "NotificationSubscriptionInterface":
        return NotificationSubscriptionInterface("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            NotificationSubscriptionConnectionGraphQLField,
            "NotificationSubscriptionEdgeFields",
            "NotificationSubscriptionInterface",
            "PageInfoFields",
        ]
    ) -> "NotificationSubscriptionConnectionFields":
        """Subfields should come from the NotificationSubscriptionConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationSubscriptionConnectionFields":
        self._alias = alias
        return self


class NotificationSubscriptionEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "NotificationSubscriptionInterface":
        return NotificationSubscriptionInterface("node")

    cursor: "NotificationSubscriptionEdgeGraphQLField" = (
        NotificationSubscriptionEdgeGraphQLField("cursor")
    )

    def fields(
        self,
        *subfields: Union[
            NotificationSubscriptionEdgeGraphQLField,
            "NotificationSubscriptionInterface",
        ]
    ) -> "NotificationSubscriptionEdgeFields":
        """Subfields should come from the NotificationSubscriptionEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationSubscriptionEdgeFields":
        self._alias = alias
        return self


class NotificationSubscriptionPayloadFields(GraphQLField):
    last_sync_id: "NotificationSubscriptionPayloadGraphQLField" = (
        NotificationSubscriptionPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def notification_subscription(cls) -> "NotificationSubscriptionInterface":
        return NotificationSubscriptionInterface("notification_subscription")

    success: "NotificationSubscriptionPayloadGraphQLField" = (
        NotificationSubscriptionPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            NotificationSubscriptionPayloadGraphQLField,
            "NotificationSubscriptionInterface",
        ]
    ) -> "NotificationSubscriptionPayloadFields":
        """Subfields should come from the NotificationSubscriptionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "NotificationSubscriptionPayloadFields":
        self._alias = alias
        return self


class OrganizationFields(GraphQLField):
    id: "OrganizationGraphQLField" = OrganizationGraphQLField("id")
    created_at: "OrganizationGraphQLField" = OrganizationGraphQLField("createdAt")
    updated_at: "OrganizationGraphQLField" = OrganizationGraphQLField("updatedAt")
    archived_at: "OrganizationGraphQLField" = OrganizationGraphQLField("archivedAt")
    name: "OrganizationGraphQLField" = OrganizationGraphQLField("name")
    url_key: "OrganizationGraphQLField" = OrganizationGraphQLField("urlKey")
    logo_url: "OrganizationGraphQLField" = OrganizationGraphQLField("logoUrl")
    period_upload_volume: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "periodUploadVolume"
    )
    git_branch_format: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "gitBranchFormat"
    )
    git_linkback_messages_enabled: "OrganizationGraphQLField" = (
        OrganizationGraphQLField("gitLinkbackMessagesEnabled")
    )
    git_public_linkback_messages_enabled: "OrganizationGraphQLField" = (
        OrganizationGraphQLField("gitPublicLinkbackMessagesEnabled")
    )
    roadmap_enabled: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "roadmapEnabled"
    )
    project_update_reminder_frequency_in_weeks: "OrganizationGraphQLField" = (
        OrganizationGraphQLField("projectUpdateReminderFrequencyInWeeks")
    )
    project_update_reminders_day: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "projectUpdateRemindersDay"
    )
    project_update_reminders_hour: "OrganizationGraphQLField" = (
        OrganizationGraphQLField("projectUpdateRemindersHour")
    )
    fiscal_year_start_month: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "fiscalYearStartMonth"
    )
    saml_enabled: "OrganizationGraphQLField" = OrganizationGraphQLField("samlEnabled")
    saml_settings: "OrganizationGraphQLField" = OrganizationGraphQLField("samlSettings")
    scim_enabled: "OrganizationGraphQLField" = OrganizationGraphQLField("scimEnabled")
    allowed_auth_services: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "allowedAuthServices"
    )

    @classmethod
    def ip_restrictions(cls) -> "OrganizationIpRestrictionFields":
        return OrganizationIpRestrictionFields("ip_restrictions")

    deletion_requested_at: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "deletionRequestedAt"
    )
    trial_ends_at: "OrganizationGraphQLField" = OrganizationGraphQLField("trialEndsAt")
    previous_url_keys: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "previousUrlKeys"
    )
    allow_members_to_invite: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "allowMembersToInvite"
    )
    theme_settings: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "themeSettings"
    )
    release_channel: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "releaseChannel"
    )
    sla_day_count: "OrganizationGraphQLField" = OrganizationGraphQLField("slaDayCount")

    @classmethod
    def project_statuses(cls) -> "ProjectStatusFields":
        return ProjectStatusFields("project_statuses")

    project_updates_reminder_frequency: "OrganizationGraphQLField" = (
        OrganizationGraphQLField("projectUpdatesReminderFrequency")
    )

    @classmethod
    def users(
        cls,
        *,
        include_disabled: Optional[bool] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "UserConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
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
        return UserConnectionFields("users", arguments=cleared_arguments)

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
    ) -> "TeamConnectionFields":
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
        return TeamConnectionFields("teams", arguments=cleared_arguments)

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
    ) -> "IntegrationConnectionFields":
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
        return IntegrationConnectionFields("integrations", arguments=cleared_arguments)

    @classmethod
    def subscription(cls) -> "PaidSubscriptionFields":
        return PaidSubscriptionFields("subscription")

    user_count: "OrganizationGraphQLField" = OrganizationGraphQLField("userCount")
    created_issue_count: "OrganizationGraphQLField" = OrganizationGraphQLField(
        "createdIssueCount"
    )

    @classmethod
    def templates(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "TemplateConnectionFields":
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
        return TemplateConnectionFields("templates", arguments=cleared_arguments)

    @classmethod
    def labels(
        cls,
        *,
        filter: Optional[IssueLabelFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueLabelConnectionFields":
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
        return IssueLabelConnectionFields("labels", arguments=cleared_arguments)

    def fields(
        self,
        *subfields: Union[
            OrganizationGraphQLField,
            "IntegrationConnectionFields",
            "IssueLabelConnectionFields",
            "OrganizationIpRestrictionFields",
            "PaidSubscriptionFields",
            "ProjectStatusFields",
            "TeamConnectionFields",
            "TemplateConnectionFields",
            "UserConnectionFields",
        ]
    ) -> "OrganizationFields":
        """Subfields should come from the OrganizationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationFields":
        self._alias = alias
        return self


class OrganizationAcceptedOrExpiredInviteDetailsPayloadFields(GraphQLField):
    status: "OrganizationAcceptedOrExpiredInviteDetailsPayloadGraphQLField" = (
        OrganizationAcceptedOrExpiredInviteDetailsPayloadGraphQLField("status")
    )

    def fields(
        self, *subfields: OrganizationAcceptedOrExpiredInviteDetailsPayloadGraphQLField
    ) -> "OrganizationAcceptedOrExpiredInviteDetailsPayloadFields":
        """Subfields should come from the OrganizationAcceptedOrExpiredInviteDetailsPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(
        self, alias: str
    ) -> "OrganizationAcceptedOrExpiredInviteDetailsPayloadFields":
        self._alias = alias
        return self


class OrganizationCancelDeletePayloadFields(GraphQLField):
    success: "OrganizationCancelDeletePayloadGraphQLField" = (
        OrganizationCancelDeletePayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: OrganizationCancelDeletePayloadGraphQLField
    ) -> "OrganizationCancelDeletePayloadFields":
        """Subfields should come from the OrganizationCancelDeletePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationCancelDeletePayloadFields":
        self._alias = alias
        return self


class OrganizationDeletePayloadFields(GraphQLField):
    success: "OrganizationDeletePayloadGraphQLField" = (
        OrganizationDeletePayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: OrganizationDeletePayloadGraphQLField
    ) -> "OrganizationDeletePayloadFields":
        """Subfields should come from the OrganizationDeletePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationDeletePayloadFields":
        self._alias = alias
        return self


class OrganizationDomainFields(GraphQLField):
    id: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField("id")
    created_at: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField(
        "createdAt"
    )
    updated_at: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField(
        "updatedAt"
    )
    archived_at: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField(
        "archivedAt"
    )
    name: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField("name")
    verified: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField(
        "verified"
    )
    verification_email: "OrganizationDomainGraphQLField" = (
        OrganizationDomainGraphQLField("verificationEmail")
    )

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    auth_type: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField(
        "authType"
    )
    claimed: "OrganizationDomainGraphQLField" = OrganizationDomainGraphQLField(
        "claimed"
    )
    disable_organization_creation: "OrganizationDomainGraphQLField" = (
        OrganizationDomainGraphQLField("disableOrganizationCreation")
    )

    def fields(
        self, *subfields: Union[OrganizationDomainGraphQLField, "UserFields"]
    ) -> "OrganizationDomainFields":
        """Subfields should come from the OrganizationDomainFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationDomainFields":
        self._alias = alias
        return self


class OrganizationDomainClaimPayloadFields(GraphQLField):
    verification_string: "OrganizationDomainClaimPayloadGraphQLField" = (
        OrganizationDomainClaimPayloadGraphQLField("verificationString")
    )

    def fields(
        self, *subfields: OrganizationDomainClaimPayloadGraphQLField
    ) -> "OrganizationDomainClaimPayloadFields":
        """Subfields should come from the OrganizationDomainClaimPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationDomainClaimPayloadFields":
        self._alias = alias
        return self


class OrganizationDomainPayloadFields(GraphQLField):
    last_sync_id: "OrganizationDomainPayloadGraphQLField" = (
        OrganizationDomainPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def organization_domain(cls) -> "OrganizationDomainFields":
        return OrganizationDomainFields("organization_domain")

    success: "OrganizationDomainPayloadGraphQLField" = (
        OrganizationDomainPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            OrganizationDomainPayloadGraphQLField, "OrganizationDomainFields"
        ]
    ) -> "OrganizationDomainPayloadFields":
        """Subfields should come from the OrganizationDomainPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationDomainPayloadFields":
        self._alias = alias
        return self


class OrganizationDomainSimplePayloadFields(GraphQLField):
    success: "OrganizationDomainSimplePayloadGraphQLField" = (
        OrganizationDomainSimplePayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: OrganizationDomainSimplePayloadGraphQLField
    ) -> "OrganizationDomainSimplePayloadFields":
        """Subfields should come from the OrganizationDomainSimplePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationDomainSimplePayloadFields":
        self._alias = alias
        return self


class OrganizationExistsPayloadFields(GraphQLField):
    success: "OrganizationExistsPayloadGraphQLField" = (
        OrganizationExistsPayloadGraphQLField("success")
    )
    exists: "OrganizationExistsPayloadGraphQLField" = (
        OrganizationExistsPayloadGraphQLField("exists")
    )

    def fields(
        self, *subfields: OrganizationExistsPayloadGraphQLField
    ) -> "OrganizationExistsPayloadFields":
        """Subfields should come from the OrganizationExistsPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationExistsPayloadFields":
        self._alias = alias
        return self


class OrganizationInviteFields(GraphQLField):
    id: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField("id")
    created_at: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField(
        "createdAt"
    )
    updated_at: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField(
        "updatedAt"
    )
    archived_at: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField(
        "archivedAt"
    )
    email: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField("email")
    role: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField("role")
    external: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField(
        "external"
    )
    accepted_at: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField(
        "acceptedAt"
    )
    expires_at: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField(
        "expiresAt"
    )
    metadata: "OrganizationInviteGraphQLField" = OrganizationInviteGraphQLField(
        "metadata"
    )

    @classmethod
    def inviter(cls) -> "UserFields":
        return UserFields("inviter")

    @classmethod
    def invitee(cls) -> "UserFields":
        return UserFields("invitee")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    def fields(
        self,
        *subfields: Union[
            OrganizationInviteGraphQLField, "OrganizationFields", "UserFields"
        ]
    ) -> "OrganizationInviteFields":
        """Subfields should come from the OrganizationInviteFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationInviteFields":
        self._alias = alias
        return self


class OrganizationInviteConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "OrganizationInviteEdgeFields":
        return OrganizationInviteEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "OrganizationInviteFields":
        return OrganizationInviteFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            OrganizationInviteConnectionGraphQLField,
            "OrganizationInviteEdgeFields",
            "OrganizationInviteFields",
            "PageInfoFields",
        ]
    ) -> "OrganizationInviteConnectionFields":
        """Subfields should come from the OrganizationInviteConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationInviteConnectionFields":
        self._alias = alias
        return self


class OrganizationInviteEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "OrganizationInviteFields":
        return OrganizationInviteFields("node")

    cursor: "OrganizationInviteEdgeGraphQLField" = OrganizationInviteEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[
            OrganizationInviteEdgeGraphQLField, "OrganizationInviteFields"
        ]
    ) -> "OrganizationInviteEdgeFields":
        """Subfields should come from the OrganizationInviteEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationInviteEdgeFields":
        self._alias = alias
        return self


class OrganizationInviteFullDetailsPayloadFields(GraphQLField):
    status: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("status")
    )
    inviter: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("inviter")
    )
    email: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("email")
    )
    role: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("role")
    )
    created_at: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("createdAt")
    )
    organization_name: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("organizationName")
    )
    organization_id: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("organizationId")
    )
    organization_logo_url: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("organizationLogoUrl")
    )
    accepted: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("accepted")
    )
    expired: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("expired")
    )
    allowed_auth_services: "OrganizationInviteFullDetailsPayloadGraphQLField" = (
        OrganizationInviteFullDetailsPayloadGraphQLField("allowedAuthServices")
    )

    def fields(
        self, *subfields: OrganizationInviteFullDetailsPayloadGraphQLField
    ) -> "OrganizationInviteFullDetailsPayloadFields":
        """Subfields should come from the OrganizationInviteFullDetailsPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationInviteFullDetailsPayloadFields":
        self._alias = alias
        return self


class OrganizationInvitePayloadFields(GraphQLField):
    last_sync_id: "OrganizationInvitePayloadGraphQLField" = (
        OrganizationInvitePayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def organization_invite(cls) -> "OrganizationInviteFields":
        return OrganizationInviteFields("organization_invite")

    success: "OrganizationInvitePayloadGraphQLField" = (
        OrganizationInvitePayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            OrganizationInvitePayloadGraphQLField, "OrganizationInviteFields"
        ]
    ) -> "OrganizationInvitePayloadFields":
        """Subfields should come from the OrganizationInvitePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationInvitePayloadFields":
        self._alias = alias
        return self


class OrganizationIpRestrictionFields(GraphQLField):
    range: "OrganizationIpRestrictionGraphQLField" = (
        OrganizationIpRestrictionGraphQLField("range")
    )
    type: "OrganizationIpRestrictionGraphQLField" = (
        OrganizationIpRestrictionGraphQLField("type")
    )
    description: "OrganizationIpRestrictionGraphQLField" = (
        OrganizationIpRestrictionGraphQLField("description")
    )
    enabled: "OrganizationIpRestrictionGraphQLField" = (
        OrganizationIpRestrictionGraphQLField("enabled")
    )

    def fields(
        self, *subfields: OrganizationIpRestrictionGraphQLField
    ) -> "OrganizationIpRestrictionFields":
        """Subfields should come from the OrganizationIpRestrictionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationIpRestrictionFields":
        self._alias = alias
        return self


class OrganizationMetaFields(GraphQLField):
    region: "OrganizationMetaGraphQLField" = OrganizationMetaGraphQLField("region")
    allowed_auth_services: "OrganizationMetaGraphQLField" = (
        OrganizationMetaGraphQLField("allowedAuthServices")
    )

    def fields(
        self, *subfields: OrganizationMetaGraphQLField
    ) -> "OrganizationMetaFields":
        """Subfields should come from the OrganizationMetaFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationMetaFields":
        self._alias = alias
        return self


class OrganizationPayloadFields(GraphQLField):
    last_sync_id: "OrganizationPayloadGraphQLField" = OrganizationPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    success: "OrganizationPayloadGraphQLField" = OrganizationPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[OrganizationPayloadGraphQLField, "OrganizationFields"]
    ) -> "OrganizationPayloadFields":
        """Subfields should come from the OrganizationPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationPayloadFields":
        self._alias = alias
        return self


class OrganizationStartTrialPayloadFields(GraphQLField):
    success: "OrganizationStartTrialPayloadGraphQLField" = (
        OrganizationStartTrialPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: OrganizationStartTrialPayloadGraphQLField
    ) -> "OrganizationStartTrialPayloadFields":
        """Subfields should come from the OrganizationStartTrialPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "OrganizationStartTrialPayloadFields":
        self._alias = alias
        return self


class PageInfoFields(GraphQLField):
    has_previous_page: "PageInfoGraphQLField" = PageInfoGraphQLField("hasPreviousPage")
    has_next_page: "PageInfoGraphQLField" = PageInfoGraphQLField("hasNextPage")
    start_cursor: "PageInfoGraphQLField" = PageInfoGraphQLField("startCursor")
    end_cursor: "PageInfoGraphQLField" = PageInfoGraphQLField("endCursor")

    def fields(self, *subfields: PageInfoGraphQLField) -> "PageInfoFields":
        """Subfields should come from the PageInfoFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PageInfoFields":
        self._alias = alias
        return self


class PaidSubscriptionFields(GraphQLField):
    id: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField("id")
    created_at: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "createdAt"
    )
    updated_at: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "updatedAt"
    )
    archived_at: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "archivedAt"
    )
    type: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField("type")
    seats: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField("seats")
    seats_minimum: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "seatsMinimum"
    )
    seats_maximum: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "seatsMaximum"
    )

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    collection_method: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "collectionMethod"
    )
    canceled_at: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "canceledAt"
    )
    pending_change_type: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "pendingChangeType"
    )
    next_billing_at: "PaidSubscriptionGraphQLField" = PaidSubscriptionGraphQLField(
        "nextBillingAt"
    )

    def fields(
        self,
        *subfields: Union[
            PaidSubscriptionGraphQLField, "OrganizationFields", "UserFields"
        ]
    ) -> "PaidSubscriptionFields":
        """Subfields should come from the PaidSubscriptionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PaidSubscriptionFields":
        self._alias = alias
        return self


class PasskeyLoginStartResponseFields(GraphQLField):
    success: "PasskeyLoginStartResponseGraphQLField" = (
        PasskeyLoginStartResponseGraphQLField("success")
    )
    options: "PasskeyLoginStartResponseGraphQLField" = (
        PasskeyLoginStartResponseGraphQLField("options")
    )

    def fields(
        self, *subfields: PasskeyLoginStartResponseGraphQLField
    ) -> "PasskeyLoginStartResponseFields":
        """Subfields should come from the PasskeyLoginStartResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PasskeyLoginStartResponseFields":
        self._alias = alias
        return self


class ProjectFields(GraphQLField):
    id: "ProjectGraphQLField" = ProjectGraphQLField("id")
    created_at: "ProjectGraphQLField" = ProjectGraphQLField("createdAt")
    updated_at: "ProjectGraphQLField" = ProjectGraphQLField("updatedAt")
    archived_at: "ProjectGraphQLField" = ProjectGraphQLField("archivedAt")
    name: "ProjectGraphQLField" = ProjectGraphQLField("name")
    description: "ProjectGraphQLField" = ProjectGraphQLField("description")
    slug_id: "ProjectGraphQLField" = ProjectGraphQLField("slugId")
    icon: "ProjectGraphQLField" = ProjectGraphQLField("icon")
    color: "ProjectGraphQLField" = ProjectGraphQLField("color")

    @classmethod
    def status(cls) -> "ProjectStatusFields":
        return ProjectStatusFields("status")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def lead(cls) -> "UserFields":
        return UserFields("lead")

    project_update_reminders_paused_until_at: "ProjectGraphQLField" = (
        ProjectGraphQLField("projectUpdateRemindersPausedUntilAt")
    )
    start_date: "ProjectGraphQLField" = ProjectGraphQLField("startDate")
    start_date_resolution: "ProjectGraphQLField" = ProjectGraphQLField(
        "startDateResolution"
    )
    target_date: "ProjectGraphQLField" = ProjectGraphQLField("targetDate")
    target_date_resolution: "ProjectGraphQLField" = ProjectGraphQLField(
        "targetDateResolution"
    )
    started_at: "ProjectGraphQLField" = ProjectGraphQLField("startedAt")
    completed_at: "ProjectGraphQLField" = ProjectGraphQLField("completedAt")
    canceled_at: "ProjectGraphQLField" = ProjectGraphQLField("canceledAt")
    auto_archived_at: "ProjectGraphQLField" = ProjectGraphQLField("autoArchivedAt")
    trashed: "ProjectGraphQLField" = ProjectGraphQLField("trashed")
    sort_order: "ProjectGraphQLField" = ProjectGraphQLField("sortOrder")
    priority_sort_order: "ProjectGraphQLField" = ProjectGraphQLField(
        "prioritySortOrder"
    )

    @classmethod
    def converted_from_issue(cls) -> "IssueFields":
        return IssueFields("converted_from_issue")

    @classmethod
    def last_applied_template(cls) -> "TemplateFields":
        return TemplateFields("last_applied_template")

    priority: "ProjectGraphQLField" = ProjectGraphQLField("priority")
    issue_count_history: "ProjectGraphQLField" = ProjectGraphQLField(
        "issueCountHistory"
    )
    completed_issue_count_history: "ProjectGraphQLField" = ProjectGraphQLField(
        "completedIssueCountHistory"
    )
    scope_history: "ProjectGraphQLField" = ProjectGraphQLField("scopeHistory")
    completed_scope_history: "ProjectGraphQLField" = ProjectGraphQLField(
        "completedScopeHistory"
    )
    in_progress_scope_history: "ProjectGraphQLField" = ProjectGraphQLField(
        "inProgressScopeHistory"
    )
    progress_history: "ProjectGraphQLField" = ProjectGraphQLField("progressHistory")
    slack_new_issue: "ProjectGraphQLField" = ProjectGraphQLField("slackNewIssue")
    slack_issue_comments: "ProjectGraphQLField" = ProjectGraphQLField(
        "slackIssueComments"
    )
    slack_issue_statuses: "ProjectGraphQLField" = ProjectGraphQLField(
        "slackIssueStatuses"
    )

    @classmethod
    def favorite(cls) -> "FavoriteFields":
        return FavoriteFields("favorite")

    url: "ProjectGraphQLField" = ProjectGraphQLField("url")

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
    ) -> "TeamConnectionFields":
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
        return TeamConnectionFields("teams", arguments=cleared_arguments)

    @classmethod
    def members(
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
    ) -> "UserConnectionFields":
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
        return UserConnectionFields("members", arguments=cleared_arguments)

    @classmethod
    def project_updates(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "ProjectUpdateConnectionFields":
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
        return ProjectUpdateConnectionFields(
            "project_updates", arguments=cleared_arguments
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
    ) -> "DocumentConnectionFields":
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
        return DocumentConnectionFields("documents", arguments=cleared_arguments)

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
    ) -> "ProjectMilestoneConnectionFields":
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
            "project_milestones", arguments=cleared_arguments
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
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    @classmethod
    def links(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "ProjectLinkConnectionFields":
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
        return ProjectLinkConnectionFields("links", arguments=cleared_arguments)

    @classmethod
    def external_links(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "EntityExternalLinkConnectionFields":
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
        return EntityExternalLinkConnectionFields(
            "external_links", arguments=cleared_arguments
        )

    progress: "ProjectGraphQLField" = ProjectGraphQLField("progress")
    health: "ProjectGraphQLField" = ProjectGraphQLField("health")
    scope: "ProjectGraphQLField" = ProjectGraphQLField("scope")

    @classmethod
    def integrations_settings(cls) -> "IntegrationsSettingsFields":
        return IntegrationsSettingsFields("integrations_settings")

    content: "ProjectGraphQLField" = ProjectGraphQLField("content")
    content_state: "ProjectGraphQLField" = ProjectGraphQLField("contentState")
    state: "ProjectGraphQLField" = ProjectGraphQLField("state")

    def fields(
        self,
        *subfields: Union[
            ProjectGraphQLField,
            "DocumentConnectionFields",
            "EntityExternalLinkConnectionFields",
            "FavoriteFields",
            "IntegrationsSettingsFields",
            "IssueConnectionFields",
            "IssueFields",
            "ProjectLinkConnectionFields",
            "ProjectMilestoneConnectionFields",
            "ProjectStatusFields",
            "ProjectUpdateConnectionFields",
            "TeamConnectionFields",
            "TemplateFields",
            "UserConnectionFields",
            "UserFields",
        ]
    ) -> "ProjectFields":
        """Subfields should come from the ProjectFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectFields":
        self._alias = alias
        return self


class ProjectArchivePayloadFields(GraphQLField):
    last_sync_id: "ProjectArchivePayloadGraphQLField" = (
        ProjectArchivePayloadGraphQLField("lastSyncId")
    )
    success: "ProjectArchivePayloadGraphQLField" = ProjectArchivePayloadGraphQLField(
        "success"
    )

    @classmethod
    def entity(cls) -> "ProjectFields":
        return ProjectFields("entity")

    def fields(
        self, *subfields: Union[ProjectArchivePayloadGraphQLField, "ProjectFields"]
    ) -> "ProjectArchivePayloadFields":
        """Subfields should come from the ProjectArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectArchivePayloadFields":
        self._alias = alias
        return self


class ProjectConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ProjectEdgeFields":
        return ProjectEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ProjectFields":
        return ProjectFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ProjectConnectionGraphQLField,
            "PageInfoFields",
            "ProjectEdgeFields",
            "ProjectFields",
        ]
    ) -> "ProjectConnectionFields":
        """Subfields should come from the ProjectConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectConnectionFields":
        self._alias = alias
        return self


class ProjectEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ProjectFields":
        return ProjectFields("node")

    cursor: "ProjectEdgeGraphQLField" = ProjectEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[ProjectEdgeGraphQLField, "ProjectFields"]
    ) -> "ProjectEdgeFields":
        """Subfields should come from the ProjectEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectEdgeFields":
        self._alias = alias
        return self


class ProjectFilterSuggestionPayloadFields(GraphQLField):
    filter: "ProjectFilterSuggestionPayloadGraphQLField" = (
        ProjectFilterSuggestionPayloadGraphQLField("filter")
    )

    def fields(
        self, *subfields: ProjectFilterSuggestionPayloadGraphQLField
    ) -> "ProjectFilterSuggestionPayloadFields":
        """Subfields should come from the ProjectFilterSuggestionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectFilterSuggestionPayloadFields":
        self._alias = alias
        return self


class ProjectLinkFields(GraphQLField):
    id: "ProjectLinkGraphQLField" = ProjectLinkGraphQLField("id")
    created_at: "ProjectLinkGraphQLField" = ProjectLinkGraphQLField("createdAt")
    updated_at: "ProjectLinkGraphQLField" = ProjectLinkGraphQLField("updatedAt")
    archived_at: "ProjectLinkGraphQLField" = ProjectLinkGraphQLField("archivedAt")
    url: "ProjectLinkGraphQLField" = ProjectLinkGraphQLField("url")
    label: "ProjectLinkGraphQLField" = ProjectLinkGraphQLField("label")
    sort_order: "ProjectLinkGraphQLField" = ProjectLinkGraphQLField("sortOrder")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    def fields(
        self, *subfields: Union[ProjectLinkGraphQLField, "ProjectFields", "UserFields"]
    ) -> "ProjectLinkFields":
        """Subfields should come from the ProjectLinkFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectLinkFields":
        self._alias = alias
        return self


class ProjectLinkConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ProjectLinkEdgeFields":
        return ProjectLinkEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ProjectLinkFields":
        return ProjectLinkFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ProjectLinkConnectionGraphQLField,
            "PageInfoFields",
            "ProjectLinkEdgeFields",
            "ProjectLinkFields",
        ]
    ) -> "ProjectLinkConnectionFields":
        """Subfields should come from the ProjectLinkConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectLinkConnectionFields":
        self._alias = alias
        return self


class ProjectLinkEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ProjectLinkFields":
        return ProjectLinkFields("node")

    cursor: "ProjectLinkEdgeGraphQLField" = ProjectLinkEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[ProjectLinkEdgeGraphQLField, "ProjectLinkFields"]
    ) -> "ProjectLinkEdgeFields":
        """Subfields should come from the ProjectLinkEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectLinkEdgeFields":
        self._alias = alias
        return self


class ProjectLinkPayloadFields(GraphQLField):
    last_sync_id: "ProjectLinkPayloadGraphQLField" = ProjectLinkPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def project_link(cls) -> "ProjectLinkFields":
        return ProjectLinkFields("project_link")

    success: "ProjectLinkPayloadGraphQLField" = ProjectLinkPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[ProjectLinkPayloadGraphQLField, "ProjectLinkFields"]
    ) -> "ProjectLinkPayloadFields":
        """Subfields should come from the ProjectLinkPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectLinkPayloadFields":
        self._alias = alias
        return self


class ProjectMilestoneFields(GraphQLField):
    id: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField("id")
    created_at: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "createdAt"
    )
    updated_at: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "updatedAt"
    )
    archived_at: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "archivedAt"
    )
    name: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField("name")
    target_date: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "targetDate"
    )

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    sort_order: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "sortOrder"
    )
    description: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "description"
    )
    description_data: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "descriptionData"
    )
    description_state: "ProjectMilestoneGraphQLField" = ProjectMilestoneGraphQLField(
        "descriptionState"
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
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    def fields(
        self,
        *subfields: Union[
            ProjectMilestoneGraphQLField, "IssueConnectionFields", "ProjectFields"
        ]
    ) -> "ProjectMilestoneFields":
        """Subfields should come from the ProjectMilestoneFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectMilestoneFields":
        self._alias = alias
        return self


class ProjectMilestoneConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ProjectMilestoneEdgeFields":
        return ProjectMilestoneEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ProjectMilestoneConnectionGraphQLField,
            "PageInfoFields",
            "ProjectMilestoneEdgeFields",
            "ProjectMilestoneFields",
        ]
    ) -> "ProjectMilestoneConnectionFields":
        """Subfields should come from the ProjectMilestoneConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectMilestoneConnectionFields":
        self._alias = alias
        return self


class ProjectMilestoneEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("node")

    cursor: "ProjectMilestoneEdgeGraphQLField" = ProjectMilestoneEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[ProjectMilestoneEdgeGraphQLField, "ProjectMilestoneFields"]
    ) -> "ProjectMilestoneEdgeFields":
        """Subfields should come from the ProjectMilestoneEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectMilestoneEdgeFields":
        self._alias = alias
        return self


class ProjectMilestonePayloadFields(GraphQLField):
    last_sync_id: "ProjectMilestonePayloadGraphQLField" = (
        ProjectMilestonePayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def project_milestone(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("project_milestone")

    success: "ProjectMilestonePayloadGraphQLField" = (
        ProjectMilestonePayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[ProjectMilestonePayloadGraphQLField, "ProjectMilestoneFields"]
    ) -> "ProjectMilestonePayloadFields":
        """Subfields should come from the ProjectMilestonePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectMilestonePayloadFields":
        self._alias = alias
        return self


class ProjectPayloadFields(GraphQLField):
    last_sync_id: "ProjectPayloadGraphQLField" = ProjectPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    success: "ProjectPayloadGraphQLField" = ProjectPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[ProjectPayloadGraphQLField, "ProjectFields"]
    ) -> "ProjectPayloadFields":
        """Subfields should come from the ProjectPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectPayloadFields":
        self._alias = alias
        return self


class ProjectRelationFields(GraphQLField):
    id: "ProjectRelationGraphQLField" = ProjectRelationGraphQLField("id")
    created_at: "ProjectRelationGraphQLField" = ProjectRelationGraphQLField("createdAt")
    updated_at: "ProjectRelationGraphQLField" = ProjectRelationGraphQLField("updatedAt")
    archived_at: "ProjectRelationGraphQLField" = ProjectRelationGraphQLField(
        "archivedAt"
    )
    type: "ProjectRelationGraphQLField" = ProjectRelationGraphQLField("type")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def project_milestone(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("project_milestone")

    anchor_type: "ProjectRelationGraphQLField" = ProjectRelationGraphQLField(
        "anchorType"
    )

    @classmethod
    def related_project(cls) -> "ProjectFields":
        return ProjectFields("related_project")

    @classmethod
    def related_project_milestone(cls) -> "ProjectMilestoneFields":
        return ProjectMilestoneFields("related_project_milestone")

    related_anchor_type: "ProjectRelationGraphQLField" = ProjectRelationGraphQLField(
        "relatedAnchorType"
    )

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    def fields(
        self,
        *subfields: Union[
            ProjectRelationGraphQLField,
            "ProjectFields",
            "ProjectMilestoneFields",
            "UserFields",
        ]
    ) -> "ProjectRelationFields":
        """Subfields should come from the ProjectRelationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectRelationFields":
        self._alias = alias
        return self


class ProjectRelationConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ProjectRelationEdgeFields":
        return ProjectRelationEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ProjectRelationFields":
        return ProjectRelationFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ProjectRelationConnectionGraphQLField,
            "PageInfoFields",
            "ProjectRelationEdgeFields",
            "ProjectRelationFields",
        ]
    ) -> "ProjectRelationConnectionFields":
        """Subfields should come from the ProjectRelationConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectRelationConnectionFields":
        self._alias = alias
        return self


class ProjectRelationEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ProjectRelationFields":
        return ProjectRelationFields("node")

    cursor: "ProjectRelationEdgeGraphQLField" = ProjectRelationEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[ProjectRelationEdgeGraphQLField, "ProjectRelationFields"]
    ) -> "ProjectRelationEdgeFields":
        """Subfields should come from the ProjectRelationEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectRelationEdgeFields":
        self._alias = alias
        return self


class ProjectRelationPayloadFields(GraphQLField):
    last_sync_id: "ProjectRelationPayloadGraphQLField" = (
        ProjectRelationPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def project_relation(cls) -> "ProjectRelationFields":
        return ProjectRelationFields("project_relation")

    success: "ProjectRelationPayloadGraphQLField" = ProjectRelationPayloadGraphQLField(
        "success"
    )

    def fields(
        self,
        *subfields: Union[ProjectRelationPayloadGraphQLField, "ProjectRelationFields"]
    ) -> "ProjectRelationPayloadFields":
        """Subfields should come from the ProjectRelationPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectRelationPayloadFields":
        self._alias = alias
        return self


class ProjectSearchPayloadFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ProjectSearchResultEdgeFields":
        return ProjectSearchResultEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ProjectSearchResultFields":
        return ProjectSearchResultFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    @classmethod
    def archive_payload(cls) -> "ArchiveResponseFields":
        return ArchiveResponseFields("archive_payload")

    total_count: "ProjectSearchPayloadGraphQLField" = ProjectSearchPayloadGraphQLField(
        "totalCount"
    )

    def fields(
        self,
        *subfields: Union[
            ProjectSearchPayloadGraphQLField,
            "ArchiveResponseFields",
            "PageInfoFields",
            "ProjectSearchResultEdgeFields",
            "ProjectSearchResultFields",
        ]
    ) -> "ProjectSearchPayloadFields":
        """Subfields should come from the ProjectSearchPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectSearchPayloadFields":
        self._alias = alias
        return self


class ProjectSearchResultFields(GraphQLField):
    id: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField("id")
    created_at: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "createdAt"
    )
    updated_at: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "updatedAt"
    )
    archived_at: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "archivedAt"
    )
    name: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField("name")
    description: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "description"
    )
    slug_id: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "slugId"
    )
    icon: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField("icon")
    color: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField("color")

    @classmethod
    def status(cls) -> "ProjectStatusFields":
        return ProjectStatusFields("status")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def lead(cls) -> "UserFields":
        return UserFields("lead")

    project_update_reminders_paused_until_at: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("projectUpdateRemindersPausedUntilAt")
    )
    start_date: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "startDate"
    )
    start_date_resolution: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("startDateResolution")
    )
    target_date: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "targetDate"
    )
    target_date_resolution: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("targetDateResolution")
    )
    started_at: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "startedAt"
    )
    completed_at: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "completedAt"
    )
    canceled_at: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "canceledAt"
    )
    auto_archived_at: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("autoArchivedAt")
    )
    trashed: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "trashed"
    )
    sort_order: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "sortOrder"
    )
    priority_sort_order: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("prioritySortOrder")
    )

    @classmethod
    def converted_from_issue(cls) -> "IssueFields":
        return IssueFields("converted_from_issue")

    @classmethod
    def last_applied_template(cls) -> "TemplateFields":
        return TemplateFields("last_applied_template")

    priority: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "priority"
    )
    issue_count_history: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("issueCountHistory")
    )
    completed_issue_count_history: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("completedIssueCountHistory")
    )
    scope_history: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "scopeHistory"
    )
    completed_scope_history: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("completedScopeHistory")
    )
    in_progress_scope_history: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("inProgressScopeHistory")
    )
    progress_history: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("progressHistory")
    )
    slack_new_issue: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("slackNewIssue")
    )
    slack_issue_comments: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("slackIssueComments")
    )
    slack_issue_statuses: "ProjectSearchResultGraphQLField" = (
        ProjectSearchResultGraphQLField("slackIssueStatuses")
    )

    @classmethod
    def favorite(cls) -> "FavoriteFields":
        return FavoriteFields("favorite")

    url: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField("url")

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
    ) -> "TeamConnectionFields":
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
        return TeamConnectionFields("teams", arguments=cleared_arguments)

    @classmethod
    def members(
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
    ) -> "UserConnectionFields":
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
        return UserConnectionFields("members", arguments=cleared_arguments)

    @classmethod
    def project_updates(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "ProjectUpdateConnectionFields":
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
        return ProjectUpdateConnectionFields(
            "project_updates", arguments=cleared_arguments
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
    ) -> "DocumentConnectionFields":
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
        return DocumentConnectionFields("documents", arguments=cleared_arguments)

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
    ) -> "ProjectMilestoneConnectionFields":
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
            "project_milestones", arguments=cleared_arguments
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
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    @classmethod
    def links(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "ProjectLinkConnectionFields":
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
        return ProjectLinkConnectionFields("links", arguments=cleared_arguments)

    @classmethod
    def external_links(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "EntityExternalLinkConnectionFields":
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
        return EntityExternalLinkConnectionFields(
            "external_links", arguments=cleared_arguments
        )

    progress: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "progress"
    )
    health: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "health"
    )
    scope: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField("scope")

    @classmethod
    def integrations_settings(cls) -> "IntegrationsSettingsFields":
        return IntegrationsSettingsFields("integrations_settings")

    content: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "content"
    )
    content_state: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "contentState"
    )
    state: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField("state")
    metadata: "ProjectSearchResultGraphQLField" = ProjectSearchResultGraphQLField(
        "metadata"
    )

    def fields(
        self,
        *subfields: Union[
            ProjectSearchResultGraphQLField,
            "DocumentConnectionFields",
            "EntityExternalLinkConnectionFields",
            "FavoriteFields",
            "IntegrationsSettingsFields",
            "IssueConnectionFields",
            "IssueFields",
            "ProjectLinkConnectionFields",
            "ProjectMilestoneConnectionFields",
            "ProjectStatusFields",
            "ProjectUpdateConnectionFields",
            "TeamConnectionFields",
            "TemplateFields",
            "UserConnectionFields",
            "UserFields",
        ]
    ) -> "ProjectSearchResultFields":
        """Subfields should come from the ProjectSearchResultFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectSearchResultFields":
        self._alias = alias
        return self


class ProjectSearchResultEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ProjectSearchResultFields":
        return ProjectSearchResultFields("node")

    cursor: "ProjectSearchResultEdgeGraphQLField" = ProjectSearchResultEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[
            ProjectSearchResultEdgeGraphQLField, "ProjectSearchResultFields"
        ]
    ) -> "ProjectSearchResultEdgeFields":
        """Subfields should come from the ProjectSearchResultEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectSearchResultEdgeFields":
        self._alias = alias
        return self


class ProjectStatusFields(GraphQLField):
    id: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("id")
    created_at: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("createdAt")
    updated_at: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("updatedAt")
    archived_at: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("archivedAt")
    name: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("name")
    color: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("color")
    description: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("description")
    position: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("position")
    type: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("type")
    indefinite: "ProjectStatusGraphQLField" = ProjectStatusGraphQLField("indefinite")

    def fields(self, *subfields: ProjectStatusGraphQLField) -> "ProjectStatusFields":
        """Subfields should come from the ProjectStatusFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectStatusFields":
        self._alias = alias
        return self


class ProjectUpdateFields(GraphQLField):
    id: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("id")
    created_at: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("createdAt")
    updated_at: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("updatedAt")
    archived_at: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("archivedAt")
    body: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("body")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    health: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("health")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    edited_at: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("editedAt")
    reaction_data: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField(
        "reactionData"
    )
    info_snapshot: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField(
        "infoSnapshot"
    )
    is_diff_hidden: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField(
        "isDiffHidden"
    )
    body_data: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("bodyData")
    slug_id: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("slugId")
    url: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("url")
    diff: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField("diff")
    diff_markdown: "ProjectUpdateGraphQLField" = ProjectUpdateGraphQLField(
        "diffMarkdown"
    )

    @classmethod
    def reactions(cls) -> "ReactionFields":
        return ReactionFields("reactions")

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
    ) -> "CommentConnectionFields":
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
        return CommentConnectionFields("comments", arguments=cleared_arguments)

    def fields(
        self,
        *subfields: Union[
            ProjectUpdateGraphQLField,
            "CommentConnectionFields",
            "ProjectFields",
            "ReactionFields",
            "UserFields",
        ]
    ) -> "ProjectUpdateFields":
        """Subfields should come from the ProjectUpdateFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateFields":
        self._alias = alias
        return self


class ProjectUpdateConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ProjectUpdateEdgeFields":
        return ProjectUpdateEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ProjectUpdateConnectionGraphQLField,
            "PageInfoFields",
            "ProjectUpdateEdgeFields",
            "ProjectUpdateFields",
        ]
    ) -> "ProjectUpdateConnectionFields":
        """Subfields should come from the ProjectUpdateConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateConnectionFields":
        self._alias = alias
        return self


class ProjectUpdateEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("node")

    cursor: "ProjectUpdateEdgeGraphQLField" = ProjectUpdateEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[ProjectUpdateEdgeGraphQLField, "ProjectUpdateFields"]
    ) -> "ProjectUpdateEdgeFields":
        """Subfields should come from the ProjectUpdateEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateEdgeFields":
        self._alias = alias
        return self


class ProjectUpdateInteractionFields(GraphQLField):
    id: "ProjectUpdateInteractionGraphQLField" = ProjectUpdateInteractionGraphQLField(
        "id"
    )
    created_at: "ProjectUpdateInteractionGraphQLField" = (
        ProjectUpdateInteractionGraphQLField("createdAt")
    )
    updated_at: "ProjectUpdateInteractionGraphQLField" = (
        ProjectUpdateInteractionGraphQLField("updatedAt")
    )
    archived_at: "ProjectUpdateInteractionGraphQLField" = (
        ProjectUpdateInteractionGraphQLField("archivedAt")
    )

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    @classmethod
    def project_update(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("project_update")

    read_at: "ProjectUpdateInteractionGraphQLField" = (
        ProjectUpdateInteractionGraphQLField("readAt")
    )

    def fields(
        self,
        *subfields: Union[
            ProjectUpdateInteractionGraphQLField, "ProjectUpdateFields", "UserFields"
        ]
    ) -> "ProjectUpdateInteractionFields":
        """Subfields should come from the ProjectUpdateInteractionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateInteractionFields":
        self._alias = alias
        return self


class ProjectUpdateInteractionConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "ProjectUpdateInteractionEdgeFields":
        return ProjectUpdateInteractionEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "ProjectUpdateInteractionFields":
        return ProjectUpdateInteractionFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            ProjectUpdateInteractionConnectionGraphQLField,
            "PageInfoFields",
            "ProjectUpdateInteractionEdgeFields",
            "ProjectUpdateInteractionFields",
        ]
    ) -> "ProjectUpdateInteractionConnectionFields":
        """Subfields should come from the ProjectUpdateInteractionConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateInteractionConnectionFields":
        self._alias = alias
        return self


class ProjectUpdateInteractionEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "ProjectUpdateInteractionFields":
        return ProjectUpdateInteractionFields("node")

    cursor: "ProjectUpdateInteractionEdgeGraphQLField" = (
        ProjectUpdateInteractionEdgeGraphQLField("cursor")
    )

    def fields(
        self,
        *subfields: Union[
            ProjectUpdateInteractionEdgeGraphQLField, "ProjectUpdateInteractionFields"
        ]
    ) -> "ProjectUpdateInteractionEdgeFields":
        """Subfields should come from the ProjectUpdateInteractionEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateInteractionEdgeFields":
        self._alias = alias
        return self


class ProjectUpdateInteractionPayloadFields(GraphQLField):
    last_sync_id: "ProjectUpdateInteractionPayloadGraphQLField" = (
        ProjectUpdateInteractionPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def project_update_interaction(cls) -> "ProjectUpdateInteractionFields":
        return ProjectUpdateInteractionFields("project_update_interaction")

    success: "ProjectUpdateInteractionPayloadGraphQLField" = (
        ProjectUpdateInteractionPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            ProjectUpdateInteractionPayloadGraphQLField,
            "ProjectUpdateInteractionFields",
        ]
    ) -> "ProjectUpdateInteractionPayloadFields":
        """Subfields should come from the ProjectUpdateInteractionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateInteractionPayloadFields":
        self._alias = alias
        return self


class ProjectUpdatePayloadFields(GraphQLField):
    last_sync_id: "ProjectUpdatePayloadGraphQLField" = ProjectUpdatePayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def project_update(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("project_update")

    success: "ProjectUpdatePayloadGraphQLField" = ProjectUpdatePayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[ProjectUpdatePayloadGraphQLField, "ProjectUpdateFields"]
    ) -> "ProjectUpdatePayloadFields":
        """Subfields should come from the ProjectUpdatePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdatePayloadFields":
        self._alias = alias
        return self


class ProjectUpdateReminderPayloadFields(GraphQLField):
    last_sync_id: "ProjectUpdateReminderPayloadGraphQLField" = (
        ProjectUpdateReminderPayloadGraphQLField("lastSyncId")
    )
    success: "ProjectUpdateReminderPayloadGraphQLField" = (
        ProjectUpdateReminderPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: ProjectUpdateReminderPayloadGraphQLField
    ) -> "ProjectUpdateReminderPayloadFields":
        """Subfields should come from the ProjectUpdateReminderPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateReminderPayloadFields":
        self._alias = alias
        return self


class ProjectUpdateWithInteractionPayloadFields(GraphQLField):
    last_sync_id: "ProjectUpdateWithInteractionPayloadGraphQLField" = (
        ProjectUpdateWithInteractionPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def project_update(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("project_update")

    success: "ProjectUpdateWithInteractionPayloadGraphQLField" = (
        ProjectUpdateWithInteractionPayloadGraphQLField("success")
    )

    @classmethod
    def interaction(cls) -> "ProjectUpdateInteractionFields":
        return ProjectUpdateInteractionFields("interaction")

    def fields(
        self,
        *subfields: Union[
            ProjectUpdateWithInteractionPayloadGraphQLField,
            "ProjectUpdateFields",
            "ProjectUpdateInteractionFields",
        ]
    ) -> "ProjectUpdateWithInteractionPayloadFields":
        """Subfields should come from the ProjectUpdateWithInteractionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ProjectUpdateWithInteractionPayloadFields":
        self._alias = alias
        return self


class PushSubscriptionFields(GraphQLField):
    id: "PushSubscriptionGraphQLField" = PushSubscriptionGraphQLField("id")
    created_at: "PushSubscriptionGraphQLField" = PushSubscriptionGraphQLField(
        "createdAt"
    )
    updated_at: "PushSubscriptionGraphQLField" = PushSubscriptionGraphQLField(
        "updatedAt"
    )
    archived_at: "PushSubscriptionGraphQLField" = PushSubscriptionGraphQLField(
        "archivedAt"
    )

    def fields(
        self, *subfields: PushSubscriptionGraphQLField
    ) -> "PushSubscriptionFields":
        """Subfields should come from the PushSubscriptionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PushSubscriptionFields":
        self._alias = alias
        return self


class PushSubscriptionPayloadFields(GraphQLField):
    last_sync_id: "PushSubscriptionPayloadGraphQLField" = (
        PushSubscriptionPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def entity(cls) -> "PushSubscriptionFields":
        return PushSubscriptionFields("entity")

    success: "PushSubscriptionPayloadGraphQLField" = (
        PushSubscriptionPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[PushSubscriptionPayloadGraphQLField, "PushSubscriptionFields"]
    ) -> "PushSubscriptionPayloadFields":
        """Subfields should come from the PushSubscriptionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PushSubscriptionPayloadFields":
        self._alias = alias
        return self


class PushSubscriptionTestPayloadFields(GraphQLField):
    success: "PushSubscriptionTestPayloadGraphQLField" = (
        PushSubscriptionTestPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: PushSubscriptionTestPayloadGraphQLField
    ) -> "PushSubscriptionTestPayloadFields":
        """Subfields should come from the PushSubscriptionTestPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "PushSubscriptionTestPayloadFields":
        self._alias = alias
        return self


class RateLimitPayloadFields(GraphQLField):
    identifier: "RateLimitPayloadGraphQLField" = RateLimitPayloadGraphQLField(
        "identifier"
    )
    kind: "RateLimitPayloadGraphQLField" = RateLimitPayloadGraphQLField("kind")

    @classmethod
    def limits(cls) -> "RateLimitResultPayloadFields":
        return RateLimitResultPayloadFields("limits")

    def fields(
        self,
        *subfields: Union[RateLimitPayloadGraphQLField, "RateLimitResultPayloadFields"]
    ) -> "RateLimitPayloadFields":
        """Subfields should come from the RateLimitPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RateLimitPayloadFields":
        self._alias = alias
        return self


class RateLimitResultPayloadFields(GraphQLField):
    type: "RateLimitResultPayloadGraphQLField" = RateLimitResultPayloadGraphQLField(
        "type"
    )
    requested_amount: "RateLimitResultPayloadGraphQLField" = (
        RateLimitResultPayloadGraphQLField("requestedAmount")
    )
    allowed_amount: "RateLimitResultPayloadGraphQLField" = (
        RateLimitResultPayloadGraphQLField("allowedAmount")
    )
    period: "RateLimitResultPayloadGraphQLField" = RateLimitResultPayloadGraphQLField(
        "period"
    )
    remaining_amount: "RateLimitResultPayloadGraphQLField" = (
        RateLimitResultPayloadGraphQLField("remainingAmount")
    )
    reset: "RateLimitResultPayloadGraphQLField" = RateLimitResultPayloadGraphQLField(
        "reset"
    )

    def fields(
        self, *subfields: RateLimitResultPayloadGraphQLField
    ) -> "RateLimitResultPayloadFields":
        """Subfields should come from the RateLimitResultPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RateLimitResultPayloadFields":
        self._alias = alias
        return self


class ReactionFields(GraphQLField):
    id: "ReactionGraphQLField" = ReactionGraphQLField("id")
    created_at: "ReactionGraphQLField" = ReactionGraphQLField("createdAt")
    updated_at: "ReactionGraphQLField" = ReactionGraphQLField("updatedAt")
    archived_at: "ReactionGraphQLField" = ReactionGraphQLField("archivedAt")
    emoji: "ReactionGraphQLField" = ReactionGraphQLField("emoji")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    @classmethod
    def comment(cls) -> "CommentFields":
        return CommentFields("comment")

    @classmethod
    def project_update(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("project_update")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    def fields(
        self,
        *subfields: Union[
            ReactionGraphQLField,
            "CommentFields",
            "IssueFields",
            "ProjectUpdateFields",
            "UserFields",
        ]
    ) -> "ReactionFields":
        """Subfields should come from the ReactionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ReactionFields":
        self._alias = alias
        return self


class ReactionPayloadFields(GraphQLField):
    last_sync_id: "ReactionPayloadGraphQLField" = ReactionPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def reaction(cls) -> "ReactionFields":
        return ReactionFields("reaction")

    success: "ReactionPayloadGraphQLField" = ReactionPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[ReactionPayloadGraphQLField, "ReactionFields"]
    ) -> "ReactionPayloadFields":
        """Subfields should come from the ReactionPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ReactionPayloadFields":
        self._alias = alias
        return self


class RoadmapFields(GraphQLField):
    id: "RoadmapGraphQLField" = RoadmapGraphQLField("id")
    created_at: "RoadmapGraphQLField" = RoadmapGraphQLField("createdAt")
    updated_at: "RoadmapGraphQLField" = RoadmapGraphQLField("updatedAt")
    archived_at: "RoadmapGraphQLField" = RoadmapGraphQLField("archivedAt")
    name: "RoadmapGraphQLField" = RoadmapGraphQLField("name")
    description: "RoadmapGraphQLField" = RoadmapGraphQLField("description")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def owner(cls) -> "UserFields":
        return UserFields("owner")

    slug_id: "RoadmapGraphQLField" = RoadmapGraphQLField("slugId")
    sort_order: "RoadmapGraphQLField" = RoadmapGraphQLField("sortOrder")
    color: "RoadmapGraphQLField" = RoadmapGraphQLField("color")

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
    ) -> "ProjectConnectionFields":
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
        return ProjectConnectionFields("projects", arguments=cleared_arguments)

    url: "RoadmapGraphQLField" = RoadmapGraphQLField("url")

    def fields(
        self,
        *subfields: Union[
            RoadmapGraphQLField,
            "OrganizationFields",
            "ProjectConnectionFields",
            "UserFields",
        ]
    ) -> "RoadmapFields":
        """Subfields should come from the RoadmapFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapFields":
        self._alias = alias
        return self


class RoadmapArchivePayloadFields(GraphQLField):
    last_sync_id: "RoadmapArchivePayloadGraphQLField" = (
        RoadmapArchivePayloadGraphQLField("lastSyncId")
    )
    success: "RoadmapArchivePayloadGraphQLField" = RoadmapArchivePayloadGraphQLField(
        "success"
    )

    @classmethod
    def entity(cls) -> "RoadmapFields":
        return RoadmapFields("entity")

    def fields(
        self, *subfields: Union[RoadmapArchivePayloadGraphQLField, "RoadmapFields"]
    ) -> "RoadmapArchivePayloadFields":
        """Subfields should come from the RoadmapArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapArchivePayloadFields":
        self._alias = alias
        return self


class RoadmapConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "RoadmapEdgeFields":
        return RoadmapEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "RoadmapFields":
        return RoadmapFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            RoadmapConnectionGraphQLField,
            "PageInfoFields",
            "RoadmapEdgeFields",
            "RoadmapFields",
        ]
    ) -> "RoadmapConnectionFields":
        """Subfields should come from the RoadmapConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapConnectionFields":
        self._alias = alias
        return self


class RoadmapEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "RoadmapFields":
        return RoadmapFields("node")

    cursor: "RoadmapEdgeGraphQLField" = RoadmapEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[RoadmapEdgeGraphQLField, "RoadmapFields"]
    ) -> "RoadmapEdgeFields":
        """Subfields should come from the RoadmapEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapEdgeFields":
        self._alias = alias
        return self


class RoadmapPayloadFields(GraphQLField):
    last_sync_id: "RoadmapPayloadGraphQLField" = RoadmapPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def roadmap(cls) -> "RoadmapFields":
        return RoadmapFields("roadmap")

    success: "RoadmapPayloadGraphQLField" = RoadmapPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[RoadmapPayloadGraphQLField, "RoadmapFields"]
    ) -> "RoadmapPayloadFields":
        """Subfields should come from the RoadmapPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapPayloadFields":
        self._alias = alias
        return self


class RoadmapToProjectFields(GraphQLField):
    id: "RoadmapToProjectGraphQLField" = RoadmapToProjectGraphQLField("id")
    created_at: "RoadmapToProjectGraphQLField" = RoadmapToProjectGraphQLField(
        "createdAt"
    )
    updated_at: "RoadmapToProjectGraphQLField" = RoadmapToProjectGraphQLField(
        "updatedAt"
    )
    archived_at: "RoadmapToProjectGraphQLField" = RoadmapToProjectGraphQLField(
        "archivedAt"
    )

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def roadmap(cls) -> "RoadmapFields":
        return RoadmapFields("roadmap")

    sort_order: "RoadmapToProjectGraphQLField" = RoadmapToProjectGraphQLField(
        "sortOrder"
    )

    def fields(
        self,
        *subfields: Union[
            RoadmapToProjectGraphQLField, "ProjectFields", "RoadmapFields"
        ]
    ) -> "RoadmapToProjectFields":
        """Subfields should come from the RoadmapToProjectFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapToProjectFields":
        self._alias = alias
        return self


class RoadmapToProjectConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "RoadmapToProjectEdgeFields":
        return RoadmapToProjectEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "RoadmapToProjectFields":
        return RoadmapToProjectFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            RoadmapToProjectConnectionGraphQLField,
            "PageInfoFields",
            "RoadmapToProjectEdgeFields",
            "RoadmapToProjectFields",
        ]
    ) -> "RoadmapToProjectConnectionFields":
        """Subfields should come from the RoadmapToProjectConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapToProjectConnectionFields":
        self._alias = alias
        return self


class RoadmapToProjectEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "RoadmapToProjectFields":
        return RoadmapToProjectFields("node")

    cursor: "RoadmapToProjectEdgeGraphQLField" = RoadmapToProjectEdgeGraphQLField(
        "cursor"
    )

    def fields(
        self,
        *subfields: Union[RoadmapToProjectEdgeGraphQLField, "RoadmapToProjectFields"]
    ) -> "RoadmapToProjectEdgeFields":
        """Subfields should come from the RoadmapToProjectEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapToProjectEdgeFields":
        self._alias = alias
        return self


class RoadmapToProjectPayloadFields(GraphQLField):
    last_sync_id: "RoadmapToProjectPayloadGraphQLField" = (
        RoadmapToProjectPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def roadmap_to_project(cls) -> "RoadmapToProjectFields":
        return RoadmapToProjectFields("roadmap_to_project")

    success: "RoadmapToProjectPayloadGraphQLField" = (
        RoadmapToProjectPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[RoadmapToProjectPayloadGraphQLField, "RoadmapToProjectFields"]
    ) -> "RoadmapToProjectPayloadFields":
        """Subfields should come from the RoadmapToProjectPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "RoadmapToProjectPayloadFields":
        self._alias = alias
        return self


class SlackAsksTeamSettingsFields(GraphQLField):
    id: "SlackAsksTeamSettingsGraphQLField" = SlackAsksTeamSettingsGraphQLField("id")
    has_default_ask: "SlackAsksTeamSettingsGraphQLField" = (
        SlackAsksTeamSettingsGraphQLField("hasDefaultAsk")
    )

    def fields(
        self, *subfields: SlackAsksTeamSettingsGraphQLField
    ) -> "SlackAsksTeamSettingsFields":
        """Subfields should come from the SlackAsksTeamSettingsFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SlackAsksTeamSettingsFields":
        self._alias = alias
        return self


class SlackChannelConnectPayloadFields(GraphQLField):
    last_sync_id: "SlackChannelConnectPayloadGraphQLField" = (
        SlackChannelConnectPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def integration(cls) -> "IntegrationFields":
        return IntegrationFields("integration")

    success: "SlackChannelConnectPayloadGraphQLField" = (
        SlackChannelConnectPayloadGraphQLField("success")
    )
    add_bot: "SlackChannelConnectPayloadGraphQLField" = (
        SlackChannelConnectPayloadGraphQLField("addBot")
    )
    nudge_to_connect_main_slack_integration: (
        "SlackChannelConnectPayloadGraphQLField"
    ) = SlackChannelConnectPayloadGraphQLField("nudgeToConnectMainSlackIntegration")
    nudge_to_update_main_slack_integration: "SlackChannelConnectPayloadGraphQLField" = (
        SlackChannelConnectPayloadGraphQLField("nudgeToUpdateMainSlackIntegration")
    )

    def fields(
        self,
        *subfields: Union[SlackChannelConnectPayloadGraphQLField, "IntegrationFields"]
    ) -> "SlackChannelConnectPayloadFields":
        """Subfields should come from the SlackChannelConnectPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SlackChannelConnectPayloadFields":
        self._alias = alias
        return self


class SlackChannelNameMappingFields(GraphQLField):
    id: "SlackChannelNameMappingGraphQLField" = SlackChannelNameMappingGraphQLField(
        "id"
    )
    name: "SlackChannelNameMappingGraphQLField" = SlackChannelNameMappingGraphQLField(
        "name"
    )
    is_private: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("isPrivate")
    )
    is_shared: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("isShared")
    )
    bot_added: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("botAdded")
    )

    @classmethod
    def teams(cls) -> "SlackAsksTeamSettingsFields":
        return SlackAsksTeamSettingsFields("teams")

    auto_create_on_message: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("autoCreateOnMessage")
    )
    auto_create_on_emoji: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("autoCreateOnEmoji")
    )
    auto_create_on_bot_mention: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("autoCreateOnBotMention")
    )
    auto_create_template_id: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("autoCreateTemplateId")
    )
    post_cancellation_updates: "SlackChannelNameMappingGraphQLField" = (
        SlackChannelNameMappingGraphQLField("postCancellationUpdates")
    )

    def fields(
        self,
        *subfields: Union[
            SlackChannelNameMappingGraphQLField, "SlackAsksTeamSettingsFields"
        ]
    ) -> "SlackChannelNameMappingFields":
        """Subfields should come from the SlackChannelNameMappingFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SlackChannelNameMappingFields":
        self._alias = alias
        return self


class SsoUrlFromEmailResponseFields(GraphQLField):
    success: "SsoUrlFromEmailResponseGraphQLField" = (
        SsoUrlFromEmailResponseGraphQLField("success")
    )
    saml_sso_url: "SsoUrlFromEmailResponseGraphQLField" = (
        SsoUrlFromEmailResponseGraphQLField("samlSsoUrl")
    )

    def fields(
        self, *subfields: SsoUrlFromEmailResponseGraphQLField
    ) -> "SsoUrlFromEmailResponseFields":
        """Subfields should come from the SsoUrlFromEmailResponseFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SsoUrlFromEmailResponseFields":
        self._alias = alias
        return self


class SuccessPayloadFields(GraphQLField):
    last_sync_id: "SuccessPayloadGraphQLField" = SuccessPayloadGraphQLField(
        "lastSyncId"
    )
    success: "SuccessPayloadGraphQLField" = SuccessPayloadGraphQLField("success")

    def fields(self, *subfields: SuccessPayloadGraphQLField) -> "SuccessPayloadFields":
        """Subfields should come from the SuccessPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SuccessPayloadFields":
        self._alias = alias
        return self


class SummaryPayloadFields(GraphQLField):
    summary: "SummaryPayloadGraphQLField" = SummaryPayloadGraphQLField("summary")

    def fields(self, *subfields: SummaryPayloadGraphQLField) -> "SummaryPayloadFields":
        """Subfields should come from the SummaryPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "SummaryPayloadFields":
        self._alias = alias
        return self


class TeamFields(GraphQLField):
    id: "TeamGraphQLField" = TeamGraphQLField("id")
    created_at: "TeamGraphQLField" = TeamGraphQLField("createdAt")
    updated_at: "TeamGraphQLField" = TeamGraphQLField("updatedAt")
    archived_at: "TeamGraphQLField" = TeamGraphQLField("archivedAt")
    name: "TeamGraphQLField" = TeamGraphQLField("name")
    key: "TeamGraphQLField" = TeamGraphQLField("key")
    description: "TeamGraphQLField" = TeamGraphQLField("description")
    icon: "TeamGraphQLField" = TeamGraphQLField("icon")
    color: "TeamGraphQLField" = TeamGraphQLField("color")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    cycles_enabled: "TeamGraphQLField" = TeamGraphQLField("cyclesEnabled")
    cycle_start_day: "TeamGraphQLField" = TeamGraphQLField("cycleStartDay")
    cycle_duration: "TeamGraphQLField" = TeamGraphQLField("cycleDuration")
    cycle_cooldown_time: "TeamGraphQLField" = TeamGraphQLField("cycleCooldownTime")
    cycle_issue_auto_assign_started: "TeamGraphQLField" = TeamGraphQLField(
        "cycleIssueAutoAssignStarted"
    )
    cycle_issue_auto_assign_completed: "TeamGraphQLField" = TeamGraphQLField(
        "cycleIssueAutoAssignCompleted"
    )
    cycle_lock_to_active: "TeamGraphQLField" = TeamGraphQLField("cycleLockToActive")
    upcoming_cycle_count: "TeamGraphQLField" = TeamGraphQLField("upcomingCycleCount")
    timezone: "TeamGraphQLField" = TeamGraphQLField("timezone")
    invite_hash: "TeamGraphQLField" = TeamGraphQLField("inviteHash")
    issue_estimation_type: "TeamGraphQLField" = TeamGraphQLField("issueEstimationType")
    issue_ordering_no_priority_first: "TeamGraphQLField" = TeamGraphQLField(
        "issueOrderingNoPriorityFirst"
    )
    issue_estimation_allow_zero: "TeamGraphQLField" = TeamGraphQLField(
        "issueEstimationAllowZero"
    )
    set_issue_sort_order_on_state_change: "TeamGraphQLField" = TeamGraphQLField(
        "setIssueSortOrderOnStateChange"
    )
    issue_estimation_extended: "TeamGraphQLField" = TeamGraphQLField(
        "issueEstimationExtended"
    )
    default_issue_estimate: "TeamGraphQLField" = TeamGraphQLField(
        "defaultIssueEstimate"
    )
    triage_enabled: "TeamGraphQLField" = TeamGraphQLField("triageEnabled")
    require_priority_to_leave_triage: "TeamGraphQLField" = TeamGraphQLField(
        "requirePriorityToLeaveTriage"
    )

    @classmethod
    def default_issue_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("default_issue_state")

    @classmethod
    def default_template_for_members(cls) -> "TemplateFields":
        return TemplateFields("default_template_for_members")

    default_template_for_members_id: "TeamGraphQLField" = TeamGraphQLField(
        "defaultTemplateForMembersId"
    )

    @classmethod
    def default_template_for_non_members(cls) -> "TemplateFields":
        return TemplateFields("default_template_for_non_members")

    default_template_for_non_members_id: "TeamGraphQLField" = TeamGraphQLField(
        "defaultTemplateForNonMembersId"
    )

    @classmethod
    def default_project_template(cls) -> "TemplateFields":
        return TemplateFields("default_project_template")

    @classmethod
    def triage_issue_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("triage_issue_state")

    private: "TeamGraphQLField" = TeamGraphQLField("private")
    scim_managed: "TeamGraphQLField" = TeamGraphQLField("scimManaged")
    scim_group_name: "TeamGraphQLField" = TeamGraphQLField("scimGroupName")
    progress_history: "TeamGraphQLField" = TeamGraphQLField("progressHistory")

    @classmethod
    def draft_workflow_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("draft_workflow_state")

    @classmethod
    def start_workflow_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("start_workflow_state")

    @classmethod
    def review_workflow_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("review_workflow_state")

    @classmethod
    def mergeable_workflow_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("mergeable_workflow_state")

    @classmethod
    def merge_workflow_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("merge_workflow_state")

    group_issue_history: "TeamGraphQLField" = TeamGraphQLField("groupIssueHistory")
    slack_new_issue: "TeamGraphQLField" = TeamGraphQLField("slackNewIssue")
    slack_issue_comments: "TeamGraphQLField" = TeamGraphQLField("slackIssueComments")
    slack_issue_statuses: "TeamGraphQLField" = TeamGraphQLField("slackIssueStatuses")
    auto_close_period: "TeamGraphQLField" = TeamGraphQLField("autoClosePeriod")
    auto_close_state_id: "TeamGraphQLField" = TeamGraphQLField("autoCloseStateId")
    auto_archive_period: "TeamGraphQLField" = TeamGraphQLField("autoArchivePeriod")

    @classmethod
    def marked_as_duplicate_workflow_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("marked_as_duplicate_workflow_state")

    join_by_default: "TeamGraphQLField" = TeamGraphQLField("joinByDefault")
    cycle_calender_url: "TeamGraphQLField" = TeamGraphQLField("cycleCalenderUrl")

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
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    @classmethod
    def issue_count(
        cls, *, include_archived: Optional[bool] = None
    ) -> "TeamGraphQLField":
        arguments: Dict[str, Dict[str, Any]] = {
            "includeArchived": {"type": "Boolean", "value": include_archived}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamGraphQLField("issue_count", arguments=cleared_arguments)

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
    ) -> "CycleConnectionFields":
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
        return CycleConnectionFields("cycles", arguments=cleared_arguments)

    @classmethod
    def active_cycle(cls) -> "CycleFields":
        return CycleFields("active_cycle")

    @classmethod
    def triage_responsibility(cls) -> "TriageResponsibilityFields":
        return TriageResponsibilityFields("triage_responsibility")

    @classmethod
    def members(
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
    ) -> "UserConnectionFields":
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
        return UserConnectionFields("members", arguments=cleared_arguments)

    @classmethod
    def membership(cls, user_id: str) -> "TeamMembershipFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "userId": {"type": "String!", "value": user_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamMembershipFields("membership", arguments=cleared_arguments)

    @classmethod
    def memberships(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "TeamMembershipConnectionFields":
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
            "memberships", arguments=cleared_arguments
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
    ) -> "ProjectConnectionFields":
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
        return ProjectConnectionFields("projects", arguments=cleared_arguments)

    @classmethod
    def states(
        cls,
        *,
        filter: Optional[WorkflowStateFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "WorkflowStateConnectionFields":
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
        return WorkflowStateConnectionFields("states", arguments=cleared_arguments)

    @classmethod
    def git_automation_states(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "GitAutomationStateConnectionFields":
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
        return GitAutomationStateConnectionFields(
            "git_automation_states", arguments=cleared_arguments
        )

    @classmethod
    def templates(
        cls,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "TemplateConnectionFields":
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
        return TemplateConnectionFields("templates", arguments=cleared_arguments)

    @classmethod
    def labels(
        cls,
        *,
        filter: Optional[IssueLabelFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueLabelConnectionFields":
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
        return IssueLabelConnectionFields("labels", arguments=cleared_arguments)

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
    ) -> "WebhookConnectionFields":
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
        return WebhookConnectionFields("webhooks", arguments=cleared_arguments)

    @classmethod
    def integrations_settings(cls) -> "IntegrationsSettingsFields":
        return IntegrationsSettingsFields("integrations_settings")

    issue_sort_order_default_to_bottom: "TeamGraphQLField" = TeamGraphQLField(
        "issueSortOrderDefaultToBottom"
    )

    def fields(
        self,
        *subfields: Union[
            TeamGraphQLField,
            "CycleConnectionFields",
            "CycleFields",
            "GitAutomationStateConnectionFields",
            "IntegrationsSettingsFields",
            "IssueConnectionFields",
            "IssueLabelConnectionFields",
            "OrganizationFields",
            "ProjectConnectionFields",
            "TeamMembershipConnectionFields",
            "TeamMembershipFields",
            "TemplateConnectionFields",
            "TemplateFields",
            "TriageResponsibilityFields",
            "UserConnectionFields",
            "WebhookConnectionFields",
            "WorkflowStateConnectionFields",
            "WorkflowStateFields",
        ]
    ) -> "TeamFields":
        """Subfields should come from the TeamFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamFields":
        self._alias = alias
        return self


class TeamArchivePayloadFields(GraphQLField):
    last_sync_id: "TeamArchivePayloadGraphQLField" = TeamArchivePayloadGraphQLField(
        "lastSyncId"
    )
    success: "TeamArchivePayloadGraphQLField" = TeamArchivePayloadGraphQLField(
        "success"
    )

    @classmethod
    def entity(cls) -> "TeamFields":
        return TeamFields("entity")

    def fields(
        self, *subfields: Union[TeamArchivePayloadGraphQLField, "TeamFields"]
    ) -> "TeamArchivePayloadFields":
        """Subfields should come from the TeamArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamArchivePayloadFields":
        self._alias = alias
        return self


class TeamConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "TeamEdgeFields":
        return TeamEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "TeamFields":
        return TeamFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            TeamConnectionGraphQLField, "PageInfoFields", "TeamEdgeFields", "TeamFields"
        ]
    ) -> "TeamConnectionFields":
        """Subfields should come from the TeamConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamConnectionFields":
        self._alias = alias
        return self


class TeamEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "TeamFields":
        return TeamFields("node")

    cursor: "TeamEdgeGraphQLField" = TeamEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[TeamEdgeGraphQLField, "TeamFields"]
    ) -> "TeamEdgeFields":
        """Subfields should come from the TeamEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamEdgeFields":
        self._alias = alias
        return self


class TeamMembershipFields(GraphQLField):
    id: "TeamMembershipGraphQLField" = TeamMembershipGraphQLField("id")
    created_at: "TeamMembershipGraphQLField" = TeamMembershipGraphQLField("createdAt")
    updated_at: "TeamMembershipGraphQLField" = TeamMembershipGraphQLField("updatedAt")
    archived_at: "TeamMembershipGraphQLField" = TeamMembershipGraphQLField("archivedAt")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    owner: "TeamMembershipGraphQLField" = TeamMembershipGraphQLField("owner")
    sort_order: "TeamMembershipGraphQLField" = TeamMembershipGraphQLField("sortOrder")

    def fields(
        self, *subfields: Union[TeamMembershipGraphQLField, "TeamFields", "UserFields"]
    ) -> "TeamMembershipFields":
        """Subfields should come from the TeamMembershipFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamMembershipFields":
        self._alias = alias
        return self


class TeamMembershipConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "TeamMembershipEdgeFields":
        return TeamMembershipEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "TeamMembershipFields":
        return TeamMembershipFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            TeamMembershipConnectionGraphQLField,
            "PageInfoFields",
            "TeamMembershipEdgeFields",
            "TeamMembershipFields",
        ]
    ) -> "TeamMembershipConnectionFields":
        """Subfields should come from the TeamMembershipConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamMembershipConnectionFields":
        self._alias = alias
        return self


class TeamMembershipEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "TeamMembershipFields":
        return TeamMembershipFields("node")

    cursor: "TeamMembershipEdgeGraphQLField" = TeamMembershipEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[TeamMembershipEdgeGraphQLField, "TeamMembershipFields"]
    ) -> "TeamMembershipEdgeFields":
        """Subfields should come from the TeamMembershipEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamMembershipEdgeFields":
        self._alias = alias
        return self


class TeamMembershipPayloadFields(GraphQLField):
    last_sync_id: "TeamMembershipPayloadGraphQLField" = (
        TeamMembershipPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def team_membership(cls) -> "TeamMembershipFields":
        return TeamMembershipFields("team_membership")

    success: "TeamMembershipPayloadGraphQLField" = TeamMembershipPayloadGraphQLField(
        "success"
    )

    def fields(
        self,
        *subfields: Union[TeamMembershipPayloadGraphQLField, "TeamMembershipFields"]
    ) -> "TeamMembershipPayloadFields":
        """Subfields should come from the TeamMembershipPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamMembershipPayloadFields":
        self._alias = alias
        return self


class TeamPayloadFields(GraphQLField):
    last_sync_id: "TeamPayloadGraphQLField" = TeamPayloadGraphQLField("lastSyncId")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    success: "TeamPayloadGraphQLField" = TeamPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[TeamPayloadGraphQLField, "TeamFields"]
    ) -> "TeamPayloadFields":
        """Subfields should come from the TeamPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TeamPayloadFields":
        self._alias = alias
        return self


class TemplateFields(GraphQLField):
    id: "TemplateGraphQLField" = TemplateGraphQLField("id")
    created_at: "TemplateGraphQLField" = TemplateGraphQLField("createdAt")
    updated_at: "TemplateGraphQLField" = TemplateGraphQLField("updatedAt")
    archived_at: "TemplateGraphQLField" = TemplateGraphQLField("archivedAt")
    type: "TemplateGraphQLField" = TemplateGraphQLField("type")
    name: "TemplateGraphQLField" = TemplateGraphQLField("name")
    description: "TemplateGraphQLField" = TemplateGraphQLField("description")
    template_data: "TemplateGraphQLField" = TemplateGraphQLField("templateData")
    sort_order: "TemplateGraphQLField" = TemplateGraphQLField("sortOrder")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    @classmethod
    def last_updated_by(cls) -> "UserFields":
        return UserFields("last_updated_by")

    def fields(
        self,
        *subfields: Union[
            TemplateGraphQLField, "OrganizationFields", "TeamFields", "UserFields"
        ]
    ) -> "TemplateFields":
        """Subfields should come from the TemplateFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TemplateFields":
        self._alias = alias
        return self


class TemplateConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "TemplateEdgeFields":
        return TemplateEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "TemplateFields":
        return TemplateFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            TemplateConnectionGraphQLField,
            "PageInfoFields",
            "TemplateEdgeFields",
            "TemplateFields",
        ]
    ) -> "TemplateConnectionFields":
        """Subfields should come from the TemplateConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TemplateConnectionFields":
        self._alias = alias
        return self


class TemplateEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "TemplateFields":
        return TemplateFields("node")

    cursor: "TemplateEdgeGraphQLField" = TemplateEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[TemplateEdgeGraphQLField, "TemplateFields"]
    ) -> "TemplateEdgeFields":
        """Subfields should come from the TemplateEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TemplateEdgeFields":
        self._alias = alias
        return self


class TemplatePayloadFields(GraphQLField):
    last_sync_id: "TemplatePayloadGraphQLField" = TemplatePayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def template(cls) -> "TemplateFields":
        return TemplateFields("template")

    success: "TemplatePayloadGraphQLField" = TemplatePayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[TemplatePayloadGraphQLField, "TemplateFields"]
    ) -> "TemplatePayloadFields":
        """Subfields should come from the TemplatePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TemplatePayloadFields":
        self._alias = alias
        return self


class TextDraftFields(GraphQLField):
    id: "TextDraftGraphQLField" = TextDraftGraphQLField("id")
    created_at: "TextDraftGraphQLField" = TextDraftGraphQLField("createdAt")
    updated_at: "TextDraftGraphQLField" = TextDraftGraphQLField("updatedAt")
    archived_at: "TextDraftGraphQLField" = TextDraftGraphQLField("archivedAt")
    body_data: "TextDraftGraphQLField" = TextDraftGraphQLField("bodyData")
    data: "TextDraftGraphQLField" = TextDraftGraphQLField("data")
    is_autogenerated: "TextDraftGraphQLField" = TextDraftGraphQLField("isAutogenerated")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    @classmethod
    def issue(cls) -> "IssueFields":
        return IssueFields("issue")

    @classmethod
    def project(cls) -> "ProjectFields":
        return ProjectFields("project")

    @classmethod
    def project_update(cls) -> "ProjectUpdateFields":
        return ProjectUpdateFields("project_update")

    @classmethod
    def parent_comment(cls) -> "CommentFields":
        return CommentFields("parent_comment")

    def fields(
        self,
        *subfields: Union[
            TextDraftGraphQLField,
            "CommentFields",
            "IssueFields",
            "ProjectFields",
            "ProjectUpdateFields",
            "UserFields",
        ]
    ) -> "TextDraftFields":
        """Subfields should come from the TextDraftFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TextDraftFields":
        self._alias = alias
        return self


class TimeScheduleFields(GraphQLField):
    id: "TimeScheduleGraphQLField" = TimeScheduleGraphQLField("id")
    created_at: "TimeScheduleGraphQLField" = TimeScheduleGraphQLField("createdAt")
    updated_at: "TimeScheduleGraphQLField" = TimeScheduleGraphQLField("updatedAt")
    archived_at: "TimeScheduleGraphQLField" = TimeScheduleGraphQLField("archivedAt")
    name: "TimeScheduleGraphQLField" = TimeScheduleGraphQLField("name")

    @classmethod
    def entries(cls) -> "TimeScheduleEntryFields":
        return TimeScheduleEntryFields("entries")

    external_id: "TimeScheduleGraphQLField" = TimeScheduleGraphQLField("externalId")
    external_url: "TimeScheduleGraphQLField" = TimeScheduleGraphQLField("externalUrl")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    @classmethod
    def integration(cls) -> "IntegrationFields":
        return IntegrationFields("integration")

    def fields(
        self,
        *subfields: Union[
            TimeScheduleGraphQLField,
            "IntegrationFields",
            "OrganizationFields",
            "TimeScheduleEntryFields",
        ]
    ) -> "TimeScheduleFields":
        """Subfields should come from the TimeScheduleFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimeScheduleFields":
        self._alias = alias
        return self


class TimeScheduleConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "TimeScheduleEdgeFields":
        return TimeScheduleEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "TimeScheduleFields":
        return TimeScheduleFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            TimeScheduleConnectionGraphQLField,
            "PageInfoFields",
            "TimeScheduleEdgeFields",
            "TimeScheduleFields",
        ]
    ) -> "TimeScheduleConnectionFields":
        """Subfields should come from the TimeScheduleConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimeScheduleConnectionFields":
        self._alias = alias
        return self


class TimeScheduleEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "TimeScheduleFields":
        return TimeScheduleFields("node")

    cursor: "TimeScheduleEdgeGraphQLField" = TimeScheduleEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[TimeScheduleEdgeGraphQLField, "TimeScheduleFields"]
    ) -> "TimeScheduleEdgeFields":
        """Subfields should come from the TimeScheduleEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimeScheduleEdgeFields":
        self._alias = alias
        return self


class TimeScheduleEntryFields(GraphQLField):
    starts_at: "TimeScheduleEntryGraphQLField" = TimeScheduleEntryGraphQLField(
        "startsAt"
    )
    ends_at: "TimeScheduleEntryGraphQLField" = TimeScheduleEntryGraphQLField("endsAt")
    user_id: "TimeScheduleEntryGraphQLField" = TimeScheduleEntryGraphQLField("userId")
    user_email: "TimeScheduleEntryGraphQLField" = TimeScheduleEntryGraphQLField(
        "userEmail"
    )

    def fields(
        self, *subfields: TimeScheduleEntryGraphQLField
    ) -> "TimeScheduleEntryFields":
        """Subfields should come from the TimeScheduleEntryFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimeScheduleEntryFields":
        self._alias = alias
        return self


class TimeSchedulePayloadFields(GraphQLField):
    last_sync_id: "TimeSchedulePayloadGraphQLField" = TimeSchedulePayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def time_schedule(cls) -> "TimeScheduleFields":
        return TimeScheduleFields("time_schedule")

    success: "TimeSchedulePayloadGraphQLField" = TimeSchedulePayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[TimeSchedulePayloadGraphQLField, "TimeScheduleFields"]
    ) -> "TimeSchedulePayloadFields":
        """Subfields should come from the TimeSchedulePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TimeSchedulePayloadFields":
        self._alias = alias
        return self


class TriageResponsibilityFields(GraphQLField):
    id: "TriageResponsibilityGraphQLField" = TriageResponsibilityGraphQLField("id")
    created_at: "TriageResponsibilityGraphQLField" = TriageResponsibilityGraphQLField(
        "createdAt"
    )
    updated_at: "TriageResponsibilityGraphQLField" = TriageResponsibilityGraphQLField(
        "updatedAt"
    )
    archived_at: "TriageResponsibilityGraphQLField" = TriageResponsibilityGraphQLField(
        "archivedAt"
    )
    action: "TriageResponsibilityGraphQLField" = TriageResponsibilityGraphQLField(
        "action"
    )

    @classmethod
    def manual_selection(cls) -> "TriageResponsibilityManualSelectionFields":
        return TriageResponsibilityManualSelectionFields("manual_selection")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    @classmethod
    def time_schedule(cls) -> "TimeScheduleFields":
        return TimeScheduleFields("time_schedule")

    @classmethod
    def current_user(cls) -> "UserFields":
        return UserFields("current_user")

    def fields(
        self,
        *subfields: Union[
            TriageResponsibilityGraphQLField,
            "TeamFields",
            "TimeScheduleFields",
            "TriageResponsibilityManualSelectionFields",
            "UserFields",
        ]
    ) -> "TriageResponsibilityFields":
        """Subfields should come from the TriageResponsibilityFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TriageResponsibilityFields":
        self._alias = alias
        return self


class TriageResponsibilityConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "TriageResponsibilityEdgeFields":
        return TriageResponsibilityEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "TriageResponsibilityFields":
        return TriageResponsibilityFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            TriageResponsibilityConnectionGraphQLField,
            "PageInfoFields",
            "TriageResponsibilityEdgeFields",
            "TriageResponsibilityFields",
        ]
    ) -> "TriageResponsibilityConnectionFields":
        """Subfields should come from the TriageResponsibilityConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TriageResponsibilityConnectionFields":
        self._alias = alias
        return self


class TriageResponsibilityEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "TriageResponsibilityFields":
        return TriageResponsibilityFields("node")

    cursor: "TriageResponsibilityEdgeGraphQLField" = (
        TriageResponsibilityEdgeGraphQLField("cursor")
    )

    def fields(
        self,
        *subfields: Union[
            TriageResponsibilityEdgeGraphQLField, "TriageResponsibilityFields"
        ]
    ) -> "TriageResponsibilityEdgeFields":
        """Subfields should come from the TriageResponsibilityEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TriageResponsibilityEdgeFields":
        self._alias = alias
        return self


class TriageResponsibilityManualSelectionFields(GraphQLField):
    user_ids: "TriageResponsibilityManualSelectionGraphQLField" = (
        TriageResponsibilityManualSelectionGraphQLField("userIds")
    )
    assignment_index: "TriageResponsibilityManualSelectionGraphQLField" = (
        TriageResponsibilityManualSelectionGraphQLField("assignmentIndex")
    )

    def fields(
        self, *subfields: TriageResponsibilityManualSelectionGraphQLField
    ) -> "TriageResponsibilityManualSelectionFields":
        """Subfields should come from the TriageResponsibilityManualSelectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TriageResponsibilityManualSelectionFields":
        self._alias = alias
        return self


class TriageResponsibilityPayloadFields(GraphQLField):
    last_sync_id: "TriageResponsibilityPayloadGraphQLField" = (
        TriageResponsibilityPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def triage_responsibility(cls) -> "TriageResponsibilityFields":
        return TriageResponsibilityFields("triage_responsibility")

    success: "TriageResponsibilityPayloadGraphQLField" = (
        TriageResponsibilityPayloadGraphQLField("success")
    )

    def fields(
        self,
        *subfields: Union[
            TriageResponsibilityPayloadGraphQLField, "TriageResponsibilityFields"
        ]
    ) -> "TriageResponsibilityPayloadFields":
        """Subfields should come from the TriageResponsibilityPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "TriageResponsibilityPayloadFields":
        self._alias = alias
        return self


class UploadFileFields(GraphQLField):
    filename: "UploadFileGraphQLField" = UploadFileGraphQLField("filename")
    content_type: "UploadFileGraphQLField" = UploadFileGraphQLField("contentType")
    size: "UploadFileGraphQLField" = UploadFileGraphQLField("size")
    upload_url: "UploadFileGraphQLField" = UploadFileGraphQLField("uploadUrl")
    asset_url: "UploadFileGraphQLField" = UploadFileGraphQLField("assetUrl")
    meta_data: "UploadFileGraphQLField" = UploadFileGraphQLField("metaData")

    @classmethod
    def headers(cls) -> "UploadFileHeaderFields":
        return UploadFileHeaderFields("headers")

    def fields(
        self, *subfields: Union[UploadFileGraphQLField, "UploadFileHeaderFields"]
    ) -> "UploadFileFields":
        """Subfields should come from the UploadFileFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UploadFileFields":
        self._alias = alias
        return self


class UploadFileHeaderFields(GraphQLField):
    key: "UploadFileHeaderGraphQLField" = UploadFileHeaderGraphQLField("key")
    value: "UploadFileHeaderGraphQLField" = UploadFileHeaderGraphQLField("value")

    def fields(
        self, *subfields: UploadFileHeaderGraphQLField
    ) -> "UploadFileHeaderFields":
        """Subfields should come from the UploadFileHeaderFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UploadFileHeaderFields":
        self._alias = alias
        return self


class UploadPayloadFields(GraphQLField):
    last_sync_id: "UploadPayloadGraphQLField" = UploadPayloadGraphQLField("lastSyncId")

    @classmethod
    def upload_file(cls) -> "UploadFileFields":
        return UploadFileFields("upload_file")

    success: "UploadPayloadGraphQLField" = UploadPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[UploadPayloadGraphQLField, "UploadFileFields"]
    ) -> "UploadPayloadFields":
        """Subfields should come from the UploadPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UploadPayloadFields":
        self._alias = alias
        return self


class UserFields(GraphQLField):
    id: "UserGraphQLField" = UserGraphQLField("id")
    created_at: "UserGraphQLField" = UserGraphQLField("createdAt")
    updated_at: "UserGraphQLField" = UserGraphQLField("updatedAt")
    archived_at: "UserGraphQLField" = UserGraphQLField("archivedAt")
    name: "UserGraphQLField" = UserGraphQLField("name")
    display_name: "UserGraphQLField" = UserGraphQLField("displayName")
    email: "UserGraphQLField" = UserGraphQLField("email")
    avatar_url: "UserGraphQLField" = UserGraphQLField("avatarUrl")
    disable_reason: "UserGraphQLField" = UserGraphQLField("disableReason")
    invite_hash: "UserGraphQLField" = UserGraphQLField("inviteHash")
    calendar_hash: "UserGraphQLField" = UserGraphQLField("calendarHash")
    description: "UserGraphQLField" = UserGraphQLField("description")
    status_emoji: "UserGraphQLField" = UserGraphQLField("statusEmoji")
    status_label: "UserGraphQLField" = UserGraphQLField("statusLabel")
    status_until_at: "UserGraphQLField" = UserGraphQLField("statusUntilAt")
    timezone: "UserGraphQLField" = UserGraphQLField("timezone")

    @classmethod
    def organization(cls) -> "OrganizationFields":
        return OrganizationFields("organization")

    last_seen: "UserGraphQLField" = UserGraphQLField("lastSeen")
    initials: "UserGraphQLField" = UserGraphQLField("initials")
    avatar_background_color: "UserGraphQLField" = UserGraphQLField(
        "avatarBackgroundColor"
    )
    guest: "UserGraphQLField" = UserGraphQLField("guest")
    active: "UserGraphQLField" = UserGraphQLField("active")
    url: "UserGraphQLField" = UserGraphQLField("url")

    @classmethod
    def text_drafts(cls) -> "TextDraftFields":
        return TextDraftFields("text_drafts")

    @classmethod
    def assigned_issues(
        cls,
        *,
        filter: Optional[IssueFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("assigned_issues", arguments=cleared_arguments)

    @classmethod
    def created_issues(
        cls,
        *,
        filter: Optional[IssueFilter] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        include_archived: Optional[bool] = None,
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("created_issues", arguments=cleared_arguments)

    created_issue_count: "UserGraphQLField" = UserGraphQLField("createdIssueCount")

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
    ) -> "TeamConnectionFields":
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
        return TeamConnectionFields("teams", arguments=cleared_arguments)

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
    ) -> "TeamMembershipConnectionFields":
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
            "team_memberships", arguments=cleared_arguments
        )

    is_me: "UserGraphQLField" = UserGraphQLField("isMe")
    admin: "UserGraphQLField" = UserGraphQLField("admin")

    def fields(
        self,
        *subfields: Union[
            UserGraphQLField,
            "IssueConnectionFields",
            "OrganizationFields",
            "TeamConnectionFields",
            "TeamMembershipConnectionFields",
            "TextDraftFields",
        ]
    ) -> "UserFields":
        """Subfields should come from the UserFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserFields":
        self._alias = alias
        return self


class UserAdminPayloadFields(GraphQLField):
    success: "UserAdminPayloadGraphQLField" = UserAdminPayloadGraphQLField("success")

    def fields(
        self, *subfields: UserAdminPayloadGraphQLField
    ) -> "UserAdminPayloadFields":
        """Subfields should come from the UserAdminPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserAdminPayloadFields":
        self._alias = alias
        return self


class UserAuthorizedApplicationFields(GraphQLField):
    id: "UserAuthorizedApplicationGraphQLField" = UserAuthorizedApplicationGraphQLField(
        "id"
    )
    client_id: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("clientId")
    )
    name: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("name")
    )
    description: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("description")
    )
    developer: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("developer")
    )
    developer_url: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("developerUrl")
    )
    image_url: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("imageUrl")
    )
    is_authorized: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("isAuthorized")
    )
    created_by_linear: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("createdByLinear")
    )
    webhooks_enabled: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("webhooksEnabled")
    )
    approval_error_code: "UserAuthorizedApplicationGraphQLField" = (
        UserAuthorizedApplicationGraphQLField("approvalErrorCode")
    )

    def fields(
        self, *subfields: UserAuthorizedApplicationGraphQLField
    ) -> "UserAuthorizedApplicationFields":
        """Subfields should come from the UserAuthorizedApplicationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserAuthorizedApplicationFields":
        self._alias = alias
        return self


class UserConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "UserEdgeFields":
        return UserEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "UserFields":
        return UserFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            UserConnectionGraphQLField, "PageInfoFields", "UserEdgeFields", "UserFields"
        ]
    ) -> "UserConnectionFields":
        """Subfields should come from the UserConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserConnectionFields":
        self._alias = alias
        return self


class UserEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "UserFields":
        return UserFields("node")

    cursor: "UserEdgeGraphQLField" = UserEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[UserEdgeGraphQLField, "UserFields"]
    ) -> "UserEdgeFields":
        """Subfields should come from the UserEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserEdgeFields":
        self._alias = alias
        return self


class UserPayloadFields(GraphQLField):
    last_sync_id: "UserPayloadGraphQLField" = UserPayloadGraphQLField("lastSyncId")

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    success: "UserPayloadGraphQLField" = UserPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[UserPayloadGraphQLField, "UserFields"]
    ) -> "UserPayloadFields":
        """Subfields should come from the UserPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserPayloadFields":
        self._alias = alias
        return self


class UserSettingsFields(GraphQLField):
    id: "UserSettingsGraphQLField" = UserSettingsGraphQLField("id")
    created_at: "UserSettingsGraphQLField" = UserSettingsGraphQLField("createdAt")
    updated_at: "UserSettingsGraphQLField" = UserSettingsGraphQLField("updatedAt")
    archived_at: "UserSettingsGraphQLField" = UserSettingsGraphQLField("archivedAt")
    notification_preferences: "UserSettingsGraphQLField" = UserSettingsGraphQLField(
        "notificationPreferences"
    )

    @classmethod
    def notification_delivery_preferences(
        cls,
    ) -> "NotificationDeliveryPreferencesFields":
        return NotificationDeliveryPreferencesFields(
            "notification_delivery_preferences"
        )

    unsubscribed_from: "UserSettingsGraphQLField" = UserSettingsGraphQLField(
        "unsubscribedFrom"
    )

    @classmethod
    def user(cls) -> "UserFields":
        return UserFields("user")

    calendar_hash: "UserSettingsGraphQLField" = UserSettingsGraphQLField("calendarHash")
    subscribed_to_changelog: "UserSettingsGraphQLField" = UserSettingsGraphQLField(
        "subscribedToChangelog"
    )
    subscribed_to_dpa: "UserSettingsGraphQLField" = UserSettingsGraphQLField(
        "subscribedToDPA"
    )
    subscribed_to_invite_accepted: "UserSettingsGraphQLField" = (
        UserSettingsGraphQLField("subscribedToInviteAccepted")
    )
    subscribed_to_privacy_legal_updates: "UserSettingsGraphQLField" = (
        UserSettingsGraphQLField("subscribedToPrivacyLegalUpdates")
    )
    subscribed_to_unread_notifications_reminder: "UserSettingsGraphQLField" = (
        UserSettingsGraphQLField("subscribedToUnreadNotificationsReminder")
    )
    show_full_user_names: "UserSettingsGraphQLField" = UserSettingsGraphQLField(
        "showFullUserNames"
    )

    def fields(
        self,
        *subfields: Union[
            UserSettingsGraphQLField,
            "NotificationDeliveryPreferencesFields",
            "UserFields",
        ]
    ) -> "UserSettingsFields":
        """Subfields should come from the UserSettingsFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserSettingsFields":
        self._alias = alias
        return self


class UserSettingsFlagPayloadFields(GraphQLField):
    last_sync_id: "UserSettingsFlagPayloadGraphQLField" = (
        UserSettingsFlagPayloadGraphQLField("lastSyncId")
    )
    flag: "UserSettingsFlagPayloadGraphQLField" = UserSettingsFlagPayloadGraphQLField(
        "flag"
    )
    value: "UserSettingsFlagPayloadGraphQLField" = UserSettingsFlagPayloadGraphQLField(
        "value"
    )
    success: "UserSettingsFlagPayloadGraphQLField" = (
        UserSettingsFlagPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: UserSettingsFlagPayloadGraphQLField
    ) -> "UserSettingsFlagPayloadFields":
        """Subfields should come from the UserSettingsFlagPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserSettingsFlagPayloadFields":
        self._alias = alias
        return self


class UserSettingsFlagsResetPayloadFields(GraphQLField):
    last_sync_id: "UserSettingsFlagsResetPayloadGraphQLField" = (
        UserSettingsFlagsResetPayloadGraphQLField("lastSyncId")
    )
    success: "UserSettingsFlagsResetPayloadGraphQLField" = (
        UserSettingsFlagsResetPayloadGraphQLField("success")
    )

    def fields(
        self, *subfields: UserSettingsFlagsResetPayloadGraphQLField
    ) -> "UserSettingsFlagsResetPayloadFields":
        """Subfields should come from the UserSettingsFlagsResetPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserSettingsFlagsResetPayloadFields":
        self._alias = alias
        return self


class UserSettingsPayloadFields(GraphQLField):
    last_sync_id: "UserSettingsPayloadGraphQLField" = UserSettingsPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def user_settings(cls) -> "UserSettingsFields":
        return UserSettingsFields("user_settings")

    success: "UserSettingsPayloadGraphQLField" = UserSettingsPayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[UserSettingsPayloadGraphQLField, "UserSettingsFields"]
    ) -> "UserSettingsPayloadFields":
        """Subfields should come from the UserSettingsPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "UserSettingsPayloadFields":
        self._alias = alias
        return self


class ViewPreferencesFields(GraphQLField):
    id: "ViewPreferencesGraphQLField" = ViewPreferencesGraphQLField("id")
    created_at: "ViewPreferencesGraphQLField" = ViewPreferencesGraphQLField("createdAt")
    updated_at: "ViewPreferencesGraphQLField" = ViewPreferencesGraphQLField("updatedAt")
    archived_at: "ViewPreferencesGraphQLField" = ViewPreferencesGraphQLField(
        "archivedAt"
    )
    type: "ViewPreferencesGraphQLField" = ViewPreferencesGraphQLField("type")
    view_type: "ViewPreferencesGraphQLField" = ViewPreferencesGraphQLField("viewType")

    @classmethod
    def preferences(cls) -> "ViewPreferencesValuesFields":
        return ViewPreferencesValuesFields("preferences")

    def fields(
        self,
        *subfields: Union[ViewPreferencesGraphQLField, "ViewPreferencesValuesFields"]
    ) -> "ViewPreferencesFields":
        """Subfields should come from the ViewPreferencesFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ViewPreferencesFields":
        self._alias = alias
        return self


class ViewPreferencesPayloadFields(GraphQLField):
    last_sync_id: "ViewPreferencesPayloadGraphQLField" = (
        ViewPreferencesPayloadGraphQLField("lastSyncId")
    )

    @classmethod
    def view_preferences(cls) -> "ViewPreferencesFields":
        return ViewPreferencesFields("view_preferences")

    success: "ViewPreferencesPayloadGraphQLField" = ViewPreferencesPayloadGraphQLField(
        "success"
    )

    def fields(
        self,
        *subfields: Union[ViewPreferencesPayloadGraphQLField, "ViewPreferencesFields"]
    ) -> "ViewPreferencesPayloadFields":
        """Subfields should come from the ViewPreferencesPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ViewPreferencesPayloadFields":
        self._alias = alias
        return self


class ViewPreferencesValuesFields(GraphQLField):
    view_ordering: "ViewPreferencesValuesGraphQLField" = (
        ViewPreferencesValuesGraphQLField("viewOrdering")
    )
    issue_grouping: "ViewPreferencesValuesGraphQLField" = (
        ViewPreferencesValuesGraphQLField("issueGrouping")
    )
    show_completed_issues: "ViewPreferencesValuesGraphQLField" = (
        ViewPreferencesValuesGraphQLField("showCompletedIssues")
    )

    def fields(
        self, *subfields: ViewPreferencesValuesGraphQLField
    ) -> "ViewPreferencesValuesFields":
        """Subfields should come from the ViewPreferencesValuesFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "ViewPreferencesValuesFields":
        self._alias = alias
        return self


class WebhookFields(GraphQLField):
    id: "WebhookGraphQLField" = WebhookGraphQLField("id")
    created_at: "WebhookGraphQLField" = WebhookGraphQLField("createdAt")
    updated_at: "WebhookGraphQLField" = WebhookGraphQLField("updatedAt")
    archived_at: "WebhookGraphQLField" = WebhookGraphQLField("archivedAt")
    label: "WebhookGraphQLField" = WebhookGraphQLField("label")
    url: "WebhookGraphQLField" = WebhookGraphQLField("url")
    enabled: "WebhookGraphQLField" = WebhookGraphQLField("enabled")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

    all_public_teams: "WebhookGraphQLField" = WebhookGraphQLField("allPublicTeams")

    @classmethod
    def creator(cls) -> "UserFields":
        return UserFields("creator")

    secret: "WebhookGraphQLField" = WebhookGraphQLField("secret")
    resource_types: "WebhookGraphQLField" = WebhookGraphQLField("resourceTypes")

    def fields(
        self, *subfields: Union[WebhookGraphQLField, "TeamFields", "UserFields"]
    ) -> "WebhookFields":
        """Subfields should come from the WebhookFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WebhookFields":
        self._alias = alias
        return self


class WebhookConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "WebhookEdgeFields":
        return WebhookEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "WebhookFields":
        return WebhookFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            WebhookConnectionGraphQLField,
            "PageInfoFields",
            "WebhookEdgeFields",
            "WebhookFields",
        ]
    ) -> "WebhookConnectionFields":
        """Subfields should come from the WebhookConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WebhookConnectionFields":
        self._alias = alias
        return self


class WebhookEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "WebhookFields":
        return WebhookFields("node")

    cursor: "WebhookEdgeGraphQLField" = WebhookEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[WebhookEdgeGraphQLField, "WebhookFields"]
    ) -> "WebhookEdgeFields":
        """Subfields should come from the WebhookEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WebhookEdgeFields":
        self._alias = alias
        return self


class WebhookPayloadFields(GraphQLField):
    last_sync_id: "WebhookPayloadGraphQLField" = WebhookPayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def webhook(cls) -> "WebhookFields":
        return WebhookFields("webhook")

    success: "WebhookPayloadGraphQLField" = WebhookPayloadGraphQLField("success")

    def fields(
        self, *subfields: Union[WebhookPayloadGraphQLField, "WebhookFields"]
    ) -> "WebhookPayloadFields":
        """Subfields should come from the WebhookPayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WebhookPayloadFields":
        self._alias = alias
        return self


class WorkflowStateFields(GraphQLField):
    id: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("id")
    created_at: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("createdAt")
    updated_at: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("updatedAt")
    archived_at: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("archivedAt")
    name: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("name")
    color: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("color")
    description: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("description")
    position: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("position")
    type: "WorkflowStateGraphQLField" = WorkflowStateGraphQLField("type")

    @classmethod
    def team(cls) -> "TeamFields":
        return TeamFields("team")

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
        order_by: Optional[PaginationOrderBy] = None
    ) -> "IssueConnectionFields":
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "IssueFilter", "value": filter},
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
        return IssueConnectionFields("issues", arguments=cleared_arguments)

    def fields(
        self,
        *subfields: Union[
            WorkflowStateGraphQLField, "IssueConnectionFields", "TeamFields"
        ]
    ) -> "WorkflowStateFields":
        """Subfields should come from the WorkflowStateFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkflowStateFields":
        self._alias = alias
        return self


class WorkflowStateArchivePayloadFields(GraphQLField):
    last_sync_id: "WorkflowStateArchivePayloadGraphQLField" = (
        WorkflowStateArchivePayloadGraphQLField("lastSyncId")
    )
    success: "WorkflowStateArchivePayloadGraphQLField" = (
        WorkflowStateArchivePayloadGraphQLField("success")
    )

    @classmethod
    def entity(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("entity")

    def fields(
        self,
        *subfields: Union[
            WorkflowStateArchivePayloadGraphQLField, "WorkflowStateFields"
        ]
    ) -> "WorkflowStateArchivePayloadFields":
        """Subfields should come from the WorkflowStateArchivePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkflowStateArchivePayloadFields":
        self._alias = alias
        return self


class WorkflowStateConnectionFields(GraphQLField):
    @classmethod
    def edges(cls) -> "WorkflowStateEdgeFields":
        return WorkflowStateEdgeFields("edges")

    @classmethod
    def nodes(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("nodes")

    @classmethod
    def page_info(cls) -> "PageInfoFields":
        return PageInfoFields("page_info")

    def fields(
        self,
        *subfields: Union[
            WorkflowStateConnectionGraphQLField,
            "PageInfoFields",
            "WorkflowStateEdgeFields",
            "WorkflowStateFields",
        ]
    ) -> "WorkflowStateConnectionFields":
        """Subfields should come from the WorkflowStateConnectionFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkflowStateConnectionFields":
        self._alias = alias
        return self


class WorkflowStateEdgeFields(GraphQLField):
    @classmethod
    def node(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("node")

    cursor: "WorkflowStateEdgeGraphQLField" = WorkflowStateEdgeGraphQLField("cursor")

    def fields(
        self, *subfields: Union[WorkflowStateEdgeGraphQLField, "WorkflowStateFields"]
    ) -> "WorkflowStateEdgeFields":
        """Subfields should come from the WorkflowStateEdgeFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkflowStateEdgeFields":
        self._alias = alias
        return self


class WorkflowStatePayloadFields(GraphQLField):
    last_sync_id: "WorkflowStatePayloadGraphQLField" = WorkflowStatePayloadGraphQLField(
        "lastSyncId"
    )

    @classmethod
    def workflow_state(cls) -> "WorkflowStateFields":
        return WorkflowStateFields("workflow_state")

    success: "WorkflowStatePayloadGraphQLField" = WorkflowStatePayloadGraphQLField(
        "success"
    )

    def fields(
        self, *subfields: Union[WorkflowStatePayloadGraphQLField, "WorkflowStateFields"]
    ) -> "WorkflowStatePayloadFields":
        """Subfields should come from the WorkflowStatePayloadFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkflowStatePayloadFields":
        self._alias = alias
        return self


class WorkspaceAuthorizedApplicationFields(GraphQLField):
    name: "WorkspaceAuthorizedApplicationGraphQLField" = (
        WorkspaceAuthorizedApplicationGraphQLField("name")
    )
    image_url: "WorkspaceAuthorizedApplicationGraphQLField" = (
        WorkspaceAuthorizedApplicationGraphQLField("imageUrl")
    )
    scope: "WorkspaceAuthorizedApplicationGraphQLField" = (
        WorkspaceAuthorizedApplicationGraphQLField("scope")
    )
    app_id: "WorkspaceAuthorizedApplicationGraphQLField" = (
        WorkspaceAuthorizedApplicationGraphQLField("appId")
    )
    client_id: "WorkspaceAuthorizedApplicationGraphQLField" = (
        WorkspaceAuthorizedApplicationGraphQLField("clientId")
    )
    webhooks_enabled: "WorkspaceAuthorizedApplicationGraphQLField" = (
        WorkspaceAuthorizedApplicationGraphQLField("webhooksEnabled")
    )
    total_members: "WorkspaceAuthorizedApplicationGraphQLField" = (
        WorkspaceAuthorizedApplicationGraphQLField("totalMembers")
    )

    @classmethod
    def memberships(cls) -> "AuthMembershipFields":
        return AuthMembershipFields("memberships")

    def fields(
        self,
        *subfields: Union[
            WorkspaceAuthorizedApplicationGraphQLField, "AuthMembershipFields"
        ]
    ) -> "WorkspaceAuthorizedApplicationFields":
        """Subfields should come from the WorkspaceAuthorizedApplicationFields class"""
        self._subfields.extend(subfields)
        return self

    def alias(self, alias: str) -> "WorkspaceAuthorizedApplicationFields":
        self._alias = alias
        return self
