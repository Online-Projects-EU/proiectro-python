from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublishRFPToPartners")


@_attrs_define
class PublishRFPToPartners:
    """Input schema for publishing an RFP to selected partners

    Attributes:
        rfp_id (str):
        partners (list[str]):
    """

    rfp_id: str
    partners: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rfp_id = self.rfp_id

        partners = self.partners

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rfp_id": rfp_id,
                "partners": partners,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rfp_id = d.pop("rfp_id")

        partners = cast(list[str], d.pop("partners"))

        publish_rfp_to_partners = cls(
            rfp_id=rfp_id,
            partners=partners,
        )

        publish_rfp_to_partners.additional_properties = d
        return publish_rfp_to_partners

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
