#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2026, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_config.config_app

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from pydantic import ConfigDict

from sqlalchemy import BigInteger, Text, Boolean

from shudaodao_core import SQLModel, BaseResponse, Field, Relationship, get_primary_id
from ...package_config import PackageConfig

if TYPE_CHECKING:
    from .config_namespace import ConfigNamespace


class ConfigApp(PackageConfig.RegistryModel, table=True):
    """数据库对象模型"""

    __tablename__ = "config_app"
    __table_args__ = {"schema": PackageConfig.SchemaTable, "comment": "配置中心-应用表"}
    # 仅用于内部处理
    __database_schema__ = PackageConfig.SchemaName
    __primary_key__ = ["app_id"]

    app_id: int = Field(default_factory=get_primary_id, primary_key=True, sa_type=BigInteger)
    app_code: str = Field(
        max_length=100, unique=True, index=True, description="应用唯一标识，如 order-service"
    )
    app_name: str = Field(max_length=200)
    description: Optional[str] = Field(default=None, sa_type=Text, nullable=True)
    is_active: bool = Field(sa_type=Boolean, description="是否启用")
    created_at: datetime = Field()
    updated_at: datetime = Field()
    # 正向关系 - 子对象
    ConfigNamespaces: list["ConfigNamespace"] = Relationship(back_populates="ConfigApp", cascade_delete=True)


class ConfigAppCreate(SQLModel):
    """前端创建模型 - 用于接口请求"""

    app_code: str = Field(max_length=100, description="应用唯一标识，如 order-service")
    app_name: str = Field(max_length=200)
    description: Optional[str] = Field(default=None)
    is_active: bool = Field(description="是否启用")
    created_at: datetime = Field()
    updated_at: datetime = Field()

    model_config = ConfigDict(populate_by_name=True)


class ConfigAppUpdate(SQLModel):
    """前端更新模型 - 用于接口请求"""

    app_id: Optional[int] = Field(default=None, sa_type=BigInteger)
    app_code: Optional[str] = Field(
        default=None, max_length=100, description="应用唯一标识，如 order-service"
    )
    app_name: Optional[str] = Field(default=None, max_length=200)
    description: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=None, description="是否启用")
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


class ConfigAppResponse(BaseResponse):
    """前端响应模型 - 用于接口响应"""

    __database_schema__ = PackageConfig.SchemaName  # 仅用于内部处理
    app_id: int = Field(sa_type=BigInteger)
    app_code: str = Field(description="应用唯一标识，如 order-service")
    app_name: str = Field()
    description: Optional[str] = Field(default=None)
    is_active: bool = Field(description="是否启用")
    created_at: datetime = Field()
    updated_at: datetime = Field()

    model_config = ConfigDict(populate_by_name=True)
