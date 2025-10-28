#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.meta_column

from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .meta_table import MetaTable
    from .meta_view import MetaView


class MetaColumn(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "meta_column"
    __table_args__ = {"schema": get_table_schema(), "comment": "字段元数据"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    meta_column_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="字段内码"
    )
    meta_table_id: Optional[int] = Field(
        default=None, nullable=True, sa_type=BigInteger, description="表内码",
        foreign_key=f"{get_foreign_schema()}meta_table.meta_table_id"
    )
    meta_view_id: Optional[int] = Field(
        default=None, nullable=True, sa_type=BigInteger, description="视图内码",
        foreign_key=f"{get_foreign_schema()}meta_view.meta_view_id"
    )
    name: str = Field(max_length=255, description="字段名")
    autoincrement: Optional[bool] = Field(default=None, nullable=True, sa_type=Boolean, description="启用自增")
    py_type: str = Field(max_length=30, description="python类型")
    sa_type: str = Field(max_length=30, description="sqlalchemy类型")
    type: str = Field(max_length=20, description="database类型")
    primary_key: bool = Field(sa_type=Boolean, description="是否主键")
    nullable: bool = Field(sa_type=Boolean, description="是否可空")
    default: Optional[str] = Field(default=None, max_length=50, nullable=True, description="默认值(一般不用)")
    comment: Optional[str] = Field(default=None, max_length=255, nullable=True, description="字段说明")
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
    MetaTable: "MetaTable" = Relationship(back_populates="MetaColumns")
    MetaView: "MetaView" = Relationship(back_populates="MetaColumns")


class MetaColumnBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    meta_table_id: Optional[int] = Field(default=None, sa_type=BigInteger, description="表内码")
    meta_view_id: Optional[int] = Field(default=None, sa_type=BigInteger, description="视图内码")
    name: str = Field(max_length=255, description="字段名")
    autoincrement: Optional[bool] = Field(default=None, description="启用自增")
    py_type: str = Field(max_length=30, description="python类型")
    sa_type: str = Field(max_length=30, description="sqlalchemy类型")
    type: str = Field(max_length=20, description="database类型")
    primary_key: bool = Field(description="是否主键")
    nullable: bool = Field(description="是否可空")
    default: Optional[str] = Field(default=None, max_length=50, description="默认值(一般不用)")
    comment: Optional[str] = Field(default=None, max_length=255, description="字段说明")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class MetaColumnCreate(MetaColumnBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class MetaColumnUpdate(MetaColumnBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class MetaColumnResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    meta_column_id: int = Field(description="字段内码", sa_type=BigInteger)
    meta_table_id: Optional[int] = Field(description="表内码", default=None, sa_type=BigInteger)
    meta_view_id: Optional[int] = Field(description="视图内码", default=None, sa_type=BigInteger)
    name: str = Field(description="字段名")
    autoincrement: Optional[bool] = Field(description="启用自增", default=None)
    py_type: str = Field(description="python类型")
    sa_type: str = Field(description="sqlalchemy类型")
    type: str = Field(description="database类型")
    primary_key: bool = Field(description="是否主键")
    nullable: bool = Field(description="是否可空")
    default: Optional[str] = Field(description="默认值(一般不用)", default=None)
    comment: Optional[str] = Field(description="字段说明", default=None)
    sort_order: int = Field(description="排序权重")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
