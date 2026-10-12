from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_share_access import OutputShareAccess


T = TypeVar("T", bound="OutputShareAccesses")


@_attrs_define
class OutputShareAccesses:
    """
    Attributes:
        share_id (str):
        next_page (int):
        accesses (list[OutputShareAccess]):
    """

    share_id: str
    next_page: int
    accesses: list[OutputShareAccess]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_id = self.share_id

        next_page = self.next_page

        accesses = []
        for accesses_item_data in self.accesses:
            accesses_item = accesses_item_data.to_dict()
            accesses.append(accesses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "share_id": share_id,
                "next_page": next_page,
                "accesses": accesses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_share_access import OutputShareAccess

        d = dict(src_dict)
        share_id = d.pop("share_id")

        next_page = d.pop("next_page")

        accesses = []
        _accesses = d.pop("accesses")
        for accesses_item_data in _accesses:
            accesses_item = OutputShareAccess.from_dict(accesses_item_data)

            accesses.append(accesses_item)

        output_share_accesses = cls(
            share_id=share_id,
            next_page=next_page,
            accesses=accesses,
        )

        output_share_accesses.additional_properties = d
        return output_share_accesses

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
