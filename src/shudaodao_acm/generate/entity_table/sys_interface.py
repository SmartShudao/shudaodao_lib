#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2026, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_acm.sys_interface

from datetime import datetime
from typing import Optional
from pydantic import ConfigDict

from sqlalchemy import BigInteger, Boolean

from shudaodao_core import SQLModel, BaseResponse, Field, get_primary_id
from ...package_config import PackageConfig


class Interface(PackageConfig.RegistryModel, table=True):
    """数据库对象模型"""

    __tablename__ = "sys_interface"
    __table_args__ = {"schema": PackageConfig.SchemaTable, "comment": "API接口表"}
    # 仅用于内部处理
    __database_schema__ = PackageConfig.SchemaName
    __primary_key__ = ["interface_id"]

    interface_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="接口ID"
    )
    tags: Optional[str] = Field(default=None, nullable=True, max_length=255, description="分组标签")
    summary: Optional[str] = Field(default=None, nullable=True, max_length=255, description="接口信息")
    path: str = Field(max_length=255, description="接口路径")
    method: str = Field(max_length=20, description="请求方法")
    module: Optional[str] = Field(default=None, nullable=True, max_length=255, description="包名")
    endpoint_name: Optional[str] = Field(default=None, nullable=True, max_length=255, description="入口名称")
    name: Optional[str] = Field(default=None, nullable=True, max_length=128, description="接口名称")
    is_active: bool = Field(sa_type=Boolean, description="启用状态")
    api_hash: Optional[str] = Field(default=None, nullable=True, max_length=32, description="hash标识")
    create_by: Optional[str] = Field(default=None, nullable=True, max_length=50, description="创建账户")
    create_at: Optional[datetime] = Field(default=None, nullable=True, description="创建日期")
    update_by: Optional[str] = Field(default=None, nullable=True, max_length=50, description="修改账户")
    update_at: Optional[datetime] = Field(default=None, nullable=True, description="修改日期")
    description: Optional[str] = Field(default=None, nullable=True, max_length=512, description="接口描述")
    tenant_id: Optional[int] = Field(default=None, sa_type=BigInteger, nullable=True, description="租户内码")


class InterfaceCreate(SQLModel):
    """前端创建模型 - 用于接口请求"""

    tags: Optional[str] = Field(default=None, max_length=255, description="分组标签")
    summary: Optional[str] = Field(default=None, max_length=255, description="接口信息")
    path: str = Field(max_length=255, description="接口路径")
    method: str = Field(max_length=20, description="请求方法")
    module: Optional[str] = Field(default=None, max_length=255, description="包名")
    endpoint_name: Optional[str] = Field(default=None, max_length=255, description="入口名称")
    name: Optional[str] = Field(default=None, max_length=128, description="接口名称")
    is_active: bool = Field(description="启用状态")
    api_hash: Optional[str] = Field(default=None, max_length=32, description="hash标识")
    description: Optional[str] = Field(default=None, max_length=512, description="接口描述")

    model_config = ConfigDict(populate_by_name=True)


class InterfaceUpdate(SQLModel):
    """前端更新模型 - 用于接口请求"""

    interface_id: Optional[int] = Field(default=None, sa_type=BigInteger, description="接口ID")
    tags: Optional[str] = Field(default=None, max_length=255, description="分组标签")
    summary: Optional[str] = Field(default=None, max_length=255, description="接口信息")
    path: Optional[str] = Field(default=None, max_length=255, description="接口路径")
    method: Optional[str] = Field(default=None, max_length=20, description="请求方法")
    module: Optional[str] = Field(default=None, max_length=255, description="包名")
    endpoint_name: Optional[str] = Field(default=None, max_length=255, description="入口名称")
    name: Optional[str] = Field(default=None, max_length=128, description="接口名称")
    is_active: Optional[bool] = Field(default=None, description="启用状态")
    api_hash: Optional[str] = Field(default=None, max_length=32, description="hash标识")
    description: Optional[str] = Field(default=None, max_length=512, description="接口描述")

    model_config = ConfigDict(populate_by_name=True)


class InterfaceResponse(BaseResponse):
    """前端响应模型 - 用于接口响应"""

    __database_schema__ = PackageConfig.SchemaName  # 仅用于内部处理
    interface_id: int = Field(description="接口ID", sa_type=BigInteger)
    tags: Optional[str] = Field(description="分组标签", default=None)
    summary: Optional[str] = Field(description="接口信息", default=None)
    path: str = Field(description="接口路径")
    method: str = Field(description="请求方法")
    module: Optional[str] = Field(description="包名", default=None)
    endpoint_name: Optional[str] = Field(description="入口名称", default=None)
    name: Optional[str] = Field(description="接口名称", default=None)
    is_active: bool = Field(description="启用状态")
    api_hash: Optional[str] = Field(description="hash标识", default=None)
    create_by: Optional[str] = Field(description="创建账户", default=None)
    create_at: Optional[datetime] = Field(description="创建日期", default=None)
    update_by: Optional[str] = Field(description="修改账户", default=None)
    update_at: Optional[datetime] = Field(description="修改日期", default=None)
    description: Optional[str] = Field(description="接口描述", default=None)

    model_config = ConfigDict(populate_by_name=True)
