from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trash_file_info import TrashFileInfo


T = TypeVar("T", bound="OutputTenantTrashFiles")


@_attrs_define
class OutputTenantTrashFiles:
    """List of all files in trash for a tenant

    Attributes:
        trash_files (list[TrashFileInfo]):
        total_count (int):
        total_size (str):
    """

    trash_files: list[TrashFileInfo]
    total_count: int
    total_size: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trash_files = []
        for trash_files_item_data in self.trash_files:
            trash_files_item = trash_files_item_data.to_dict()
            trash_files.append(trash_files_item)

        total_count = self.total_count

        total_size = self.total_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trash_files": trash_files,
                "total_count": total_count,
                "total_size": total_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trash_file_info import TrashFileInfo

        d = dict(src_dict)
        trash_files = []
        _trash_files = d.pop("trash_files")
        for trash_files_item_data in _trash_files:
            trash_files_item = TrashFileInfo.from_dict(trash_files_item_data)

            trash_files.append(trash_files_item)

        total_count = d.pop("total_count")

        total_size = d.pop("total_size")

        output_tenant_trash_files = cls(
            trash_files=trash_files,
            total_count=total_count,
            total_size=total_size,
        )

        output_tenant_trash_files.additional_properties = d
        return output_tenant_trash_files

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
