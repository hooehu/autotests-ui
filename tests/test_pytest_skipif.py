import pytest, sys

SYSTEM_VERSION = "v1.2.0"


# Проверяет условие.
@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason="Тест не может быть запущен на текущей версии"
)
def test_system_version_valid():
    ...

# Если True, то тест пропускается
@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="Тест не может быть запущен на текущей версии"
)
def test_system_version_invalid():
    ...
