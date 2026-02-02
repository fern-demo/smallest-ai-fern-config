"""
Atoms (Voice Agent) tests based on the Smallest AI cookbook examples.

These tests validate that the Fern-generated SDK can perform agent management
operations as demonstrated in the cookbook:
- https://github.com/smallest-inc/smallest-python-sdk (AtomsClient examples)
- https://github.com/smallest-inc/cookbook/tree/main/voice-agents

The tests validate the SDK interface matches cookbook expectations.
"""

import pytest
from unittest.mock import Mock, patch


class TestAtomsClientInterface:
    """Test that Atoms client interface matches cookbook expectations."""

    def test_atoms_client_accessible(self, client):
        """
        Cookbook: atoms_client = AtomsClient()
        Fern SDK: client.atoms
        """
        assert hasattr(client, 'atoms'), "Client should have 'atoms' attribute"

    def test_atoms_has_user_client(self, client):
        """Verify atoms has user management client."""
        assert hasattr(client.atoms, 'user'), "Atoms should have 'user' client"

    def test_atoms_has_organization_client(self, client):
        """Verify atoms has organization management client."""
        assert hasattr(client.atoms, 'organization'), "Atoms should have 'organization' client"

    def test_atoms_has_agent_templates_client(self, client):
        """Verify atoms has agent templates client."""
        assert hasattr(client.atoms, 'agent_templates'), "Atoms should have 'agent_templates' client"


class TestAgentOperations:
    """Test agent CRUD operations from cookbook."""

    def test_agents_client_exists(self, client):
        """
        Cookbook: atoms_client.create_agent(...)
        """
        assert hasattr(client.atoms, 'agents'), "Atoms should have 'agents' client"

    def test_agents_has_create_method(self, client):
        """
        Cookbook: agent_id = atoms_client.create_agent(create_agent_request={...})
        Fern SDK: client.atoms.agents.create_a_new_agent(name="...")
        """
        agents = client.atoms.agents
        assert hasattr(agents, 'create_a_new_agent'), \
            "Agents client should have 'create_a_new_agent' method"

    def test_agents_has_get_method(self, client):
        """
        Cookbook: atoms_client.get_agent_by_id(id=agent_id)
        """
        agents = client.atoms.agents
        assert hasattr(agents, 'get') or hasattr(agents, 'get_by_id') or hasattr(agents, 'get_agent_by_id'), \
            "Agents client should have a get method"

    def test_agents_has_list_method(self, client):
        """
        Cookbook: atoms_client.get_agents()
        Fern SDK: client.atoms.agents.get_all_agents()
        """
        agents = client.atoms.agents
        assert hasattr(agents, 'get_all_agents'), \
            "Agents client should have 'get_all_agents' method"

    def test_agents_has_update_method(self, client):
        """
        Cookbook: atoms_client.update_agent(id=agent_id, ...)
        Fern SDK: client.atoms.agents.update_an_agent(id="...")
        """
        agents = client.atoms.agents
        assert hasattr(agents, 'update_an_agent'), \
            "Agents client should have 'update_an_agent' method"

    def test_agents_has_delete_method(self, client):
        """
        Cookbook: atoms_client.delete_agent(id=agent_id)
        Fern SDK: client.atoms.agents.delete_an_agent(id="...")
        """
        agents = client.atoms.agents
        assert hasattr(agents, 'delete_an_agent'), \
            "Agents client should have 'delete_an_agent' method"


class TestCallOperations:
    """Test call operations from cookbook."""

    def test_calls_client_exists(self, client):
        """
        Cookbook: atoms_client.start_outbound_call(...)
        """
        assert hasattr(client.atoms, 'calls'), "Atoms should have 'calls' client"

    def test_calls_has_start_outbound_method(self, client):
        """
        Cookbook: call_response = atoms_client.start_outbound_call(
            start_outbound_call_request={
                "agent_id": MY_AGENT_ID,
                "phone_number": TARGET_PHONE_NUMBER,
            }
        )
        Fern SDK: client.atoms.calls.start_an_outbound_call(agent_id="...", phone_number="...")
        """
        calls = client.atoms.calls
        assert hasattr(calls, 'start_an_outbound_call'), \
            "Calls client should have 'start_an_outbound_call' method"


