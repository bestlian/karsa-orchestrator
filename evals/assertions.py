"""
Deterministic Assertion Engine for KARSA Behavioral & Contract Evals
"""

from typing import Any, Dict, List, Tuple


def evaluate_assertion(response_text: str, assertion: Dict[str, Any]) -> Tuple[bool, str]:
    atype = assertion.get("type")
    desc = assertion.get("description", atype)
    text_lower = response_text.lower()

    if atype == "contains":
        val = assertion.get("value", "").lower()
        passed = val in text_lower
        reason = f"Expected '{val}' to be in response" if not passed else "OK"
        return passed, f"{desc}: {reason}"

    elif atype == "contains_any":
        vals = [v.lower() for v in assertion.get("values", [])]
        passed = any(v in text_lower for v in vals)
        reason = f"Expected at least one of {vals} to be in response" if not passed else "OK"
        return passed, f"{desc}: {reason}"

    elif atype == "not_contains":
        val = assertion.get("value", "").lower()
        passed = val not in text_lower
        reason = f"Forbidden string '{val}' found in response" if not passed else "OK"
        return passed, f"{desc}: {reason}"

    elif atype == "not_contains_any":
        vals = [v.lower() for v in assertion.get("values", [])]
        found = [v for v in vals if v in text_lower]
        passed = len(found) == 0
        reason = f"Forbidden values {found} found in response" if not passed else "OK"
        return passed, f"{desc}: {reason}"

    else:
        return False, f"Unknown assertion type: {atype}"
