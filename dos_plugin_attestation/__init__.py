"""Remote-attestation / confidential-computing verifier (TDX, SEV-SNP).

EXPERIMENTAL / INTERFACE ONLY. Verifies an attestation quote and yields a trust
boolean the kernel can consume (e.g. deny actions from an unattested workload).
Real verification requires vendor quote-verification libraries and endorsements.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class AttestationVerifier(Protocol):
    platform: str

    def is_trustworthy(self, quote: bytes) -> bool: ...


class StubVerifier:
    platform = "stub"

    def is_trustworthy(self, quote: bytes) -> bool:  # pragma: no cover
        raise NotImplementedError("Wire a TDX/SEV-SNP quote verifier here.")
