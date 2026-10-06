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