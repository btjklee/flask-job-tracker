# Flask Job Tracker

A simple web-based job tracking application to manage job applications efficiently.

## 🚀 Live Demo
[Flask Job Tracker](https://flask-job-tracker.onrender.com)

## 📌 Features
- Add, update, and delete job applications
- Stores data using PostgreSQL
- REST API endpoints for easy integration
- Responsive UI with Bootstrap

## 🖥️ Screenshot
![Job Tracker Screenshot](job-tracker-screenshot.png)

## 💻 Tech Stack
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: Bootstrap, HTML, JavaScript
- **Deployment**: Render.com

## 📜 API Endpoints
| Method | Endpoint          | Description                 |
|--------|------------------|-----------------------------|
| GET    | `/jobs`         | Retrieve all job entries    |
| POST   | `/add`          | Add a new job               |
| PUT    | `/update/<id>`  | Update job status by ID     |
| DELETE | `/delete/<id>`  | Delete a job entry by ID    |

### Example API Request (Adding a Job)
```bash
curl -X POST "https://flask-job-tracker.onrender.com/add" \
     -H "Content-Type: application/json" \
     -d '{"company": "Amazon", "position": "Backend Engineer", "status": "Interview Scheduled", "notes": "Phone screen next week"}'
```

## 🛠️ Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/btjklee/flask-job-tracker.git
cd flask-job-tracker
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your **DATABASE_URL**
```
DATABASE_URL=postgresql://your_username:your_password@your_host/your_database
```

### 5️⃣ Run the Application
```bash
flask run
```
Your app will be running on `http://127.0.0.1:5000`

## 🚀 Future Improvements
- Add **user authentication** for private job tracking
- Improve **security** by adding API keys
- Enhance **data visualization** (charts, insights, analytics)

## 📜 License
This project is open-source and available under the MIT License.

---

