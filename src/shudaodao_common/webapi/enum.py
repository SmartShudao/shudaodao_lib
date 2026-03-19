#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/10/22 下午9:25
# @Desc     ：

from typing import Dict

from fastapi import Path
from sqlmodel.ext.asyncio.session import AsyncSession

from shudaodao_auth import AuthAPIRouter
from shudaodao_core import Depends, ResponseUtil
from shudaodao_meta import PackageConfig, EnumQuery
from ..schema.enum import EnumItemResponse

Meta_Enum_Router = AuthAPIRouter(
    prefix=f"/enums",
    tags=[f"通用接口 - 枚举管理"],
    db_engine_name=PackageConfig.EngineName,  # 配置文件中的数据库连接名称
)


@Meta_Enum_Router.get(
    path="/schemas/{schema_name}/values", summary=["获取schema下所有枚举字段的枚举值"],
    response_model=Dict[str, EnumItemResponse]
)
async def query_schema(
        schema_name: str = Path(description="数据库模式名称"),
        db: AsyncSession = Depends(Meta_Enum_Router.get_async_session)
):
    query_result = await EnumQuery.query_schema(
        db=db, schema_name=schema_name
    )
    return ResponseUtil.success(message="获取枚举成功", data=query_result)


@Meta_Enum_Router.get(
    path="/schemas/{schema_name}/fields/{field_name}/values",
    summary=["获取schema下指定单个字段的枚举值"],
    response_model=Dict[str, EnumItemResponse]
)
async def query_field(
        schema_name: str = Path(description="数据库模式名称"),
        field_name: str = Path(description="字段名字"),
        db: AsyncSession = Depends(Meta_Enum_Router.get_async_session)
):
    query_result = await EnumQuery.query_field(
        db=db, schema_name=schema_name, field_name=field_name
    )
    return ResponseUtil.success(message="获取枚举成功", data=query_result)
