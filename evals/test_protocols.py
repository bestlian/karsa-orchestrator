#!/usr/bin/env python3
"""
Deterministic Protocol & Contract Evals for KARSA (L1 Test Suite)
Runs statically without API tokens or network latency.
"""

import os
import re
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class TestKarsaProtocols(unittest.TestCase):

    def test_a2a_protocol_specification(self):
        a2a_path = os.path.join(ROOT, "skills", "karsa-orchestrator", "references", "a2a-protocol.md")
        self.assertTrue(os.path.isfile(a2a_path), "a2a-protocol.md must exist on disk")

        with open(a2a_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Envelope version
        self.assertIn("karsa-a2a/v1", content, "A2A protocol must specify 'karsa-a2a/v1' version")

        # Message status verbs
        for verb in ["HANDOFF", "DEFECT", "VERDICT", "STALE", "BLOCKER", "DIGEST"]:
            self.assertIn(verb, content, f"A2A protocol must define verb: {verb}")

        # Fix loop limit
        self.assertIn("round", content.lower())
        self.assertTrue(re.search(r"3\s*rounds?", content, re.IGNORECASE), "Fix loop must be bounded to 3 rounds")

    def test_depth_rubric_invariants(self):
        rubric_path = os.path.join(ROOT, "skills", "karsa-orchestrator", "references", "depth-rubric.md")
        self.assertTrue(os.path.isfile(rubric_path), "depth-rubric.md must exist on disk")

        with open(rubric_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Minimum line threshold and zero placeholder
        self.assertIn("30 substantive lines", content)
        self.assertIn("Zero-Placeholder", content)

        # Mandatory planning documents covered
        mandated_docs = [
            "04_functional_requirements.md",
            "05_domain_and_business_rules.md",
            "06_api_contract.md",
            "09_architecture_operations.md",
            "10_security_privacy.md",
            "11_quality_metrics_release.md",
            "12_insight_resolution_plan.md",
            "14_source_traceability.md",
            "15_execution_flow.md",
        ]
        for doc in mandated_docs:
            self.assertIn(doc, content, f"Depth rubric must explicitly define criteria for {doc}")

    def test_builder_workspace_isolation_and_merge_gate(self):
        skill_path = os.path.join(ROOT, "skills", "karsa-orchestrator", "SKILL.md")
        self.assertTrue(os.path.isfile(skill_path), "SKILL.md must exist on disk")

        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("Workspace: branch", content, "SKILL.md must specify isolated branch workspace for builder")
        self.assertIn("UAT Report", content, "SKILL.md must require UAT Report pass before merge")
        self.assertIn("Vulnerability Report", content, "SKILL.md must require Vulnerability Report pass before merge")
        self.assertIn("HEAD of `main` has not drifted", content, "SKILL.md must verify main HEAD drift before merge")

    def test_subagent_anti_prompt_injection_guardrail(self):
        subagents = [
            "delivery-planner",
            "integration-tester",
            "strict-programmer",
        ]
        for name in subagents:
            agent_file = os.path.join(ROOT, "agents", name, "agent.md")
            self.assertTrue(os.path.isfile(agent_file), f"agent.md missing for {name}")
            with open(agent_file, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertTrue(
                "Untrusted Data Isolation" in content or "Anti-Prompt Injection" in content,
                f"Agent {name} must declare Untrusted Data Isolation / Anti-Prompt Injection guardrail",
            )

    def test_artifacts_evidence_directory_contract(self):
        recon_path = os.path.join(ROOT, "skills", "karsa-orchestrator", "references", "evidence-reconciliation.md")
        self.assertTrue(os.path.isfile(recon_path), "evidence-reconciliation.md must exist")
        with open(recon_path, "r", encoding="utf-8") as f:
            content = f.read()

        mandated_artifact_dirs = [
            "artifacts/audit/dispatch-log.jsonl",
            "artifacts/handoffs/",
            "artifacts/proof/",
            "artifacts/implementation/",
            "artifacts/quality/",
            "artifacts/security/",
            "artifacts/release/",
            "artifacts/increment_manifest.md",
        ]
        for adir in mandated_artifact_dirs:
            self.assertIn(adir, content, f"evidence-reconciliation.md must mandate: {adir}")

        skill_path = os.path.join(ROOT, "skills", "karsa-orchestrator", "SKILL.md")
        with open(skill_path, "r", encoding="utf-8") as f:
            skill_content = f.read()
        self.assertIn("artifacts/audit/dispatch-log.jsonl", skill_content)

    def test_dispatch_ledger_schema(self):
        # Validate sample valid entry
        sample_entry = {
            "timestamp": "2026-10-12T14:40:00Z",
            "dispatch_id": "DSP-001",
            "agent": "strict-programmer",
            "model": "flash",
            "workspace": "branch",
            "phase": "S0",
            "item_id": "FEAT-001",
            "rounds": 1,
            "status": "PASS",
            "evidence_path": "artifacts/implementation/FEAT-001-implementation-report.md",
            "failure_category": None,
        }

        required_keys = {
            "timestamp", "dispatch_id", "agent", "model", "workspace",
            "phase", "item_id", "rounds", "status", "evidence_path", "failure_category"
        }
        self.assertEqual(set(sample_entry.keys()), required_keys)
        self.assertIn(sample_entry["status"], ["PASS", "FAIL", "BLOCKED", "STALE_CHECKSUM"])
        self.assertTrue(sample_entry["evidence_path"].startswith("artifacts/"))
        self.assertIsInstance(sample_entry["rounds"], int)

    def test_version_parity(self):
        import json
        with open(os.path.join(ROOT, "plugin.json"), "r", encoding="utf-8") as f:
            plugin_ver = json.load(f).get("version")
        with open(os.path.join(ROOT, "CHANGELOG.md"), "r", encoding="utf-8") as f:
            match = re.search(r"^##\s*\[([0-9]+\.[0-9]+\.[0-9]+)\]", f.read(), re.MULTILINE)
        self.assertIsNotNone(match, "CHANGELOG.md must define a version header")
        self.assertEqual(plugin_ver, match.group(1), "plugin.json version must match CHANGELOG.md")


if __name__ == "__main__":
    unittest.main()

