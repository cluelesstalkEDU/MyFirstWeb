from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/p2")
def page2():
    my_name = "Rafin"
    return render_template('page2.html', this_guy=my_name)

@app.route("/bio")
def bio():
    return render_template('bio.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)