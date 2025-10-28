#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.meta_primary_key

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, Text

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .meta_table import MetaTable


class MetaPrimaryKey(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "meta_primary_key"
    __table_args__ = {"schema": get_table_schema(), "comment": "主键表"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    meta_primary_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="主键内码"
    )
    meta_table_id: int = Field(
        unique=True, sa_type=BigInteger, description="表内码",
        foreign_key=f"{get_foreign_schema()}meta_table.meta_table_id"
    )
    name: Optional[str] = Field(default=None, max_length=255, nullable=True, description="约束名字")
    constrained_columns: str = Field(sa_type=Text, description="字段集合")
    description: Optional[str] = Field(default=None, max_length=500, nullable=True, description="描述")
    create_by: Optional[str] = Field(default=None, max_length=50, nullable=True, description="创建人")
    create_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0), nullable=True, description="创建日期"
    )
    update_by: Optional[str] = Field(default=None, max_length=50, nullable=True, description="修改人")
    update_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0), nullable=True, description="修改日期"
    )
    # 反向关系 -> 父对象
    # noinspection SpellCheckingInspection
    MetaTable: "MetaTable" = Relationship(
        back_populates="MetaPrimaryKey", 
        sa_relationship_kwargs={"uselist": False}
    )


class MetaPrimaryKeyBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    meta_table_id: int = Field(sa_type=BigInteger, description="表内码")
    name: Optional[str] = Field(default=None, max_length=255, description="约束名字")
    constrained_columns: str = Field(description="字段集合")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class MetaPrimaryKeyCreate(MetaPrimaryKeyBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class MetaPrimaryKeyUpdate(MetaPrimaryKeyBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class MetaPrimaryKeyResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    meta_primary_id: int = Field(description="主键内码", sa_type=BigInteger)
    meta_table_id: int = Field(description="表内码", sa_type=BigInteger)
    name: Optional[str] = Field(description="约束名字", default=None)
    constrained_columns: str = Field(description="字段集合")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
