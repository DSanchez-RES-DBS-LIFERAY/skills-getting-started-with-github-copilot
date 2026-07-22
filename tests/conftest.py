from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Preserve and restore the in-memory store so tests do not leak state.
    original_state = deepcopy(activities)
    yield
    activities.clear()
    activities.update(deepcopy(original_state))
