#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.meta_view

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, Text, Boolean

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .meta_schema import MetaSchema
    from .meta_column import MetaColumn


class MetaView(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "meta_view"
    __table_args__ = {"schema": get_table_schema(), "comment": "视图元数据"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    view_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="主键"
    )
    schema_id: int = Field(
        sa_type=BigInteger, description="主键", foreign_key=f"{get_foreign_schema()}meta_schema.schema_id"
    )
    view_name: str = Field(max_length=255, description="视图名字")
    definition: Optional[str] = Field(default=None, nullable=True, sa_type=Text, description="SQL脚本")
    class_name: Optional[str] = Field(default=None, max_length=50, nullable=True, description="类名")
    file_name: Optional[str] = Field(default=None, max_length=50, nullable=True, description="文件名")
    comment: Optional[str] = Field(default=None, nullable=True, sa_type=Text, description="备注")
    is_active: bool = Field(sa_type=Boolean, description="启用状态")
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
    Schema: "MetaSchema" = Relationship(back_populates="MetaViews")
    # 正向关系 -> 子对象
    MetaColumns: list["MetaColumn"] = Relationship(
        back_populates="View", sa_relationship_kwargs={
            "order_by": "MetaColumn.sort_order.asc()"
        }
    )


class MetaViewBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    schema_id: int = Field(sa_type=BigInteger, description="主键")
    view_name: str = Field(max_length=255, description="视图名字")
    definition: Optional[str] = Field(default=None, description="SQL脚本")
    class_name: Optional[str] = Field(default=None, max_length=50, description="类名")
    file_name: Optional[str] = Field(default=None, max_length=50, description="文件名")
    comment: Optional[str] = Field(default=None, description="备注")
    is_active: bool = Field(description="启用状态")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class MetaViewCreate(MetaViewBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class MetaViewUpdate(MetaViewBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class MetaViewResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    view_id: int = Field(description="主键", sa_type=BigInteger)
    schema_id: int = Field(description="主键", sa_type=BigInteger)
    view_name: str = Field(description="视图名字")
    definition: Optional[str] = Field(description="SQL脚本", default=None)
    class_name: Optional[str] = Field(description="类名", default=None)
    file_name: Optional[str] = Field(description="文件名", default=None)
    comment: Optional[str] = Field(description="备注", default=None)
    is_active: bool = Field(description="启用状态")
    sort_order: int = Field(description="排序权重")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
