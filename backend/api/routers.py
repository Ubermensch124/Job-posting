from fastapi import APIRouter

import os, sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from v1.route_homepage import homepage_router
from v1.route_users import users_router
from v1.route_jobs import jobs_router


main_router = APIRouter()
main_router.include_router(homepage_router, tags=['main'], prefix='')
main_router.include_router(users_router, tags=['user'], prefix='/user')
main_router.include_router(jobs_router, tags=['job'], prefix='/job')
