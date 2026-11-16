from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EditBrandCoverFocus")


@_attrs_define
class EditBrandCoverFocus:
    """Where the cover picture stays centred on a narrower screen, in percent of its width and height.

    Attributes:
        focal_x (int):
        focal_y (int):
    """

    focal_x: int
    focal_y: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        focal_x = self.focal_x

        focal_y = self.focal_y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "focal_x": focal_x,
                "focal_y": focal_y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        focal_x = d.pop("focal_x")

        focal_y = d.pop("focal_y")

        edit_brand_cover_focus = cls(
            focal_x=focal_x,
            focal_y=focal_y,
        )

        edit_brand_cover_focus.additional_properties = d
        return edit_brand_cover_focus

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
