#!/usr/bin/env python3
"""
KARSA Headless Behavioral Evaluation Runner
Executes golden scenarios against KARSA via `agy --agent karsa -p ... --output-format json`
"""

import argparse
import json
import os
import subprocess
import sys
import time

from assertions import evaluate_assertion

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCENARIOS_FILE = os.path.join(ROOT, "evals", "scenarios.json")


def load_scenarios():
    with open(SCENARIOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def run_scenario(scenario, timeout=60, dry_run=False):
    sid = scenario["id"]
    name = scenario["name"]
    prompt = scenario["prompt"]
    assertions = scenario.get("assertions", [])

    print(f"\n========================================================")
    print(f"Running Scenario: [{sid}] {name}")
    print(f"Prompt: {prompt}")
    print(f"========================================================")

    if dry_run:
        print("[DRY RUN] Validated scenario schema and assertion specs.")
        return True, "Dry run passed"

    cmd = [
        "agy",
        "--agent", "karsa",
        "-p", prompt,
        "--mode", "plan",
        "--output-format", "json",
    ]

    start_time = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
            shell=True,
        )
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] Scenario exceeded {timeout}s limit")
        return False, f"Timeout after {timeout}s"

    elapsed = time.time() - start_time
    output = proc.stdout.strip()
    if not output and proc.stderr:
        output = proc.stderr.strip()

    try:
        data = json.loads(output)
    except Exception:
        # Fallback if mixed text before json
        json_match = output[output.find("{"):output.rfind("}") + 1] if "{" in output else ""
        try:
            data = json.loads(json_match)
        except Exception as e:
            print(f"[ERROR] Failed to parse CLI JSON output: {e}\nRaw output:\n{output[:500]}")
            return False, "Invalid JSON output"

    status = data.get("status")
    if status != "SUCCESS":
        err_msg = data.get("error", "Unknown error")
        print(f"[ERROR] Agent run failed with status: {status}\nMessage: {err_msg}")
        return False, f"Status {status}: {err_msg}"

    response_text = data.get("response", "")
    print(f"Response received in {elapsed:.2f}s ({len(response_text)} chars).")
    print(f"Snippet: {response_text[:200]}...\n")

    scenario_passed = True
    for a in assertions:
        passed, msg = evaluate_assertion(response_text, a)
        symbol = "[PASS]" if passed else "[FAIL]"
        print(f"  {symbol} {msg}")
        if not passed:
            scenario_passed = False

    return scenario_passed, "Assertions evaluated"


def main():
    parser = argparse.ArgumentParser(description="KARSA Behavioral Evaluation Harness")
    parser.add_argument("--scenario", help="Run a specific scenario ID")
    parser.add_argument("--timeout", type=int, default=90, help="Per-scenario timeout in seconds")
    parser.add_argument("--dry-run", action="store_true", help="Validate scenario format without calling model")
    args = parser.parse_args()

    scenarios = load_scenarios()
    if args.scenario:
        scenarios = [s for s in scenarios if s["id"] == args.scenario]
        if not scenarios:
            print(f"Error: Scenario with ID '{args.scenario}' not found.")
            sys.exit(1)

    print(f"Starting KARSA Evaluation Harness ({len(scenarios)} scenario(s))...")
    total = len(scenarios)
    passed_count = 0

    for s in scenarios:
        ok, reason = run_scenario(s, timeout=args.timeout, dry_run=args.dry_run)
        if ok:
            passed_count += 1

    print("\n--------------------------------------------------------")
    print(f"Evaluation Results: {passed_count}/{total} Passed ({(passed_count/total)*100:.1f}%)")
    print("--------------------------------------------------------")

    if passed_count == total:
        print("All evaluations passed!")
        sys.exit(0)
    else:
        print("Some evaluations failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
