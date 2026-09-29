import random
import pytest

PLATFORM = "Windows"

@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Перезапуски реализуются на уровне маркировки flaky
def test_reruns():
    assert random.choice([True, False])  # Случайный выбор для демонстрации нестабильного теста

# Перезапуск автотеста для класса
@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun1(self):
        assert random.choice([True, False])

    def test_rerun2(self):
        assert random.choice([True, False])

# Перезапуск с условием
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([True, False])