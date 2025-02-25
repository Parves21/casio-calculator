from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    
    try:
        # Replace functions with math equivalents
        expression = (
            expression.replace('sin(', 'math.sin(')
            .replace('cos(', 'math.cos(')
            .replace('tan(', 'math.tan(')
            .replace('log(', 'math.log10(')
            .replace('ln(', 'math.log(')
            .replace('√(', 'math.sqrt(')
            .replace('^', '**')
            .replace('π', str(math.pi))
            .replace('e', str(math.e))
        )
        
        # Safe evaluation with math functions
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return jsonify({'result': round(result, 10)})
    except Exception as e:
        return jsonify({'result': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)
    