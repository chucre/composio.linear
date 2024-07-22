from typing import Any, Dict, Optional

from . import UserFlagType, UserFlagUpdateOperation
from .custom_fields import (
    ApiKeyPayloadFields,
    AsksChannelConnectPayloadFields,
    AttachmentArchivePayloadFields,
    AttachmentPayloadFields,
    AuthResolverResponseFields,
    CommentPayloadFields,
    ContactPayloadFields,
    CreateCsvExportReportPayloadFields,
    CreateOrJoinOrganizationResponseFields,
    CustomerNeedPayloadFields,
    CustomerPayloadFields,
    CustomerStatusPayloadFields,
    CustomViewPayloadFields,
    CycleArchivePayloadFields,
    CyclePayloadFields,
    DeletePayloadFields,
    DiaryEntryPayloadFields,
    DocumentArchivePayloadFields,
    DocumentPayloadFields,
    EmailIntakeAddressPayloadFields,
    EmailUnsubscribePayloadFields,
    EmailUserAccountAuthChallengeResponseFields,
    EmojiPayloadFields,
    EntityExternalLinkPayloadFields,
    FavoritePayloadFields,
    FrontAttachmentPayloadFields,
    GitAutomationStatePayloadFields,
    GitAutomationTargetBranchPayloadFields,
    GitHubCommitIntegrationPayloadFields,
    GitHubEnterpriseServerPayloadFields,
    ImageUploadFromUrlPayloadFields,
    InitiativeArchivePayloadFields,
    InitiativePayloadFields,
    InitiativeToProjectPayloadFields,
    IntegrationPayloadFields,
    IntegrationRequestPayloadFields,
    IntegrationsSettingsPayloadFields,
    IntegrationTemplatePayloadFields,
    IssueArchivePayloadFields,
    IssueBatchPayloadFields,
    IssueImportDeletePayloadFields,
    IssueImportPayloadFields,
    IssueLabelPayloadFields,
    IssuePayloadFields,
    IssueRelationPayloadFields,
    LogoutResponseFields,
    NotificationArchivePayloadFields,
    NotificationBatchActionPayloadFields,
    NotificationPayloadFields,
    NotificationSubscriptionPayloadFields,
    OrganizationCancelDeletePayloadFields,
    OrganizationDeletePayloadFields,
    OrganizationDomainPayloadFields,
    OrganizationDomainSimplePayloadFields,
    OrganizationInvitePayloadFields,
    OrganizationPayloadFields,
    OrganizationStartTrialPayloadFields,
    PasskeyLoginStartResponseFields,
    ProjectArchivePayloadFields,
    ProjectLinkPayloadFields,
    ProjectMilestonePayloadFields,
    ProjectPayloadFields,
    ProjectRelationPayloadFields,
    ProjectUpdateInteractionPayloadFields,
    ProjectUpdatePayloadFields,
    ProjectUpdateReminderPayloadFields,
    ProjectUpdateWithInteractionPayloadFields,
    PushSubscriptionPayloadFields,
    ReactionPayloadFields,
    RoadmapArchivePayloadFields,
    RoadmapPayloadFields,
    RoadmapToProjectPayloadFields,
    SlackChannelConnectPayloadFields,
    SuccessPayloadFields,
    TeamArchivePayloadFields,
    TeamMembershipPayloadFields,
    TeamPayloadFields,
    TemplatePayloadFields,
    TimeSchedulePayloadFields,
    TriageResponsibilityPayloadFields,
    UploadPayloadFields,
    UserAdminPayloadFields,
    UserPayloadFields,
    UserSettingsFlagPayloadFields,
    UserSettingsFlagsResetPayloadFields,
    UserSettingsPayloadFields,
    ViewPreferencesPayloadFields,
    WebhookPayloadFields,
    WorkflowStateArchivePayloadFields,
    WorkflowStatePayloadFields,
)
from .input_types import (
    AirbyteConfigurationInput,
    ApiKeyCreateInput,
    AttachmentCreateInput,
    AttachmentUpdateInput,
    CommentCreateInput,
    CommentUpdateInput,
    ContactCreateInput,
    ContactSalesCreateInput,
    CreateOrganizationInput,
    CustomerCreateInput,
    CustomerNeedCreateInput,
    CustomerNeedUpdateInput,
    CustomerStatusCreateInput,
    CustomerStatusUpdateInput,
    CustomerUpdateInput,
    CustomViewCreateInput,
    CustomViewUpdateInput,
    CycleCreateInput,
    CycleShiftAllInput,
    CycleUpdateInput,
    DeleteOrganizationInput,
    DiaryEntryCreateInput,
    DiaryEntryUpdateInput,
    DocumentCreateInput,
    DocumentUpdateInput,
    EmailIntakeAddressCreateInput,
    EmailIntakeAddressUpdateInput,
    EmailUnsubscribeInput,
    EmailUserAccountAuthChallengeInput,
    EmojiCreateInput,
    EntityExternalLinkCreateInput,
    EntityExternalLinkUpdateInput,
    FavoriteCreateInput,
    FavoriteUpdateInput,
    GitAutomationStateCreateInput,
    GitAutomationStateUpdateInput,
    GitAutomationTargetBranchCreateInput,
    GitAutomationTargetBranchUpdateInput,
    GoogleUserAccountAuthInput,
    InitiativeCreateInput,
    InitiativeToProjectCreateInput,
    InitiativeToProjectUpdateInput,
    InitiativeUpdateInput,
    IntegrationRequestInput,
    IntegrationSettingsInput,
    IntegrationsSettingsCreateInput,
    IntegrationsSettingsUpdateInput,
    IntegrationTemplateCreateInput,
    IntercomSettingsInput,
    IssueCreateInput,
    IssueImportUpdateInput,
    IssueLabelCreateInput,
    IssueLabelUpdateInput,
    IssueRelationCreateInput,
    IssueRelationUpdateInput,
    IssueUpdateInput,
    JiraConfigurationInput,
    JiraUpdateInput,
    JoinOrganizationInput,
    NotificationEntityInput,
    NotificationSubscriptionCreateInput,
    NotificationSubscriptionUpdateInput,
    NotificationUpdateInput,
    OnboardingCustomerSurvey,
    OrganizationDomainCreateInput,
    OrganizationDomainUpdateInput,
    OrganizationDomainVerificationInput,
    OrganizationInviteCreateInput,
    OrganizationInviteUpdateInput,
    OrganizationUpdateInput,
    ProjectCreateInput,
    ProjectLinkCreateInput,
    ProjectLinkUpdateInput,
    ProjectMilestoneCreateInput,
    ProjectMilestoneUpdateInput,
    ProjectRelationCreateInput,
    ProjectRelationUpdateInput,
    ProjectUpdateCreateInput,
    ProjectUpdateInput,
    ProjectUpdateInteractionCreateInput,
    ProjectUpdateUpdateInput,
    PushSubscriptionCreateInput,
    ReactionCreateInput,
    RoadmapCreateInput,
    RoadmapToProjectCreateInput,
    RoadmapToProjectUpdateInput,
    RoadmapUpdateInput,
    TeamCreateInput,
    TeamMembershipCreateInput,
    TeamMembershipUpdateInput,
    TeamUpdateInput,
    TemplateCreateInput,
    TemplateUpdateInput,
    TimeScheduleCreateInput,
    TimeScheduleUpdateInput,
    TokenUserAccountAuthInput,
    TriageResponsibilityCreateInput,
    TriageResponsibilityUpdateInput,
    UserSettingsUpdateInput,
    UserUpdateInput,
    ViewPreferencesCreateInput,
    ViewPreferencesUpdateInput,
    WebhookCreateInput,
    WebhookUpdateInput,
    WorkflowStateCreateInput,
    WorkflowStateUpdateInput,
)


