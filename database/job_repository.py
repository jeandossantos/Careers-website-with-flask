from sqlalchemy import text

from .db_setup import engine


def get_jobs():
  jobs = []

  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    # cria uma lista com as colunas da tabela
    columns = list(result.keys())

    for row_values in result_all:
      job = {}
      # cria um dicionário com as colunas e seus valores
      for col in range(len(columns)):
        job[columns[col]] = row_values[col]
      
      # adiciona o dicionário à lista de jobs
      jobs.append(job)

  return jobs
