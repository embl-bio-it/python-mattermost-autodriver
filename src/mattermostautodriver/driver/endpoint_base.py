from .base import BaseDriver
from ..client import Client
from ..endpoints.access_control import AccessControl
from ..endpoints.agents import Agents
from ..endpoints.audit_logs import AuditLogs
from ..endpoints.authentication import Authentication
from ..endpoints.bleve import Bleve
from ..endpoints.bookmarks import Bookmarks
from ..endpoints.bots import Bots
from ..endpoints.brand import Brand
from ..endpoints.channels import Channels
from ..endpoints.cloud import Cloud
from ..endpoints.cluster import Cluster
from ..endpoints.commands import Commands
from ..endpoints.compliance import Compliance
from ..endpoints.conditions import Conditions
from ..endpoints.custom_profile_attributes import CustomProfileAttributes
from ..endpoints.data_retention import DataRetention
from ..endpoints.elasticsearch import Elasticsearch
from ..endpoints.emoji import Emoji
from ..endpoints.exports import Exports
from ..endpoints.files import Files
from ..endpoints.filtering import Filtering
from ..endpoints.group_message import GroupMessage
from ..endpoints.groups import Groups
from ..endpoints.imports import Imports
from ..endpoints.integration_actions import IntegrationActions
from ..endpoints.internal import Internal
from ..endpoints.ip import Ip
from ..endpoints.jobs import Jobs
from ..endpoints.ldap import Ldap
from ..endpoints.logs import Logs
from ..endpoints.metrics import Metrics
from ..endpoints.migrate import Migrate
from ..endpoints.o_auth import OAuth
from ..endpoints.oauth import Oauth
from ..endpoints.outgoing_connections import OutgoingConnections
from ..endpoints.outgoing_oauth_connections import OutgoingOauthConnections
from ..endpoints.permissions import Permissions
from ..endpoints.playbook_autofollows import PlaybookAutofollows
from ..endpoints.playbook_runs import PlaybookRuns
from ..endpoints.playbooks import Playbooks
from ..endpoints.plugins import Plugins
from ..endpoints.posts import Posts
from ..endpoints.preferences import Preferences
from ..endpoints.reactions import Reactions
from ..endpoints.remote_clusters import RemoteClusters
from ..endpoints.reports import Reports
from ..endpoints.roles import Roles
from ..endpoints.root import Root
from ..endpoints.saml import Saml
from ..endpoints.scheduled_post import ScheduledPost
from ..endpoints.schemes import Schemes
from ..endpoints.search import Search
from ..endpoints.shared_channels import SharedChannels
from ..endpoints.status import Status
from ..endpoints.system import System
from ..endpoints.teams import Teams
from ..endpoints.terms_of_service import TermsOfService
from ..endpoints.threads import Threads
from ..endpoints.timeline import Timeline
from ..endpoints.uploads import Uploads
from ..endpoints.usage import Usage
from ..endpoints.users import Users
from ..endpoints.webhooks import Webhooks
from ..endpoints_old.access_control import AccessControl as OldAccessControl
from ..endpoints_old.agents import Agents as OldAgents
from ..endpoints_old.audit_logs import AuditLogs as OldAuditLogs
from ..endpoints_old.authentication import Authentication as OldAuthentication
from ..endpoints_old.bleve import Bleve as OldBleve
from ..endpoints_old.bookmarks import Bookmarks as OldBookmarks
from ..endpoints_old.bots import Bots as OldBots
from ..endpoints_old.brand import Brand as OldBrand
from ..endpoints_old.channels import Channels as OldChannels
from ..endpoints_old.cloud import Cloud as OldCloud
from ..endpoints_old.cluster import Cluster as OldCluster
from ..endpoints_old.commands import Commands as OldCommands
from ..endpoints_old.compliance import Compliance as OldCompliance
from ..endpoints_old.conditions import Conditions as OldConditions
from ..endpoints_old.custom_profile_attributes import CustomProfileAttributes as OldCustomProfileAttributes
from ..endpoints_old.data_retention import DataRetention as OldDataRetention
from ..endpoints_old.elasticsearch import Elasticsearch as OldElasticsearch
from ..endpoints_old.emoji import Emoji as OldEmoji
from ..endpoints_old.exports import Exports as OldExports
from ..endpoints_old.files import Files as OldFiles
from ..endpoints_old.filtering import Filtering as OldFiltering
from ..endpoints_old.group_message import GroupMessage as OldGroupMessage
from ..endpoints_old.groups import Groups as OldGroups
from ..endpoints_old.imports import Imports as OldImports
from ..endpoints_old.integration_actions import IntegrationActions as OldIntegrationActions
from ..endpoints_old.internal import Internal as OldInternal
from ..endpoints_old.ip import Ip as OldIp
from ..endpoints_old.jobs import Jobs as OldJobs
from ..endpoints_old.ldap import Ldap as OldLdap
from ..endpoints_old.logs import Logs as OldLogs
from ..endpoints_old.metrics import Metrics as OldMetrics
from ..endpoints_old.migrate import Migrate as OldMigrate
from ..endpoints_old.o_auth import OAuth as OldOAuth
from ..endpoints_old.oauth import Oauth as OldOauth
from ..endpoints_old.outgoing_connections import OutgoingConnections as OldOutgoingConnections
from ..endpoints_old.outgoing_oauth_connections import OutgoingOauthConnections as OldOutgoingOauthConnections
from ..endpoints_old.permissions import Permissions as OldPermissions
from ..endpoints_old.playbook_autofollows import PlaybookAutofollows as OldPlaybookAutofollows
from ..endpoints_old.playbook_runs import PlaybookRuns as OldPlaybookRuns
from ..endpoints_old.playbooks import Playbooks as OldPlaybooks
from ..endpoints_old.plugins import Plugins as OldPlugins
from ..endpoints_old.posts import Posts as OldPosts
from ..endpoints_old.preferences import Preferences as OldPreferences
from ..endpoints_old.reactions import Reactions as OldReactions
from ..endpoints_old.remote_clusters import RemoteClusters as OldRemoteClusters
from ..endpoints_old.reports import Reports as OldReports
from ..endpoints_old.roles import Roles as OldRoles
from ..endpoints_old.root import Root as OldRoot
from ..endpoints_old.saml import Saml as OldSaml
from ..endpoints_old.scheduled_post import ScheduledPost as OldScheduledPost
from ..endpoints_old.schemes import Schemes as OldSchemes
from ..endpoints_old.search import Search as OldSearch
from ..endpoints_old.shared_channels import SharedChannels as OldSharedChannels
from ..endpoints_old.status import Status as OldStatus
from ..endpoints_old.system import System as OldSystem
from ..endpoints_old.teams import Teams as OldTeams
from ..endpoints_old.terms_of_service import TermsOfService as OldTermsOfService
from ..endpoints_old.threads import Threads as OldThreads
from ..endpoints_old.timeline import Timeline as OldTimeline
from ..endpoints_old.uploads import Uploads as OldUploads
from ..endpoints_old.usage import Usage as OldUsage
from ..endpoints_old.users import Users as OldUsers
from ..endpoints_old.webhooks import Webhooks as OldWebhooks


