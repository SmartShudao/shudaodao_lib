from ..app.base_context import (
    UserInfo as UserInfo,
    get_current_user_info as get_current_user_info,
    set_current_user_info as set_current_user_info,
)
from ..exception.service_exception import (
    PermError as PermError,
    ValidError as ValidError,
)

class TenantManager:
    @classmethod
    def disable(cls) -> None: ...
    @classmethod
    def set(cls, *, username, tenant_id) -> None: ...
    @classmethod
    def set_from_token(cls, *, username, tenant_id, tenant_enabled=None) -> None: ...
    @classmethod
    def apply_tenant_condition(cls, *, db_model, conditions): ...
    @classmethod
    def get_tenant_condition(cls, *, db_model): ...
    @classmethod
    def set_field_with_user_and_tenant(cls, db_model) -> None: ...
    @classmethod
    def check_permission(cls, db_model) -> None: ...
