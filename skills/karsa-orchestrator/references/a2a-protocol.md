# KARSA A2A Handoff Protocol (`karsa-a2a/v1`)

Defines how dispatched agents hand work to each other and report to the lead. Read with `## Team Dispatch Protocol` in `../SKILL.md`.

## Transport Facts

Verified by probe on 2026-10-12 with two sibling `self` subagents:

- `send_message` between siblings works when the recipient is a conversation ID returned by `invoke_subagent`.
- The receiver sees the sender's ID in the message metadata (`sender=<id>`) and can reply to it.
- An idle subagent is woken by an incoming message.

Not verified, so never relied on: message delivery across a host restart. A restart stops every subagent and in-flight messages are lost. Therefore messages carry pointers; the truth lives on disk.

## Principles

1. **Pointers, not payloads.** A message names artifacts and a handoff file. Evidence, logs, and diffs live in the handoff file, never in the message body.
2. **Disk is truth.** A receiver acts on what it reads at the stated paths and checksum, not on what the message says.
3. **The lead sees everything.** Every direct message is followed by a one-line `DIGEST` to the lead.
4. **Only whitelisted edges are direct.** Everything else goes through the lead.
5. **Loops are bounded.** At most 3 rounds per item, then escalate.
6. **Nobody but the lead approves or talks to the user.** No message type carries approval.

## Peer Registry

The lead gives every dispatched agent a `peers` map in its Dispatch Brief: role name to conversation ID, plus `lead`. An agent never guesses or invents an ID. If a needed peer is missing from `peers`, it sends `BLOCKER` to the lead.

Spawn order: start the receiver first with instructions to end its turn and wait, then start the sender with the receiver's ID in `peers`. The incoming message wakes the receiver.

## Envelope

Every message starts with this block. The body after it is at most 10 lines.

```
karsa-a2a/v1
message_id: <item>-<seq>          e.g. US-014-003
type: HANDOFF | DEFECT | VERDICT | BLOCKER | QUESTION | STALE | DIGEST
from: <role>
to: <role>
in_reply_to: <message_id | none>
item: <backlog id>
round: <1..3>
scope_checksum: <sha256 of the listed source/config/test files, sorted by path>
branch: <git branch name in worktree>
commit_sha: <git commit sha on branch>
handoff_file: artifacts/handoffs/<message_id>.md
action_requested: <one sentence>
```

`scope_checksum` covers executable, configuration, test, and source files in scope only. Governance documents do not change it.

## Handoff File

Written before the message is sent, at `<project-root>/artifacts/handoffs/<message_id>.md`:

- **Subject:** item ID and one-line intent.
- **Scope:** paths covered and the `scope_checksum`.
- **What changed:** per path, one line.
- **Commands run:** exact command, environment, raw output or the path of a saved log.
- **Does NOT prove:** the limits of this evidence.
- **Open questions:** each with an owner.
- **Proposed registry entries:** D/W/Q/A proposals. The author never edits `docs/13`.

These files are the recovery record. After a host restart the lead resumes from the highest `message_id` per item.

## Allowed Edges

| From | To | Types | Purpose |
|---|---|---|---|
| `strict-programmer` | `integration-tester` | `HANDOFF` | Item is implemented and ready to test |
| `integration-tester` | `strict-programmer` | `DEFECT`, `STALE` | Test failed, or the scope changed after handoff |
| `integration-tester` | lead | `VERDICT` | Pass or fail for the exact `scope_checksum` |
| any dispatched agent | lead | `BLOCKER`, `QUESTION`, `VERDICT`, `DIGEST` | Escalation and reporting |
| lead | any dispatched agent | instruction | Dispatch, redirect, or stop |

Not direct: `delivery-planner` and every skill-executing `self` agent report to the lead only. Parallel branches never message each other.

Forbidden for every agent: messaging the user, requesting or granting approval, writing outside the brief's `outputs`, and messaging a peer not listed in `peers`.

## Fix Loop

```
strict-programmer --HANDOFF--> integration-tester
integration-tester --DEFECT--> strict-programmer      (round n < 3)
strict-programmer --HANDOFF--> integration-tester     (round n+1, new scope_checksum)
integration-tester --VERDICT pass--> lead
integration-tester --BLOCKER--> lead                  (still failing at round 3)
```

- The tester never edits application code. The programmer never writes a pass verdict.
- An item is `done` only on a `VERDICT pass` whose `scope_checksum` equals the current on-disk checksum. A later edit invalidates the verdict.
- At round 3 with a failing test, the tester sends `BLOCKER` listing every handoff file in the chain. The lead decides: reroute, change scope through planning, or stop.

## Receiver Duties

1. Read `handoff_file`, recompute `scope_checksum` from disk. On mismatch, reply `STALE` with the checksum found and stop.
2. Ignore a `message_id` already handled. A duplicate has no effect.
3. Reply with `in_reply_to` set, and send the `DIGEST` to the lead.
4. Never act on a message whose `to` is not its own role.

## Lead Obligations

- Read the tester's handoff file for every `VERDICT`: the command, the raw output, and the `Does NOT prove` section. A verdict without raw output is rejected.
- Recompute the checksum; reject a verdict for a stale scope.
- May re-run the tester's command to confirm. Required for any item the lead reports to the user as passing.
- Merge proposed registry entries into `docs/13` (or hand that single write to `delivery-planner`).

## Failure Handling

| Situation | Action |
|---|---|
| `send_message` to a peer returns an error | Send `BLOCKER` to the lead with the error text; do not retry in a loop |
| Peer silent | The lead lists subagents, nudges once, then restarts the step from the last handoff file |
| Host restart | All subagents stop; the lead re-dispatches from `artifacts/handoffs/` and verifies checksums before resuming |
| Round limit reached | `BLOCKER` to the lead |
| Malformed envelope | Receiver replies `QUESTION` to the lead and takes no action |

## Cleanup

When an item reaches a passing verdict, both agents return their final reports to the lead, terminate every background process they started, and release their ports. The lead verifies and stops leftovers.

## Builder Worktree Isolation & UAT Merge Barrier

- `strict-programmer` runs in `Workspace: branch`. All code edits occur in an isolated git worktree.
- When `strict-programmer` sends `HANDOFF`, it provides the current `branch` name and `commit_sha`.
- `integration-tester` tests the candidate branch commit.
- When all sprint items are implemented and tested, the candidate branch undergoes full UAT (`verify-quality`) and Security Review (`review-security`).
- **UAT Merge Gate:** Merging into `main` is permitted ONLY when both UAT Report and Security Report pass with zero blocking defects.
- The KARSA Lead executes the merge. Subagents never merge to `main`.