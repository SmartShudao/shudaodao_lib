from _typeshed import Incomplete

class GenConverter:
    case_mapping: Incomplete
    private_mapping: Incomplete
    @staticmethod
    def set_update_property(data_model, meta_model): ...
    @staticmethod
    def get_file_name(table_or_view_name: str) -> str: ...
    @classmethod
    def get_class_name(cls, table_or_view_name: str) -> str:
        """（驼峰命名，去除前缀 t/v/sys）"""
    @staticmethod
    def dump_json(data): ...
    @classmethod
    def is_private(cls, column_name): ...
    @classmethod
    def is_primary(cls, column_name, constrained_columns): ...
    @classmethod
    def is_unique(cls, column_name, meta_indexes): ...
