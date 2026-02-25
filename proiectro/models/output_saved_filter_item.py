from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputSavedFilterItem")


@_attrs_define
class OutputSavedFilterItem:
    """Individual saved filter item for list display

    Attributes:
        id (str):
        name (str):
        description (str):
        author_name (str):
        is_shared (bool):
        filter_params (str):
        is_own_filter (bool):
    """

    id: str
    name: str
    description: str
    author_name: str
    is_shared: bool
    filter_params: str
    is_own_filter: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        author_name = self.author_name

        is_shared = self.is_shared

        filter_params = self.filter_params

        is_own_filter = self.is_own_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "author_name": author_name,
                "is_shared": is_shared,
                "filter_params": filter_params,
                "is_own_filter": is_own_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        author_name = d.pop("author_name")

        is_shared = d.pop("is_shared")

        filter_params = d.pop("filter_params")

        is_own_filter = d.pop("is_own_filter")

        output_saved_filter_item = cls(
            id=id,
            name=name,
            description=description,
            author_name=author_name,
            is_shared=is_shared,
            filter_params=filter_params,
            is_own_filter=is_own_filter,
        )

        output_saved_filter_item.additional_properties = d
        return output_saved_filter_item

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
