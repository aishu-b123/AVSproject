
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Function to load data from CSV files into a list of dictionaries
def load_data():
    data = []
    # Add more CSV files here if needed
    csv_files = ['products1.csv', 'products2.csv']
    for file_name in csv_files:
        with open(f'csv_files/{file_name}', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    return data

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Search functionality
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['search_query'].lower()
    data = load_data()
    search_results = []
    for product in data:
        if query in product['product_name'].lower():
            search_results.append(product)
    return render_template('index.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
