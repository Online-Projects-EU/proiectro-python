from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.files_entity_storage_entity_breakdown import (
        FilesEntityStorageEntityBreakdown,
    )
    from ..models.files_entity_storage_entity_file_counts import (
        FilesEntityStorageEntityFileCounts,
    )


T = TypeVar("T", bound="FilesEntityStorage")


@_attrs_define
class FilesEntityStorage:
    """Storage breakdown by entity type

    Attributes:
        total_size (str):
        entity_breakdown (FilesEntityStorageEntityBreakdown):
        total_files (int):
        entity_file_counts (FilesEntityStorageEntityFileCounts):
    """

    total_size: str
    entity_breakdown: FilesEntityStorageEntityBreakdown
    total_files: int
    entity_file_counts: FilesEntityStorageEntityFileCounts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_size = self.total_size

        entity_breakdown = self.entity_breakdown.to_dict()

        total_files = self.total_files

        entity_file_counts = self.entity_file_counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_size": total_size,
                "entity_breakdown": entity_breakdown,
                "total_files": total_files,
                "entity_file_counts": entity_file_counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.files_entity_storage_entity_breakdown import (
            FilesEntityStorageEntityBreakdown,
        )
        from ..models.files_entity_storage_entity_file_counts import (
            FilesEntityStorageEntityFileCounts,
        )

        d = dict(src_dict)
        total_size = d.pop("total_size")

        entity_breakdown = FilesEntityStorageEntityBreakdown.from_dict(
            d.pop("entity_breakdown")
        )

        total_files = d.pop("total_files")

        entity_file_counts = FilesEntityStorageEntityFileCounts.from_dict(
            d.pop("entity_file_counts")
        )

        files_entity_storage = cls(
            total_size=total_size,
            entity_breakdown=entity_breakdown,
            total_files=total_files,
            entity_file_counts=entity_file_counts,
        )

        files_entity_storage.additional_properties = d
        return files_entity_storage

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
