import pytest, sys

SYSTEM_VERSION = "v1.2.0"


# Если условие = True, то тест запускается
@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason="Тест не может быть запущен на текущей версии"
)
def test_system_version_valid():
    ...

# Если условие !=True, то тест пропускается. В теминале видим указанную в reason причину
@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="Тест не может быть запущен на текущей версии"
)
def test_system_version_invalid():
    ...