#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2026/2/8 下午9:39
# @Desc     ：

from datetime import date

from fastapi import Path
from sqlmodel.ext.asyncio.session import AsyncSession

from shudaodao_auth import AuthAPIRouter
from shudaodao_core import AsyncStorageService, DataService
from shudaodao_core import ResponseUtil, Depends, get_primary_id, StorageTypeEnum
from shudaodao_core.tools import RustfsChecker
from shudaodao_meta import PackageConfig, ObjectStore
from ..schema.signed_model import ResponseSignedModel

ObjectStorage_Router = AuthAPIRouter(
    prefix="/object-storage",
    tags=[f"通用接口 - 分布式文件存储"],
    db_engine_name=PackageConfig.EngineName,  # 配置文件中的数据库连接名称
)


@ObjectStorage_Router.get(
    "/upload_signed_url/{schema}/{table}/{field}/{files}", summary=["生成上传预签名URL"],
    response_model=list[ResponseSignedModel]
)
async def generate_upload_signed_url(
        schema: str = Path(..., description="数据库模式"),
        table: str = Path(..., description="数据库表名"),
        field: str = Path(..., description="数据表字段"),
        files: str = Path(..., description="要上传的文件名清单(逗号分隔)"),
        db: AsyncSession = Depends(ObjectStorage_Router.get_async_session)
):
    file_names = files.split(",")
    store_date: date = date.today()
    # prefix 的规则 表名+字段名+年+月+日
    date_prefix = f"table={table}/{store_date.strftime('year=%Y/month=%m/day=%d')}"
    user_name = ObjectStorage_Router.curr_user.username
    store_bucket = RustfsChecker.get_bucket_name(schema)
    store_service = AsyncStorageService()
    store_client = store_service.get_s3_client(schema_name=schema)
    result: list[ResponseSignedModel] = []
    for file_name in file_names:
        object_store_id = get_primary_id()
        file_type = file_name.split(".")[-1]
        # key 的规则 prefix/id=id/文件名
        store_key = f"{date_prefix}/id={object_store_id}/{file_name}"
        model_create = {  # 采用 dict 作为参数可以传递 object_store_id
            "object_store_id": object_store_id, "user_name": user_name,
            "store_type": StorageTypeEnum.Business.value,  # 区分个人还是业务
            "store_bucket": store_bucket, "store_key": store_key, "store_date": store_date,
            "file_name": file_name, "file_type": file_type,
            "db_schema": schema, "db_table": table, "db_field": field,
        }
        await DataService.create(db=db, create_model=model_create, model_class=ObjectStore)
        result.append(ResponseSignedModel(
            key=object_store_id,
            url=store_service.generate_signed_url(
                s3_client=store_client, schema_name=schema, store_key=store_key, method="put_object"
            )
        ))
    return ResponseUtil.success(data=result)


@ObjectStorage_Router.get(
    "/download_signed_url/{ids}", summary=["生成下载预签名URL"],
    response_model=list[ResponseSignedModel]
)
async def generate_download_signed_url(
        ids: str = Path(description="文件存储的内码(逗号分隔)"),
        db: AsyncSession = Depends(ObjectStorage_Router.get_async_session)
):  # -> list[ResponseSignedModel]:
    primary_ids = ids.split(",")
    store_service = AsyncStorageService()
    result: list[ResponseSignedModel] = []
    for primary_id in primary_ids:
        object_response = await DataService.read(
            db=db, primary_id=int(primary_id), model_class=ObjectStore
        )
        result.append(ResponseSignedModel(
            key=object_response.object_store_id,
            url=store_service.generate_signed_url(
                schema_name=object_response.db_schema,
                store_key=object_response.store_key, method="get_object"
            )
        ))
    return ResponseUtil.success(data=result)
