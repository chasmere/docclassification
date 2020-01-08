from flask import Flask, render_template,  request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        data = request.form['content']
        if data == '':
            return render_template("index.html")
        else:
            result= 'Testing'
            return render_template("index.html", result = result)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()
