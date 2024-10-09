import cloudinary
import cloudinary.uploader
import qrcode
from io import BytesIO


cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

def upload_image_to_cloudinary(file):
    """Загрузка изображения в Cloudinary"""
    result = cloudinary.uploader.upload(file)
    return result['url'], result['public_id']

def transform_image(public_id):
    """Трансформация изображения"""
    transformed_url = cloudinary.CloudinaryImage(public_id).build_url(transformation=[
        {'width': 500, 'height': 500, 'crop': 'fill'}
    ])
    return transformed_url

def generate_qr_code(link: str):
    """Генерация QR-кода для ссылки"""
    img = qrcode.make(link)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
