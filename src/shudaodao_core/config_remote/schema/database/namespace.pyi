from _typeshed import Incomplete
from datetime import datetime
from sqlmodel import SQLModel

class ConfigNamespace(SQLModel, table=True):
    __tablename__: str
    __table_args__: Incomplete
    namespace_id: int | None
    app_id: int
    namespace_name: str
    environment: str
    description: str | None
    is_active: bool
    created_by: str | None
    created_at: datetime
    updated_by: str | None
    updated_at: datetime
