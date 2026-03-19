#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/6/29 下午9:08
# @Desc     ：

from typing import Dict, Any, List, Optional

from pydantic import BaseModel, Field

from ...utils.core_utils import CoreUtil


class RedisConfigSetting(BaseModel):
    """redis"""
    name: str = Field("Default", description="唯一标识")
    enabled: bool = Field(True, description="是否启用")
    host: str = Field("localhost", description="主机地址")
    port: int = Field(6379, description="端口")
    db: int = Field(0, description="数据库编号")
    kwargs: Dict[str, Any] = {}


class DiskConfigSetting(BaseModel):
    """文件系统"""
    name: str = Field("Default", description="唯一标识")
    enabled: bool = Field(True, description="是否启用")
    path: str = Field("storage/default", description="目录")


class ObjectConfigSetting(BaseModel):
    name: str = Field(..., description="唯一标识")
    enabled: bool = Field(True, description="是否启用")
    # service_name: str = Field("s3", description="指定服务名称")
    endpoint_url: str = Field(..., description="终端点地址")
    region_name: str = Field("us-east-1", description="服务所在的区域")
    access_key_id: Optional[str] = Field(None, description="访问密钥ID")
    secret_access_key: Optional[str] = Field(None, description="访问密钥Key")
    session_token: Optional[str] = Field(None, description="会话令牌")
    use_ssl: bool = Field(False, description="是否使用SSL")
    verify: bool = Field(False, description="证书验证")


class DataBaseConfigSetting(BaseModel):
    """数据库引擎"""
    # 基础配置
    name: str = Field(..., description="数据库配置名称")
    dialect: str = Field(..., description="数据库类型")
    enabled: bool = Field(True, description="是否启用")
    # 驱动配置
    driver: str = Field(..., description="驱动")
    # 连接串
    url: str = Field(...)
    # 额外参数
    connect_args: Dict[str, Any] = {}
    # echo
    echo: bool = Field(True, description="是否启用日志")

    def get_async_url(self) -> str:
        """生成 连接 URL"""
        base_url = f"{self.dialect}+{self.driver}://" if self.driver else f"{self.dialect}://"
        # 连接串
        if "sqlite" in self.dialect.lower():
            # 生成 sqlite 连接URL
            if ":memory:" in self.url:
                base_url += f"/{self.url}"
            else:
                base_url += f"/{CoreUtil.get_path(self.url)}"
        else:
            # 其他 database 连接URL
            base_url += f"{self.url}"
        return base_url

    def get_url(self) -> str:
        """生成 连接 URL"""
        base_url = f"{self.dialect}://"
        # 连接串
        if "sqlite" in self.dialect.lower():
            # 生成 sqlite 连接URL
            if ":memory:" in self.url:
                base_url += f"/{self.url}"
            else:
                base_url += f"/{CoreUtil.get_path(self.url)}"
        else:
            # 其他 database 连接URL
            base_url += f"{self.url}"
        return base_url


class StorageConfigSetting(BaseModel):
    redis: List[RedisConfigSetting] = Field(None, description="Redis连接")
    database: List[DataBaseConfigSetting] = Field(None, description="数据库连接")
    disk: List[DiskConfigSetting] = Field(None, description="本地文件存储")
    object: List[ObjectConfigSetting] = Field(None, description="分布式文件存储")
