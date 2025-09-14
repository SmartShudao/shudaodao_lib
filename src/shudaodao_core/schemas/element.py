#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/8/28 下午2:02
# @Desc     ：

from pydantic import BaseModel


class PagingElement(BaseModel):
    items: list
    total: int
    page: int
    size: int
    pages: int


class ListElement(BaseModel):
    items: list


class SelectElement(BaseModel):
    items: list
