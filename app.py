from flask import Flask, render_template, url_for, request, jsonify
import cohere
import cohereIntegration

app = Flask(__name__, template_folder='static/templates') 

#app decorator that creates a default route for program; defined in function
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)











