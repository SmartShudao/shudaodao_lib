#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_meta.kg_graph

from datetime import datetime
from typing import Optional
from pydantic import ConfigDict

from sqlalchemy import BigInteger, Boolean

from shudaodao_core import SQLModel, BaseResponse, Field, get_primary_id
from ...package_config import PackageConfig


class KgGraph(PackageConfig.RegistryModel, table=True):
    """数据库对象模型"""

    __tablename__ = "kg_graph"
    __table_args__ = {"schema": PackageConfig.SchemaTable, "comment": "图谱注册表"}
    # 仅用于内部处理
    __database_schema__ = PackageConfig.SchemaName
    __primary_key__ = ["graph_id"]

    graph_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="主键"
    )
    graph_name: str = Field(max_length=50, description="图谱名称")
    display_name: str = Field(max_length=50, description="图谱展示名称")
    description: Optional[str] = Field(default=None, nullable=True, max_length=500, description="描述")
    is_active: bool = Field(sa_type=Boolean, description="启用状态")
    sort_order: int = Field(description="排序权重")
    create_by: Optional[str] = Field(default=None, nullable=True, max_length=50, description="创建人")
    create_at: Optional[datetime] = Field(default=None, nullable=True, description="创建日期")
    update_by: Optional[str] = Field(default=None, nullable=True, max_length=50, description="修改人")
    update_at: Optional[datetime] = Field(default=None, nullable=True, description="修改日期")
    tenant_id: Optional[int] = Field(default=None, sa_type=BigInteger, nullable=True, description="主键")


class KgGraphCreate(SQLModel):
    """前端创建模型 - 用于接口请求"""

    graph_name: str = Field(max_length=50, description="图谱名称")
    display_name: str = Field(max_length=50, description="图谱展示名称")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")
    is_active: bool = Field(description="启用状态")
    sort_order: int = Field(description="排序权重")

    model_config = ConfigDict(populate_by_name=True)


class KgGraphUpdate(SQLModel):
    """前端更新模型 - 用于接口请求"""

    graph_id: Optional[int] = Field(default=None, sa_type=BigInteger, description="主键")
    graph_name: Optional[str] = Field(default=None, max_length=50, description="图谱名称")
    display_name: Optional[str] = Field(default=None, max_length=50, description="图谱展示名称")
    description: Optional[str] = Field(default=None, max_length=500, description="描述")
    is_active: Optional[bool] = Field(default=None, description="启用状态")
    sort_order: Optional[int] = Field(default=None, description="排序权重")

    model_config = ConfigDict(populate_by_name=True)


class KgGraphResponse(BaseResponse):
    """前端响应模型 - 用于接口响应"""

    __database_schema__ = PackageConfig.SchemaName  # 仅用于内部处理
    graph_id: int = Field(description="主键", sa_type=BigInteger)
    graph_name: str = Field(description="图谱名称")
    display_name: str = Field(description="图谱展示名称")
    description: Optional[str] = Field(description="描述", default=None)
    is_active: bool = Field(description="启用状态")
    sort_order: int = Field(description="排序权重")
    create_by: Optional[str] = Field(description="创建人", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改人", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)

    model_config = ConfigDict(populate_by_name=True)
