"""Smoke tests for package import and metadata."""

import lobbying_research


def test_version_defined() -> None:
    assert hasattr(lobbying_research, "__version__")
    assert isinstance(lobbying_research.__version__, str)
