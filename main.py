from fastapi import FastAPI, UploadFile, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import PhotoLink
from photo_service import upload_image_to_cloudinary, transform_image, generate_qr_code

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile, db: Session = Depends(get_db)):
    
    original_url, public_id = upload_image_to_cloudinary(file.file)

    
    transformed_url = transform_image(public_id)

    
    qr_code_img = generate_qr_code(transformed_url)
    
    
    with open("qr_code.png", "wb") as f:
        f.write(qr_code_img.read())

    
    photo_link = PhotoLink(
        original_url=original_url,
        transformed_url=transformed_url,
        qr_code_url="path_to_saved_qr_code"
    )
    db.add(photo_link)
    db.commit()

    return {"original_url": original_url, "transformed_url": transformed_url, "qr_code_url": "path_to_saved_qr_code"}
