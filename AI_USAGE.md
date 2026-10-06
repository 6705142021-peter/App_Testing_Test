# AI Usage Declaration and Audit

Group: Trojan
Members: Thin Thiri Zaw, Paing Oo Thant, L Peter San Awng,
Kaung Myat Tun, Aung Kyaw Phyo

## Part 1 -- AI Declaration

L Peter San Awng used OpenAI Codex for step-by-step setup guidance,
candidate test code, the cart-total fix, report wording and audit guidance.
The supplied examples were entered, reviewed and executed locally.
The cart-total regression was verified to fail before the fix and pass
afterward. Other members must add their own actual AI usage.

## Part 2 -- Supplied-Test Audit

Auditor for the following entries: L Peter San Awng.

Original application version: 4eadded
Current partially fixed application versions: `32aa9ac` for the cart-total
and cart-add audits; `41fb0d5` for the import-count audit.

| Test | Original | Current | Verdict |
|---|---|---|---|
| test_cart_total_sums_items | FAIL | PASS | Genuine detection |
| test_add_to_cart_returns_true_for_known_product | PASS | PASS | Detects nothing |
| test_import_returns_count | FAIL | PASS | Genuine detection |

### test_cart_total_sums_items

The test checks that prices 10 and 20 produce a total of 30.
Original code returned 10; the corrected code passed the assertion.
This detects the total defect recorded as Bug 1 in FINDINGS.md.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_cart_total_sums_items -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test_original
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED        [100%]

================================== FAILURES ===================================
_________________________ test_cart_total_sums_items __________________________

    def test_cart_total_sums_items():
        """Claims to check the cart total is correct."""
        cat = Catalog(); cat.add_product(1, "A", 10); cat.add_product(2, "B", 20)
        c = Cart(cat); c.add(1); c.add(2)
>       assert c.total() == 30
E       assert 10 == 30
E        +  where 10 = total()
E        +    where total = <bookstore_app.cart.Cart object at 0x000001A941CAFE00>.total

ai_review\test_ai_generated.py:16: AssertionError
=========================== short test summary info ===========================
FAILED ai_review/test_ai_generated.py::test_cart_total_sums_items - assert 10...
============================== 1 failed in 0.03s ==============================
```

#### Current-code evidence

Version: `32aa9ac`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_cart_total_sums_items -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED        [100%]

============================== 1 passed in 0.01s ==============================
```

Verdict: Genuine detection. The test fails on the original total of 10
and passes after the fix makes the total 30.

### test_add_to_cart_returns_true_for_known_product

The test passes before and after the total fix, so it does not detect
an original defect. It asserts only the return value from add().
Checking cart.items as well would make its insertion check stronger.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test_original
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED [100%]

============================== 1 passed in 0.01s ==============================
```

#### Current-code evidence

Version: `32aa9ac`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED [100%]

============================== 1 passed in 0.01s ==============================
```

Verdict: Detects nothing in the original bug hunt. Both runs pass.
This test checks the return value but does not verify cart contents.

### test_import_returns_count

Assigned area: Aung Kyaw Phyo.
Actual auditor: L Peter San Awng, with AI assistance.

The test imports two products and asserts that the returned count is 2.
It detects the import-count defect recorded as Bug 2 in FINDINGS.md.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_import_returns_count -v
```

Relevant actual output:

```text
E       AssertionError: assert 3 == 2
1 failed in 0.03s
```

Full captured output: [Original evidence](evidence/aung_import_original.txt)

#### Current-code evidence

Version: `41fb0d5`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_import_returns_count -v
```

Relevant actual output:

```text
ai_review/test_ai_generated.py::test_import_returns_count PASSED
1 passed in 0.01s
```

Full captured output: [Current evidence](evidence/aung_import_current.txt)

Verdict: Genuine detection. Original code returned 3 for two products.
After correcting the counter's return value, the test passed.

## Status

Three audit entries include commands and actual output for the original
application and the corresponding partially fixed application.
Five other audits, the coverage table and group reflection are pending.
Repeat the fixed-code evidence against the final integrated application.
