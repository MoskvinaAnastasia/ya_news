import pytest
from django.test.client import Client
from django.urls import reverse
from news.models import News, Comment


@pytest.fixture
# Используем встроенную фикстуру модели пользователей
# для создания пользователя - Автор.
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
# Используем встроенную фикстуру модели пользователей
# для создания пользователя - Не автор.
def not_author(django_user_model):
    return django_user_model.objects.create(username='Не Автор')


@pytest.fixture
# Создаем клиента Автора.
def author_client(author):  # Вызываем фикстуру автора.
    # Создаём новый экземпляр клиента, чтобы не менять глобальный.
    client = Client()
    client.force_login(author)  # Логиним автора в клиенте.
    return client


@pytest.fixture
# Создаем клиента не Автора.
def not_author_client(not_author):  # Вызываем фикстуру не автора.
    client = Client()
    client.force_login(not_author)  # Логиним обычного пользователя в клиенте.
    return client


@pytest.fixture
# Создаём анонимного клиента.
def anonymous_client():
    # Создаём новый экземпляр клиента, чтобы не менять глобальный.
    client = Client()
    return client


@pytest.fixture
# Создаём объект новости.
def news(author):
    news = News.objects.create(
        title='Заголовок новости',
        text='ТекстВ',
    )
    return news


@pytest.fixture
# Фикстура запрашивает другую фикстуру создания новости.
def news_id_for_args(news):
    return (news.id,)


@pytest.fixture
# Создаём объект комментарий.
def comment(author, news):
    comment = Comment.objects.create(  # Создаём объект комментария.
        news=news,
        author=author,
        text='Текст комментария'
    )
    return comment


@pytest.fixture
# Фикстура запрашивает другую фикстуру создания комментария новости.
def comment_id_for_args(comment):
    return (comment.id,)


@pytest.fixture
# Адрес страницы новости.
def detail_url(news):
    return reverse('news:detail', args=(news.id,))
