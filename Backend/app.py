from flask import Flask, request, jsonify, send_file
from io import BytesIO
from PIL import Image
import rembg
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow React to connect

@app.route('/remove-background', methods=['POST'])
def remove_bg():
    try:
        print("Received Image")
        # Get the image from the request
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        file = request.files['image']
        
        # Read the image file
        input_image = file.read()

        # Remove background using rembg
        output_image = rembg.remove(input_image)

        # Convert the output to a PIL Image
        img = Image.open(BytesIO(output_image))

        # Save the processed image to a buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Return the image with no background
        return send_file(buffer, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # Get name parameter
    greeting = f"Hello, {name}!"
    return jsonify({'greeting': greeting})  # Return JSON response


@app.route('/generate-qr', methods=['POST'])
def create_qr():
    try:
        # Get the data type (either 'image', 'text', or 'link')
        data_type = request.form.get('type', 'text')  # Default to 'text' if no type is provided
        
        if data_type == 'image':
            # Handle image upload and QR code overlay
            if 'image' not in request.files:
                return jsonify({'error': 'No image file uploaded'}), 400
            image_file = request.files['image']
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

            # Return the image as a response
            return send_file(buffer, mimetype='image/png')

        elif data_type == 'link' or data_type == 'text':
            # Handle QR code generation for a link or text
            content = request.form.get('content')
            if not content:
                return jsonify({'error': 'No content provided'}), 400

            # Generate QR code for the link/text
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(content)
            qr.make(fit=True)

            # Create a QR code image
            qr_image = qr.make_image(fill_color="green", back_color="black")
            
            # Save the QR code image to a buffer
            buffer = BytesIO()
            qr_image.save(buffer, format="PNG")
            buffer.seek(0)

            # Return the QR code image as a response
            return send_file(buffer, mimetype='image/png')

        else:
            return jsonify({'error': 'Invalid type parameter'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500



    
    
if __name__ == '__main__':
    app.run(debug=True)
