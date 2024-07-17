
# Import necessary modules
from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    # Render the index.html file
    return render_template('index.html')

# Define the results route
@app.route('/results', methods=['POST'])
def results():
    # Get the user's input
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    # Calculate the sum of the two numbers
    sum = int(num1) + int(num2)

    # Render the results.html file with the calculated sum
    return render_template('results.html', sum=sum)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
