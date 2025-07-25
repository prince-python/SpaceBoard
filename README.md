# 🌌 SpaceBoard - Satellite & Planetary Dashboard

**SpaceBoard** is a Django-powered web application with a responsive Bootstrap frontend that visualizes real-time space data — from live satellite tracking to the latest Mars rover images.

## 🚀 Features

- 🛰️ **Satellite Constellation Visualizer**  
  Displays live satellite positions (like Starlink, GPS, NOAA) using TLE data from CelesTrak.

- 🌍 **ISS Tracker**  
  Shows the current position of the International Space Station (ISS) in real time on an interactive map.

- 🔴 **Mars Rover Image Viewer**  
  Fetches and displays recent images from NASA's Mars rovers (Curiosity, Perseverance, etc.) using the NASA Mars Rover API.

---

## 🗂️ Project Structure

spaceboard/
├── core/
│ ├── migrations/
│ ├── static/
│ │ └── css, js, images/
│ ├── templates/
│ │ ├── index.html
│ │ ├── iss_tracker.html
│ │ ├── constellation.html
│ │ └── mars.html
│ ├── urls.py
│ └── views.py
├── spaceboard/
│ ├── settings.py
│ └── urls.py
├── manage.py
└── db.sqlite3

yaml
Copy
Edit

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **APIs**:
  - [CelesTrak](https://celestrak.org/) – for TLE satellite data
  - [Open Notify](http://api.open-notify.org/) – for ISS real-time position
  - [NASA Mars Rover API](https://api.nasa.gov/) – for Mars rover images

---

## 🌐 URL Routing

| Route | Purpose |
|-------|---------|
| `/` | Landing/Home page |
| `/mars/` | Mars Rover Photo Viewer |
| `/iss-tracker/` | Live ISS Tracker |
| `/satellite-constellation/` | Satellite Visualization Map |

---

## ⚙️ Installation & Run

### 1. Clone this repository

```bash
git clone https://github.com/your-username/spaceboard.git
cd spaceboard
2. Install required packages
bash
Copy
Edit
pip install -r requirements.txt
3. Run migrations
bash
Copy
Edit
python manage.py migrate
4. Start the development server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

📸 Screenshots
Add screenshots here if needed.

📌 Future Updates (Planned)
🌐 Satellite filter by country/operator

📍 Constellation toggle with real-time orbits

📁 PDF export of rover photos

🛰️ 3D Globe using CesiumJS (optional upgrade)

📝 License
This project is under the MIT License.
Feel free to use, modify, and share — just give credit 💖

👨‍💻 Developed By
Prince Chaudhary
Cybersecurity & Space Tech Enthusiast 🚀
LinkedIn | Email