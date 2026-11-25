# Spec Sandbox: CoachLoop Check-in Streaks

A tiny sandbox for spec-driven development, modeled on Sean Grove's "The New Code"
(OpenAI Model Spec: Markdown files in Git, each clause with an ID, tests keyed to IDs).

## Structure
- `spec/` holds the **what**. Each requirement is a clause with a stable ID (e.g. `CS-03`).
  The spec is the source of truth; code is a lossy projection of it.
- `tests/` holds success criteria **keyed to clause IDs**. `tests/CS-03.md` lists the hard
  cases in plain language; `tests/test_CS-03.py` makes them executable.
- `src/` holds the generated or hand-written implementation. It can be thrown away and
  regenerated from the spec.
- **Git holds history**: every spec change is a commit or PR that people review and debate
  before an agent builds against it.
- `TASKS.md` is the simple task list: **who** is doing **what**, referencing clause IDs.

## Workflow
1. Write or change a clause in `spec/` and open a PR. Review the spec, not the diff.
2. Add or update the matching `tests/<ID>.md` cases and executable test.
3. Assign the work in `TASKS.md` (human or AI agent), citing the clause ID.
4. The agent implements in `src/` until the tests for that ID pass.

Run the tests: `python3 tests/test_CS-03.py`
