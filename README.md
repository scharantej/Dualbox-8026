### HTML Files
- **index.html**
  - This is the main HTML file for the application. 
  - It contains two text boxes for user input and a button to submit the data.

- **results.html**
  - This HTML file displays the results of the user's input. 
  -  It is rendered when the user clicks the submit button.

### Routes
- **@app.route('/')**
  - This is the main route of the application. 
  - It renders the index.html file.

- **@app.route('/results', methods=['POST'])**
  - This route handles the submission of the form from index.html. 
  - It processes the user's input and renders the results.html file with the appropriate data.