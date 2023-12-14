from flask import Flask, jsonify, render_template, request

from database.job_repository import load_job_from_db, load_jobs_from_db
from database.application_repository import add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)

  if job is None:
    return 'Not Founded', 404
    
  return render_template('job-page.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  
  #save into database
  add_application_to_db(id, data)

  return render_template('application_submited.html', application=data, job=job)
  
#-------- API ROUTES ---------


@app.route('/api/jobs/<id>')
def get_job(id):
  job = load_job_from_db(id)

  return jsonify(job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3001, debug=True)
