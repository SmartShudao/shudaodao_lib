from _typeshed import Incomplete

class MetaConverter:
    irregular_plurals: Incomplete
    special_endings: Incomplete
    case_mapping: Incomplete
    column_type_mapping: Incomplete
    @staticmethod
    def set_update_property(data_model, meta_model): ...
    @staticmethod
    def get_file_name(table_or_view_name: str) -> str: ...
    @classmethod
    def get_camel_name(cls, table_or_view_name: str) -> str:
        """（驼峰命名，去除前缀 t/v/sys）"""
    @staticmethod
    def dump_json(data): ...
    @classmethod
    def set_column_type(cls, column_name): ...
    @classmethod
    def is_primary(cls, column_name, constrained_columns): ...
    @classmethod
    def is_unique(cls, column_name, meta_indexes): ...
    @classmethod
    def get_plural_name(cls, column_name) -> str:
        """将名称转换为复数形式  注意：这是一个简单的规则实现，可能不适用于所有情况"""
