import pytest


@pytest.mark.change            #Тест має мітку change.
def test_remove_name(user):    # Створити тест test_remove_name. Використовує фікстуру user.
    user.name = ''             # Першим кроком тест змінює поле name об’єкта user на пустий рядок.
    assert user.name == ''     # Другим кромом тест перевіряє, що зміни відбулися і вони правильні.


@pytest.mark.check                 # Тест має мітку check.
def test_name(user):               # Створити тест test_name. Використовує фікстуру user.
    assert user.name == 'Halyna'   # Перевіряє, що поле name об’єкту user відповідає очікуваному.
    

@pytest.mark.check                       # Тест має мітку check.
def test_second_name(user):              # Створити тест test_second_name. Використовує фікстуру user.
    assert user.second_name == 'Stulbo'  # Перевіряє, що поле second_name об’єкту user відповідає очікуваному.
    


