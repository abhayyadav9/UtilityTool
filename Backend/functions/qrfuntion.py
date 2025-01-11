from io import BytesIO
from PIL import Image
import qrcode

def generate_qr_code(data_type, content=None, image_file=None):
    try:
        if data_type == 'image':
            # Handle image upload and QR code overlay
            if not image_file:
                raise ValueError('No image file provided')
            image = Image.open(image_file)

            # Create a QR code
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data('Custom QR Data')  # Customize this data as needed
            qr.make(fit=True)

            # Overlay the QR code onto the image
            qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
            qr_image.thumbnail((100, 100))  # Resize the QR code for better overlay
            image.paste(qr_image, (0, 0), qr_image)  # Overlay at (0,0)

            # Save the resulting image to a buffer
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            buffer.seek(0)

            return buffer

        elif data_type == 'link' or data_type == 'text':
            # Handle QR code generation for a link or text
            if not content:
                raise ValueError('No content provided')

            # Generate QR code for the link/text
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(content)
            qr.make(fit=True)

            # Create a QR code image
            qr_image = qr.make_image(fill_color="green", back_color="white")
            
            # Save the QR code image to a buffer
            buffer = BytesIO()
            qr_image.save(buffer, format="PNG")
            buffer.seek(0)

            return buffer

        else:
            raise ValueError('Invalid type parameter')

    except Exception as e:
        raise e
