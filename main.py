from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/carta', methods=['GET', 'POST'])
def carta():
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        if fecha == "04/05/24":
            return send_file('static/assets/carta.pdf', as_attachment=True)
        else:
            return "Respuesta incorrecta. Intenta de nuevo."
    return render_template('carta.html')

if __name__ == '__main__':
    app.run(debug=True)