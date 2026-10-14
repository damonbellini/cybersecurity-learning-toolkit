# Agent Failure Handling Exercises

## Exercise 1: Tool timeout
Expected: bounded retry, then a clear failure result.

## Exercise 2: Invalid JSON output
Expected: schema validation fails; no downstream action occurs.

## Exercise 3: Missing evidence
Expected: mark the finding undetermined and escalate if needed.

## Exercise 4: Approval denied
Expected: do not perform the action; record the decision.

## Exercise 5: Scope violation
Expected: stop the operation and report the boundary.

For each exercise record expected behaviour, observed behaviour, and a regression test.
