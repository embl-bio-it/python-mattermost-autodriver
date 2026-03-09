from ._base import Base

__all__ = ["Agents"]


class Agents(Base):

    def get_agents(self):
        """Get available agents
        `Read in Mattermost API docs (agents - GetAgents) <https://developers.mattermost.com/api-documentation/#/operations/GetAgents>`_

        """
        return self.client.get("""/api/v4/agents""")

    def get_agents_status(self):
        """Get agents bridge status
        `Read in Mattermost API docs (agents - GetAgentsStatus) <https://developers.mattermost.com/api-documentation/#/operations/GetAgentsStatus>`_

        """
        return self.client.get("""/api/v4/agents/status""")

    def get_llm_services(self):
        """Get available LLM services
        `Read in Mattermost API docs (agents - GetLLMServices) <https://developers.mattermost.com/api-documentation/#/operations/GetLLMServices>`_

        """
        return self.client.get("""/api/v4/llmservices""")
