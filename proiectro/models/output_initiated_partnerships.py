from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.initiated_partnership_item import InitiatedPartnershipItem


T = TypeVar("T", bound="OutputInitiatedPartnerships")


@_attrs_define
class OutputInitiatedPartnerships:
    """List of initiated partnerships

    Attributes:
        partnerships (list[InitiatedPartnershipItem]):
        total (int):
    """

    partnerships: list[InitiatedPartnershipItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partnerships = []
        for partnerships_item_data in self.partnerships:
            partnerships_item = partnerships_item_data.to_dict()
            partnerships.append(partnerships_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partnerships": partnerships,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.initiated_partnership_item import InitiatedPartnershipItem

        d = dict(src_dict)
        partnerships = []
        _partnerships = d.pop("partnerships")
        for partnerships_item_data in _partnerships:
            partnerships_item = InitiatedPartnershipItem.from_dict(
                partnerships_item_data
            )

            partnerships.append(partnerships_item)

        total = d.pop("total")

        output_initiated_partnerships = cls(
            partnerships=partnerships,
            total=total,
        )

        output_initiated_partnerships.additional_properties = d
        return output_initiated_partnerships

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
