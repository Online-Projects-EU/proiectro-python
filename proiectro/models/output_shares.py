from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_share import OutputShare


T = TypeVar("T", bound="OutputShares")


@_attrs_define
class OutputShares:
    """
    Attributes:
        org_id (str):
        shares (list[OutputShare]):
        total_count (int | Unset):  Default: 0.
        has_portal_contacts (bool | Unset):  Default: False.
    """

    org_id: str
    shares: list[OutputShare]
    total_count: int | Unset = 0
    has_portal_contacts: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        shares = []
        for shares_item_data in self.shares:
            shares_item = shares_item_data.to_dict()
            shares.append(shares_item)

        total_count = self.total_count

        has_portal_contacts = self.has_portal_contacts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "shares": shares,
            }
        )
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if has_portal_contacts is not UNSET:
            field_dict["has_portal_contacts"] = has_portal_contacts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_share import OutputShare

        d = dict(src_dict)
        org_id = d.pop("org_id")

        shares = []
        _shares = d.pop("shares")
        for shares_item_data in _shares:
            shares_item = OutputShare.from_dict(shares_item_data)

            shares.append(shares_item)

        total_count = d.pop("total_count", UNSET)

        has_portal_contacts = d.pop("has_portal_contacts", UNSET)

        output_shares = cls(
            org_id=org_id,
            shares=shares,
            total_count=total_count,
            has_portal_contacts=has_portal_contacts,
        )

        output_shares.additional_properties = d
        return output_shares

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
