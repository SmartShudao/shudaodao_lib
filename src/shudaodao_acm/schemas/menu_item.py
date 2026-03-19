#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/11/18 下午10:02
# @Desc     ：

from typing import List, Optional

from pydantic import BaseModel


class AuthItem(BaseModel):
    """权限项"""

    # 权限名称
    title: str
    # 权限标识
    authMark: str


class Meta(BaseModel):
    """菜单元数据"""

    # 路由标题
    title: str
    # 路由图标
    icon: Optional[str] = None
    # 是否显示徽章
    showBadge: Optional[bool] = None
    # 文本徽章
    showTextBadge: Optional[str] = None
    # 是否在菜单中隐藏
    isHide: Optional[bool] = None
    # 是否在标签页中隐藏
    isHideTab: Optional[bool] = None
    # 外部链接
    link: Optional[str] = None
    # 是否为 iframe
    isIframe: Optional[bool] = None
    # 是否缓存
    keepAlive: Optional[bool] = None
    # 操作权限列表
    authList: Optional[List[AuthItem]] = None
    # 是否为一级菜单（通常由后端自动计算）
    isFirstLevel: Optional[bool] = None
    # 角色权限
    roles: Optional[List[str]] = None
    # 是否固定标签页
    fixedTab: Optional[bool] = None


class MenuItem(BaseModel):
    """菜单项（支持无限嵌套）"""
    # 组件名（路由 name）
    name: str
    # 路由路径
    path: str
    # 组件路径
    component: Optional[str] = None
    # 元信息
    meta: Meta
    # 子菜单（自引用）
    children: Optional[List['MenuItem']] = None

    model_config = {"extra": "ignore"}


MenuItem.model_rebuild()
