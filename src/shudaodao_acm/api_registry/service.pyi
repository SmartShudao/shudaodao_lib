from ..generate.entity_table.sys_interface import Interface as Interface
from .hasher import build_api_hash as build_api_hash
from .scanner import scan_fastapi_routes as scan_fastapi_routes
from fastapi import FastAPI as FastAPI

async def sync_api_registry(app: FastAPI) -> None: ...
