#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/11/17 下午2:13
# @Desc     ：

from fastapi import Depends

from shudaodao_auth import AuthAPIRouter, AuthService
from shudaodao_auth.entity_table.t_auth_user import AuthUserResponse
from shudaodao_core import ResponseUtil
from ..package_config import PackageConfig
from ..schemas.menu_item import MenuItem

Acm_Controller = AuthAPIRouter(
    prefix=f"/v1/{PackageConfig.RouterPath}",
    tags=[f"{PackageConfig.RouterTags}"],
    db_engine_name=PackageConfig.EngineName,
)


# 受保护的路由
@Acm_Controller.get(
    "/system/menus", summary="获取当前用户的系统菜单",
    response_model=MenuItem
)
async def system_menus(
        current_user: AuthUserResponse = Depends(AuthService.get_current_user)
):
    menus_data = [
        {
            "path": "shudaodao_acm",
            "name": "22554984923009024",
            "component": "/index/index",
            "meta": {
                "title": "系统设置",
                "icon": "ri:user-3-line"
            },
            "children": [
                {
                    "path": "system",
                    "name": "22554830581010432",
                    "component": "/shudaodao_demo/system",
                    "meta": {
                        "title": "模块(菜单)管理",
                        "icon": "ri:user-line",
                        "keepAlive": True,
                        "roles": [
                            "R_SUPER",
                            "R_ADMIN"
                        ]
                    }
                }
            ]
        },
        {
            "path": "shudaodao_acm1",
            "name": "225549849230090243",
            "component": "/index/index",
            "meta": {
                "title": "系统设置1",
                # "icon": "ri:user-3-line"
            },
            "children": [
                {
                    "path": "sys_department",
                    "name": "22554356268142591",
                    "component": "/shudaodao_acm/generate/table/sys_department",
                    "meta": {
                        "title": "部门(组织)管理",
                        "icon": "ri:user-settings-line",
                        "keepAlive": True,
                        "roles": [
                            "R_SUPER"
                        ]
                    }
                },
                {
                    "path": "table-form-compose",
                    "name": "22554356268142592",
                    "component": "/shudaodao_demo/table-form-compose",
                    "meta": {
                        "title": "TableForm - 组装",
                        "icon": "ri:user-line",
                        "isHide": False,
                        "keepAlive": True,
                        "isHideTab": False
                    }
                },
                {
                    "path": "table-form",
                    "name": "22554356268142593",
                    "component": "/shudaodao_demo/table-form",
                    "meta": {
                        "title": "TableForm - 标准",
                        "icon": "ri:user-line",
                        "isHide": False,
                        "keepAlive": True,
                        "isHideTab": False
                    }
                },
                {
                    "path": "department",
                    "name": "22554356268142594",
                    "component": "/shudaodao_acm/generate/table/sys_department",
                    "meta": {
                        "title": "部门管理",
                        "icon": "ri:user-line",
                        "isHide": False,
                        "keepAlive": True,
                        "isHideTab": False
                    }
                },
                {
                    "path": "menu",
                    "name": "Menus",
                    "component": "/system/menu",
                    "meta": {
                        "title": "menus.system.menu",
                        "icon": "ri:menu-line",
                        "keepAlive": True,
                        "roles": [
                            "R_SUPER"
                        ],
                        "authList": [
                            {
                                "title": "新增",
                                "authMark": "add"
                            },
                            {
                                "title": "编辑",
                                "authMark": "edit"
                            },
                            {
                                "title": "删除",
                                "authMark": "delete"
                            }
                        ]
                    }
                }
            ]
            # },
            # {
            #     "path": "user-center",
            #     "name": "UserCenter",
            #     "component": "/shudaodao_acm/me/index",
            #     "meta": {
            #         "title": "个人中心",
            #         # "icon": "ri:user-3-line",
            #         "keepAlive": True,
            #         "isHide": True,
            #         # "isHideTab": True
            #     }
        }
    ]
    return ResponseUtil.success(
        message="获取当前用户的系统菜单成功",
        data=menus_data
    )
