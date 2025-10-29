#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.meta_constraint

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, Boolean

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .meta_table import MetaTable


class MetaConstraint(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "meta_constraint"
    __table_args__ = {"schema": get_table_schema(), "comment": "表约束元数据"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    constraint_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="主键"
    )
    table_id: int = Field(
        sa_type=BigInteger, description="外键-表", foreign_key=f"{get_foreign_schema()}meta_table.table_id"
    )
    constr_type: str = Field(max_length=255, description="约束类型")
    constr_name: Optional[str] = Field(default=None, max_length=255, nullable=True, description="约束名称")
    constr_unique: Optional[bool] = Field(default=None, nullable=True, sa_type=Boolean, description="是否唯一")
    constr_direction: Optional[str] = Field(default=None, max_length=255, nullable=True,
                                            description="正向关系(子)、反向关系(父)")
    constr_schema: Optional[str] = Field(default=None, max_length=255, nullable=True, description="当前对象 - 模式")
    constr_table: Optional[str] = Field(default=None, max_length=255, nullable=True, description="当前对象 - 表")
    constr_columns: str = Field(max_length=255, description="当前对象 - 列")
    constr_index: Optional[str] = Field(default=None, max_length=255, nullable=True, description="当前对象 - 索引")
    constr_field: Optional[str] = Field(default=None, max_length=255, nullable=True, description="当前对象 - 字段")
    constr_class: Optional[str] = Field(default=None, max_length=255, nullable=True, description="当前对象 - 类")
    relationship_field: Optional[str] = Field(default=None, max_length=255, nullable=True, description="关系字段")
    relationship_orderby: Optional[str] = Field(default=None, max_length=255, nullable=True, description="关系列表的排序字段")
    constr_options: Optional[str] = Field(default=None, max_length=255, nullable=True, description="行为选项")
    referred_schema: Optional[str] = Field(default=None, max_length=255, nullable=True, description="引用对象 - 模式")
    referred_table: Optional[str] = Field(default=None, max_length=255, nullable=True, description="引用对象 - 表")
    referred_columns: Optional[str] = Field(default=None, max_length=255, nullable=True, description="引用对象 - 列")
    referred_index: Optional[str] = Field(default=None, max_length=255, nullable=True, description="引用对象 - 索引")
    is_active: bool = Field(sa_type=Boolean, description="启用状态")
    sort_order: Optional[int] = Field(default=10, nullable=True, description="排序权重")
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
    Table: "MetaTable" = Relationship(back_populates="MetaConstraints")


class MetaConstraintBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    table_id: int = Field(sa_type=BigInteger, description="外键-表")
    constr_type: str = Field(max_length=255, description="约束类型")
    constr_name: Optional[str] = Field(default=None, max_length=255, description="约束名称")
    constr_unique: Optional[bool] = Field(default=None, description="是否唯一")
    constr_direction: Optional[str] = Field(default=None, max_length=255, description="正向关系(子)、反向关系(父)")
    constr_schema: Optional[str] = Field(default=None, max_length=255, description="当前对象 - 模式")
    constr_table: Optional[str] = Field(default=None, max_length=255, description="当前对象 - 表")
    constr_columns: str = Field(max_length=255, description="当前对象 - 列")
    constr_index: Optional[str] = Field(default=None, max_length=255, description="当前对象 - 索引")
    constr_field: Optional[str] = Field(default=None, max_length=255, description="当前对象 - 字段")
    constr_class: Optional[str] = Field(default=None, max_length=255, description="当前对象 - 类")
    relationship_field: Optional[str] = Field(default=None, max_length=255, description="关系字段")
    relationship_orderby: Optional[str] = Field(default=None, max_length=255, description="关系列表的排序字段")
    constr_options: Optional[str] = Field(default=None, max_length=255, description="行为选项")
    referred_schema: Optional[str] = Field(default=None, max_length=255, description="引用对象 - 模式")
    referred_table: Optional[str] = Field(default=None, max_length=255, description="引用对象 - 表")
    referred_columns: Optional[str] = Field(default=None, max_length=255, description="引用对象 - 列")
    referred_index: Optional[str] = Field(default=None, max_length=255, description="引用对象 - 索引")
    is_active: bool = Field(description="启用状态")
    sort_order: Optional[int] = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class MetaConstraintCreate(MetaConstraintBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class MetaConstraintUpdate(MetaConstraintBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class MetaConstraintResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    constraint_id: int = Field(description="主键", sa_type=BigInteger)
    table_id: int = Field(description="外键-表", sa_type=BigInteger)
    constr_type: str = Field(description="约束类型")
    constr_name: Optional[str] = Field(description="约束名称", default=None)
    constr_unique: Optional[bool] = Field(description="是否唯一", default=None)
    constr_direction: Optional[str] = Field(description="正向关系(子)、反向关系(父)", default=None)
    constr_schema: Optional[str] = Field(description="当前对象 - 模式", default=None)
    constr_table: Optional[str] = Field(description="当前对象 - 表", default=None)
    constr_columns: str = Field(description="当前对象 - 列")
    constr_index: Optional[str] = Field(description="当前对象 - 索引", default=None)
    constr_field: Optional[str] = Field(description="当前对象 - 字段", default=None)
    constr_class: Optional[str] = Field(description="当前对象 - 类", default=None)
    relationship_field: Optional[str] = Field(description="关系字段", default=None)
    relationship_orderby: Optional[str] = Field(description="关系列表的排序字段", default=None)
    constr_options: Optional[str] = Field(description="行为选项", default=None)
    referred_schema: Optional[str] = Field(description="引用对象 - 模式", default=None)
    referred_table: Optional[str] = Field(description="引用对象 - 表", default=None)
    referred_columns: Optional[str] = Field(description="引用对象 - 列", default=None)
    referred_index: Optional[str] = Field(description="引用对象 - 索引", default=None)
    is_active: bool = Field(description="启用状态")
    sort_order: Optional[int] = Field(description="排序权重", default=None)
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
