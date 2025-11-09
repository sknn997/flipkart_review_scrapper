# python_project2_flipkart_review_scrapper

# 🛒 Flipkart Product Review Scraper

A Flask-based web application that scrapes **product reviews from Flipkart** and stores them in **MongoDB** for analysis.  
This project demonstrates full-stack integration of **web scraping, data storage, and frontend display** using Python.

---

## 📸 Preview

> **User Flow:**
> 1. Enter a product name in the search bar.  
> 2. The app scrapes the top product page on Flipkart.  
> 3. Extracted reviews (name, rating, comment) are displayed beautifully and saved in MongoDB.

---

## 🚀 Features

- 🧠 **BeautifulSoup + Requests + urllib** used for web scraping.  
- 🗃️ **MongoDB Atlas** used for cloud-based review storage.  
- ⚡ **Flask web framework** for handling routes and templates.  
- 💾 Reviews saved in `.csv` and database simultaneously.  
- 🧰 Structured logging using Python’s `logging` module.  
- 🎨 Simple and responsive frontend using HTML + CSS.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Frontend** | HTML, CSS, Jinja2 Templates |
| **Backend** | Python (Flask) |
| **Database** | MongoDB Atlas |
| **Web Scraping** | BeautifulSoup, Requests, urllib |
| **Logging** | Python Logging Module |

---

## ⚙️ Project Structure

Flipkart-Review-Scraper/
│
├── static/
│ └── css/
│ └── style.css # Styling for the HTML pages
│
├── templates/
│ ├── index.html # Homepage with search form
│ └── result.html # Displays scraped reviews
│
├── app.py # Main Flask application
├── scrapper.log # Logging file (auto-generated)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


<img width="1920" height="1008" alt="Screenshot 2025-11-09 164432" src="https://github.com/user-attachments/assets/09f15efe-7d47-4101-93ba-b472810a281e" />

