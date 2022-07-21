from flask import Flask,render_template

app = Flask(__name__)

x=8
@app.route("/")
def home():
    return render_template('home.html', title='Best Football Site', x=x)

if __name__ == '__main__':
    app.run(debug=True)