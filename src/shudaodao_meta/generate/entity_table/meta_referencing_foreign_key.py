#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.meta_referencing_foreign_key

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, Text

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .meta_foreign_key import MetaForeignKey
    from .meta_table import MetaTable


class MetaReferencingForeignKey(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "meta_referencing_foreign_key"
    __table_args__ = {"schema": get_table_schema(), "comment": "引用当前表的外键"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    meta_referencing_foreign_key_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="外键内码"
    )
    meta_foreign_key_id: int = Field(
        sa_type=BigInteger, description="外键内码",
        foreign_key=f"{get_foreign_schema()}meta_foreign_key.meta_foreign_key_id"
    )
    meta_table_id: int = Field(
        sa_type=BigInteger, description="表内码", foreign_key=f"{get_foreign_schema()}meta_table.meta_table_id"
    )
    name: Optional[str] = Field(default=None, max_length=255, nullable=True, description="约束名称")
    constrained_schema: Optional[str] = Field(default=None, max_length=128, nullable=True, description="当前架构")
    constrained_table: Optional[str] = Field(default=None, max_length=255, nullable=True, description="当前表")
    constrained_columns: str = Field(max_length=255, description="当前字段集合")
    referred_schema: Optional[str] = Field(default=None, max_length=128, nullable=True, description="引用架构")
    referred_table: str = Field(max_length=255, description="引用表")
    referred_columns: Optional[str] = Field(default=None, nullable=True, sa_type=Text, description="引用字段集合")
    options: Optional[str] = Field(default=None, max_length=255, nullable=True, description="行为选项")
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
    MetaForeignKey: "MetaForeignKey" = Relationship(back_populates="MetaReferencingForeignKeys")
    MetaTable: "MetaTable" = Relationship(back_populates="MetaReferencingForeignKeys")


class MetaReferencingForeignKeyBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    meta_foreign_key_id: int = Field(sa_type=BigInteger, description="外键内码")
    meta_table_id: int = Field(sa_type=BigInteger, description="表内码")
    name: Optional[str] = Field(default=None, max_length=255, description="约束名称")
    constrained_schema: Optional[str] = Field(default=None, max_length=128, description="当前架构")
    constrained_table: Optional[str] = Field(default=None, max_length=255, description="当前表")
    constrained_columns: str = Field(max_length=255, description="当前字段集合")
    referred_schema: Optional[str] = Field(default=None, max_length=128, description="引用架构")
    referred_table: str = Field(max_length=255, description="引用表")
    referred_columns: Optional[str] = Field(default=None, description="引用字段集合")
    options: Optional[str] = Field(default=None, max_length=255, description="行为选项")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class MetaReferencingForeignKeyCreate(MetaReferencingForeignKeyBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class MetaReferencingForeignKeyUpdate(MetaReferencingForeignKeyBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class MetaReferencingForeignKeyResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    meta_referencing_foreign_key_id: int = Field(description="外键内码", sa_type=BigInteger)
    meta_foreign_key_id: int = Field(description="外键内码", sa_type=BigInteger)
    meta_table_id: int = Field(description="表内码", sa_type=BigInteger)
    name: Optional[str] = Field(description="约束名称", default=None)
    constrained_schema: Optional[str] = Field(description="当前架构", default=None)
    constrained_table: Optional[str] = Field(description="当前表", default=None)
    constrained_columns: str = Field(description="当前字段集合")
    referred_schema: Optional[str] = Field(description="引用架构", default=None)
    referred_table: str = Field(description="引用表")
    referred_columns: Optional[str] = Field(description="引用字段集合", default=None)
    options: Optional[str] = Field(description="行为选项", default=None)
    sort_order: int = Field(description="排序权重")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
