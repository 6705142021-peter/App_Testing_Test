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
A successful full run and integration into main are still pending.