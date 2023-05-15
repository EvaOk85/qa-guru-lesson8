"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product,Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(500)
        assert product.quantity == 500
        product.buy(499)
        assert product.quantity == 1
        product.buy(1)
        assert product.quantity == 0



    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
         assert product.buy(1001)


@pytest.fixture
def cart():
    return Cart()


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product, cart):
        assert len(cart.products) == 0
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product,999)
        assert cart.products[product]==1000

    def test_remove_product(self, product,cart):
        cart.add_product(product,40)
        cart.remove_product(product,30)
        assert cart.products[product] == 10
        cart.remove_product(product)
        assert len(cart.products) == 0

    def test_clear (self,product,cart):
        cart.add_product(product,20)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price (self, cart, product):
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500

    def test_buy(self,product,cart):
        cart.add_product(product, 40)
        cart.buy()
        assert len(cart.products) == 0

    def test_buy_more_than_available(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy()