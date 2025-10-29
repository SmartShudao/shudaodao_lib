#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.source_unique_constraint

from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, Text

from shudaodao_core import Field, get_primary_id
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema


class SourceUniqueConstraint(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "source_unique_constraint"
    __table_args__ = {"schema": get_table_schema(), "comment": "表约束"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    source_unique_constraint_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="约束内码"
    )
    source_table_id: int = Field(sa_type=BigInteger, description="表内码")
    name: Optional[str] = Field(default=None, max_length=255, nullable=True, description="约束名称")
    column_names: str = Field(sa_type=Text, description="字段集合")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, nullable=True, description="描述")
    create_by: Optional[str] = Field(default=None, max_length=50, nullable=True, description="创建人")
    create_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0), nullable=True, description="创建日期"
    )
    update_by: Optional[str] = Field(default=None, max_length=50, nullable=True, description="修改人")
    update_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0), nullable=True, description="修改日期"
    )


class SourceUniqueConstraintBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    source_table_id: int = Field(sa_type=BigInteger, description="表内码")
    name: Optional[str] = Field(default=None, max_length=255, description="约束名称")
    column_names: str = Field(description="字段集合")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class SourceUniqueConstraintCreate(SourceUniqueConstraintBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class SourceUniqueConstraintUpdate(SourceUniqueConstraintBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class SourceUniqueConstraintResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    source_unique_constraint_id: int = Field(description="约束内码", sa_type=BigInteger)
    source_table_id: int = Field(description="表内码", sa_type=BigInteger)
    name: Optional[str] = Field(description="约束名称", default=None)
    column_names: str = Field(description="字段集合")
    sort_order: int = Field(description="排序权重")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
