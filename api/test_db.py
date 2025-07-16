from sqlalchemy import text
from database import engine  # Import your configured engine

def test_db_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            assert result.scalar() == 1
    except Exception as e:
        assert False, f"Database connection failed: {e}"
