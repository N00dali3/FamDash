from flask import Flask, render_template

app = Flask(FamDash)

# Homepage route
@app.route('/')
def home():
    return "Welcome to the FamDash Homepage."

# Info route that renders the HTML page
@app.route('/info')
def info():
    return render_template('index.html')

if FamDash  == '__main__':
    app.run(debug=True)
