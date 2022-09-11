from schemas.job_schema import JobCreateSchema
from sqlalchemy.orm import Session
from db.models.user import Job


def create_new_job(job: JobCreateSchema, c_id, db: Session):
    job = Job(
        title = job.title,
        company = job.company,
        location = job.location,
        description = job.description,
        )

    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def retrieve_job(job_id: int, db: Session):
    ans = db.get(Job, job_id)
    if ans:
        return ans
    return False    


def retrieve_all_jobs(db: Session) -> list:
    ans = db.query(Job).all()
    return ans


def update_one_job(job_id: int, job: JobCreateSchema, db: Session):
    last_job = db.query(Job).filter(Job.id == job_id)
    if not last_job.first():
        return False
    last_job.update(job.__dict__)
    db.commit()

    return last_job


def delete_one_job(job_id: int, db: Session) -> bool:
    job = db.query(Job).filter(Job.id == job_id).delete()
    if not job:
        return False
    db.commit()

    return True