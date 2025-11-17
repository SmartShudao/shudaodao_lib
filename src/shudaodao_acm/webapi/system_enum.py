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
from ..meta_config import MetaConfig

Auth_Controller = AuthAPIRouter(
    prefix=f"/v1/{MetaConfig.RouterPath}",
    tags=[f"{MetaConfig.RouterTags}"],
    db_engine_name=MetaConfig.EngineName,
)


# 受保护的路由
@Auth_Controller.get("/system", summary="获取当前用户的路由")
async def auth_me(
        current_user: AuthUserResponse = Depends(AuthService.get_current_user)
):
    return ResponseUtil.success(
        message="获取用户信息成功",
        data="获取路由"
    )
