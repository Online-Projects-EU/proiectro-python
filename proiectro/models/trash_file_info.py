from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TrashFileInfo")


@_attrs_define
class TrashFileInfo:
    """Information about a file in trash

    Attributes:
        file_name (str):
        file_path (str):
        file_size (int):
        file_size_formatted (str):
        entity_type (str):
        entity_type_display (str):
        entity_id (str):
        entity_name (str):
        entity_exists (bool):
        moved_to_trash (datetime.datetime):
        time_until_deletion (str):
        deletion_timestamp (datetime.datetime):
    """

    file_name: str
    file_path: str
    file_size: int
    file_size_formatted: str
    entity_type: str
    entity_type_display: str
    entity_id: str
    entity_name: str
    entity_exists: bool
    moved_to_trash: datetime.datetime
    time_until_deletion: str
    deletion_timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        file_path = self.file_path

        file_size = self.file_size

        file_size_formatted = self.file_size_formatted

        entity_type = self.entity_type

        entity_type_display = self.entity_type_display

        entity_id = self.entity_id

        entity_name = self.entity_name

        entity_exists = self.entity_exists

        moved_to_trash = self.moved_to_trash.isoformat()

        time_until_deletion = self.time_until_deletion

        deletion_timestamp = self.deletion_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_name": file_name,
                "file_path": file_path,
                "file_size": file_size,
                "file_size_formatted": file_size_formatted,
                "entity_type": entity_type,
                "entity_type_display": entity_type_display,
                "entity_id": entity_id,
                "entity_name": entity_name,
                "entity_exists": entity_exists,
                "moved_to_trash": moved_to_trash,
                "time_until_deletion": time_until_deletion,
                "deletion_timestamp": deletion_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("file_name")

        file_path = d.pop("file_path")

        file_size = d.pop("file_size")

        file_size_formatted = d.pop("file_size_formatted")

        entity_type = d.pop("entity_type")

        entity_type_display = d.pop("entity_type_display")

        entity_id = d.pop("entity_id")

        entity_name = d.pop("entity_name")

        entity_exists = d.pop("entity_exists")

        moved_to_trash = isoparse(d.pop("moved_to_trash"))

        time_until_deletion = d.pop("time_until_deletion")

        deletion_timestamp = isoparse(d.pop("deletion_timestamp"))

        trash_file_info = cls(
            file_name=file_name,
            file_path=file_path,
            file_size=file_size,
            file_size_formatted=file_size_formatted,
            entity_type=entity_type,
            entity_type_display=entity_type_display,
            entity_id=entity_id,
            entity_name=entity_name,
            entity_exists=entity_exists,
            moved_to_trash=moved_to_trash,
            time_until_deletion=time_until_deletion,
            deletion_timestamp=deletion_timestamp,
        )

        trash_file_info.additional_properties = d
        return trash_file_info

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
