from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Job Application Model
class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.String(100), nullable = False)
    position = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(50), default = "Applied")
    notes = db.Column(db.Text, nullable = True)

# Create Database Tables
with app.app_context():
    db.create_all()

# Route to Add a Job Application
@app.route('/add', methods = ['POST'])
def add_job():
    data = request.json
    new_job = JobApplication(
        company = data['company'],
        position = data['position'],
        status = data.get('status', 'Applied'),
        notes = data.get('notes', '')
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job added successfully!"})

# Route to View All Job Applications
@app.route('/jobs', methods = ['GET'])
def get_jobs():
    jobs = JobApplication.query.all()
    return jsonify([{ "id": job.id, "company": job.company, "position": job.position, "status": job.status, "notes": job.notes } for job in jobs])

# Route to Update a Job Application Status
@app.route('/update/<int:id>', methods = ['PUT'])
def update_job(id):
    job =JobApplication.query.get_or_404(id)
    data = request.json
    job.status = data.get('status', job.status)
    db.session.commit()
    return jsonify({"message": "Job updated successfully!"})

# Route to Delete a Job Application
@app.route('/delete/<int:id>', methods = ['DELETE'])
def delete_job(id):
    job = JobApplication.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job deleted successfully!"})

if __name__ == '__main__':
    app.run(debug = True)