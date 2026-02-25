from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TopEntityByStorage")


@_attrs_define
class TopEntityByStorage:
    """Individual entity in top storage list

    Attributes:
        rank (int):
        entity_id (str):
        entity_name (str):
        entity_type (str):
        storage_size (str):
        file_count (int):
    """

    rank: int
    entity_id: str
    entity_name: str
    entity_type: str
    storage_size: str
    file_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        entity_id = self.entity_id

        entity_name = self.entity_name

        entity_type = self.entity_type

        storage_size = self.storage_size

        file_count = self.file_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "entity_id": entity_id,
                "entity_name": entity_name,
                "entity_type": entity_type,
                "storage_size": storage_size,
                "file_count": file_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rank = d.pop("rank")

        entity_id = d.pop("entity_id")

        entity_name = d.pop("entity_name")

        entity_type = d.pop("entity_type")

        storage_size = d.pop("storage_size")

        file_count = d.pop("file_count")

        top_entity_by_storage = cls(
            rank=rank,
            entity_id=entity_id,
            entity_name=entity_name,
            entity_type=entity_type,
            storage_size=storage_size,
            file_count=file_count,
        )

        top_entity_by_storage.additional_properties = d
        return top_entity_by_storage

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
