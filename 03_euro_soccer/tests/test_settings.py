from settings import Settings


def test_settings_class(testdb):
    settings_dev = Settings("development")
    settings_test = Settings("test")

    assert settings_dev.DB == "database.sqlite"
    assert settings_test.DB == ":memory:"
