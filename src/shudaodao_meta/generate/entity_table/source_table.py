#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.source_table

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import BigInteger, Text

from shudaodao_core import Field, get_primary_id, Relationship
from shudaodao_core import SQLModel, BaseResponse
from ... import RegistryModel, get_table_schema, get_foreign_schema

if TYPE_CHECKING:
    from .source_schema import SourceSchema
    from .source_column import SourceColumn
    from .source_foreign_key import SourceForeignKey
    from .source_index import SourceIndex
    from .source_primary_key import SourcePrimaryKey
    from .source_referencing_foreign_key import SourceReferencingForeignKey


class SourceTable(RegistryModel, table=True):
    """ 数据库对象模型 """
    __tablename__ = "source_table"
    __table_args__ = {"schema": get_table_schema(), "comment": "表元数据"}
    # 非数据库字段：仅用于内部处理
    __database_schema__ = "shudaodao_meta"
    # 数据库字段
    source_table_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="内码"
    )
    source_schema_id: int = Field(
        sa_type=BigInteger, description="架构内码", foreign_key=f"{get_foreign_schema()}source_schema.source_schema_id"
    )
    table_name: str = Field(max_length=255, description="表名字")
    comment: Optional[str] = Field(default=None, nullable=True, sa_type=Text, description="备注")
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
    SourceSchema: "SourceSchema" = Relationship(back_populates="SourceTables")
    # 正向关系 -> 子对象
    SourceColumns: list["SourceColumn"] = Relationship(
        back_populates="SourceTable", sa_relationship_kwargs={
            "order_by": "SourceColumn.sort_order.asc()"
        }
    )
    SourceForeignKeys: list["SourceForeignKey"] = Relationship(
        back_populates="SourceTable", sa_relationship_kwargs={
            "order_by": "SourceForeignKey.sort_order.asc()"
        }
    )
    SourceIndexes: list["SourceIndex"] = Relationship(
        back_populates="SourceTable", sa_relationship_kwargs={
            "order_by": "SourceIndex.sort_order.asc()"
        }
    )
    SourcePrimaryKey: "SourcePrimaryKey" = Relationship(back_populates="SourceTable")
    SourceReferencingForeignKeys: list["SourceReferencingForeignKey"] = Relationship(
        back_populates="SourceTable", sa_relationship_kwargs={
            "order_by": "SourceReferencingForeignKey.sort_order.asc()"
        }
    )


class SourceTableBase(SQLModel):
    """ 创建、更新模型 共用字段 """
    source_schema_id: int = Field(sa_type=BigInteger, description="架构内码")
    table_name: str = Field(max_length=255, description="表名字")
    comment: Optional[str] = Field(default=None, description="备注")
    sort_order: int = Field(default=10, description="排序权重")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")


class SourceTableCreate(SourceTableBase):
    """ 前端创建模型 - 用于接口请求 """
    ...


class SourceTableUpdate(SourceTableBase):
    """ 前端更新模型 - 用于接口请求 """
    ...


class SourceTableResponse(BaseResponse):
    """ 前端响应模型 - 用于接口响应 """
    __database_schema__ = "shudaodao_meta"  # 仅用于内部处理

    source_table_id: int = Field(description="内码", sa_type=BigInteger)
    source_schema_id: int = Field(description="架构内码", sa_type=BigInteger)
    table_name: str = Field(description="表名字")
    comment: Optional[str] = Field(description="备注", default=None)
    sort_order: int = Field(description="排序权重")
    description: Optional[str] = Field(description="描述", default=None)
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
