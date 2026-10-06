# Bug-Hunt Findings Log

Group: <Trojan>
Members: Thin Thiri Zaw, Paing Oo Thant, L Peter San Awng,
Kaung Myat Tun, Aung Kyaw Phyo

## Bug 1: Cart total omits the last item

- **Module / function:** `bookstore_app/cart.py` -> `Cart.total()`
- **What we suspected and why:** The loop uses `range(len(self.items) - 1)`,
  which stops before the last item.
- **What we did:** Added Book A priced at 10 and Book B priced at 20,
  then ran `test_cart_total_counts_every_item`.
- **What we observed:** The total was 10. The test failed with `assert 10 == 30`.
- **What we expected instead:** 30, because the method promises to total
  everything currently in the cart: 10 + 20 = 30.
- **The fix we made:** Replaced the index loop with a loop over every
  product ID in the cart, so the last item's price is included.
- **Failing-test commit:** `c856eba`
- **Author of this finding:** L Peter San Awng, with declared AI assistance.
- **Original application commit:** `4eadded`

### Before-fix command

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py::test_cart_total_counts_every_item -v
```

### Before-fix evidence

```text
E       assert 10 == 30
```
### After-fix command

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py::test_cart_total_counts_every_item -v
```

### After-fix evidence

```text
tests/test_bookstore.py::test_cart_total_counts_every_item PASSED
1 passed in 0.01s
```

### Full-suite check

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py -v
```

```text
6 passed in 0.01s
```

## Bug 2: Product import overcounts by one

- **Module / function:** `bookstore_app/cart.py` -> `Cart.import_products()`
- **What we suspected and why:** The method returns `count + 1`,
  although `count` already tracks the processed records.
- **What we did:** Imported two products, Book A and Book B, using
  `test_import_reports_exact_count`.
- **What we observed:** The method returned 3 for two input records.
- **What we expected instead:** 2, because the method promises to
  return how many products were imported.
- **The fix we made:** Changed `return count + 1` to `return count`.
  The counter already records the number of processed products.
- **Failing-test commit:** `e9a793a`
- **Author of this finding:** L Peter San Awng, with AI assistance.
- **Assigned role:** Aung Kyaw Phyo's import-testing area.

### Before-fix command

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py::test_import_reports_exact_count -v
```

### Before-fix evidence

```text
E       AssertionError: assert 3 == 2
1 failed in 0.06s
```

### After-fix verification

Command:

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py -v
```

Relevant actual output:

```text
tests/test_bookstore.py::test_import_reports_exact_count PASSED
8 passed in 0.75s
```
## Bug 3: Login rejects an exact password containing punctuation

- **Module / function:** `bookstore_app/users.py` -> `Users.login()`
- **What we suspected and why:** Login removes non-alphanumeric characters
  from the supplied password before comparing it with the stored password.
- **What we did:** Registered alice with `secret!123`, then tried logging
  in with that same password using `test_login_preserves_password_punctuation`.
- **What we observed:** Login returned False. The test failed with
  `AssertionError: assert False is True`.
- **What we expected instead:** True, because the supplied password exactly
  matches the registered password, including punctuation.
- **The fix we made:** Removed password cleaning and compared the
  supplied password directly with the stored password.
- **Failing-test commit:** `cf72c2f`
- **Author of this finding:** L Peter San Awng, with AI assistance.
- **Assigned role:** Thin Thiri Zaw's account-testing area.

### Before-fix command

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py::test_login_preserves_password_punctuation -v
```

### Before-fix evidence

```text
E       AssertionError: assert False is True
1 failed in 0.06s
```
### After-fix verification

Regression command:

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py::test_login_preserves_password_punctuation -v
```

Actual summary:

```text
1 passed in 0.01s
```

Full-suite command:

```cmd
.venv\Scripts\python.exe -m pytest tests/test_bookstore.py -v
```

Actual summary:

```text
10 passed in 1.06s
```