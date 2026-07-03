from dos_plugin_attestation import AttestationVerifier, StubVerifier
import pytest


def test_stub_matches_protocol_and_is_honest():
    assert isinstance(StubVerifier(), AttestationVerifier)
    with pytest.raises(NotImplementedError):
        StubVerifier().is_trustworthy(b"quote")
