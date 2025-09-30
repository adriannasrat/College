# Assignment 1 – Leaflet Web Map

This project is part of the course **Web-based Geographic Information Systems (GIS)** at Dalarna University. It features a simple interactive web map built using **Leaflet.js**, served via **Flask** for local development and GeoJSON file support.

---

## How to Run the Application

To run the project, **download the `flask` folder as a ZIP file or clone the repository**, then follow these steps:

### 1. Install Flask (if you haven't already):

```bash
pip install flask
```

### 2. Start the Flask server:

In the terminal, navigate to the project folder and run:

```bash
python main.py
```

### 3. Open in browser:

Once the server is running, open your browser and go to:

```
http://127.0.0.1:5000/
```

The map and web interface should now be visible.

---

## Folder Structure

```
Assignment_1/
├── main.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── script.js
│   └── data/
│       └── your-geojson-file.geojson
```

- HTML goes inside the `templates/` folder  
- CSS, JS, and GeoJSON files go in `static/` or its subfolders

---

## Technologies Used

- Python
- Flask
- Leaflet.js
- HTML/CSS/JavaScript
- GeoJSON

---

>  This application demonstrates how to combine Python + Flask with Leaflet for interactive web mapping.
