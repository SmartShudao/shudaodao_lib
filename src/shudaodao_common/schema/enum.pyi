from pydantic import BaseModel

class EnumItemResponse(BaseModel):
    """模块类型定义（包含子节点）"""

    label: str
    value: str
    disabled: bool | None
    children: list["EnumItemResponse"] | None
