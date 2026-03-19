#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/9/21 下午3:11
# @Desc     ：
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/6/22 下午6:32
# @Desc     ：

from typing import List, Optional

from pydantic import BaseModel, Field


class PackageConfigSetting(BaseModel):
    name: str = Field(..., description="包名")
    enabled: bool = Field(True, description="是否启用")
    check_database: bool = Field(False, description="检查数据库")
    prefix: str = Field("/api", description="url前缀")
    tags: List[str] = Field(None, description="文档分类标签")
    object_storage: Optional[str] = Field(None, description="分布式对象存储配置的name值（RustFS）")
    redis_storage: Optional[str] = Field(None, description="键值型数据库配置的name值（Redis）")
