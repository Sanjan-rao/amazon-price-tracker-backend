from flask import Flask, request
from main import fetch_Data, scrape_Data

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/addproduct', methods=['POST'])
def add_url():
    try:
        if request.is_json:
            data = request.json
            url = data.get('url')
            if url:
                with open('product_asins.txt', 'a') as file:
                    file.write(url + '\n')
                fetch_Data()
                scrape_Data()
                return 'URL added successfully', 200
            else:
                return 'Error: No URL provided in JSON data', 400
        else:
            return 'Error: Request body is not JSON', 400
    except Exception as e:
        return f'Error: {e}', 500

if __name__ == "__main__":
    app.run(debug=True)