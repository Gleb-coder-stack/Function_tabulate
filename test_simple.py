from main import calculate_y
import pytest

class TestCalculator:
    # Тест 1: x=1.2
    def test_1(self):
        calculate_y(1.2)

    # Тест 2: x=17
    def test_2(self):
        result = calculate_y(17)
        assert round(result, 1) == 10.1

    # Тест 3: x='пять'
    def test_3(self):
        calculate_y('пять')

    # Тест 4: x=8.3
    def test_4(self):
        result = calculate_y(8.3)
        assert round(result, 2) == 9.89

    # Тест 5: x='VI'
    def test_5(self):
        calculate_y('VI')

    # Тест 6: x=0
    def test_6(self):
        result = calculate_y(0)
        assert round(result, 1) == 9.2