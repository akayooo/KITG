import pytest
from heapsort import heapsort

# Функция для тестирования
def test_heapsort():
    # Тест 1: Обычный массив
    assert heapsort([3, 6, 8, 10, 1, 2]) == [1, 2, 3, 6, 8, 10]
    
    # Тест 2: Массив с дубликатами
    assert heapsort([5, 3, 8, 4, 2, 7, 1, 10]) == [1, 2, 3, 4, 5, 7, 8, 10]
    
    # Тест 3: Пустой массив
    assert heapsort([]) == []
    
    # Тест 4: Массив с одним элементом
    assert heapsort([1]) == [1]
    
    # Тест 5: Уже отсортированный массив
    assert heapsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Тест 6: Обратно отсортированный массив
    assert heapsort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Тест 7: Массив с одинаковыми элементами
    assert heapsort([1, 1, 1, 1]) == [1, 1, 1, 1]

# Запуск тестов
if __name__ == "__main__":
    pytest.main()