from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.support_request_severity_item import SupportRequestSeverityItem
    from ..models.support_request_type_item import SupportRequestTypeItem


T = TypeVar("T", bound="PartnerPortalSupportRequestTypes")


@_attrs_define
class PartnerPortalSupportRequestTypes:
    """Available request types/severities for partner portal

    Attributes:
        bridge_id (str):
        types (list[SupportRequestTypeItem]):
        severities (list[SupportRequestSeverityItem]):
    """

    bridge_id: str
    types: list[SupportRequestTypeItem]
    severities: list[SupportRequestSeverityItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        types = []
        for types_item_data in self.types:
            types_item = types_item_data.to_dict()
            types.append(types_item)

        severities = []
        for severities_item_data in self.severities:
            severities_item = severities_item_data.to_dict()
            severities.append(severities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "types": types,
                "severities": severities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.support_request_severity_item import SupportRequestSeverityItem
        from ..models.support_request_type_item import SupportRequestTypeItem

        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        types = []
        _types = d.pop("types")
        for types_item_data in _types:
            types_item = SupportRequestTypeItem.from_dict(types_item_data)

            types.append(types_item)

        severities = []
        _severities = d.pop("severities")
        for severities_item_data in _severities:
            severities_item = SupportRequestSeverityItem.from_dict(severities_item_data)

            severities.append(severities_item)

        partner_portal_support_request_types = cls(
            bridge_id=bridge_id,
            types=types,
            severities=severities,
        )

        partner_portal_support_request_types.additional_properties = d
        return partner_portal_support_request_types

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
