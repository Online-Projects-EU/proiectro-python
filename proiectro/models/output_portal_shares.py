from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_portal_share_summary import OutputPortalShareSummary


T = TypeVar("T", bound="OutputPortalShares")


@_attrs_define
class OutputPortalShares:
    """
    Attributes:
        org_id (str):
        shares (list[OutputPortalShareSummary]):
    """

    org_id: str
    shares: list[OutputPortalShareSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        shares = []
        for shares_item_data in self.shares:
            shares_item = shares_item_data.to_dict()
            shares.append(shares_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "shares": shares,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_portal_share_summary import OutputPortalShareSummary

        d = dict(src_dict)
        org_id = d.pop("org_id")

        shares = []
        _shares = d.pop("shares")
        for shares_item_data in _shares:
            shares_item = OutputPortalShareSummary.from_dict(shares_item_data)

            shares.append(shares_item)

        output_portal_shares = cls(
            org_id=org_id,
            shares=shares,
        )

        output_portal_shares.additional_properties = d
        return output_portal_shares

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