class BaseDriverWithEndpoints(BaseDriver):

    def __init__(self, options=None, client_cls=Client, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)
        self.access_control = OldAccessControl(self.client)
        self.agents = OldAgents(self.client)
        self.audit_logs = OldAuditLogs(self.client)
        self.authentication = OldAuthentication(self.client)
        self.bleve = OldBleve(self.client)
        self.bookmarks = OldBookmarks(self.client)
        self.bots = OldBots(self.client)
        self.brand = OldBrand(self.client)
        self.channels = OldChannels(self.client)
        self.cloud = OldCloud(self.client)
        self.cluster = OldCluster(self.client)
        self.commands = OldCommands(self.client)
        self.compliance = OldCompliance(self.client)
        self.conditions = OldConditions(self.client)
        self.custom_profile_attributes = OldCustomProfileAttributes(self.client)
        self.data_retention = OldDataRetention(self.client)
        self.elasticsearch = OldElasticsearch(self.client)
        self.emoji = OldEmoji(self.client)
        self.exports = OldExports(self.client)
        self.files = OldFiles(self.client)
        self.filtering = OldFiltering(self.client)
        self.group_message = OldGroupMessage(self.client)
        self.groups = OldGroups(self.client)
        self.imports = OldImports(self.client)
        self.integration_actions = OldIntegrationActions(self.client)
        self.internal = OldInternal(self.client)
        self.ip = OldIp(self.client)
        self.jobs = OldJobs(self.client)
        self.ldap = OldLdap(self.client)
        self.logs = OldLogs(self.client)
        self.metrics = OldMetrics(self.client)
        self.migrate = OldMigrate(self.client)
        self.o_auth = OldOAuth(self.client)
        self.oauth = OldOauth(self.client)
        self.outgoing_connections = OldOutgoingConnections(self.client)
        self.outgoing_oauth_connections = OldOutgoingOauthConnections(self.client)
        self.permissions = OldPermissions(self.client)
        self.playbook_autofollows = OldPlaybookAutofollows(self.client)
        self.playbook_runs = OldPlaybookRuns(self.client)
        self.playbooks = OldPlaybooks(self.client)
        self.plugins = OldPlugins(self.client)
        self.posts = OldPosts(self.client)
        self.preferences = OldPreferences(self.client)
        self.reactions = OldReactions(self.client)
        self.remote_clusters = OldRemoteClusters(self.client)
        self.reports = OldReports(self.client)
        self.roles = OldRoles(self.client)
        self.root = OldRoot(self.client)
        self.saml = OldSaml(self.client)
        self.scheduled_post = OldScheduledPost(self.client)
        self.schemes = OldSchemes(self.client)
        self.search = OldSearch(self.client)
        self.shared_channels = OldSharedChannels(self.client)
        self.status = OldStatus(self.client)
        self.system = OldSystem(self.client)
        self.teams = OldTeams(self.client)
        self.terms_of_service = OldTermsOfService(self.client)
        self.threads = OldThreads(self.client)
        self.timeline = OldTimeline(self.client)
        self.uploads = OldUploads(self.client)
        self.usage = OldUsage(self.client)
        self.users = OldUsers(self.client)
        self.webhooks = OldWebhooks(self.client)


