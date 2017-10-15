#!/usr/bin/env python3
import pytest
import os, sys
from cozify import hub, config, multisensor
from cozify.test import debug

class tmp_hub():
    """Creates a temporary hub section (with test data) in the current state.
    """
    def __init__(self):
        self.id = 'deadbeef-aaaa-bbbb-cccc-dddddddddddd'
        self.name = 'HubbyMcHubFace'
        self.section = 'Hubs.%s' % self.id
    def __enter__(self):
        config.state.add_section(self.section)
        config.state[self.section]['hubname'] = self.name
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            debug.logger.error("%s, %s, %s" % (exc_type, exc_value, traceback))
            return False
        config.state.remove_section(self.section)

@pytest.fixture
def tmphub(scope='module'):
    with tmp_hub() as hub:
        yield hub

def test_tz():
    hub.ping() # make sure we have valid auth

    # hand craft data needed for low-level api call _tz
    hubSection = 'Hubs.' + config.state['Hubs']['default']
    print(hub._tz(
        host=config.state[hubSection]['host'],
        hub_token=config.state[hubSection]['hubtoken'],
        cloud_token=config.state['Cloud']['remotetoken']
        ))

def test_hub_id_to_name(tmphub):
    assert hub.getHubName(tmphub.id) == tmphub.name

def test_hub_name_to_id(tmphub):
    assert hub.getHubId(tmphub.name) == tmphub.id

def test_multisensor():
    data = hub.getDevices()
    print(multisensor.getMultisensorData(data))