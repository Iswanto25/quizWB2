
from flask import Flask,request
app = Flask(__name__)


@app.route('/BMI', methods=['POST'])
def BMI():
    tinggi = float(request.form.get("tinggi"))
    berat = float(request.form.get("berat"))
    BMI = berat / (tinggi/100)**2
    if BMI <= 18.5:
        hasil = "KURUS"
    elif BMI <= 25:
        hasil = "SEHAT"
    elif BMI <= 40:
        hasil = "BERLEBIHAN"
    else:
        hasil = "OBESITAS"
    data = {'Score BMI': BMI,'Tergolong': hasil}
    return data


if __name__ == '__main__':
    app.run(debug=True,)