from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_share_file import OutputShareFile


T = TypeVar("T", bound="OutputShareFiles")


@_attrs_define
class OutputShareFiles:
    """
    Attributes:
        share_id (str):
        share_open (bool):
        items (list[OutputShareFile]):
    """

    share_id: str
    share_open: bool
    items: list[OutputShareFile]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_id = self.share_id

        share_open = self.share_open

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "share_id": share_id,
                "share_open": share_open,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_share_file import OutputShareFile

        d = dict(src_dict)
        share_id = d.pop("share_id")

        share_open = d.pop("share_open")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OutputShareFile.from_dict(items_item_data)

            items.append(items_item)

        output_share_files = cls(
            share_id=share_id,
            share_open=share_open,
            items=items,
        )

        output_share_files.additional_properties = d
        return output_share_files

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
