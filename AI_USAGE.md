# AI Usage Declaration and Audit

Group: Trojan
Members: Thin Thiri Zaw, Paing Oo Thant, L Peter San Awng,
Kaung Myat Tun, Aung Kyaw Phyo

## Part 1 -- AI Declaration

L Peter San Awng used OpenAI Codex for step-by-step setup guidance,
candidate test code, cart-total, import-count, password and checkout fixes, report
wording and audit guidance. Codex also helped insert saved output into this file.
The supplied examples were entered, reviewed and executed locally.
The cart-total regression was verified to fail before the fix and pass
afterward. Other members must add their own actual AI usage.

## Part 2 -- Supplied-Test Audit

Auditor for the following entries: L Peter San Awng.

Original application version: 4eadded
Current partially fixed application versions: `32aa9ac` for the cart-total
and cart-add audits; `41fb0d5` for the import-count audit; `58ec97e` for
the wrong-password and duplicate-registration audits; `8fc783e` for the
empty-checkout audit; `9fb7625` for the two search audits.

| Test | Original | Current | Verdict |
|---|---|---|---|
| test_cart_total_sums_items | FAIL | PASS | Genuine detection |
| test_add_to_cart_returns_true_for_known_product | PASS | PASS | Detects nothing |
| test_import_returns_count | FAIL | PASS | Genuine detection |
| test_login_rejects_wrong_password | PASS | PASS | Detects nothing |
| test_register_duplicate_returns_false | PASS | PASS | Detects nothing |
| test_checkout_empty_returns_none | FAIL | PASS | Genuine detection |
| test_search_finds_exact_title | PASS | PASS | Detects nothing |
| test_search_is_limited_to_ten_results | FAIL | FAIL | Invented requirement |

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

### test_login_rejects_wrong_password

Assigned area: Thin Thiri Zaw.
Actual auditor: L Peter San Awng, with AI assistance.

The test registers `alice` with `secret1` and checks that `wrongpw` is rejected.
Both inputs are alphanumeric, so this assertion does not exercise the password
cleaning defect recorded as Bug 3 in FINDINGS.md.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_login_rejects_wrong_password -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test_original
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED [100%]

============================== 1 passed in 0.01s ==============================
```

Saved output: [Original login evidence](evidence/thin_login_original.txt)

#### Current-code evidence

Version: `58ec97e`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_login_rejects_wrong_password -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED [100%]

============================== 1 passed in 0.01s ==============================
```

Saved output: [Current login evidence](evidence/thin_login_current.txt)

Verdict: Detects nothing in the original bug hunt. PASS/PASS shows that the
assertion did not distinguish the original defect from the corrected behavior.
It remains a useful ordinary wrong-password check. To detect Bug 3, a test
must exercise punctuation, such as requiring the exact registered password
`secret!123` to succeed, as our own regression does.

### test_register_duplicate_returns_false

Assigned area: Thin Thiri Zaw.
Actual auditor: L Peter San Awng, with AI assistance.

The test registers `bob` and verifies that registering the same username again
returns False. This behavior already works in the original application and is
unaffected by the password-comparison fix.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_register_duplicate_returns_false -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test_original
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED [100%]

============================== 1 passed in 0.01s ==============================
```

Saved output: [Original registration evidence](evidence/thin_register_original.txt)

#### Current-code evidence

Version: `58ec97e`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_register_duplicate_returns_false -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED [100%]

============================== 1 passed in 0.01s ==============================
```

Saved output: [Current registration evidence](evidence/thin_register_current.txt)

Verdict: Detects nothing in the original bug hunt. PASS/PASS demonstrates an
existing duplicate-registration guard, not detection of a planted defect.
The assertion is consistent with the register docstring, so its usefulness as
basic coverage should not be confused with original-defect detection.

### test_checkout_empty_returns_none

Assigned area: Kaung Myat Tun.
Actual auditor: L Peter San Awng, with AI assistance.

The test checks that an empty cart returns None from checkout, as explicitly
promised by the method's docstring. Original code returned an empty list instead.
This detects the checkout defect recorded as Bug 4 in FINDINGS.md.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_checkout_empty_returns_none -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test_original
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED  [100%]

================================== FAILURES ===================================
______________________ test_checkout_empty_returns_none _______________________

    def test_checkout_empty_returns_none():
        """Claims to check that checking out an empty cart returns None."""
>       assert Cart(Catalog()).checkout() is None
E       assert [] is None
E        +  where [] = checkout()
E        +    where checkout = <bookstore_app.cart.Cart object at 0x000001BDC233FE00>.checkout
E        +      where <bookstore_app.cart.Cart object at 0x000001BDC233FE00> = Cart(<bookstore_app.catalog.Catalog object at 0x000001BDC233F620>)
E        +        where <bookstore_app.catalog.Catalog object at 0x000001BDC233F620> = Catalog()

