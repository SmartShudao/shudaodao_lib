from ..utils.response_utils import ResponseUtil as ResponseUtil
from .service_exception import AuthException as AuthException, ShudaodaoException as ShudaodaoException
from fastapi import FastAPI as FastAPI, Request as Request

def register_exception_handlers(app: FastAPI): ...
