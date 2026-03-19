#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2026, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_config.config_namespace

from datetime import datetime
from typing import Optional, TYPE_CHECKING

from pydantic import ConfigDict
from sqlalchemy import BigInteger, Text, Boolean

from shudaodao_core import SQLModel, BaseResponse, Field, Relationship, get_primary_id
from ...package_config import PackageConfig

if TYPE_CHECKING:
    from .config_app import ConfigApp
    from .config_item import ConfigItem


class ConfigNamespace(PackageConfig.RegistryModel, table=True):
    """数据库对象模型"""

    __tablename__ = "config_namespace"
    __table_args__ = {"schema": PackageConfig.SchemaTable, "comment": "配置中心-命名空间表"}
    # 仅用于内部处理
    __database_schema__ = PackageConfig.SchemaName
    __primary_key__ = ["namespace_id"]

    namespace_id: int = Field(
        default_factory=get_primary_id, primary_key=True, sa_type=BigInteger, description="命名空间ID"
    )
    app_id: int = Field(
        foreign_key=f"{PackageConfig.SchemaForeignKey}config_app.app_id",
        ondelete="CASCADE",
        sa_type=BigInteger,
        description="应用ID",
    )
    environment: str = Field(max_length=50, description="环境：dev/prod")
    namespace_name: str = Field(max_length=100, description="命名空间名称")
    description: Optional[str] = Field(default=None, sa_type=Text, nullable=True)
    is_active: bool = Field(sa_type=Boolean)
    created_at: datetime = Field()
    updated_at: datetime = Field()
    # 反向关系 - 父对象
    ConfigApp: "ConfigApp" = Relationship(back_populates="ConfigNamespaces")
    # 正向关系 - 子对象
    ConfigItems: list["ConfigItem"] = Relationship(back_populates="ConfigNamespace", cascade_delete=True)


class ConfigNamespaceCreate(SQLModel):
    """前端创建模型 - 用于接口请求"""

    app_id: int = Field(sa_type=BigInteger)
    environment: str = Field(max_length=50, description="环境：dev/prod")
    namespace_name: str = Field(max_length=100, description="命名空间名称")
    description: Optional[str] = Field(default=None)
    is_active: bool = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    model_config = ConfigDict(populate_by_name=True)


class ConfigNamespaceUpdate(SQLModel):
    """前端更新模型 - 用于接口请求"""

    namespace_id: Optional[int] = Field(default=None, sa_type=BigInteger)
    app_id: Optional[int] = Field(default=None, sa_type=BigInteger)
    environment: Optional[str] = Field(default=None, max_length=50, description="环境：dev/prod")
    namespace_name: Optional[str] = Field(default=None, max_length=100, description="命名空间名称")
    description: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


class ConfigNamespaceResponse(BaseResponse):
    """前端响应模型 - 用于接口响应"""

    __database_schema__ = PackageConfig.SchemaName  # 仅用于内部处理
    namespace_id: int = Field(sa_type=BigInteger)
    app_id: int = Field(sa_type=BigInteger)
    environment: str = Field(description="环境：dev/prod")
    namespace_name: str = Field(description="命名空间名称")
    description: Optional[str] = Field(default=None)
    is_active: bool = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    model_config = ConfigDict(populate_by_name=True)
