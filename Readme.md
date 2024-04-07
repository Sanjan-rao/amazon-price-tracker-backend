# Amazon Price Tracker

Amazon Price Tracker is a web scraping and data visualization tool that allows users to monitor the price trends of products on Amazon.

## Features

- Web scrapes product pages from Amazon based on a list of ASINs provided in a text file.
- Stores scraped data (ASIN, title, price, and date/time) in a MongoDB database.
- Utilizes React Charts to visualize the price trends of products over time.
- Supports headless browsing for efficient web scraping.

## Technologies Used

- Python for backend web scraping and data storage using Selenium, BeautifulSoup, and pymongo.
- Next.js for frontend development.
- React Charts for data visualization.
- MongoDB for database storage.
- Chrome WebDriver for browser automation.

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Sanjan-rao/amazon-price-tracker.git

```
2. Configure MongoDB connection:

Make sure MongoDB is installed and running on your system.
Update the MongoDB connection URL across the project

3. Run the backend

```bash
cd backend
python main.py

```

4. Run the frontend

```bash
cd ..
cd frontend
npm install
npm run dev
```

### Usage

 - Add ASINs of products to be tracked in product_asins.txt.
 - Run fetch_data.py to scrape product data from Amazon.
 - Run scrape_data.py to extract relevant information from scraped HTML files and store it in the MongoDB database.
 - Access the frontend to view price trends graphically.

### Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests.

### License
This project is licensed under the MIT License.