class TypedBaseDriverWithEndpoints(BaseDriver):

    def __init__(self, options=None, client_cls=Client, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)
        self.access_control = AccessControl(self.client)
        self.agents = Agents(self.client)
        self.audit_logs = AuditLogs(self.client)
        self.authentication = Authentication(self.client)
        self.bleve = Bleve(self.client)
        self.bookmarks = Bookmarks(self.client)
        self.bots = Bots(self.client)
        self.brand = Brand(self.client)
        self.channels = Channels(self.client)
        self.cloud = Cloud(self.client)
        self.cluster = Cluster(self.client)
        self.commands = Commands(self.client)
        self.compliance = Compliance(self.client)
        self.conditions = Conditions(self.client)
        self.custom_profile_attributes = CustomProfileAttributes(self.client)
        self.data_retention = DataRetention(self.client)
        self.elasticsearch = Elasticsearch(self.client)
        self.emoji = Emoji(self.client)
        self.exports = Exports(self.client)
        self.files = Files(self.client)
        self.filtering = Filtering(self.client)
        self.group_message = GroupMessage(self.client)
        self.groups = Groups(self.client)
        self.imports = Imports(self.client)
        self.integration_actions = IntegrationActions(self.client)
        self.internal = Internal(self.client)
        self.ip = Ip(self.client)
        self.jobs = Jobs(self.client)
        self.ldap = Ldap(self.client)
        self.logs = Logs(self.client)
        self.metrics = Metrics(self.client)
        self.migrate = Migrate(self.client)
        self.o_auth = OAuth(self.client)
        self.oauth = Oauth(self.client)
        self.outgoing_connections = OutgoingConnections(self.client)
        self.outgoing_oauth_connections = OutgoingOauthConnections(self.client)
        self.permissions = Permissions(self.client)
        self.playbook_autofollows = PlaybookAutofollows(self.client)
        self.playbook_runs = PlaybookRuns(self.client)
        self.playbooks = Playbooks(self.client)
        self.plugins = Plugins(self.client)
        self.posts = Posts(self.client)
        self.preferences = Preferences(self.client)
        self.reactions = Reactions(self.client)
        self.remote_clusters = RemoteClusters(self.client)
        self.reports = Reports(self.client)
        self.roles = Roles(self.client)
        self.root = Root(self.client)
        self.saml = Saml(self.client)
        self.scheduled_post = ScheduledPost(self.client)
        self.schemes = Schemes(self.client)
        self.search = Search(self.client)
        self.shared_channels = SharedChannels(self.client)
        self.status = Status(self.client)
        self.system = System(self.client)
        self.teams = Teams(self.client)
        self.terms_of_service = TermsOfService(self.client)
        self.threads = Threads(self.client)
        self.timeline = Timeline(self.client)
        self.uploads = Uploads(self.client)
        self.usage = Usage(self.client)
        self.users = Users(self.client)
        self.webhooks = Webhooks(self.client)
