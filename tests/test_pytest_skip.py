import pytest

# reason в консоли отображает причину пропуска теста
# Пример использования: тест готов еще не на выкаченную функциональность / отключенные на время фичи
@pytest.mark.skip(reason='Фича еще в разработке')
def test_feature_in_development():
    pass