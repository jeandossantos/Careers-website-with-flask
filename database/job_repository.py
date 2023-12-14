from sqlalchemy import text

from .db_setup import engine


def parse_sqlachemy_row_to_dict(columns, row):
  job = {}
  # cria um dicionário com as colunas e seus valores
  for col in range(len(columns)):
    job[columns[col]] = row[col]

  return job


def load_jobs_from_db():
   with engine.connect() as conn:
    jobs = conn.execute(text("select * from jobs"))

    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :id"),
                          {"id": id})
    result_all = result.all()

    if len(result_all) == 0:
      return None

    columns = list(result.keys())
    job = parse_sqlachemy_row_to_dict(columns, tuple(result_all[0]))

    return job
