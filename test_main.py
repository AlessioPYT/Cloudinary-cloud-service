import pytest
from fastapi.testclient import TestClient
from main import app
from io import BytesIO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    
    with TestClient(app) as c:
        yield c

def test_upload_image(client):
    
    test_image = BytesIO(b"this is a test image")
    test_image.name = "test_image.png"

    response = client.post("/upload/", files={"file": test_image})

    assert response.status_code == 200
    data = response.json()
    assert "original_url" in data
    assert "transformed_url" in data
    assert "qr_code_url" in data

def test_generate_qr_code():
    from photo_service import generate_qr_code

    link = "http://example.com"
    qr_code_img = generate_qr_code(link)

    assert qr_code_img is not None
    assert isinstance(qr_code_img, BytesIO)
