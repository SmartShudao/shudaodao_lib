#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.source_schema

from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import BigInteger

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema

if TYPE_CHECKING:
    from .source_table import SourceTable
    from .source_view import SourceView


class SourceSchema(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "source_schema"
    __table_args__ = {"schema": get_table_schema(), "comment": "架构元数据"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    source_schema_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="架构内码"
    )
    schema_label: Optional[str] = Field(default=None, max_length=128, nullable=True, description="架构中文")
    schema_name: str = Field(max_length=128, description="数据库架构")
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
    # 正向关系 -> 子对象
    SourceTables: list["SourceTable"] = Relationship(
        back_populates="SourceSchema", sa_relationship_kwargs={
            "order_by": "SourceTable.sort_order.asc()"
        }
    )
    SourceViews: list["SourceView"] = Relationship(
        back_populates="SourceSchema", sa_relationship_kwargs={
            "order_by": "SourceView.sort_order.asc()"
        }
    )


class SourceSchemaBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    schema_label: Optional[str] = Field(default=None, max_length=128, description="架构中文")
    schema_name: str = Field(max_length=128, description="数据库架构")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class SourceSchemaCreate(SourceSchemaBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class SourceSchemaUpdate(SourceSchemaBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class SourceSchemaResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    source_schema_id: int = Field(description="架构内码", sa_type=BigInteger)
    schema_label: Optional[str] = Field(description="架构中文", default=None)
    schema_name: str = Field(description="数据库架构")
    sort_order: int = Field(description="排序权重")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
