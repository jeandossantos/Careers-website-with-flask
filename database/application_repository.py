from sqlalchemy import text

from .db_setup import engine

def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    
    conn.execute(query, {
      "job_id": job_id,
      "full_name": application['full_name'],
      "email": application['email'],
      "linkedin_url": application['linkedin_url'],
      "education": application['education'],
      "work_experience": application['work_experience'],
      "resume_url": application['resume_url']
    })