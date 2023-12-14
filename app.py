from flask import Flask, jsonify, render_template

from database.job_repository import get_jobs

app = Flask(__name__)


@app.route("/")
def hello():
  jobs = get_jobs()
  return render_template('home.html', jobs=jobs, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  jobs = get_jobs()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3001, debug=True)
