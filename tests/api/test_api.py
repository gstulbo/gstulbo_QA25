import pytest


@pytest.mark.change
def test_remove_name(user):   # передаем как параметр в каждый тест для работы сос воим экземпляром класса User
    user.name = ''             # 1 тест удаляет имя
    assert user.name == '' 


@pytest.mark.check
def test_name(user):               # 2 тест проверяет имя на значение 'Sergii'
    assert user.name == 'Halyna'
    

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Stulbo'
    


