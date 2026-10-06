# Bookstore Midterm Report

Group: Trojan

Members: Thin Thiri Zaw, Paing Oo Thant, L Peter San Awng,
Kaung Myat Tun, Aung Kyaw Phyo

Repository: https://github.com/6705142021-peter/App_Testing_Test

## Part A -- Test Types

### Slow Testing -- L Peter San Awng

Slow tests check correctness using workloads that take noticeably longer
than basic checks, such as large datasets or repeated operations. They
should run in scheduled nightly suites and before important releases.

Two bookstore examples are importing tens of thousands of products and
repeatedly calculating totals for a large shopping cart.

## Part B -- Scenario Classification

### Scenario 3 -- L Peter San Awng

Classification: slow.

Generating a sales report from ten years of orders processes a large
historical dataset. The test should verify the report's correctness,
not merely that processing finishes.

## Part F -- Team Reflection

### Question 3 -- L Peter San Awng

If slow tests never run, defects involving large datasets or repeated
operations can remain undetected. Small tests may pass while larger
workloads produce incorrect results or take too long to process.

## Peter's Slow-Test Evidence

Test: `test_large_cart_repeated_totals`

The test adds 100,000 copies each of two products, creating a cart with
200,000 items. It calculates the expected total 100 times, then checks
the checkout quantities and confirms that the cart is empty.

Command:

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py::test_large_cart_repeated_totals -v --durations=0
```

Observed output:

```text
0.74s call tests/test_bookstore.py::test_large_cart_repeated_totals
1 passed in 0.76s
```

For comparison, the separate smoke run reported:

```text
5 passed, 2 deselected in 0.01s
```

The complete current student suite reported:

```text
7 passed in 0.74s
```

These measurements are from our local machine; durations may differ
on another computer or the GitHub Actions runner.

## Report Status

This report currently contains L Peter San Awng's assigned sections.
The other members' sections and final group verification are pending.

## Additional Sections -- Aung Kyaw Phyo's Assigned Area

Completed by: L Peter San Awng, with AI assistance.
These sections will be placed under the corresponding headings
when the final group report is assembled.

### Part B -- Scenario 6

Classification: slow.

Testing recommendations with one million titles exercises a large
dataset and substantial processing work. It would also be regression
if it reproduced a specific previously fixed defect, but the scenario
does not state such a history.

### Part F -- Question 4

A test can belong to two categories because the categories describe
different characteristics. A large import test reproducing a known
counting defect can be regression in purpose and slow in workload.
Such a test belongs in scheduled full runs and suitable release checks.

### Bulk-Import Slow Test

Test: `test_bulk_import_many_products`

The test imports 500,000 unique products. It checks the returned count,
catalog size, and the title and price of records from the beginning,
middle and end of the dataset.

Measured test duration: 0.31 seconds on our local machine.

### Combined Slow-Test Verification

Command:

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py -m slow -v --durations=0
```

Relevant actual output:

```text
0.80s call tests/test_bookstore.py::test_large_cart_repeated_totals
0.31s call tests/test_bookstore.py::test_bulk_import_many_products
2 passed, 7 deselected in 1.13s
```

### Current Full-Suite Verification

Command:

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py -v
```

Actual summary:

```text
9 passed in 1.12s
```

These measurements are local results. Runtime may differ on GitHub Actions.
CI configuration and the supplied import-test audit are still pending.

## Part E -- Continuous Integration Progress

Assigned role: Aung Kyaw Phyo.
Implemented by: L Peter San Awng, with AI assistance.

The workflow runs smoke tests on pushes and pull requests.
The complete student suite is configured for nightly runs at
01:00 Bangkok time and manual execution.

### Verified Push Smoke Run

Branch: `aung-import-ci`
Commit: `3c49e6f`

[Successful GitHub Actions smoke job](https://github.com/6705142021-peter/App_Testing_Test/actions/runs/37441987447/job/112197697170)

Actual result:

```text
5 passed, 4 deselected in 0.02s
```

The full job was skipped as configured for a push event.
### Verified Manual Full Run

The import fix, slow import test and workflow were merged into `main`.

Application commit: `78463cc`
Trigger: manual (`workflow_dispatch`)

[Successful full GitHub Actions job](https://github.com/6705142021-peter/App_Testing_Test/actions/runs/37443599748/job/112202990424)

Actual result:

```text
9 passed in 60.14s (0:01:00)
```

Both smoke and full jobs succeeded. The full job included both slow tests.
The nightly schedule is configured; this evidence is from a manual run,
not a scheduled run.
## Additional Sections -- Thin Thiri Zaw's Assigned Area

Completed by: L Peter San Awng, with AI assistance.
These sections will be moved under the corresponding headings
when the final group report is assembled.

### Part A -- Smoke Testing

Smoke tests quickly check whether essential features work at a basic
level. They should run on every push and early in deployment checks
so major failures are detected quickly.

Two bookstore examples are registering a new account and checking
out a nonempty cart.

### Part B -- Scenario 1

Classification: smoke, and potentially slow.

Password-reset email delivery checks an essential account feature.
An end-to-end test using a real mail service may also be slow,
but the one-minute deadline alone does not establish its runtime.

### Part F -- Question 1

Running only regression tests can spend time on historical defect
cases while missing a broader failure in an essential feature.
A practical approach combines quick smoke checks, relevant regression
tests and scheduled full suites. Small regression suites can still
be inexpensive enough to run on every commit.

### Account-Fix Verification

The exact-password regression failed before the fix and passed afterward.

Failing-test commit: cf72c2f
Fix commit: 58ec97e

The current full student suite reported:
10 passed in 1.06s

The two supplied account-test audits are still pending.

## Additional Sections -- Kaung Myat Tun's Assigned Area

Completed by: L Peter San Awng, with AI assistance.
These sections will be moved under the corresponding headings
when the final group report is assembled.

### Part B -- Scenario 4

Classification: smoke.

Checking whether the payment page loads after deployment quickly
verifies an essential customer feature. It provides basic deployment
feedback without exhaustively testing payment processing.

### Part F -- Question 5

When the bug finder and fixer are different people, the bug report
must let the fixer reproduce the problem independently. It should
include the application version, affected function, exact input,
runnable command, actual result and expected result with its reason.

For our empty-checkout defect, the recorded test creates an empty
cart and shows that checkout returns [] instead of the documented
None. This evidence would allow another person to reproduce the
problem. In this work, L Peter San Awng performed both roles;
we do not claim that a separate teammate completed that handoff.

### Checkout-Fix Verification

Failing-test commit: ab52f61
Fix commit: 8fc783e

The regression passed after adding the empty-cart check.
The full student suite reported 11 passed in 1.09s.

The supplied checkout-test audit is documented in AI_USAGE.md with actual
original and current output: FAIL before the fix, PASS afterward.
The history investigation remains pending.
