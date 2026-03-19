#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2026, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.object_store

from datetime import datetime, date
from typing import Optional
from pydantic import ConfigDict

from sqlalchemy import BigInteger

from shudaodao_core import SQLModel, BaseResponse, Field, get_primary_id
from ...package_config import PackageConfig


class ObjectStore(PackageConfig.RegistryModel, table=True):
    """数据库对象模型"""

    __tablename__ = "object_store"
    __table_args__ = {"schema": PackageConfig.SchemaTable, "comment": "对象存储系统的元数据"}
    # 仅用于内部处理
    __database_schema__ = PackageConfig.SchemaName
    __primary_key__ = ["object_store_id"]

    object_store_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="对象存储内码"
    )
    user_name: str = Field(max_length=50, index=True, description="账户名")
    store_type: int = Field(description="存储类型(业务、个人)")
    store_bucket: str = Field(max_length=255, description="存储桶")
    store_key: str = Field(max_length=512, description="存储对象")
    store_date: date = Field(description="存储日期")
    file_path: Optional[str] = Field(default=None, nullable=True, max_length=255, description="目录名")
    file_name: str = Field(max_length=255, description="文件名")
    file_type: str = Field(max_length=20, description="文件类型")
    db_schema: Optional[str] = Field(
        default=None, nullable=True, max_length=128, description="数据库(schema)"
    )
    db_table: Optional[str] = Field(default=None, nullable=True, max_length=255, description="数据表(table)")
    db_field: Optional[str] = Field(default=None, nullable=True, max_length=255, description="字段名(field)")
    create_by: Optional[str] = Field(default=None, nullable=True, max_length=50, description="创建人")
    create_at: Optional[datetime] = Field(default=None, nullable=True, description="创建日期")
    update_by: Optional[str] = Field(default=None, nullable=True, max_length=50, description="修改人")
    update_at: Optional[datetime] = Field(default=None, nullable=True, description="修改日期")
    tenant_id: Optional[int] = Field(default=None, sa_type=BigInteger, nullable=True, description="租户内码")


class ObjectStoreCreate(SQLModel):
    """前端创建模型 - 用于接口请求"""

    user_name: str = Field(max_length=50, description="账户名")
    store_type: int = Field(description="存储类型(业务、个人)")
    store_bucket: str = Field(max_length=255, description="存储桶")
    store_key: str = Field(max_length=512, description="存储对象")
    store_date: date = Field(description="存储日期")
    file_path: Optional[str] = Field(default=None, max_length=255, description="目录名")
    file_name: str = Field(max_length=255, description="文件名")
    file_type: str = Field(max_length=20, description="文件类型")
    db_schema: Optional[str] = Field(default=None, max_length=128, description="数据库(schema)")
    db_table: Optional[str] = Field(default=None, max_length=255, description="数据表(table)")
    db_field: Optional[str] = Field(default=None, max_length=255, description="字段名(field)")

    model_config = ConfigDict(populate_by_name=True)


class ObjectStoreUpdate(SQLModel):
    """前端更新模型 - 用于接口请求"""

    object_store_id: Optional[int] = Field(default=None, sa_type=BigInteger, description="对象存储内码")
    user_name: Optional[str] = Field(default=None, max_length=50, description="账户名")
    store_type: Optional[int] = Field(default=None, description="存储类型(业务、个人)")
    store_bucket: Optional[str] = Field(default=None, max_length=255, description="存储桶")
    store_key: Optional[str] = Field(default=None, max_length=512, description="存储对象")
    store_date: Optional[date] = Field(default=None, description="存储日期")
    file_path: Optional[str] = Field(default=None, max_length=255, description="目录名")
    file_name: Optional[str] = Field(default=None, max_length=255, description="文件名")
    file_type: Optional[str] = Field(default=None, max_length=20, description="文件类型")
    db_schema: Optional[str] = Field(default=None, max_length=128, description="数据库(schema)")
    db_table: Optional[str] = Field(default=None, max_length=255, description="数据表(table)")
    db_field: Optional[str] = Field(default=None, max_length=255, description="字段名(field)")

    model_config = ConfigDict(populate_by_name=True)


class ObjectStoreResponse(BaseResponse):
    """前端响应模型 - 用于接口响应"""

    __database_schema__ = PackageConfig.SchemaName  # 仅用于内部处理
    object_store_id: int = Field(description="对象存储内码", sa_type=BigInteger)
    user_name: str = Field(description="账户名")
    store_type: int = Field(description="存储类型(业务、个人)")
    store_bucket: str = Field(description="存储桶")
    store_key: str = Field(description="存储对象")
    store_date: date = Field(description="存储日期")
    file_path: Optional[str] = Field(description="目录名", default=None)
    file_name: str = Field(description="文件名")
    file_type: str = Field(description="文件类型")
    db_schema: Optional[str] = Field(description="数据库(schema)", default=None)
    db_table: Optional[str] = Field(description="数据表(table)", default=None)
    db_field: Optional[str] = Field(description="字段名(field)", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)

    model_config = ConfigDict(populate_by_name=True)
