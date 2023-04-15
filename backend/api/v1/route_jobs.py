from typing import List

from db.models.user import User
from db.repository.jobs import (
    create_new_job,
    delete_one_job,
    retrieve_all_jobs,
    retrieve_job,
    update_one_job,
)
from db.session import get_session
from fastapi import APIRouter, Depends, HTTPException
from schemas.job_schema import JobCreateSchema, JobShowSchema
from sqlalchemy.orm import Session
from v1.route_login import get_current_user

jobs_router = APIRouter()


@jobs_router.post("", response_model=JobShowSchema, status_code=201)
def create_job(
    job: JobCreateSchema,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    job = create_new_job(job=job, owner_id=current_user.id, session=session)
    return job


@jobs_router.get("{job_id}", response_model=JobShowSchema, status_code=200)
def get_job(job_id: int, session: Session = Depends(get_session)):
    job = retrieve_job(job_id=job_id, session=session)
    if job:
        return job
    raise HTTPException(404, f"Нет job с id={job_id}")


@jobs_router.get("/all", response_model=List[JobShowSchema], status_code=200)
def get_all_jobs(session: Session = Depends(get_session)):
    job = retrieve_all_jobs(session=session)
    return job


@jobs_router.put("/update{job_id}", status_code=201)
def update_job(job_id: int, job: JobCreateSchema, session: Session = Depends(get_session)):
    job = update_one_job(job_id=job_id, job=job, session=session)
    if job:
        return {"result": "Data was updated"}
    raise HTTPException(404, f"Нет job с id={job_id}")


@jobs_router.delete("/job{job_id}")
def delete_job(job_id: int, session: Session = Depends(get_session)):
    job = delete_one_job(job_id=job_id, session=session)
    if job:
        return {"result": "Data was deleted"}
    raise HTTPException(404, f"Нет job с id={job_id}")
