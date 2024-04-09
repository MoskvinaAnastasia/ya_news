# Импортируем функцию для получения модели пользователя.
from django.contrib.auth import get_user_model
# Импортируем функцию reverse(), она понадобится для получения адреса страницы.
from django.urls import reverse
# Импортируем класс формы.
from news.forms import CommentForm
# Импортируем библиотеку pytest.
import pytest


@pytest.mark.parametrize(
    # Задаём названия для параметров:
    'parametrized_client, form_in_context',
    (
        # Передаём фикстуры в параметры при помощи "ленивых фикстур":
        (pytest.lazy_fixture('author_client'), True),
        (pytest.lazy_fixture('anonymous_client'), False),
    )
)
def test_different_user_has_or_not_form(
        parametrized_client,
        detail_url,
        form_in_context,
):
    response = parametrized_client.get(detail_url)
    assert ('form' in response.context) is form_in_context
    if form_in_context:
        assert isinstance(response.context['form'], CommentForm)
