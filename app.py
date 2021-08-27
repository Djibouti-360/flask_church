from flask import Flask, render_template

# set up application
app = Flask(__name__)

# set up index route
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/outreach', methods=['POST','GET'])
def outreach():
    return render_template('outreach.html')

@app.route('/about', methods=['POST','GET'])
def about():
    return render_template('about.html')

@app.route('/give', methods=['POST','GET'])
def give():
    return render_template('give.html')

if __name__ == "__main__":
    app.run(debug=True)