class Mutation:
    @classmethod
    def api_key_create(cls, input: ApiKeyCreateInput) -> ApiKeyPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ApiKeyCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ApiKeyPayloadFields(
            field_name="apiKeyCreate", arguments=cleared_arguments
        )

    @classmethod
    def api_key_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="apiKeyDelete", arguments=cleared_arguments
        )

    @classmethod
    def attachment_create(cls, input: AttachmentCreateInput) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "AttachmentCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentCreate", arguments=cleared_arguments
        )

    @classmethod
    def attachment_update(
        cls, input: AttachmentUpdateInput, id: str
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "AttachmentUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentUpdate", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_url(
        cls,
        url: str,
        issue_id: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "url": {"type": "String!", "value": url},
            "issueId": {"type": "String!", "value": issue_id},
            "id": {"type": "String", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkURL", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_git_lab_mr(
        cls,
        issue_id: str,
        url: str,
        project_path_with_namespace: str,
        number: float,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "issueId": {"type": "String!", "value": issue_id},
            "id": {"type": "String", "value": id},
            "url": {"type": "String!", "value": url},
            "projectPathWithNamespace": {
                "type": "String!",
                "value": project_path_with_namespace,
            },
            "number": {"type": "Float!", "value": number},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkGitLabMR", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_git_hub_issue(
        cls,
        issue_id: str,
        url: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "issueId": {"type": "String!", "value": issue_id},
            "id": {"type": "String", "value": id},
            "url": {"type": "String!", "value": url},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkGitHubIssue", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_git_hub_pr(
        cls,
        issue_id: str,
        url: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None,
        owner: Optional[str] = None,
        repo: Optional[str] = None,
        number: Optional[float] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "issueId": {"type": "String!", "value": issue_id},
            "id": {"type": "String", "value": id},
            "url": {"type": "String!", "value": url},
            "owner": {"type": "String", "value": owner},
            "repo": {"type": "String", "value": repo},
            "number": {"type": "Float", "value": number},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkGitHubPR", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_zendesk(
        cls,
        ticket_id: str,
        issue_id: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "ticketId": {"type": "String!", "value": ticket_id},
            "issueId": {"type": "String!", "value": issue_id},
            "id": {"type": "String", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkZendesk", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_discord(
        cls,
        issue_id: str,
        channel_id: str,
        message_id: str,
        url: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "issueId": {"type": "String!", "value": issue_id},
            "id": {"type": "String", "value": id},
            "channelId": {"type": "String!", "value": channel_id},
            "messageId": {"type": "String!", "value": message_id},
            "url": {"type": "String!", "value": url},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkDiscord", arguments=cleared_arguments
        )

    @classmethod
    def attachment_sync_to_slack(cls, id: str) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentSyncToSlack", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_slack(
        cls,
        issue_id: str,
        url: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        channel: Optional[str] = None,
        ts: Optional[str] = None,
        latest: Optional[str] = None,
        id: Optional[str] = None,
        sync_to_comment_thread: Optional[bool] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "channel": {"type": "String", "value": channel},
            "ts": {"type": "String", "value": ts},
            "latest": {"type": "String", "value": latest},
            "issueId": {"type": "String!", "value": issue_id},
            "url": {"type": "String!", "value": url},
            "id": {"type": "String", "value": id},
            "syncToCommentThread": {"type": "Boolean", "value": sync_to_comment_thread},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkSlack", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_front(
        cls,
        conversation_id: str,
        issue_id: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None
    ) -> FrontAttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "conversationId": {"type": "String!", "value": conversation_id},
            "issueId": {"type": "String!", "value": issue_id},
            "id": {"type": "String", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FrontAttachmentPayloadFields(
            field_name="attachmentLinkFront", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_intercom(
        cls,
        conversation_id: str,
        issue_id: str,
        *,
        create_as_user: Optional[str] = None,
        display_icon_url: Optional[str] = None,
        title: Optional[str] = None,
        id: Optional[str] = None
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "createAsUser": {"type": "String", "value": create_as_user},
            "displayIconUrl": {"type": "String", "value": display_icon_url},
            "title": {"type": "String", "value": title},
            "conversationId": {"type": "String!", "value": conversation_id},
            "id": {"type": "String", "value": id},
            "issueId": {"type": "String!", "value": issue_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkIntercom", arguments=cleared_arguments
        )

    @classmethod
    def attachment_link_jira_issue(
        cls, issue_id: str, jira_issue_id: str
    ) -> AttachmentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "issueId": {"type": "String!", "value": issue_id},
            "jiraIssueId": {"type": "String!", "value": jira_issue_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentPayloadFields(
            field_name="attachmentLinkJiraIssue", arguments=cleared_arguments
        )

    @classmethod
    def attachment_archive(cls, id: str) -> AttachmentArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AttachmentArchivePayloadFields(
            field_name="attachmentArchive", arguments=cleared_arguments
        )

    @classmethod
    def attachment_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="attachmentDelete", arguments=cleared_arguments
        )

    @classmethod
    def email_user_account_auth_challenge(
        cls, input: EmailUserAccountAuthChallengeInput
    ) -> EmailUserAccountAuthChallengeResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "EmailUserAccountAuthChallengeInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmailUserAccountAuthChallengeResponseFields(
            field_name="emailUserAccountAuthChallenge", arguments=cleared_arguments
        )

    @classmethod
    def email_token_user_account_auth(
        cls, input: TokenUserAccountAuthInput
    ) -> AuthResolverResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TokenUserAccountAuthInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AuthResolverResponseFields(
            field_name="emailTokenUserAccountAuth", arguments=cleared_arguments
        )

    @classmethod
    def saml_token_user_account_auth(
        cls, input: TokenUserAccountAuthInput
    ) -> AuthResolverResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TokenUserAccountAuthInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AuthResolverResponseFields(
            field_name="samlTokenUserAccountAuth", arguments=cleared_arguments
        )

    @classmethod
    def google_user_account_auth(
        cls, input: GoogleUserAccountAuthInput
    ) -> AuthResolverResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "GoogleUserAccountAuthInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AuthResolverResponseFields(
            field_name="googleUserAccountAuth", arguments=cleared_arguments
        )

    @classmethod
    def passkey_login_start(cls, auth_id: str) -> PasskeyLoginStartResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "authId": {"type": "String!", "value": auth_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PasskeyLoginStartResponseFields(
            field_name="passkeyLoginStart", arguments=cleared_arguments
        )

    @classmethod
    def passkey_login_finish(
        cls, response: Any, auth_id: str
    ) -> AuthResolverResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "response": {"type": "JSONObject!", "value": response},
            "authId": {"type": "String!", "value": auth_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AuthResolverResponseFields(
            field_name="passkeyLoginFinish", arguments=cleared_arguments
        )

    @classmethod
    def create_organization_from_onboarding(
        cls,
        input: CreateOrganizationInput,
        *,
        survey: Optional[OnboardingCustomerSurvey] = None
    ) -> CreateOrJoinOrganizationResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "survey": {"type": "OnboardingCustomerSurvey", "value": survey},
            "input": {"type": "CreateOrganizationInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreateOrJoinOrganizationResponseFields(
            field_name="createOrganizationFromOnboarding", arguments=cleared_arguments
        )

    @classmethod
    def join_organization_from_onboarding(
        cls, input: JoinOrganizationInput
    ) -> CreateOrJoinOrganizationResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "JoinOrganizationInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreateOrJoinOrganizationResponseFields(
            field_name="joinOrganizationFromOnboarding", arguments=cleared_arguments
        )

    @classmethod
    def leave_organization(
        cls, organization_id: str
    ) -> CreateOrJoinOrganizationResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationId": {"type": "String!", "value": organization_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreateOrJoinOrganizationResponseFields(
            field_name="leaveOrganization", arguments=cleared_arguments
        )

    @classmethod
    def logout(cls) -> LogoutResponseFields:
        return LogoutResponseFields(field_name="logout")

    @classmethod
    def logout_session(cls, session_id: str) -> LogoutResponseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "sessionId": {"type": "String!", "value": session_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return LogoutResponseFields(
            field_name="logoutSession", arguments=cleared_arguments
        )

    @classmethod
    def logout_all_sessions(cls) -> LogoutResponseFields:
        return LogoutResponseFields(field_name="logoutAllSessions")

    @classmethod
    def logout_other_sessions(cls) -> LogoutResponseFields:
        return LogoutResponseFields(field_name="logoutOtherSessions")

    @classmethod
    def comment_create(cls, input: CommentCreateInput) -> CommentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CommentCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CommentPayloadFields(
            field_name="commentCreate", arguments=cleared_arguments
        )

    @classmethod
    def comment_update(cls, input: CommentUpdateInput, id: str) -> CommentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CommentUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CommentPayloadFields(
            field_name="commentUpdate", arguments=cleared_arguments
        )

    @classmethod
    def comment_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="commentDelete", arguments=cleared_arguments
        )

    @classmethod
    def comment_resolve(
        cls, id: str, *, resolving_comment_id: Optional[str] = None
    ) -> CommentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "resolvingCommentId": {"type": "String", "value": resolving_comment_id},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CommentPayloadFields(
            field_name="commentResolve", arguments=cleared_arguments
        )

    @classmethod
    def comment_unresolve(cls, id: str) -> CommentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CommentPayloadFields(
            field_name="commentUnresolve", arguments=cleared_arguments
        )

    @classmethod
    def contact_create(cls, input: ContactCreateInput) -> ContactPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ContactCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ContactPayloadFields(
            field_name="contactCreate", arguments=cleared_arguments
        )

    @classmethod
    def contact_sales_create(
        cls, input: ContactSalesCreateInput
    ) -> ContactPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ContactSalesCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ContactPayloadFields(
            field_name="contactSalesCreate", arguments=cleared_arguments
        )

    @classmethod
    def customer_need_create(
        cls, input: CustomerNeedCreateInput
    ) -> CustomerNeedPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomerNeedCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerNeedPayloadFields(
            field_name="customerNeedCreate", arguments=cleared_arguments
        )

    @classmethod
    def customer_need_update(
        cls, input: CustomerNeedUpdateInput, id: str
    ) -> CustomerNeedPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomerNeedUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerNeedPayloadFields(
            field_name="customerNeedUpdate", arguments=cleared_arguments
        )

    @classmethod
    def customer_need_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="customerNeedDelete", arguments=cleared_arguments
        )

    @classmethod
    def customer_create(cls, input: CustomerCreateInput) -> CustomerPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomerCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerPayloadFields(
            field_name="customerCreate", arguments=cleared_arguments
        )

    @classmethod
    def customer_update(
        cls, input: CustomerUpdateInput, id: str
    ) -> CustomerPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomerUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerPayloadFields(
            field_name="customerUpdate", arguments=cleared_arguments
        )

    @classmethod
    def customer_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="customerDelete", arguments=cleared_arguments
        )

    @classmethod
    def customer_status_create(
        cls, input: CustomerStatusCreateInput
    ) -> CustomerStatusPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomerStatusCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerStatusPayloadFields(
            field_name="customerStatusCreate", arguments=cleared_arguments
        )

    @classmethod
    def customer_status_update(
        cls, input: CustomerStatusUpdateInput, id: str
    ) -> CustomerStatusPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomerStatusUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomerStatusPayloadFields(
            field_name="customerStatusUpdate", arguments=cleared_arguments
        )

    @classmethod
    def customer_status_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="customerStatusDelete", arguments=cleared_arguments
        )

    @classmethod
    def custom_view_create(
        cls, input: CustomViewCreateInput
    ) -> CustomViewPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomViewCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomViewPayloadFields(
            field_name="customViewCreate", arguments=cleared_arguments
        )

    @classmethod
    def custom_view_update(
        cls, input: CustomViewUpdateInput, id: str
    ) -> CustomViewPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CustomViewUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CustomViewPayloadFields(
            field_name="customViewUpdate", arguments=cleared_arguments
        )

    @classmethod
    def custom_view_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="customViewDelete", arguments=cleared_arguments
        )

    @classmethod
    def cycle_create(cls, input: CycleCreateInput) -> CyclePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CycleCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CyclePayloadFields(field_name="cycleCreate", arguments=cleared_arguments)

    @classmethod
    def cycle_update(cls, input: CycleUpdateInput, id: str) -> CyclePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CycleUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CyclePayloadFields(field_name="cycleUpdate", arguments=cleared_arguments)

    @classmethod
    def cycle_archive(cls, id: str) -> CycleArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CycleArchivePayloadFields(
            field_name="cycleArchive", arguments=cleared_arguments
        )

    @classmethod
    def cycle_shift_all(cls, input: CycleShiftAllInput) -> CyclePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "CycleShiftAllInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CyclePayloadFields(
            field_name="cycleShiftAll", arguments=cleared_arguments
        )

    @classmethod
    def diary_entry_create(
        cls, input: DiaryEntryCreateInput
    ) -> DiaryEntryPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "DiaryEntryCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DiaryEntryPayloadFields(
            field_name="diaryEntryCreate", arguments=cleared_arguments
        )

    @classmethod
    def diary_entry_update(
        cls, input: DiaryEntryUpdateInput, id: str
    ) -> DiaryEntryPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "DiaryEntryUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DiaryEntryPayloadFields(
            field_name="diaryEntryUpdate", arguments=cleared_arguments
        )

    @classmethod
    def diary_entry_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="diaryEntryDelete", arguments=cleared_arguments
        )

    @classmethod
    def document_create(cls, input: DocumentCreateInput) -> DocumentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "DocumentCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentPayloadFields(
            field_name="documentCreate", arguments=cleared_arguments
        )

    @classmethod
    def document_update(
        cls, input: DocumentUpdateInput, id: str
    ) -> DocumentPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "DocumentUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentPayloadFields(
            field_name="documentUpdate", arguments=cleared_arguments
        )

    @classmethod
    def document_delete(cls, id: str) -> DocumentArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentArchivePayloadFields(
            field_name="documentDelete", arguments=cleared_arguments
        )

    @classmethod
    def document_unarchive(cls, id: str) -> DocumentArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DocumentArchivePayloadFields(
            field_name="documentUnarchive", arguments=cleared_arguments
        )

    @classmethod
    def email_intake_address_create(
        cls, input: EmailIntakeAddressCreateInput
    ) -> EmailIntakeAddressPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "EmailIntakeAddressCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmailIntakeAddressPayloadFields(
            field_name="emailIntakeAddressCreate", arguments=cleared_arguments
        )

    @classmethod
    def email_intake_address_rotate(cls, id: str) -> EmailIntakeAddressPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmailIntakeAddressPayloadFields(
            field_name="emailIntakeAddressRotate", arguments=cleared_arguments
        )

    @classmethod
    def email_intake_address_update(
        cls, input: EmailIntakeAddressUpdateInput, id: str
    ) -> EmailIntakeAddressPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "EmailIntakeAddressUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmailIntakeAddressPayloadFields(
            field_name="emailIntakeAddressUpdate", arguments=cleared_arguments
        )

    @classmethod
    def email_intake_address_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="emailIntakeAddressDelete", arguments=cleared_arguments
        )

    @classmethod
    def email_unsubscribe(
        cls, input: EmailUnsubscribeInput
    ) -> EmailUnsubscribePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "EmailUnsubscribeInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmailUnsubscribePayloadFields(
            field_name="emailUnsubscribe", arguments=cleared_arguments
        )

    @classmethod
    def emoji_create(cls, input: EmojiCreateInput) -> EmojiPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "EmojiCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EmojiPayloadFields(field_name="emojiCreate", arguments=cleared_arguments)

    @classmethod
    def emoji_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="emojiDelete", arguments=cleared_arguments
        )

    @classmethod
    def entity_external_link_create(
        cls, input: EntityExternalLinkCreateInput
    ) -> EntityExternalLinkPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "EntityExternalLinkCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EntityExternalLinkPayloadFields(
            field_name="entityExternalLinkCreate", arguments=cleared_arguments
        )

    @classmethod
    def entity_external_link_update(
        cls, input: EntityExternalLinkUpdateInput, id: str
    ) -> EntityExternalLinkPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "EntityExternalLinkUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EntityExternalLinkPayloadFields(
            field_name="entityExternalLinkUpdate", arguments=cleared_arguments
        )

    @classmethod
    def entity_external_link_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="entityExternalLinkDelete", arguments=cleared_arguments
        )

    @classmethod
    def initiative_to_project_create(
        cls, input: InitiativeToProjectCreateInput
    ) -> InitiativeToProjectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "InitiativeToProjectCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeToProjectPayloadFields(
            field_name="initiativeToProjectCreate", arguments=cleared_arguments
        )

    @classmethod
    def initiative_to_project_update(
        cls, input: InitiativeToProjectUpdateInput, id: str
    ) -> InitiativeToProjectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "InitiativeToProjectUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeToProjectPayloadFields(
            field_name="initiativeToProjectUpdate", arguments=cleared_arguments
        )

    @classmethod
    def initiative_to_project_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="initiativeToProjectDelete", arguments=cleared_arguments
        )

    @classmethod
    def initiative_create(cls, input: InitiativeCreateInput) -> InitiativePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "InitiativeCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativePayloadFields(
            field_name="initiativeCreate", arguments=cleared_arguments
        )

    @classmethod
    def initiative_update(
        cls, input: InitiativeUpdateInput, id: str
    ) -> InitiativePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "InitiativeUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativePayloadFields(
            field_name="initiativeUpdate", arguments=cleared_arguments
        )

    @classmethod
    def initiative_archive(cls, id: str) -> InitiativeArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeArchivePayloadFields(
            field_name="initiativeArchive", arguments=cleared_arguments
        )

    @classmethod
    def initiative_unarchive(cls, id: str) -> InitiativeArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return InitiativeArchivePayloadFields(
            field_name="initiativeUnarchive", arguments=cleared_arguments
        )

    @classmethod
    def initiative_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="initiativeDelete", arguments=cleared_arguments
        )

    @classmethod
    def favorite_create(cls, input: FavoriteCreateInput) -> FavoritePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "FavoriteCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FavoritePayloadFields(
            field_name="favoriteCreate", arguments=cleared_arguments
        )

    @classmethod
    def favorite_update(
        cls, input: FavoriteUpdateInput, id: str
    ) -> FavoritePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "FavoriteUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return FavoritePayloadFields(
            field_name="favoriteUpdate", arguments=cleared_arguments
        )

    @classmethod
    def favorite_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="favoriteDelete", arguments=cleared_arguments
        )

    @classmethod
    def file_upload(
        cls,
        size: int,
        content_type: str,
        filename: str,
        *,
        meta_data: Optional[Any] = None,
        make_public: Optional[bool] = None
    ) -> UploadPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "metaData": {"type": "JSON", "value": meta_data},
            "makePublic": {"type": "Boolean", "value": make_public},
            "size": {"type": "Int!", "value": size},
            "contentType": {"type": "String!", "value": content_type},
            "filename": {"type": "String!", "value": filename},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UploadPayloadFields(field_name="fileUpload", arguments=cleared_arguments)

    @classmethod
    def import_file_upload(
        cls,
        size: int,
        content_type: str,
        filename: str,
        *,
        meta_data: Optional[Any] = None
    ) -> UploadPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "metaData": {"type": "JSON", "value": meta_data},
            "size": {"type": "Int!", "value": size},
            "contentType": {"type": "String!", "value": content_type},
            "filename": {"type": "String!", "value": filename},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UploadPayloadFields(
            field_name="importFileUpload", arguments=cleared_arguments
        )

    @classmethod
    def image_upload_from_url(cls, url: str) -> ImageUploadFromUrlPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "url": {"type": "String!", "value": url}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ImageUploadFromUrlPayloadFields(
            field_name="imageUploadFromUrl", arguments=cleared_arguments
        )

    @classmethod
    def git_automation_state_create(
        cls, input: GitAutomationStateCreateInput
    ) -> GitAutomationStatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "GitAutomationStateCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GitAutomationStatePayloadFields(
            field_name="gitAutomationStateCreate", arguments=cleared_arguments
        )

    @classmethod
    def git_automation_state_update(
        cls, input: GitAutomationStateUpdateInput, id: str
    ) -> GitAutomationStatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "GitAutomationStateUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GitAutomationStatePayloadFields(
            field_name="gitAutomationStateUpdate", arguments=cleared_arguments
        )

    @classmethod
    def git_automation_state_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="gitAutomationStateDelete", arguments=cleared_arguments
        )

    @classmethod
    def git_automation_target_branch_create(
        cls, input: GitAutomationTargetBranchCreateInput
    ) -> GitAutomationTargetBranchPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "GitAutomationTargetBranchCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GitAutomationTargetBranchPayloadFields(
            field_name="gitAutomationTargetBranchCreate", arguments=cleared_arguments
        )

    @classmethod
    def git_automation_target_branch_update(
        cls, input: GitAutomationTargetBranchUpdateInput, id: str
    ) -> GitAutomationTargetBranchPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "GitAutomationTargetBranchUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GitAutomationTargetBranchPayloadFields(
            field_name="gitAutomationTargetBranchUpdate", arguments=cleared_arguments
        )

    @classmethod
    def git_automation_target_branch_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="gitAutomationTargetBranchDelete", arguments=cleared_arguments
        )

    @classmethod
    def integration_request(
        cls, input: IntegrationRequestInput
    ) -> IntegrationRequestPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IntegrationRequestInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationRequestPayloadFields(
            field_name="integrationRequest", arguments=cleared_arguments
        )

    @classmethod
    def integration_settings_update(
        cls, input: IntegrationSettingsInput, id: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IntegrationSettingsInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationSettingsUpdate", arguments=cleared_arguments
        )

    @classmethod
    def integration_github_commit_create(cls) -> GitHubCommitIntegrationPayloadFields:
        return GitHubCommitIntegrationPayloadFields(
            field_name="integrationGithubCommitCreate"
        )

    @classmethod
    def integration_github_connect(
        cls, installation_id: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "installationId": {"type": "String!", "value": installation_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationGithubConnect", arguments=cleared_arguments
        )

    @classmethod
    def integration_github_import_connect(
        cls, installation_id: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "installationId": {"type": "String!", "value": installation_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationGithubImportConnect", arguments=cleared_arguments
        )

    @classmethod
    def integration_git_hub_enterprise_server_connect(
        cls, github_url: str, *, organization_name: Optional[str] = None
    ) -> GitHubEnterpriseServerPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationName": {"type": "String", "value": organization_name},
            "githubUrl": {"type": "String!", "value": github_url},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GitHubEnterpriseServerPayloadFields(
            field_name="integrationGitHubEnterpriseServerConnect",
            arguments=cleared_arguments,
        )

    @classmethod
    def integration_gitlab_connect(
        cls, gitlab_url: str, access_token: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "gitlabUrl": {"type": "String!", "value": gitlab_url},
            "accessToken": {"type": "String!", "value": access_token},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationGitlabConnect", arguments=cleared_arguments
        )

    @classmethod
    def airbyte_integration_connect(
        cls, input: AirbyteConfigurationInput
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "AirbyteConfigurationInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="airbyteIntegrationConnect", arguments=cleared_arguments
        )

    @classmethod
    def integration_google_calendar_personal_connect(
        cls, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "code": {"type": "String!", "value": code}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationGoogleCalendarPersonalConnect",
            arguments=cleared_arguments,
        )

    @classmethod
    def integration_launch_darkly_connect(
        cls, api_key: str, project_key: str, environment: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "apiKey": {"type": "String!", "value": api_key},
            "projectKey": {"type": "String!", "value": project_key},
            "environment": {"type": "String!", "value": environment},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationLaunchDarklyConnect", arguments=cleared_arguments
        )

    @classmethod
    def jira_integration_connect(
        cls, input: JiraConfigurationInput
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "JiraConfigurationInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="jiraIntegrationConnect", arguments=cleared_arguments
        )

    @classmethod
    def integration_jira_update(
        cls, input: JiraUpdateInput
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "JiraUpdateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationJiraUpdate", arguments=cleared_arguments
        )

    @classmethod
    def integration_jira_personal(
        cls, *, code: Optional[str] = None, access_token: Optional[str] = None
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "code": {"type": "String", "value": code},
            "accessToken": {"type": "String", "value": access_token},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationJiraPersonal", arguments=cleared_arguments
        )

    @classmethod
    def integration_git_hub_personal(cls, code: str) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "code": {"type": "String!", "value": code}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationGitHubPersonal", arguments=cleared_arguments
        )

    @classmethod
    def integration_intercom(
        cls, redirect_uri: str, code: str, *, domain_url: Optional[str] = None
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "domainUrl": {"type": "String", "value": domain_url},
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationIntercom", arguments=cleared_arguments
        )

    @classmethod
    def integration_intercom_delete(cls) -> IntegrationPayloadFields:
        return IntegrationPayloadFields(field_name="integrationIntercomDelete")

    @classmethod
    def integration_intercom_settings_update(
        cls, input: IntercomSettingsInput
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IntercomSettingsInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationIntercomSettingsUpdate", arguments=cleared_arguments
        )

    @classmethod
    def integration_discord(
        cls, redirect_uri: str, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationDiscord", arguments=cleared_arguments
        )

    @classmethod
    def integration_opsgenie_connect(cls, api_key: str) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "apiKey": {"type": "String!", "value": api_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationOpsgenieConnect", arguments=cleared_arguments
        )

    @classmethod
    def integration_opsgenie_refresh_schedule_mappings(cls) -> IntegrationPayloadFields:
        return IntegrationPayloadFields(
            field_name="integrationOpsgenieRefreshScheduleMappings"
        )

    @classmethod
    def integration_pager_duty_connect(
        cls, code: str, redirect_uri: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "code": {"type": "String!", "value": code},
            "redirectUri": {"type": "String!", "value": redirect_uri},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationPagerDutyConnect", arguments=cleared_arguments
        )

    @classmethod
    def integration_pager_duty_refresh_schedule_mappings(
        cls,
    ) -> IntegrationPayloadFields:
        return IntegrationPayloadFields(
            field_name="integrationPagerDutyRefreshScheduleMappings"
        )

    @classmethod
    def integration_update_slack(
        cls, redirect_uri: str, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationUpdateSlack", arguments=cleared_arguments
        )

    @classmethod
    def integration_slack(
        cls, redirect_uri: str, code: str, *, should_use_v_2_auth: Optional[bool] = None
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "shouldUseV2Auth": {"type": "Boolean", "value": should_use_v_2_auth},
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationSlack", arguments=cleared_arguments
        )

    @classmethod
    def integration_slack_asks(
        cls, redirect_uri: str, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationSlackAsks", arguments=cleared_arguments
        )

    @classmethod
    def integration_slack_personal(
        cls, redirect_uri: str, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationSlackPersonal", arguments=cleared_arguments
        )

    @classmethod
    def integration_asks_connect_channel(
        cls, redirect_uri: str, code: str
    ) -> AsksChannelConnectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AsksChannelConnectPayloadFields(
            field_name="integrationAsksConnectChannel", arguments=cleared_arguments
        )

    @classmethod
    def integration_slack_post(
        cls,
        redirect_uri: str,
        team_id: str,
        code: str,
        *,
        should_use_v_2_auth: Optional[bool] = None
    ) -> SlackChannelConnectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "shouldUseV2Auth": {"type": "Boolean", "value": should_use_v_2_auth},
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "teamId": {"type": "String!", "value": team_id},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SlackChannelConnectPayloadFields(
            field_name="integrationSlackPost", arguments=cleared_arguments
        )

    @classmethod
    def integration_slack_project_post(
        cls, service: str, redirect_uri: str, project_id: str, code: str
    ) -> SlackChannelConnectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "service": {"type": "String!", "value": service},
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "projectId": {"type": "String!", "value": project_id},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SlackChannelConnectPayloadFields(
            field_name="integrationSlackProjectPost", arguments=cleared_arguments
        )

    @classmethod
    def integration_slack_custom_view_notifications(
        cls, redirect_uri: str, custom_view_id: str, code: str
    ) -> SlackChannelConnectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "customViewId": {"type": "String!", "value": custom_view_id},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SlackChannelConnectPayloadFields(
            field_name="integrationSlackCustomViewNotifications",
            arguments=cleared_arguments,
        )

    @classmethod
    def integration_slack_org_project_updates_post(
        cls, redirect_uri: str, code: str
    ) -> SlackChannelConnectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SlackChannelConnectPayloadFields(
            field_name="integrationSlackOrgProjectUpdatesPost",
            arguments=cleared_arguments,
        )

    @classmethod
    def integration_slack_import_emojis(
        cls, redirect_uri: str, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationSlackImportEmojis", arguments=cleared_arguments
        )

    @classmethod
    def integration_figma(
        cls, redirect_uri: str, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationFigma", arguments=cleared_arguments
        )

    @classmethod
    def integration_google_sheets(cls, code: str) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "code": {"type": "String!", "value": code}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationGoogleSheets", arguments=cleared_arguments
        )

    @classmethod
    def refresh_google_sheets_data(cls, id: str) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="refreshGoogleSheetsData", arguments=cleared_arguments
        )

    @classmethod
    def integration_sentry_connect(
        cls, organization_slug: str, code: str, installation_id: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationSlug": {"type": "String!", "value": organization_slug},
            "code": {"type": "String!", "value": code},
            "installationId": {"type": "String!", "value": installation_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationSentryConnect", arguments=cleared_arguments
        )

    @classmethod
    def integration_front(
        cls, redirect_uri: str, code: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationFront", arguments=cleared_arguments
        )

    @classmethod
    def integration_zendesk(
        cls, subdomain: str, code: str, scope: str, redirect_uri: str
    ) -> IntegrationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "subdomain": {"type": "String!", "value": subdomain},
            "code": {"type": "String!", "value": code},
            "scope": {"type": "String!", "value": scope},
            "redirectUri": {"type": "String!", "value": redirect_uri},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationPayloadFields(
            field_name="integrationZendesk", arguments=cleared_arguments
        )

    @classmethod
    def integration_loom(cls) -> IntegrationPayloadFields:
        return IntegrationPayloadFields(field_name="integrationLoom")

    @classmethod
    def integration_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="integrationDelete", arguments=cleared_arguments
        )

    @classmethod
    def integration_archive(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="integrationArchive", arguments=cleared_arguments
        )

    @classmethod
    def integrations_settings_create(
        cls, input: IntegrationsSettingsCreateInput
    ) -> IntegrationsSettingsPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IntegrationsSettingsCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationsSettingsPayloadFields(
            field_name="integrationsSettingsCreate", arguments=cleared_arguments
        )

    @classmethod
    def integrations_settings_update(
        cls, input: IntegrationsSettingsUpdateInput, id: str
    ) -> IntegrationsSettingsPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IntegrationsSettingsUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationsSettingsPayloadFields(
            field_name="integrationsSettingsUpdate", arguments=cleared_arguments
        )

    @classmethod
    def integration_template_create(
        cls, input: IntegrationTemplateCreateInput
    ) -> IntegrationTemplatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IntegrationTemplateCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IntegrationTemplatePayloadFields(
            field_name="integrationTemplateCreate", arguments=cleared_arguments
        )

    @classmethod
    def integration_template_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="integrationTemplateDelete", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_create_github(
        cls,
        *,
        organization_id: Optional[str] = None,
        team_id: Optional[str] = None,
        team_name: Optional[str] = None,
        github_token: Optional[str] = None,
        github_repo_name: Optional[str] = None,
        github_repo_owner: Optional[str] = None,
        github_repo_id: Optional[str] = None,
        github_repo_ids: Optional[int] = None,
        integration_id: Optional[str] = None,
        github_should_import_org_projects: Optional[bool] = None,
        instant_process: Optional[bool] = None,
        include_closed_issues: Optional[bool] = None
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationId": {"type": "String", "value": organization_id},
            "teamId": {"type": "String", "value": team_id},
            "teamName": {"type": "String", "value": team_name},
            "githubToken": {"type": "String", "value": github_token},
            "githubRepoName": {"type": "String", "value": github_repo_name},
            "githubRepoOwner": {"type": "String", "value": github_repo_owner},
            "githubRepoId": {"type": "String", "value": github_repo_id},
            "githubRepoIds": {"type": "Int", "value": github_repo_ids},
            "integrationId": {"type": "String", "value": integration_id},
            "githubShouldImportOrgProjects": {
                "type": "Boolean",
                "value": github_should_import_org_projects,
            },
            "instantProcess": {"type": "Boolean", "value": instant_process},
            "includeClosedIssues": {"type": "Boolean", "value": include_closed_issues},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportCreateGithub", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_create_jira(
        cls,
        jira_token: str,
        jira_project: str,
        jira_email: str,
        jira_hostname: str,
        *,
        organization_id: Optional[str] = None,
        team_id: Optional[str] = None,
        team_name: Optional[str] = None,
        instant_process: Optional[bool] = None,
        include_closed_issues: Optional[bool] = None,
        id: Optional[str] = None
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationId": {"type": "String", "value": organization_id},
            "teamId": {"type": "String", "value": team_id},
            "teamName": {"type": "String", "value": team_name},
            "jiraToken": {"type": "String!", "value": jira_token},
            "jiraProject": {"type": "String!", "value": jira_project},
            "jiraEmail": {"type": "String!", "value": jira_email},
            "jiraHostname": {"type": "String!", "value": jira_hostname},
            "instantProcess": {"type": "Boolean", "value": instant_process},
            "includeClosedIssues": {"type": "Boolean", "value": include_closed_issues},
            "id": {"type": "String", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportCreateJira", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_create_csv_jira(
        cls,
        csv_url: str,
        *,
        organization_id: Optional[str] = None,
        team_id: Optional[str] = None,
        team_name: Optional[str] = None,
        jira_hostname: Optional[str] = None,
        jira_token: Optional[str] = None,
        jira_email: Optional[str] = None
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationId": {"type": "String", "value": organization_id},
            "teamId": {"type": "String", "value": team_id},
            "teamName": {"type": "String", "value": team_name},
            "csvUrl": {"type": "String!", "value": csv_url},
            "jiraHostname": {"type": "String", "value": jira_hostname},
            "jiraToken": {"type": "String", "value": jira_token},
            "jiraEmail": {"type": "String", "value": jira_email},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportCreateCSVJira", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_create_clubhouse(
        cls,
        clubhouse_token: str,
        clubhouse_group_name: str,
        *,
        organization_id: Optional[str] = None,
        team_id: Optional[str] = None,
        team_name: Optional[str] = None,
        instant_process: Optional[bool] = None,
        include_closed_issues: Optional[bool] = None,
        id: Optional[str] = None
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationId": {"type": "String", "value": organization_id},
            "teamId": {"type": "String", "value": team_id},
            "teamName": {"type": "String", "value": team_name},
            "clubhouseToken": {"type": "String!", "value": clubhouse_token},
            "clubhouseGroupName": {"type": "String!", "value": clubhouse_group_name},
            "instantProcess": {"type": "Boolean", "value": instant_process},
            "includeClosedIssues": {"type": "Boolean", "value": include_closed_issues},
            "id": {"type": "String", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportCreateClubhouse", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_create_asana(
        cls,
        asana_token: str,
        asana_team_name: str,
        *,
        organization_id: Optional[str] = None,
        team_id: Optional[str] = None,
        team_name: Optional[str] = None,
        instant_process: Optional[bool] = None,
        include_closed_issues: Optional[bool] = None,
        id: Optional[str] = None
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "organizationId": {"type": "String", "value": organization_id},
            "teamId": {"type": "String", "value": team_id},
            "teamName": {"type": "String", "value": team_name},
            "asanaToken": {"type": "String!", "value": asana_token},
            "asanaTeamName": {"type": "String!", "value": asana_team_name},
            "instantProcess": {"type": "Boolean", "value": instant_process},
            "includeClosedIssues": {"type": "Boolean", "value": include_closed_issues},
            "id": {"type": "String", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportCreateAsana", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_create_linear_v_2(
        cls, linear_source_organization_id: str, *, id: Optional[str] = None
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "linearSourceOrganizationId": {
                "type": "String!",
                "value": linear_source_organization_id,
            },
            "id": {"type": "String", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportCreateLinearV2", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_delete(
        cls, issue_import_id: str
    ) -> IssueImportDeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "issueImportId": {"type": "String!", "value": issue_import_id}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportDeletePayloadFields(
            field_name="issueImportDelete", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_process(
        cls, mapping: Any, issue_import_id: str
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "mapping": {"type": "JSONObject!", "value": mapping},
            "issueImportId": {"type": "String!", "value": issue_import_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportProcess", arguments=cleared_arguments
        )

    @classmethod
    def issue_import_update(
        cls, input: IssueImportUpdateInput, id: str
    ) -> IssueImportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IssueImportUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueImportPayloadFields(
            field_name="issueImportUpdate", arguments=cleared_arguments
        )

    @classmethod
    def issue_label_create(
        cls, input: IssueLabelCreateInput, *, replace_team_labels: Optional[bool] = None
    ) -> IssueLabelPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "replaceTeamLabels": {"type": "Boolean", "value": replace_team_labels},
            "input": {"type": "IssueLabelCreateInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueLabelPayloadFields(
            field_name="issueLabelCreate", arguments=cleared_arguments
        )

    @classmethod
    def issue_label_update(
        cls,
        input: IssueLabelUpdateInput,
        id: str,
        *,
        replace_team_labels: Optional[bool] = None
    ) -> IssueLabelPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "replaceTeamLabels": {"type": "Boolean", "value": replace_team_labels},
            "input": {"type": "IssueLabelUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueLabelPayloadFields(
            field_name="issueLabelUpdate", arguments=cleared_arguments
        )

    @classmethod
    def issue_label_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="issueLabelDelete", arguments=cleared_arguments
        )

    @classmethod
    def issue_relation_create(
        cls,
        input: IssueRelationCreateInput,
        *,
        override_created_at: Optional[Any] = None
    ) -> IssueRelationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "overrideCreatedAt": {"type": "DateTime", "value": override_created_at},
            "input": {"type": "IssueRelationCreateInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueRelationPayloadFields(
            field_name="issueRelationCreate", arguments=cleared_arguments
        )

    @classmethod
    def issue_relation_update(
        cls, input: IssueRelationUpdateInput, id: str
    ) -> IssueRelationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IssueRelationUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueRelationPayloadFields(
            field_name="issueRelationUpdate", arguments=cleared_arguments
        )

    @classmethod
    def issue_relation_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="issueRelationDelete", arguments=cleared_arguments
        )

    @classmethod
    def issue_create(cls, input: IssueCreateInput) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IssueCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(field_name="issueCreate", arguments=cleared_arguments)

    @classmethod
    def issue_update(cls, input: IssueUpdateInput, id: str) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IssueUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(field_name="issueUpdate", arguments=cleared_arguments)

    @classmethod
    def issue_batch_update(
        cls, input: IssueUpdateInput, ids: Any
    ) -> IssueBatchPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "IssueUpdateInput!", "value": input},
            "ids": {"type": "UUID!", "value": ids},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueBatchPayloadFields(
            field_name="issueBatchUpdate", arguments=cleared_arguments
        )

    @classmethod
    def issue_archive(
        cls, id: str, *, trash: Optional[bool] = None
    ) -> IssueArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "trash": {"type": "Boolean", "value": trash},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueArchivePayloadFields(
            field_name="issueArchive", arguments=cleared_arguments
        )

    @classmethod
    def issue_unarchive(cls, id: str) -> IssueArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueArchivePayloadFields(
            field_name="issueUnarchive", arguments=cleared_arguments
        )

    @classmethod
    def issue_delete(
        cls, id: str, *, permanently_delete: Optional[bool] = None
    ) -> IssueArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "permanentlyDelete": {"type": "Boolean", "value": permanently_delete},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssueArchivePayloadFields(
            field_name="issueDelete", arguments=cleared_arguments
        )

    @classmethod
    def issue_add_label(cls, label_id: str, id: str) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "labelId": {"type": "String!", "value": label_id},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(
            field_name="issueAddLabel", arguments=cleared_arguments
        )

    @classmethod
    def issue_remove_label(cls, label_id: str, id: str) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "labelId": {"type": "String!", "value": label_id},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(
            field_name="issueRemoveLabel", arguments=cleared_arguments
        )

    @classmethod
    def issue_reminder(cls, reminder_at: Any, id: str) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "reminderAt": {"type": "DateTime!", "value": reminder_at},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(
            field_name="issueReminder", arguments=cleared_arguments
        )

    @classmethod
    def issue_subscribe(
        cls, id: str, *, user_id: Optional[str] = None
    ) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "userId": {"type": "String", "value": user_id},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(
            field_name="issueSubscribe", arguments=cleared_arguments
        )

    @classmethod
    def issue_unsubscribe(
        cls, id: str, *, user_id: Optional[str] = None
    ) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "userId": {"type": "String", "value": user_id},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(
            field_name="issueUnsubscribe", arguments=cleared_arguments
        )

    @classmethod
    def issue_description_update_from_front(
        cls, description: str, id: str
    ) -> IssuePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "description": {"type": "String!", "value": description},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return IssuePayloadFields(
            field_name="issueDescriptionUpdateFromFront", arguments=cleared_arguments
        )

    @classmethod
    def notification_update(
        cls, input: NotificationUpdateInput, id: str
    ) -> NotificationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "NotificationUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationPayloadFields(
            field_name="notificationUpdate", arguments=cleared_arguments
        )

    @classmethod
    def notification_mark_read_all(
        cls, read_at: Any, input: NotificationEntityInput
    ) -> NotificationBatchActionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "readAt": {"type": "DateTime!", "value": read_at},
            "input": {"type": "NotificationEntityInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationBatchActionPayloadFields(
            field_name="notificationMarkReadAll", arguments=cleared_arguments
        )

    @classmethod
    def notification_mark_unread_all(
        cls, input: NotificationEntityInput
    ) -> NotificationBatchActionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "NotificationEntityInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationBatchActionPayloadFields(
            field_name="notificationMarkUnreadAll", arguments=cleared_arguments
        )

    @classmethod
    def notification_snooze_all(
        cls, snoozed_until_at: Any, input: NotificationEntityInput
    ) -> NotificationBatchActionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "snoozedUntilAt": {"type": "DateTime!", "value": snoozed_until_at},
            "input": {"type": "NotificationEntityInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationBatchActionPayloadFields(
            field_name="notificationSnoozeAll", arguments=cleared_arguments
        )

    @classmethod
    def notification_unsnooze_all(
        cls, unsnoozed_at: Any, input: NotificationEntityInput
    ) -> NotificationBatchActionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "unsnoozedAt": {"type": "DateTime!", "value": unsnoozed_at},
            "input": {"type": "NotificationEntityInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationBatchActionPayloadFields(
            field_name="notificationUnsnoozeAll", arguments=cleared_arguments
        )

    @classmethod
    def notification_archive(cls, id: str) -> NotificationArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationArchivePayloadFields(
            field_name="notificationArchive", arguments=cleared_arguments
        )

    @classmethod
    def notification_archive_all(
        cls, input: NotificationEntityInput
    ) -> NotificationBatchActionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "NotificationEntityInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationBatchActionPayloadFields(
            field_name="notificationArchiveAll", arguments=cleared_arguments
        )

    @classmethod
    def notification_unarchive(cls, id: str) -> NotificationArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationArchivePayloadFields(
            field_name="notificationUnarchive", arguments=cleared_arguments
        )

    @classmethod
    def notification_subscription_create(
        cls, input: NotificationSubscriptionCreateInput
    ) -> NotificationSubscriptionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "NotificationSubscriptionCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationSubscriptionPayloadFields(
            field_name="notificationSubscriptionCreate", arguments=cleared_arguments
        )

    @classmethod
    def notification_subscription_update(
        cls, input: NotificationSubscriptionUpdateInput, id: str
    ) -> NotificationSubscriptionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "NotificationSubscriptionUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return NotificationSubscriptionPayloadFields(
            field_name="notificationSubscriptionUpdate", arguments=cleared_arguments
        )

    @classmethod
    def notification_subscription_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="notificationSubscriptionDelete", arguments=cleared_arguments
        )

    @classmethod
    def organization_domain_claim(
        cls, id: str
    ) -> OrganizationDomainSimplePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationDomainSimplePayloadFields(
            field_name="organizationDomainClaim", arguments=cleared_arguments
        )

    @classmethod
    def organization_domain_verify(
        cls, input: OrganizationDomainVerificationInput
    ) -> OrganizationDomainPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "OrganizationDomainVerificationInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationDomainPayloadFields(
            field_name="organizationDomainVerify", arguments=cleared_arguments
        )

    @classmethod
    def organization_domain_create(
        cls,
        input: OrganizationDomainCreateInput,
        *,
        trigger_email_verification: Optional[bool] = None
    ) -> OrganizationDomainPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "triggerEmailVerification": {
                "type": "Boolean",
                "value": trigger_email_verification,
            },
            "input": {"type": "OrganizationDomainCreateInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationDomainPayloadFields(
            field_name="organizationDomainCreate", arguments=cleared_arguments
        )

    @classmethod
    def organization_domain_update(
        cls, input: OrganizationDomainUpdateInput, id: str
    ) -> OrganizationDomainPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "OrganizationDomainUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationDomainPayloadFields(
            field_name="organizationDomainUpdate", arguments=cleared_arguments
        )

    @classmethod
    def organization_domain_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="organizationDomainDelete", arguments=cleared_arguments
        )

    @classmethod
    def organization_invite_create(
        cls, input: OrganizationInviteCreateInput
    ) -> OrganizationInvitePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "OrganizationInviteCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationInvitePayloadFields(
            field_name="organizationInviteCreate", arguments=cleared_arguments
        )

    @classmethod
    def organization_invite_update(
        cls, input: OrganizationInviteUpdateInput, id: str
    ) -> OrganizationInvitePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "OrganizationInviteUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationInvitePayloadFields(
            field_name="organizationInviteUpdate", arguments=cleared_arguments
        )

    @classmethod
    def resend_organization_invite(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="resendOrganizationInvite", arguments=cleared_arguments
        )

    @classmethod
    def organization_invite_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="organizationInviteDelete", arguments=cleared_arguments
        )

    @classmethod
    def organization_update(
        cls, input: OrganizationUpdateInput
    ) -> OrganizationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "OrganizationUpdateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationPayloadFields(
            field_name="organizationUpdate", arguments=cleared_arguments
        )

    @classmethod
    def organization_delete_challenge(cls) -> OrganizationDeletePayloadFields:
        return OrganizationDeletePayloadFields(field_name="organizationDeleteChallenge")

    @classmethod
    def organization_delete(
        cls, input: DeleteOrganizationInput
    ) -> OrganizationDeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "DeleteOrganizationInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return OrganizationDeletePayloadFields(
            field_name="organizationDelete", arguments=cleared_arguments
        )

    @classmethod
    def organization_cancel_delete(cls) -> OrganizationCancelDeletePayloadFields:
        return OrganizationCancelDeletePayloadFields(
            field_name="organizationCancelDelete"
        )

    @classmethod
    def organization_start_trial(cls) -> OrganizationStartTrialPayloadFields:
        return OrganizationStartTrialPayloadFields(field_name="organizationStartTrial")

    @classmethod
    def project_link_create(
        cls, input: ProjectLinkCreateInput
    ) -> ProjectLinkPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectLinkCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectLinkPayloadFields(
            field_name="projectLinkCreate", arguments=cleared_arguments
        )

    @classmethod
    def project_link_update(
        cls, input: ProjectLinkUpdateInput, id: str
    ) -> ProjectLinkPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectLinkUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectLinkPayloadFields(
            field_name="projectLinkUpdate", arguments=cleared_arguments
        )

    @classmethod
    def project_link_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="projectLinkDelete", arguments=cleared_arguments
        )

    @classmethod
    def project_milestone_create(
        cls, input: ProjectMilestoneCreateInput
    ) -> ProjectMilestonePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectMilestoneCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectMilestonePayloadFields(
            field_name="projectMilestoneCreate", arguments=cleared_arguments
        )

    @classmethod
    def project_milestone_update(
        cls, input: ProjectMilestoneUpdateInput, id: str
    ) -> ProjectMilestonePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectMilestoneUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectMilestonePayloadFields(
            field_name="projectMilestoneUpdate", arguments=cleared_arguments
        )

    @classmethod
    def project_milestone_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="projectMilestoneDelete", arguments=cleared_arguments
        )

    @classmethod
    def project_relation_create(
        cls, input: ProjectRelationCreateInput
    ) -> ProjectRelationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectRelationCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectRelationPayloadFields(
            field_name="projectRelationCreate", arguments=cleared_arguments
        )

    @classmethod
    def project_relation_update(
        cls, input: ProjectRelationUpdateInput, id: str
    ) -> ProjectRelationPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectRelationUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectRelationPayloadFields(
            field_name="projectRelationUpdate", arguments=cleared_arguments
        )

    @classmethod
    def project_relation_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="projectRelationDelete", arguments=cleared_arguments
        )

    @classmethod
    def project_create(
        cls, input: ProjectCreateInput, *, connect_slack_channel: Optional[bool] = None
    ) -> ProjectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "connectSlackChannel": {"type": "Boolean", "value": connect_slack_channel},
            "input": {"type": "ProjectCreateInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectPayloadFields(
            field_name="projectCreate", arguments=cleared_arguments
        )

    @classmethod
    def project_update(cls, input: ProjectUpdateInput, id: str) -> ProjectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectPayloadFields(
            field_name="projectUpdate", arguments=cleared_arguments
        )

    @classmethod
    def project_reassign_status(
        cls, new_project_status_id: str, original_project_status_id: str
    ) -> SuccessPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "newProjectStatusId": {"type": "String!", "value": new_project_status_id},
            "originalProjectStatusId": {
                "type": "String!",
                "value": original_project_status_id,
            },
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return SuccessPayloadFields(
            field_name="projectReassignStatus", arguments=cleared_arguments
        )

    @classmethod
    def project_delete(cls, id: str) -> ProjectArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectArchivePayloadFields(
            field_name="projectDelete", arguments=cleared_arguments
        )

    @classmethod
    def project_archive(
        cls, id: str, *, trash: Optional[bool] = None
    ) -> ProjectArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "trash": {"type": "Boolean", "value": trash},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectArchivePayloadFields(
            field_name="projectArchive", arguments=cleared_arguments
        )

    @classmethod
    def project_unarchive(cls, id: str) -> ProjectArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectArchivePayloadFields(
            field_name="projectUnarchive", arguments=cleared_arguments
        )

    @classmethod
    def project_update_interaction_create(
        cls, input: ProjectUpdateInteractionCreateInput
    ) -> ProjectUpdateInteractionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectUpdateInteractionCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdateInteractionPayloadFields(
            field_name="projectUpdateInteractionCreate", arguments=cleared_arguments
        )

    @classmethod
    def project_update_create(
        cls, input: ProjectUpdateCreateInput
    ) -> ProjectUpdatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectUpdateCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdatePayloadFields(
            field_name="projectUpdateCreate", arguments=cleared_arguments
        )

    @classmethod
    def project_update_update(
        cls, input: ProjectUpdateUpdateInput, id: str
    ) -> ProjectUpdatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ProjectUpdateUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdatePayloadFields(
            field_name="projectUpdateUpdate", arguments=cleared_arguments
        )

    @classmethod
    def project_update_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="projectUpdateDelete", arguments=cleared_arguments
        )

    @classmethod
    def project_update_mark_as_read(
        cls, id: str
    ) -> ProjectUpdateWithInteractionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdateWithInteractionPayloadFields(
            field_name="projectUpdateMarkAsRead", arguments=cleared_arguments
        )

    @classmethod
    def create_project_update_reminder(
        cls, project_id: str, *, user_id: Optional[str] = None
    ) -> ProjectUpdateReminderPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "userId": {"type": "String", "value": user_id},
            "projectId": {"type": "String!", "value": project_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ProjectUpdateReminderPayloadFields(
            field_name="createProjectUpdateReminder", arguments=cleared_arguments
        )

    @classmethod
    def push_subscription_create(
        cls, input: PushSubscriptionCreateInput
    ) -> PushSubscriptionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "PushSubscriptionCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PushSubscriptionPayloadFields(
            field_name="pushSubscriptionCreate", arguments=cleared_arguments
        )

    @classmethod
    def push_subscription_delete(cls, id: str) -> PushSubscriptionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PushSubscriptionPayloadFields(
            field_name="pushSubscriptionDelete", arguments=cleared_arguments
        )

    @classmethod
    def reaction_create(cls, input: ReactionCreateInput) -> ReactionPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ReactionCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ReactionPayloadFields(
            field_name="reactionCreate", arguments=cleared_arguments
        )

    @classmethod
    def reaction_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="reactionDelete", arguments=cleared_arguments
        )

    @classmethod
    def create_csv_export_report(
        cls, *, include_private_team_ids: Optional[str] = None
    ) -> CreateCsvExportReportPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "includePrivateTeamIds": {
                "type": "String",
                "value": include_private_team_ids,
            }
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CreateCsvExportReportPayloadFields(
            field_name="createCsvExportReport", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_create(cls, input: RoadmapCreateInput) -> RoadmapPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "RoadmapCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapPayloadFields(
            field_name="roadmapCreate", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_update(cls, input: RoadmapUpdateInput, id: str) -> RoadmapPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "RoadmapUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapPayloadFields(
            field_name="roadmapUpdate", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_archive(cls, id: str) -> RoadmapArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapArchivePayloadFields(
            field_name="roadmapArchive", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_unarchive(cls, id: str) -> RoadmapArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapArchivePayloadFields(
            field_name="roadmapUnarchive", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="roadmapDelete", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_to_project_create(
        cls, input: RoadmapToProjectCreateInput
    ) -> RoadmapToProjectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "RoadmapToProjectCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapToProjectPayloadFields(
            field_name="roadmapToProjectCreate", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_to_project_update(
        cls, input: RoadmapToProjectUpdateInput, id: str
    ) -> RoadmapToProjectPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "RoadmapToProjectUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return RoadmapToProjectPayloadFields(
            field_name="roadmapToProjectUpdate", arguments=cleared_arguments
        )

    @classmethod
    def roadmap_to_project_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="roadmapToProjectDelete", arguments=cleared_arguments
        )

    @classmethod
    def team_key_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="teamKeyDelete", arguments=cleared_arguments
        )

    @classmethod
    def team_membership_create(
        cls, input: TeamMembershipCreateInput
    ) -> TeamMembershipPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TeamMembershipCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamMembershipPayloadFields(
            field_name="teamMembershipCreate", arguments=cleared_arguments
        )

    @classmethod
    def team_membership_update(
        cls, input: TeamMembershipUpdateInput, id: str
    ) -> TeamMembershipPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TeamMembershipUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamMembershipPayloadFields(
            field_name="teamMembershipUpdate", arguments=cleared_arguments
        )

    @classmethod
    def team_membership_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="teamMembershipDelete", arguments=cleared_arguments
        )

    @classmethod
    def team_create(
        cls, input: TeamCreateInput, *, copy_settings_from_team_id: Optional[str] = None
    ) -> TeamPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "copySettingsFromTeamId": {
                "type": "String",
                "value": copy_settings_from_team_id,
            },
            "input": {"type": "TeamCreateInput!", "value": input},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamPayloadFields(field_name="teamCreate", arguments=cleared_arguments)

    @classmethod
    def team_update(cls, input: TeamUpdateInput, id: str) -> TeamPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TeamUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamPayloadFields(field_name="teamUpdate", arguments=cleared_arguments)

    @classmethod
    def team_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(field_name="teamDelete", arguments=cleared_arguments)

    @classmethod
    def team_unarchive(cls, id: str) -> TeamArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamArchivePayloadFields(
            field_name="teamUnarchive", arguments=cleared_arguments
        )

    @classmethod
    def team_cycles_delete(cls, id: str) -> TeamPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TeamPayloadFields(
            field_name="teamCyclesDelete", arguments=cleared_arguments
        )

    @classmethod
    def template_create(cls, input: TemplateCreateInput) -> TemplatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TemplateCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TemplatePayloadFields(
            field_name="templateCreate", arguments=cleared_arguments
        )

    @classmethod
    def template_update(
        cls, input: TemplateUpdateInput, id: str
    ) -> TemplatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TemplateUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TemplatePayloadFields(
            field_name="templateUpdate", arguments=cleared_arguments
        )

    @classmethod
    def template_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="templateDelete", arguments=cleared_arguments
        )

    @classmethod
    def time_schedule_create(
        cls, input: TimeScheduleCreateInput
    ) -> TimeSchedulePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TimeScheduleCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimeSchedulePayloadFields(
            field_name="timeScheduleCreate", arguments=cleared_arguments
        )

    @classmethod
    def time_schedule_update(
        cls, input: TimeScheduleUpdateInput, id: str
    ) -> TimeSchedulePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TimeScheduleUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimeSchedulePayloadFields(
            field_name="timeScheduleUpdate", arguments=cleared_arguments
        )

    @classmethod
    def time_schedule_upsert_external(
        cls, input: TimeScheduleUpdateInput, external_id: str
    ) -> TimeSchedulePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TimeScheduleUpdateInput!", "value": input},
            "externalId": {"type": "String!", "value": external_id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimeSchedulePayloadFields(
            field_name="timeScheduleUpsertExternal", arguments=cleared_arguments
        )

    @classmethod
    def time_schedule_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="timeScheduleDelete", arguments=cleared_arguments
        )

    @classmethod
    def time_schedule_refresh_integration_schedule(
        cls, id: str
    ) -> TimeSchedulePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TimeSchedulePayloadFields(
            field_name="timeScheduleRefreshIntegrationSchedule",
            arguments=cleared_arguments,
        )

    @classmethod
    def triage_responsibility_create(
        cls, input: TriageResponsibilityCreateInput
    ) -> TriageResponsibilityPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TriageResponsibilityCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TriageResponsibilityPayloadFields(
            field_name="triageResponsibilityCreate", arguments=cleared_arguments
        )

    @classmethod
    def triage_responsibility_update(
        cls, input: TriageResponsibilityUpdateInput, id: str
    ) -> TriageResponsibilityPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "TriageResponsibilityUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TriageResponsibilityPayloadFields(
            field_name="triageResponsibilityUpdate", arguments=cleared_arguments
        )

    @classmethod
    def triage_responsibility_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="triageResponsibilityDelete", arguments=cleared_arguments
        )

    @classmethod
    def user_update(cls, input: UserUpdateInput, id: str) -> UserPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "UserUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserPayloadFields(field_name="userUpdate", arguments=cleared_arguments)

    @classmethod
    def user_discord_connect(cls, redirect_uri: str, code: str) -> UserPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "redirectUri": {"type": "String!", "value": redirect_uri},
            "code": {"type": "String!", "value": code},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserPayloadFields(
            field_name="userDiscordConnect", arguments=cleared_arguments
        )

    @classmethod
    def user_external_user_disconnect(cls, service: str) -> UserPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "service": {"type": "String!", "value": service}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserPayloadFields(
            field_name="userExternalUserDisconnect", arguments=cleared_arguments
        )

    @classmethod
    def user_promote_admin(cls, id: str) -> UserAdminPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserAdminPayloadFields(
            field_name="userPromoteAdmin", arguments=cleared_arguments
        )

    @classmethod
    def user_demote_admin(cls, id: str) -> UserAdminPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserAdminPayloadFields(
            field_name="userDemoteAdmin", arguments=cleared_arguments
        )

    @classmethod
    def user_promote_member(cls, id: str) -> UserAdminPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserAdminPayloadFields(
            field_name="userPromoteMember", arguments=cleared_arguments
        )

    @classmethod
    def user_demote_member(cls, id: str) -> UserAdminPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserAdminPayloadFields(
            field_name="userDemoteMember", arguments=cleared_arguments
        )

    @classmethod
    def user_suspend(cls, id: str) -> UserAdminPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserAdminPayloadFields(
            field_name="userSuspend", arguments=cleared_arguments
        )

    @classmethod
    def user_unsuspend(cls, id: str) -> UserAdminPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserAdminPayloadFields(
            field_name="userUnsuspend", arguments=cleared_arguments
        )

    @classmethod
    def user_settings_update(
        cls, input: UserSettingsUpdateInput, id: str
    ) -> UserSettingsPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "UserSettingsUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserSettingsPayloadFields(
            field_name="userSettingsUpdate", arguments=cleared_arguments
        )

    @classmethod
    def user_settings_flags_reset(
        cls, *, flags: Optional[UserFlagType] = None
    ) -> UserSettingsFlagsResetPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "flags": {"type": "UserFlagType", "value": flags}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserSettingsFlagsResetPayloadFields(
            field_name="userSettingsFlagsReset", arguments=cleared_arguments
        )

    @classmethod
    def user_flag_update(
        cls, operation: UserFlagUpdateOperation, flag: UserFlagType
    ) -> UserSettingsFlagPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "operation": {"type": "UserFlagUpdateOperation!", "value": operation},
            "flag": {"type": "UserFlagType!", "value": flag},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UserSettingsFlagPayloadFields(
            field_name="userFlagUpdate", arguments=cleared_arguments
        )

    @classmethod
    def view_preferences_create(
        cls, input: ViewPreferencesCreateInput
    ) -> ViewPreferencesPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ViewPreferencesCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ViewPreferencesPayloadFields(
            field_name="viewPreferencesCreate", arguments=cleared_arguments
        )

    @classmethod
    def view_preferences_update(
        cls, input: ViewPreferencesUpdateInput, id: str
    ) -> ViewPreferencesPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "ViewPreferencesUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ViewPreferencesPayloadFields(
            field_name="viewPreferencesUpdate", arguments=cleared_arguments
        )

    @classmethod
    def view_preferences_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="viewPreferencesDelete", arguments=cleared_arguments
        )

    @classmethod
    def webhook_create(cls, input: WebhookCreateInput) -> WebhookPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "WebhookCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WebhookPayloadFields(
            field_name="webhookCreate", arguments=cleared_arguments
        )

    @classmethod
    def webhook_update(cls, input: WebhookUpdateInput, id: str) -> WebhookPayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "WebhookUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WebhookPayloadFields(
            field_name="webhookUpdate", arguments=cleared_arguments
        )

    @classmethod
    def webhook_delete(cls, id: str) -> DeletePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DeletePayloadFields(
            field_name="webhookDelete", arguments=cleared_arguments
        )

    @classmethod
    def workflow_state_create(
        cls, input: WorkflowStateCreateInput
    ) -> WorkflowStatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "WorkflowStateCreateInput!", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkflowStatePayloadFields(
            field_name="workflowStateCreate", arguments=cleared_arguments
        )

    @classmethod
    def workflow_state_update(
        cls, input: WorkflowStateUpdateInput, id: str
    ) -> WorkflowStatePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "WorkflowStateUpdateInput!", "value": input},
            "id": {"type": "String!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkflowStatePayloadFields(
            field_name="workflowStateUpdate", arguments=cleared_arguments
        )

    @classmethod
    def workflow_state_archive(cls, id: str) -> WorkflowStateArchivePayloadFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "String!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return WorkflowStateArchivePayloadFields(
            field_name="workflowStateArchive", arguments=cleared_arguments
        )
