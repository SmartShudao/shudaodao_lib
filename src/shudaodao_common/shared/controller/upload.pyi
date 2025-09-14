from ..entity.upload import UploadFileModel as UploadFileModel
from ..service.upload_service import UploadService as UploadService
from _typeshed import Incomplete
from fastapi import UploadFile as UploadFile

Upload_Router: Incomplete

async def get_files(path_name: str): ...
async def upload(path_name: str, files: list[UploadFile] = ...): ...
async def delete_file(path_name: str, files: list[UploadFileModel]): ...
