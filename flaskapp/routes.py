from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    list_example = ['Alvin','Simon', 'Theodore']
    return render_template('index1.html', list_example=list_example)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
