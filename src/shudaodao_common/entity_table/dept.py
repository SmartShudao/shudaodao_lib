#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/8/29 上午2:13
# @Desc     ：

from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

from shudaodao_core import get_primary_id


class DeptBase(SQLModel):
    id: Optional[int] = Field(default_factory=get_primary_id, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = Field(default_factory=datetime.utcnow)


class Dept(DeptBase, table=True):
    __tablename__ = "t_dept"
    __table_args__ = {"schema": "shudao_admin", "comment": "这是表备注"}


class DeptCreate(DeptBase):
    ...


class DeptResponse(DeptBase):
    id: int


class DeptUpdate(DeptBase):
    ...

