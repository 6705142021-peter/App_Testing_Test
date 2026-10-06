import pytest
from bookstore_app import Users, Catalog, Cart


@pytest.mark.smoke
def test_registration_stores_account():
    """Author: Thin Thiri Zaw. AI-assisted smoke test for registration."""
    users = Users()

    assert users.register("alice", "secret123") is True
    assert users.users["alice"] == "secret123"

@pytest.mark.smoke
def test_catalog_stores_product():
    """Author: Paing Oo Thant. AI-assisted smoke test for product storage."""
    catalog = Catalog()

    catalog.add_product(1, "Python Testing", 30)

    assert catalog.products[1] == {
        "title": "Python Testing",
        "price": 30,
    }
    assert catalog.search("Python Testing") == [1]

@pytest.mark.smoke
def test_login_validates_password():
    """Author: L Peter San Awng. AI-assisted smoke test for login."""
    users = Users()

    assert users.register("alice", "secret123") is True
    assert users.login("alice", "secret123") is True
    assert users.login("alice", "wrong123") is False

@pytest.mark.smoke
def test_checkout_places_nonempty_order():
    """Author: Kaung Myat Tun. AI-assisted smoke test for checkout."""
    catalog = Catalog()
    catalog.add_product(1, "Python Testing", 30)

    cart = Cart(catalog)
    assert cart.add(1) is True

    assert cart.checkout() == [1]
    assert cart.items == []

@pytest.mark.smoke
def test_known_product_reaches_cart():
    """Author: Aung Kyaw Phyo. AI-assisted smoke test for cart insertion."""
    catalog = Catalog()
    catalog.add_product(1, "Python Testing", 30)

    cart = Cart(catalog)

    assert cart.add(1) is True
    assert cart.items == [1]

@pytest.mark.regression
def test_cart_total_counts_every_item():
    """Author: L Peter San Awng. AI-assisted regression for Cart.total.

    Observed defect: the last cart item's price is omitted.
    Expected behavior: every item's price contributes to the total.
    """
    catalog = Catalog()
    catalog.add_product(1, "Book A", 10)
    catalog.add_product(2, "Book B", 20)

    cart = Cart(catalog)
    assert cart.add(1) is True
    assert cart.add(2) is True

    assert cart.total() == 30

@pytest.mark.slow
def test_large_cart_repeated_totals():
    """Author: L Peter San Awng. AI-assisted slow test for large carts."""
    catalog = Catalog()
    catalog.add_product(1, "Book A", 2)
    catalog.add_product(2, "Book B", 3)
    cart = Cart(catalog)

    pair_count = 100_000

    # Large cart plus repeated full scans creates a substantial workload.
    for _ in range(pair_count):
        assert cart.add(1) is True
        assert cart.add(2) is True

    assert len(cart.items) == pair_count * 2

    for _ in range(100):
        assert cart.total() == pair_count * 5

    order = cart.checkout()
    assert len(order) == pair_count * 2
    assert order.count(1) == pair_count
    assert order.count(2) == pair_count
    assert cart.items == []

@pytest.mark.regression
def test_import_reports_exact_count():
    """Author: L Peter San Awng. AI-assisted test; assigned area: Aung Kyaw Phyo.

    Cart.import_products returns one too many.
    Expected behavior: return the exact number of imported products.
    """
    catalog = Catalog()
    cart = Cart(catalog)

    products = [
        (1, "Book A", 10),
        (2, "Book B", 20),
    ]

    assert cart.import_products(products) == 2
    assert len(catalog.products) == 2

@pytest.mark.slow
def test_bulk_import_many_products():
    """Author: L Peter San Awng. AI-assisted test; assigned area: Aung Kyaw Phyo."""
    catalog = Catalog()
    cart = Cart(catalog)
    product_count = 500_000

    # Import a large dataset and verify both the count and stored content.
    products = [
        (product_id, f"Book {product_id}", product_id % 100 + 1)
        for product_id in range(product_count)
    ]

    assert cart.import_products(products) == product_count
    assert len(catalog.products) == product_count

    for product_id in (0, product_count // 2, product_count - 1):
        assert catalog.products[product_id] == {
            "title": f"Book {product_id}",
            "price": product_id % 100 + 1,
        }

@pytest.mark.regression
def test_login_preserves_password_punctuation():
    """Author: L Peter San Awng. AI-assisted test; assigned area: Thin Thiri Zaw.

    Users.login strips punctuation from the supplied password.
    Expected behavior: the exact registered password must succeed.
    """
    users = Users()
    assert users.register("alice", "secret!123") is True

    assert users.login("alice", "secret!123") is True
    assert users.login("alice", "secret123") is False