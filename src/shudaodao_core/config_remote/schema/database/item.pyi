from _typeshed import Incomplete
from datetime import datetime
from sqlmodel import SQLModel

class ConfigItem(SQLModel, table=True):
    __tablename__: str
    __table_args__: Incomplete
    item_id: int | None
    namespace_id: int
    config_key: str
    config_value: str
    value_type: str
    is_encrypted: bool
    is_active: bool
    description: str | None
    created_by: str | None
    created_at: datetime
    updated_by: str | None
    updated_at: datetime
