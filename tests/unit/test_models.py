from website.models import User, Word, Meaning, Example
from website.utils import salt_generator


def test_user_model():
    data = {
        "username": "test_user",
        "email": "test_user@domain.com",
        "password": "test_password",
    }
    user = User(**data)
    assert user.username == "test_user"
    assert user.email == "test_user@domain.com"
    assert user.salt == salt_generator(data["email"])


def test_word_model():
    data = {
        "word": "test_word",
        "pos": "test_pos",
    }
    word = Word(**data)
    assert word.word == "test_word"
    assert word.pos == "test_pos"


def test_meaning_model():
    data = {
        "meaning": "test_meaning",
        "source": "test_source",
    }
    meaning = Meaning(**data)
    assert meaning.meaning == "test_meaning"
    assert meaning.source == "test_source"


def test_example_model():
    user_data = {
        "username": "test_user",
        "email": "test_user@domain.com",
        "password": "test_password",
    }
    user = User(**user_data)
    data = {
        "example": "test_example",
        "user": user,
    }
    example = Example(**data)
    assert example.example == "test_example"
    assert example.user.email == user.email
