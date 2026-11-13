from flask import Flask, render_template

app = Flask(__name__)

# --- route kamu di sini ---
@app.route('/')
def home():
    return render_template('index.html')

app = app

if __name__ == '__main__':
    app.run()