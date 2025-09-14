from dataclasses import dataclass

@dataclass
class GeneratorConfig:
    db_url: str
    output_schema_to_entity: bool
    output_db_engine_name: str
    output_router_path: str | None = ...
    output_path: str | None = ...
