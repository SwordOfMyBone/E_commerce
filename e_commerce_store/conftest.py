import pytest

from e_commerce_store.store.models import Category, Product
from e_commerce_store.store.tests.factories import CategoryFactory, ProductFactory
from e_commerce_store.users.models import User
from e_commerce_store.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def category(db) -> Category:
    category = CategoryFactory()
    return category


@pytest.fixture
def product(db) -> Product:
    product = ProductFactory()
    return product
