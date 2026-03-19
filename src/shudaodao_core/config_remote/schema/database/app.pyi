from _typeshed import Incomplete
from datetime import datetime
from sqlmodel import SQLModel

class ConfigApp(SQLModel, table=True):
    __tablename__: str
    __table_args__: Incomplete
    app_id: int | None
    app_code: str
    app_name: str
    description: str | None
    is_active: bool
    created_by: str | None
    created_at: datetime
    updated_by: str | None
    updated_at: datetime
