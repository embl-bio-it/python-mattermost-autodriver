from .base import BaseDriver
from ..client import Client
from endpoints.authentication import Authentication
from endpoints.bleve import Bleve
from endpoints.bookmarks import Bookmarks
from endpoints.bots import Bots
from endpoints.brand import Brand
from endpoints.channels import Channels
from endpoints.cloud import Cloud
from endpoints.cluster import Cluster
from endpoints.commands import Commands
from endpoints.compliance import Compliance
from endpoints.custom_profile_attributes import CustomProfileAttributes
from endpoints.data_retention import DataRetention
from endpoints.elasticsearch import Elasticsearch
from endpoints.emoji import Emoji
from endpoints.exports import Exports
from endpoints.files import Files
from endpoints.filtering import Filtering
from endpoints.groups import Groups
from endpoints.imports import Imports
from endpoints.integration_actions import IntegrationActions
from endpoints.internal import Internal
from endpoints.ip import Ip
from endpoints.jobs import Jobs
from endpoints.ldap import Ldap
from endpoints.logs import Logs
from endpoints.metrics import Metrics
from endpoints.migrate import Migrate
from endpoints.oauth import Oauth
from endpoints.outgoing_connections import OutgoingConnections
from endpoints.outgoing_oauth_connections import OutgoingOauthConnections
from endpoints.permissions import Permissions
from endpoints.playbookautofollows import PlaybookAutofollows
from endpoints.playbookruns import PlaybookRuns
from endpoints.playbooks import Playbooks
from endpoints.plugins import Plugins
from endpoints.posts import Posts
from endpoints.preferences import Preferences
from endpoints.reactions import Reactions
from endpoints.remote_clusters import RemoteClusters
from endpoints.reports import Reports
from endpoints.roles import Roles
from endpoints.root import Root
from endpoints.saml import SAML
from endpoints.scheduled_post import ScheduledPost
from endpoints.schemes import Schemes
from endpoints.search import Search
from endpoints.shared_channels import SharedChannels
from endpoints.status import Status
from endpoints.system import System
from endpoints.teams import Teams
from endpoints.terms_of_service import TermsOfService
from endpoints.threads import Threads
from endpoints.timeline import Timeline
from endpoints.uploads import Uploads
from endpoints.usage import Usage
from endpoints.users import Users
from endpoints.webhooks import Webhooks


class BaseDriverWithEndpoints(BaseDriver):

    def __init__(self, options=None, client_cls=Client, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)
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
        self.custom_profile_attributes = CustomProfileAttributes(self.client)
        self.data_retention = DataRetention(self.client)
        self.elasticsearch = Elasticsearch(self.client)
        self.emoji = Emoji(self.client)
        self.exports = Exports(self.client)
        self.files = Files(self.client)
        self.filtering = Filtering(self.client)
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
        self.oauth = Oauth(self.client)
        self.outgoing_connections = OutgoingConnections(self.client)
        self.outgoing_oauth_connections = OutgoingOauthConnections(self.client)
        self.permissions = Permissions(self.client)
        self.playbookautofollows = PlaybookAutofollows(self.client)
        self.playbookruns = PlaybookRuns(self.client)
        self.playbooks = Playbooks(self.client)
        self.plugins = Plugins(self.client)
        self.posts = Posts(self.client)
        self.preferences = Preferences(self.client)
        self.reactions = Reactions(self.client)
        self.remote_clusters = RemoteClusters(self.client)
        self.reports = Reports(self.client)
        self.roles = Roles(self.client)
        self.root = Root(self.client)
        self.saml = SAML(self.client)
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
