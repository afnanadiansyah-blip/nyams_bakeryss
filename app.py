from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Mengarahkan halaman utama ke file index.html di dalam folder templates
    return render_template('index.html')

if __name__ == '__main__':
    # Memasang mode debug agar perubahan otomatis terbarui
    app.run(debug=True)