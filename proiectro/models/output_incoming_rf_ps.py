from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_incoming_rfp_item import OutputIncomingRFPItem


T = TypeVar("T", bound="OutputIncomingRFPs")


@_attrs_define
class OutputIncomingRFPs:
    """RFPs published to this tenant by partners (solicitations)

    Attributes:
        rfps (list[OutputIncomingRFPItem]):
        won_rfps (list[OutputIncomingRFPItem] | Unset):
    """

    rfps: list[OutputIncomingRFPItem]
    won_rfps: list[OutputIncomingRFPItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rfps = []
        for rfps_item_data in self.rfps:
            rfps_item = rfps_item_data.to_dict()
            rfps.append(rfps_item)

        won_rfps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.won_rfps, Unset):
            won_rfps = []
            for won_rfps_item_data in self.won_rfps:
                won_rfps_item = won_rfps_item_data.to_dict()
                won_rfps.append(won_rfps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rfps": rfps,
            }
        )
        if won_rfps is not UNSET:
            field_dict["won_rfps"] = won_rfps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_incoming_rfp_item import OutputIncomingRFPItem

        d = dict(src_dict)
        rfps = []
        _rfps = d.pop("rfps")
        for rfps_item_data in _rfps:
            rfps_item = OutputIncomingRFPItem.from_dict(rfps_item_data)

            rfps.append(rfps_item)

        _won_rfps = d.pop("won_rfps", UNSET)
        won_rfps: list[OutputIncomingRFPItem] | Unset = UNSET
        if _won_rfps is not UNSET:
            won_rfps = []
            for won_rfps_item_data in _won_rfps:
                won_rfps_item = OutputIncomingRFPItem.from_dict(won_rfps_item_data)

                won_rfps.append(won_rfps_item)

        output_incoming_rf_ps = cls(
            rfps=rfps,
            won_rfps=won_rfps,
        )

        output_incoming_rf_ps.additional_properties = d
        return output_incoming_rf_ps

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
