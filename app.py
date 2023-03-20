from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'mobinulislammahi2627@gmail.com'
app.config['MAIL_PASSWORD'] = '122870Mahi'
mail = Mail(app)
# https://github.com/mobinulislam143/flask-mail.git
# sudo ./VentonyWeb.sh

@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']
        message = Message(subject, sender="mobinulislammahi2627@gmail.com", recipients=[email])
        message.body = msg
        mail.send(message)
        return "Your message is sending successfully."
    return render_template("index.html")



@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)