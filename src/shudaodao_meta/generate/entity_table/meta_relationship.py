#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.meta_relationship

from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .meta_table import MetaTable


class MetaRelationship(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "meta_relationship"
    __table_args__ = {"schema": get_table_schema(), "comment": "SQLModel字段关系"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    relationship_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="关系内码"
    )
    table_id: Optional[int] = Field(
        default=None, nullable=True, sa_type=BigInteger, description="表内码",
        foreign_key=f"{get_foreign_schema()}meta_table.table_id"
    )
    direction: str = Field(max_length=255, description="正向关系(子)、反向关系(父)")
    unique: bool = Field(sa_type=Boolean, description="唯一约束-判断1对1关系")
    constrained_schema: str = Field(max_length=255, description="当前对象 - 模式")
    constrained_table: str = Field(max_length=255, description="当前对象 - 表")
    constrained_column: str = Field(max_length=255, description="当前对象 - 列")
    constrained_index: str = Field(max_length=255, description="当前对象 - 索引")
    constrained_field: str = Field(max_length=255, description="当前对象 - 字段")
    constrained_class: str = Field(max_length=255, description="当前对象 - 类")
    referred_schema: str = Field(max_length=255, description="引用对象 - 模式")
    referred_table: str = Field(max_length=255, description="引用对象 - 表")
    referred_column: str = Field(max_length=255, description="引用对象 - 列")
    referred_index: str = Field(max_length=255, description="引用对象 - 索引")
    referred_field: str = Field(max_length=255, description="引用对象 - 字段")
    referred_class: str = Field(max_length=255, description="引用对象 - 类")
    options: Optional[str] = Field(default=None, max_length=255, nullable=True, description="行为选项")
    sort_order: int = Field(default=10, description="排序权重")
    is_active: bool = Field(sa_type=Boolean, description="启用状态")
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
    Table: "MetaTable" = Relationship(back_populates="MetaRelationships")


class MetaRelationshipBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    table_id: Optional[int] = Field(default=None, sa_type=BigInteger, description="表内码")
    direction: str = Field(max_length=255, description="正向关系(子)、反向关系(父)")
    unique: bool = Field(description="唯一约束-判断1对1关系")
    constrained_schema: str = Field(max_length=255, description="当前对象 - 模式")
    constrained_table: str = Field(max_length=255, description="当前对象 - 表")
    constrained_column: str = Field(max_length=255, description="当前对象 - 列")
    constrained_index: str = Field(max_length=255, description="当前对象 - 索引")
    constrained_field: str = Field(max_length=255, description="当前对象 - 字段")
    constrained_class: str = Field(max_length=255, description="当前对象 - 类")
    referred_schema: str = Field(max_length=255, description="引用对象 - 模式")
    referred_table: str = Field(max_length=255, description="引用对象 - 表")
    referred_column: str = Field(max_length=255, description="引用对象 - 列")
    referred_index: str = Field(max_length=255, description="引用对象 - 索引")
    referred_field: str = Field(max_length=255, description="引用对象 - 字段")
    referred_class: str = Field(max_length=255, description="引用对象 - 类")
    options: Optional[str] = Field(default=None, max_length=255, description="行为选项")
    sort_order: int = Field(default=10, description="排序权重")
    is_active: bool = Field(description="启用状态")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class MetaRelationshipCreate(MetaRelationshipBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class MetaRelationshipUpdate(MetaRelationshipBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class MetaRelationshipResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    relationship_id: int = Field(description="关系内码", sa_type=BigInteger)
    table_id: Optional[int] = Field(description="表内码", default=None, sa_type=BigInteger)
    direction: str = Field(description="正向关系(子)、反向关系(父)")
    unique: bool = Field(description="唯一约束-判断1对1关系")
    constrained_schema: str = Field(description="当前对象 - 模式")
    constrained_table: str = Field(description="当前对象 - 表")
    constrained_column: str = Field(description="当前对象 - 列")
    constrained_index: str = Field(description="当前对象 - 索引")
    constrained_field: str = Field(description="当前对象 - 字段")
    constrained_class: str = Field(description="当前对象 - 类")
    referred_schema: str = Field(description="引用对象 - 模式")
    referred_table: str = Field(description="引用对象 - 表")
    referred_column: str = Field(description="引用对象 - 列")
    referred_index: str = Field(description="引用对象 - 索引")
    referred_field: str = Field(description="引用对象 - 字段")
    referred_class: str = Field(description="引用对象 - 类")
    options: Optional[str] = Field(description="行为选项", default=None)
    sort_order: int = Field(description="排序权重")
    is_active: bool = Field(description="启用状态")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