ai_review\test_ai_generated.py:45: AssertionError
=========================== short test summary info ===========================
FAILED ai_review/test_ai_generated.py::test_checkout_empty_returns_none - ass...
============================== 1 failed in 0.03s ==============================
```

Saved output: [Original checkout evidence](evidence/kaung_checkout_original.txt)

#### Current-code evidence

Version: `8fc783e`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_checkout_empty_returns_none -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED  [100%]

============================== 1 passed in 0.01s ==============================
```

Saved output: [Current checkout evidence](evidence/kaung_checkout_current.txt)

Verdict: Genuine detection. The FAIL/PASS pair demonstrates detection of a
real documented return-value defect. The supplied assertion checks only the
return value; our student regression additionally checks that no empty order
is recorded. It does not establish defensive-copy behavior for order history.

### test_search_finds_exact_title

Assigned area: Paing Oo Thant.
Actual auditor: L Peter San Awng, with AI assistance.

The test adds a product titled `Python Testing` and expects its ID from an
exact-title search. This simple scenario succeeds on original and current code.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_search_finds_exact_title -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test_original
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED     [100%]

============================== 1 passed in 0.01s ==============================
```

Saved output: [Original evidence](evidence/paing_exact_original.txt)

#### Current-code evidence

Version: `9fb7625`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_search_finds_exact_title -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED     [100%]

============================== 1 passed in 0.01s ==============================
```

Saved output: [Current evidence](evidence/paing_exact_current.txt)

Verdict: Detects nothing in the original bug hunt. PASS/PASS demonstrates that
this assertion does not expose an original defect. It remains a useful basic
search check, but does not cover other keywords, absent matches or alternative
capitalization. Those cases require their own expectations and requirements;
passing this test does not establish that search is correct in all cases.

### test_search_is_limited_to_ten_results

Assigned area: Paing Oo Thant.
Actual auditor: L Peter San Awng, with AI assistance.

The test inserts 20 products with matching titles and demands no more than ten
results. Both application versions return all 20 matching IDs.

Requirement check: the instructor's supplied `ST211_MIDTERM_INSTRUCTIONS.md`
describes product search but does not set a result limit. The original
`Catalog.search` docstring promises a list of product IDs whose titles contain
the keyword; it supplies no ten-result cap or pagination contract. Returning
all 20 matching IDs is consistent with that description. The cap comes from
the supplied AI test's assertion rather than either specification.

#### Original-code evidence

Version: `4eadded`
Working folder: `C:\Github\App_Testing_Test_original`

Command:

```cmd
C:\Github\App_Testing_Test\.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test_original
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED [100%]

================================== FAILURES ===================================
____________________ test_search_is_limited_to_ten_results ____________________

    def test_search_is_limited_to_ten_results():
        """Claims the catalogue search returns at most ten results."""
        cat = Catalog()
        for i in range(20):
            cat.add_product(i, "match", 1)
>       assert len(cat.search("match")) <= 10
E       AssertionError: assert 20 <= 10
E        +  where 20 = len([0, 1, 2, 3, 4, 5, ...])
E        +    where [0, 1, 2, 3, 4, 5, ...] = search('match')
E        +      where search = <bookstore_app.catalog.Catalog object at 0x000002481CC3F620>.search

ai_review\test_ai_generated.py:60: AssertionError
=========================== short test summary info ===========================
FAILED ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results
============================== 1 failed in 0.03s ==============================
```

Saved output: [Original evidence](evidence/paing_limit_original.txt)

#### Current-code evidence

Version: `9fb7625`
Working folder: `C:\Github\App_Testing_Test`

Command:

```cmd
.venv\Scripts\python.exe -m pytest ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results -v
```

Actual output:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Github\App_Testing_Test\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Github\App_Testing_Test
configfile: pytest.ini
collecting ... collected 1 item

ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED [100%]

================================== FAILURES ===================================
____________________ test_search_is_limited_to_ten_results ____________________

    def test_search_is_limited_to_ten_results():
        """Claims the catalogue search returns at most ten results."""
        cat = Catalog()
        for i in range(20):
            cat.add_product(i, "match", 1)
>       assert len(cat.search("match")) <= 10
E       AssertionError: assert 20 <= 10
E        +  where 20 = len([0, 1, 2, 3, 4, 5, ...])
E        +    where [0, 1, 2, 3, 4, 5, ...] = search('match')
E        +      where search = <bookstore_app.catalog.Catalog object at 0x0000022990C8F620>.search

ai_review\test_ai_generated.py:60: AssertionError
=========================== short test summary info ===========================
FAILED ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results
============================== 1 failed in 0.03s ==============================
```

Saved output: [Current evidence](evidence/paing_limit_current.txt)

Verdict: Invented requirement, based on the supplied instructions and docstring.
FAIL/FAIL alone would not establish this conclusion: the requirement check is
what distinguishes the unsupported cap from an unfixed real defect. We did not
truncate results merely to make the audit pass. If the instructor supplies an
additional limit requirement, this verdict must be revisited.


## Status

All eight audit entries include commands and actual output for the original
application and the corresponding partially fixed application.
The coverage table, group reflection and final application verification are
still pending. Search and history investigations are not yet recorded as
confirmed additional planted defects.
Repeat the fixed-code evidence against the final integrated application.
