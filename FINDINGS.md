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
- **The fix we made:** Not fixed yet. Failure recorded before changing the code.
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