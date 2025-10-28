#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.meta_index

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, Text, Boolean

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .meta_table import MetaTable


class MetaIndex(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "meta_index"
    __table_args__ = {"schema": get_table_schema(), "comment": "表索引"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    meta_index_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="索引内码"
    )
    meta_table_id: int = Field(
        sa_type=BigInteger, description="表内码", foreign_key=f"{get_foreign_schema()}meta_table.meta_table_id"
    )
    name: str = Field(max_length=255, description="索引名称")
    column_names: str = Field(sa_type=Text, description="字段集合")
    unique: bool = Field(sa_type=Boolean, description="是否唯一")
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
    # 反向关系 -> 父对象
    MetaTable: "MetaTable" = Relationship(back_populates="MetaIndexes")


class MetaIndexBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    meta_table_id: int = Field(sa_type=BigInteger, description="表内码")
    name: str = Field(max_length=255, description="索引名称")
    column_names: str = Field(description="字段集合")
    unique: bool = Field(description="是否唯一")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class MetaIndexCreate(MetaIndexBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class MetaIndexUpdate(MetaIndexBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class MetaIndexResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    meta_index_id: int = Field(description="索引内码", sa_type=BigInteger)
    meta_table_id: int = Field(description="表内码", sa_type=BigInteger)
    name: str = Field(description="索引名称")
    column_names: str = Field(description="字段集合")
    unique: bool = Field(description="是否唯一")
    sort_order: int = Field(description="排序权重")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
