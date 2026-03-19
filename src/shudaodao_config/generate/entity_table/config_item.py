#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2026, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：SQLModel classes for shudaodao_config.config_item

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from pydantic import ConfigDict

from sqlalchemy import BigInteger, Text, Boolean, Index

from shudaodao_core import SQLModel, BaseResponse, Field, Relationship, get_primary_id
from ...package_config import PackageConfig

if TYPE_CHECKING:
    from .config_namespace import ConfigNamespace


class ConfigItem(PackageConfig.RegistryModel, table=True):
    """数据库对象模型"""

    __tablename__ = "config_item"
    __table_args__ = (
        Index("uk_ns_key", "namespace_id", "config_key"),
        {"schema": PackageConfig.SchemaTable, "comment": "配置中心-配置项表"},
    )
    # 仅用于内部处理
    __database_schema__ = PackageConfig.SchemaName
    __primary_key__ = ["item_id"]

    item_id: int = Field(default_factory=get_primary_id, primary_key=True, sa_type=BigInteger)
    namespace_id: int = Field(
        foreign_key=f"{PackageConfig.SchemaForeignKey}config_namespace.namespace_id",
        ondelete="CASCADE",
        sa_type=BigInteger,
    )
    config_key: str = Field(max_length=200, description="配置Key")
    config_value: str = Field(sa_type=Text)
    value_type: str = Field(max_length=50, description="string/int/bool/json")
    description: Optional[str] = Field(default=None, sa_type=Text, nullable=True)
    is_active: bool = Field(sa_type=Boolean)
    created_at: datetime = Field()
    updated_at: datetime = Field()
    # 反向关系 - 父对象
    ConfigNamespace: "ConfigNamespace" = Relationship(back_populates="ConfigItems")


class ConfigItemCreate(SQLModel):
    """前端创建模型 - 用于接口请求"""

    namespace_id: int = Field(sa_type=BigInteger)
    config_key: str = Field(max_length=200, description="配置Key")
    config_value: str = Field()
    value_type: str = Field(max_length=50, description="string/int/bool/json")
    description: Optional[str] = Field(default=None)
    is_active: bool = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    model_config = ConfigDict(populate_by_name=True)


class ConfigItemUpdate(SQLModel):
    """前端更新模型 - 用于接口请求"""

    item_id: Optional[int] = Field(default=None, sa_type=BigInteger)
    namespace_id: Optional[int] = Field(default=None, sa_type=BigInteger)
    config_key: Optional[str] = Field(default=None, max_length=200, description="配置Key")
    config_value: Optional[str] = Field(default=None)
    value_type: Optional[str] = Field(default=None, max_length=50, description="string/int/bool/json")
    description: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


class ConfigItemResponse(BaseResponse):
    """前端响应模型 - 用于接口响应"""

    __database_schema__ = PackageConfig.SchemaName  # 仅用于内部处理
    item_id: int = Field(sa_type=BigInteger)
    namespace_id: int = Field(sa_type=BigInteger)
    config_key: str = Field(description="配置Key")
    config_value: str = Field()
    value_type: str = Field(description="string/int/bool/json")
    description: Optional[str] = Field(default=None)
    is_active: bool = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    model_config = ConfigDict(populate_by_name=True)