class TestKnowledgeBaseOperations:
    """Test knowledge base operations from cookbook."""

    def test_knowledge_base_client_exists(self, client):
        """
        Cookbook: atoms_client.create_knowledge_base(...)
        """
        assert hasattr(client.atoms, 'knowledge_base'), "Atoms should have 'knowledge_base' client"

    def test_knowledge_base_has_create_method(self, client):
        """
        Cookbook: knowledge_base = atoms_client.create_knowledge_base(...)
        Fern SDK: client.atoms.knowledge_base.create_a_knowledge_base(name="...")
        """
        kb = client.atoms.knowledge_base
        assert hasattr(kb, 'create_a_knowledge_base'), \
            "Knowledge base client should have 'create_a_knowledge_base' method"

    def test_knowledge_base_has_upload_method(self, client):
        """
        Cookbook: atoms_client.upload_media_to_knowledge_base(...)
        Fern SDK: client.atoms.knowledge_base.upload_a_pdf_file_to_a_knowledge_base(id="...", media=...)
        """
        kb = client.atoms.knowledge_base
        assert hasattr(kb, 'upload_a_pdf_file_to_a_knowledge_base'), \
            "Knowledge base client should have 'upload_a_pdf_file_to_a_knowledge_base' method"


class TestCampaignOperations:
    """Test campaign operations from cookbook."""

    def test_campaigns_client_exists(self, client):
        """
        Cookbook: Campaigns for bulk calling
        """
        assert hasattr(client.atoms, 'campaigns'), "Atoms should have 'campaigns' client"

    def test_campaigns_has_create_method(self, client):
        """
        Cookbook: Create campaign for bulk calling
        Fern SDK: client.atoms.campaigns.create_a_campaign(name="...", audience_id="...", agent_id="...")
        """
        campaigns = client.atoms.campaigns
        assert hasattr(campaigns, 'create_a_campaign'), \
            "Campaigns client should have 'create_a_campaign' method"

    def test_campaigns_has_list_method(self, client):
        """
        Cookbook: List campaigns
        Fern SDK: client.atoms.campaigns.retrieve_all_campaigns()
        """
        campaigns = client.atoms.campaigns
        assert hasattr(campaigns, 'retrieve_all_campaigns'), \
            "Campaigns client should have 'retrieve_all_campaigns' method"


class TestWorkflowOperations:
    """Test workflow operations from cookbook."""

    def test_workflows_client_exists(self, client):
        """
        Cookbook: Graph-based workflows to drive conversations
        """
        assert hasattr(client.atoms, 'workflows'), "Atoms should have 'workflows' client"


class TestLogsOperations:
    """Test logs operations from cookbook."""

    def test_logs_client_exists(self, client):
        """
        Cookbook: Access call logs
        """
        assert hasattr(client.atoms, 'logs'), "Atoms should have 'logs' client"


class TestPhoneNumbersOperations:
    """Test phone numbers operations."""

    def test_phone_numbers_client_exists(self, client):
        """
        Cookbook: Manage phone numbers
        """
        assert hasattr(client.atoms, 'phone_numbers'), "Atoms should have 'phone_numbers' client"


class TestWebhooksOperations:
    """Test webhooks operations."""

    def test_webhooks_client_exists(self, client):
        """
        Cookbook: Webhook subscriptions for events
        """
        assert hasattr(client.atoms, 'webhooks'), "Atoms should have 'webhooks' client"


class TestAudienceOperations:
    """Test audience operations from cookbook."""

    def test_audience_client_exists(self, client):
        """
        Cookbook: Audience (collection of contacts) for campaigns
        """
        assert hasattr(client.atoms, 'audience'), "Atoms should have 'audience' client"


class TestAsyncAtomsInterface:
    """Test async Atoms client interface."""

    def test_async_atoms_accessible(self, async_client):
        """Verify async client has atoms sub-client."""
        assert hasattr(async_client, 'atoms'), "Async client should have 'atoms' attribute"

    def test_async_atoms_has_agents(self, async_client):
        """Verify async atoms has agents client."""
        assert hasattr(async_client.atoms, 'agents'), "Async atoms should have 'agents' client"

    def test_async_atoms_has_calls(self, async_client):
        """Verify async atoms has calls client."""
        assert hasattr(async_client.atoms, 'calls'), "Async atoms should have 'calls' client"

    def test_async_atoms_has_knowledge_base(self, async_client):
        """Verify async atoms has knowledge_base client."""
        assert hasattr(async_client.atoms, 'knowledge_base'), "Async atoms should have 'knowledge_base' client"
