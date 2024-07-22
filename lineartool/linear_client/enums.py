from enum import Enum


class AuthenticationSessionType(str, Enum):
    web = "web"
    desktop = "desktop"
    ios = "ios"
    android = "android"


class ReleaseChannel(str, Enum):
    internal = "internal"
    beta = "beta"
    preRelease = "preRelease"
    public = "public"


class OrganizationDomainAuthType(str, Enum):
    saml = "saml"
    general = "general"


class UserRoleType(str, Enum):
    admin = "admin"
    guest = "guest"
    user = "user"


class PaginationOrderBy(str, Enum):
    createdAt = "createdAt"
    updatedAt = "updatedAt"


class Day(str, Enum):
    Sunday = "Sunday"
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"


class SLADayCountType(str, Enum):
    all = "all"
    onlyBusinessDays = "onlyBusinessDays"


class ProjectUpdateReminderFrequency(str, Enum):
    week = "week"
    twoWeeks = "twoWeeks"
    month = "month"
    never = "never"


class DateResolutionType(str, Enum):
    month = "month"
    quarter = "quarter"
    halfYear = "halfYear"
    year = "year"


class ProjectUpdateHealthType(str, Enum):
    onTrack = "onTrack"
    atRisk = "atRisk"
    offTrack = "offTrack"


class SlackChannelType(str, Enum):
    DirectMessage = "DirectMessage"
    MultiPersonDirectMessage = "MultiPersonDirectMessage"
    Private = "Private"
    Public = "Public"


class GithubOrgType(str, Enum):
    user = "user"
    organization = "organization"


class SchemaFieldType(str, Enum):
    stringType = "stringType"
    numberType = "numberType"
    booleanType = "booleanType"
    dateType = "dateType"


class CustomerStatusType(str, Enum):
    active = "active"
    inactive = "inactive"


class IntegrationService(str, Enum):
    airbyte = "airbyte"
    discord = "discord"
    figma = "figma"
    figmaPlugin = "figmaPlugin"
    front = "front"
    github = "github"
    githubEnterpriseServer = "githubEnterpriseServer"
    githubCommit = "githubCommit"
    githubImport = "githubImport"
    githubPersonal = "githubPersonal"
    gitlab = "gitlab"
    googleCalendarPersonal = "googleCalendarPersonal"
    googleSheets = "googleSheets"
    intercom = "intercom"
    jira = "jira"
    jiraPersonal = "jiraPersonal"
    launchDarkly = "launchDarkly"
    loom = "loom"
    notion = "notion"
    opsgenie = "opsgenie"
    pagerDuty = "pagerDuty"
    slack = "slack"
    slackAsks = "slackAsks"
    slackCustomViewNotifications = "slackCustomViewNotifications"
    slackOrgProjectUpdatesPost = "slackOrgProjectUpdatesPost"
    slackPersonal = "slackPersonal"
    slackPost = "slackPost"
    slackProjectPost = "slackProjectPost"
    slackProjectUpdatesPost = "slackProjectUpdatesPost"
    sentry = "sentry"
    zendesk = "zendesk"
    email = "email"


class ContextViewType(str, Enum):
    activeIssues = "activeIssues"
    activeCycle = "activeCycle"
    upcomingCycle = "upcomingCycle"
    backlog = "backlog"
    triage = "triage"


class UserContextViewType(str, Enum):
    assigned = "assigned"


class InitiativeStatus(str, Enum):
    Planned = "Planned"
    Active = "Active"
    Completed = "Completed"


class FacetPageSource(str, Enum):
    projects = "projects"


class ProjectTab(str, Enum):
    documents = "documents"
    issues = "issues"


class InitiativeTab(str, Enum):
    overview = "overview"
    projects = "projects"


class FeatureFlagRolloutStageType(str, Enum):
    dev = "dev"
    internal = "internal"
    partial = "partial"
    full = "full"


class GitAutomationStates(str, Enum):
    draft = "draft"
    start = "start"
    review = "review"
    mergeable = "mergeable"
    merge = "merge"


class OAuthClientApprovalStatus(str, Enum):
    requested = "requested"
    approved = "approved"
    denied = "denied"


class ProjectStatusType(str, Enum):
    backlog = "backlog"
    planned = "planned"
    started = "started"
    paused = "paused"
    completed = "completed"
    canceled = "canceled"


class TriageResponsibilityAction(str, Enum):
    assign = "assign"
    notify = "notify"


class WorkflowType(str, Enum):
    sla = "sla"
    custom = "custom"
    viewSubscription = "viewSubscription"


class WorkflowTrigger(str, Enum):
    entityCreated = "entityCreated"
    entityUpdated = "entityUpdated"
    entityCreatedOrUpdated = "entityCreatedOrUpdated"
    entityRemoved = "entityRemoved"
    entityUnarchived = "entityUnarchived"


class WorkflowTriggerType(str, Enum):
    issue = "issue"
    project = "project"


class OrganizationInviteStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    expired = "expired"


class SlaStatus(str, Enum):
    Breached = "Breached"
    HighRisk = "HighRisk"
    MediumRisk = "MediumRisk"
    LowRisk = "LowRisk"
    Completed = "Completed"
    Failed = "Failed"


class PaginationNulls(str, Enum):
    first = "first"
    last = "last"


class PaginationSortOrder(str, Enum):
    Ascending = "Ascending"
    Descending = "Descending"


