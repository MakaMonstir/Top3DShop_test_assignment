# Creality Scanner Scraper (Not a final version)

This project is a part of a test assignment to scrape 3D scanner data from the official Creality store using Selenium, within a Dockerized environment.

## Features

- Collects product links from the Creality 3D scanners catalog page
- Extracts product name, price, and shipping info
- Runs using Docker Compose with Selenium Standalone Chrome

## Prerequisites

- Docker
- Docker Compose

## Setup and Run

1. Build and start the containers:

```bash
docker-compose up --build
```

2. The scraper will run automatically or can be triggered manually via:

```
docker-compose exec scraper python main.py
```

## 🛠 Environment Variables

- `SELENIUM_REMOTE_URL`: Remote WebDriver URL, default: `http://chrome:4444/wd/hub`

## 📄 Output

The scraper will output a CSV file with the following fields:

- Product Name
- Price
- Shipping Time
- Product URL
