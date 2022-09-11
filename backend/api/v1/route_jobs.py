from fastapi import APIRouter
from fastapi import HTTPException

from db.repository.jobs import (
    create_new_job, 
    retrieve_job, 
    retrieve_all_jobs, 
    delete_one_job, 
    update_one_job
)
from db.session import session
from schemas.job_schema import JobCreateSchema, JobShowSchema


jobs_router = APIRouter()

@jobs_router.post('', response_model=JobShowSchema, status_code=201)
def create_job(job: JobCreateSchema, current_id: int = 1):
    job = create_new_job(job=job, c_id=current_id, db=session)
    return job


@jobs_router.get('{job_id}', response_model=JobShowSchema, status_code=200)
def get_job(job_id: int):
    job = retrieve_job(job_id=job_id, db=session)
    if job:
        return job
    raise HTTPException(404, f"Нет job с id={job_id}") 


@jobs_router.get('/all', status_code=200)
def get_all_jobs():
    job = retrieve_all_jobs(db=session)
    return job


@jobs_router.put('/update{job_id}', status_code=201)
def update_job(job_id: int, job: JobCreateSchema):
    job = update_one_job(job_id=job_id, job=job, db=session)
    if job:
        return {"result": "Data was updated"}
    raise HTTPException(404, f"Нет job с id={job_id}") 


@jobs_router.delete('/job{job_id}')
def delete_job(job_id: int):
    job = delete_one_job(job_id=job_id, db=session)
    if job:
        return {"result": "Data was deleted"}
    raise HTTPException(404, f"Нет job с id={job_id}") 