class IssueRelationType(str, Enum):
    blocks = "blocks"
    duplicate = "duplicate"
    related = "related"


class PushSubscriptionType(str, Enum):
    web = "web"
    apple = "apple"
    appleDevelopment = "appleDevelopment"
    firebase = "firebase"


class ViewPreferencesType(str, Enum):
    organization = "organization"
    user = "user"


class ViewType(str, Enum):
    inbox = "inbox"
    myIssues = "myIssues"
    myIssuesCreatedByMe = "myIssuesCreatedByMe"
    myIssuesSubscribedTo = "myIssuesSubscribedTo"
    myIssuesActivity = "myIssuesActivity"
    userProfile = "userProfile"
    userProfileCreatedByUser = "userProfileCreatedByUser"
    board = "board"
    completedCycle = "completedCycle"
    cycle = "cycle"
    project = "project"
    projectDocuments = "projectDocuments"
    label = "label"
    triage = "triage"
    activeIssues = "activeIssues"
    backlog = "backlog"
    allIssues = "allIssues"
    customView = "customView"
    customViews = "customViews"
    customRoadmap = "customRoadmap"
    roadmap = "roadmap"
    roadmaps = "roadmaps"
    roadmapAll = "roadmapAll"
    roadmapClosed = "roadmapClosed"
    roadmapBacklog = "roadmapBacklog"
    initiative = "initiative"
    initiativeOverview = "initiativeOverview"
    initiatives = "initiatives"
    initiativesPlanned = "initiativesPlanned"
    initiativesCompleted = "initiativesCompleted"
    projects = "projects"
    projectsAll = "projectsAll"
    projectsBacklog = "projectsBacklog"
    projectsClosed = "projectsClosed"
    search = "search"
    splitSearch = "splitSearch"
    teams = "teams"
    archive = "archive"
    quickView = "quickView"
    issueIdentifiers = "issueIdentifiers"


class SendStrategy(str, Enum):
    desktopThenPush = "desktopThenPush"
    desktopAndPush = "desktopAndPush"
    desktop = "desktop"
    push = "push"


class UserFlagType(str, Enum):
    updatedSlackThreadSyncIntegration = "updatedSlackThreadSyncIntegration"
    completedOnboarding = "completedOnboarding"
    desktopInstalled = "desktopInstalled"
    teamsPageIntroductionDismissed = "teamsPageIntroductionDismissed"
    joinTeamIntroductionDismissed = "joinTeamIntroductionDismissed"
    desktopDownloadToastDismissed = "desktopDownloadToastDismissed"
    emptyBacklogDismissed = "emptyBacklogDismissed"
    emptyCustomViewsDismissed = "emptyCustomViewsDismissed"
    emptyActiveIssuesDismissed = "emptyActiveIssuesDismissed"
    emptyMyIssuesDismissed = "emptyMyIssuesDismissed"
    triageWelcomeDismissed = "triageWelcomeDismissed"
    cycleWelcomeDismissed = "cycleWelcomeDismissed"
    projectWelcomeDismissed = "projectWelcomeDismissed"
    projectBacklogWelcomeDismissed = "projectBacklogWelcomeDismissed"
    projectUpdatesWelcomeDismissed = "projectUpdatesWelcomeDismissed"
    analyticsWelcomeDismissed = "analyticsWelcomeDismissed"
    insightsWelcomeDismissed = "insightsWelcomeDismissed"
    insightsHelpDismissed = "insightsHelpDismissed"
    figmaPromptDismissed = "figmaPromptDismissed"
    issueMovePromptCompleted = "issueMovePromptCompleted"
    migrateThemePreference = "migrateThemePreference"
    listSelectionTip = "listSelectionTip"
    emptyParagraphSlashCommandTip = "emptyParagraphSlashCommandTip"
    editorSlashCommandUsed = "editorSlashCommandUsed"
    canPlaySnake = "canPlaySnake"
    canPlayTetris = "canPlayTetris"
    importBannerDismissed = "importBannerDismissed"
    tryInvitePeopleDismissed = "tryInvitePeopleDismissed"
    tryRoadmapsDismissed = "tryRoadmapsDismissed"
    tryCyclesDismissed = "tryCyclesDismissed"
    tryTriageDismissed = "tryTriageDismissed"
    tryGithubDismissed = "tryGithubDismissed"
    rewindBannerDismissed = "rewindBannerDismissed"
    helpIslandFeatureInsightsDismissed = "helpIslandFeatureInsightsDismissed"
    dueDateShortcutMigration = "dueDateShortcutMigration"
    slackCommentReactionTipShown = "slackCommentReactionTipShown"
    issueLabelSuggestionUsed = "issueLabelSuggestionUsed"
    threadedCommentsNudgeIsSeen = "threadedCommentsNudgeIsSeen"
    desktopTabsOnboardingDismissed = "desktopTabsOnboardingDismissed"
    milestoneOnboardingIsSeenAndDismissed = "milestoneOnboardingIsSeenAndDismissed"
    projectBoardOnboardingIsSeenAndDismissed = (
        "projectBoardOnboardingIsSeenAndDismissed"
    )
    figmaPluginBannerDismissed = "figmaPluginBannerDismissed"
    initiativesBannerDismissed = "initiativesBannerDismissed"
    all = "all"


class UserFlagUpdateOperation(str, Enum):
    incr = "incr"
    decr = "decr"
    clear = "clear"
    lock = "lock"
