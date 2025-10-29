#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：Shudaodao Auto Generator
# @Software ：PyCharm
# @Desc     ：controller classes for shudaodao_meta.source_schema

"""
本模块通过 AuthController 工厂方法，为数据库表 `source_schema` 自动生成一套完整的、带权限控制的
restful CRUD+Q（创建、读取、更新、删除、查询）API 接口。
"""

from shudaodao_core import AuthController
from ..entity_table.source_schema import (
    SourceSchema, SourceSchemaResponse,
    SourceSchemaCreate, SourceSchemaUpdate
)
from ... import get_router_path, get_router_tags, get_engine_name

SourceSchema_Router = AuthController.create(
    # prefix=f"/v1/{get_router_path()}/source_schema",
    tags=get_router_tags(),
    db_config_name=get_engine_name(),  # 配置文件中的数据库连接名称
    router_path=get_router_path(),
    schema_name="shudaodao_meta",
    table_name="source_schema",
    # 模型设置: 数据库模型、创建模型、更新模型、响应模型
    model_class=SourceSchema,
    create_schema=SourceSchemaCreate,
    update_schema=SourceSchemaUpdate,
    response_schema=SourceSchemaResponse,
)
