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