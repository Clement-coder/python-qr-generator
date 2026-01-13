from flask import Flask, request, jsonify, send_from_directory
import qrcode
import os

app = Flask(__name__, static_url_path='/static')

# Create a directory for static files if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate')
def generate_qrcode():
    text = request.args.get('text')
    if not text:
        return jsonify({'error': 'Text is required'}), 400

    img_path = os.path.join('static', 'qrcode.png')
    img = qrcode.make(text)
    img.save(img_path)
    
    return jsonify({'qr_code_url': f'/{img_path}'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
