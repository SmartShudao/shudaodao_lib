from fastapi import FastAPI as FastAPI
from fastapi.routing import APIRoute

def extract_description(route: APIRoute) -> str | None: ...
def format_summary(summary) -> str:
    """将summary统一格式化为字符串"""

def scan_fastapi_routes(app: FastAPI) -> list[dict]: ...
