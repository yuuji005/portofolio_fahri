from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Railway akan memberikan port secara otomatis melalui environment variable 'PORT'
    # Jika tidak ada (saat run di laptop), maka akan default ke port 5000
    port = int(os.environ.get("PORT", 5000))
    
    # host='0.0.0.0' wajib agar server bisa diakses dari luar
    # debug=False sebaiknya dimatikan saat sudah online (production)
    app.run(host='0.0.0.0', port=port, debug=False)