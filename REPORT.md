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