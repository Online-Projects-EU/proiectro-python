from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_start_preview_entity_data_type_0 import (
        QuickStartPreviewEntityDataType0,
    )


T = TypeVar("T", bound="QuickStartPreviewEntity")


@_attrs_define
class QuickStartPreviewEntity:
    """An entity that will be created by a template.

    Attributes:
        name (str):
        description (str):
        data (None | QuickStartPreviewEntityDataType0 | Unset):
        depth (int | Unset):  Default: 0.
    """

    name: str
    description: str
    data: None | QuickStartPreviewEntityDataType0 | Unset = UNSET
    depth: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_start_preview_entity_data_type_0 import (
            QuickStartPreviewEntityDataType0,
        )

        name = self.name

        description = self.description

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, QuickStartPreviewEntityDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        depth = self.depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if depth is not UNSET:
            field_dict["depth"] = depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_start_preview_entity_data_type_0 import (
            QuickStartPreviewEntityDataType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        def _parse_data(
            data: object,
        ) -> None | QuickStartPreviewEntityDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = QuickStartPreviewEntityDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QuickStartPreviewEntityDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        depth = d.pop("depth", UNSET)

        quick_start_preview_entity = cls(
            name=name,
            description=description,
            data=data,
            depth=depth,
        )

        quick_start_preview_entity.additional_properties = d
        return quick_start_preview_entity

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
