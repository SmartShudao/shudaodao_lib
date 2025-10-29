#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.source_primary_key

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, Text

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .source_table import SourceTable


class SourcePrimaryKey(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "source_primary_key"
    __table_args__ = {"schema": get_table_schema(), "comment": "主键表"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    source_primary_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="主键内码"
    )
    source_table_id: int = Field(
        unique=True, sa_type=BigInteger, description="表内码",
        foreign_key=f"{get_foreign_schema()}source_table.source_table_id"
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
    SourceTable: "SourceTable" = Relationship(
        back_populates="SourcePrimaryKey", 
        sa_relationship_kwargs={"uselist": False}
    )


class SourcePrimaryKeyBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    source_table_id: int = Field(sa_type=BigInteger, description="表内码")
    name: Optional[str] = Field(default=None, max_length=255, description="约束名字")
    constrained_columns: str = Field(description="字段集合")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class SourcePrimaryKeyCreate(SourcePrimaryKeyBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class SourcePrimaryKeyUpdate(SourcePrimaryKeyBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class SourcePrimaryKeyResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    source_primary_id: int = Field(description="主键内码", sa_type=BigInteger)
    source_table_id: int = Field(description="表内码", sa_type=BigInteger)
    name: Optional[str] = Field(description="约束名字", default=None)
    constrained_columns: str = Field(description="字段集合")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
