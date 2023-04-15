from db.models.job import Job
from schemas.job_schema import JobCreateSchema
from sqlalchemy.orm import Session


def create_new_job(job: JobCreateSchema, owner_id: int, session: Session):
    job = Job(
        title=job.title,
        company=job.company,
        location=job.location,
        description=job.description,
        owner_id=owner_id,
    )
    session.add(job)
    session.commit()
    session.refresh(job)
    return job


def retrieve_job(job_id: int, session: Session):
    ans = session.get(Job, job_id)
    if not ans:
        return False
    return ans


def retrieve_all_jobs(session: Session) -> list:
    ans = session.query(Job).all()
    return ans


def update_one_job(job_id: int, job: JobCreateSchema, session: Session):
    last_job = session.query(Job).filter(Job.id == job_id)
    if not last_job.first():
        return False
    last_job.update(job.__dict__)
    session.commit()

    return last_job


def delete_one_job(job_id: int, session: Session) -> bool:
    job = session.query(Job).filter(Job.id == job_id).delete()
    if not job:
        return False
    session.commit()

    return True
