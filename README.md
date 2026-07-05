# plugin-attestation

Remote-attestation / confidential-computing verifier seam for the Decision OS /
AuthGate stack.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Plugins are advisory only and hold
> **no authority**; the kernel remains the single authority.

**Status: interface-only (Protocol + honest stub).**

## What it does

Defines the `AttestationVerifier` seam: verify a remote-attestation quote from a
confidential-computing platform (Intel TDX, AMD SEV-SNP) and yield a trust boolean
the kernel can consume — e.g. deny actions originating from an unattested workload.

## Authority

This plugin holds **no authority**. It only produces a trust signal; the kernel
decides what to do with it.

## Install

```bash
pip install "decision-os-min @ git+https://github.com/Aliipou/decision-os-min.git"
pip install -e . --no-deps
pytest -q          # AUTHGATE_BACKEND=python
```

## Usage

```python
from dos_plugin_attestation import AttestationVerifier, StubVerifier
isinstance(StubVerifier(), AttestationVerifier)   # True
# StubVerifier().is_trustworthy(quote) raises NotImplementedError by design.
```

## Status and limitations

- **Interface only.** `StubVerifier` deliberately raises `NotImplementedError`.
  Real verification requires vendor quote-verification libraries and endorsement
  chains (TDX/SEV-SNP), which are not implemented here and require real hardware
  to test.
