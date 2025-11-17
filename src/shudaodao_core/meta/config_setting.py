#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/11/5 下午2:12
# @Desc     ：

from sqlalchemy.orm import registry
from sqlmodel import SQLModel

from ..engine.database_engine import DatabaseEngine
from ..logger.logging_ import logging


class MetaConfigSetting:

    def __init__(self, *, engine_name, schema_name, router_path, router_tags, auth_role=None):
        # 注册表
        self.Registry = registry()

        class _RegistryModel(SQLModel, registry=self.Registry):
            ...

        # 注册表的基类
        self.RegistryModel = _RegistryModel

        # 数据库引擎连接名
        self.EngineName = engine_name
        # 路由标签
        self.RouterTags = router_tags
        # 路由路径
        self.RouterPath = router_path
        # 数据库 schema_name
        self.SchemaName = schema_name
        # 数据库表 schema_name
        self.SchemaTable = self._get_table_schema()
        # 外键的 schema_name
        self.SchemaForeignKey = self._get_foreign_schema()
        # 路由与表名的对应关系，用于授权验证
        self._router_list = {}

        self.AuthRole = auth_role

    def _get_table_schema(self):
        try:
            if DatabaseEngine().support_schema(name=self.EngineName):
                return self.SchemaName
        except Exception as e:
            logging.warning(f"获取引擎信息失败: {e}")
            return None

    def _get_foreign_schema(self):
        table_schema = self._get_table_schema()
        return table_schema + "." if table_schema else ""

    def add_router_path(self, router_path, table_or_view_name):
        self._router_list[router_path] = table_or_view_name

    def get_router_path(self, router_path):
        if router_path not in self._router_list:
            return None
        return self._router_list[router_path]

    def remove_router_path(self, router_path):
        if router_path in self._router_list:
            del self._router_list[router_path]

    def clear_router_paths(self):
        self._router_list.clear()
