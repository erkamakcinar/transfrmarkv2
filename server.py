from flask import Flask,render_template, url_for

app = Flask(__name__)
teams = ["fb", "gs", "bjk", "ts"]
x=8
@app.route("/")
def home():
    return render_template('home.html', title='Best Football Site', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)