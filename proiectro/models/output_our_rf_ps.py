from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_our_rfp_item import OutputOurRFPItem


T = TypeVar("T", bound="OutputOurRFPs")


@_attrs_define
class OutputOurRFPs:
    """All RFPs created by the tenant (all statuses)

    Attributes:
        rfps (list[OutputOurRFPItem]):
    """

    rfps: list[OutputOurRFPItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rfps = []
        for rfps_item_data in self.rfps:
            rfps_item = rfps_item_data.to_dict()
            rfps.append(rfps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rfps": rfps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_our_rfp_item import OutputOurRFPItem

        d = dict(src_dict)
        rfps = []
        _rfps = d.pop("rfps")
        for rfps_item_data in _rfps:
            rfps_item = OutputOurRFPItem.from_dict(rfps_item_data)

            rfps.append(rfps_item)

        output_our_rf_ps = cls(
            rfps=rfps,
        )

        output_our_rf_ps.additional_properties = d
        return output_our_rf_ps

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
