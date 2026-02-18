from utils.db_client import DBClient

def test_user_exists():
    result = DBClient.fetch_user(1)
    assert result is not None
