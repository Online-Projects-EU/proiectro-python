from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_partner_portal_form_link import OutputPartnerPortalFormLink


T = TypeVar("T", bound="OutputPartnerPortalFormLinks")


@_attrs_define
class OutputPartnerPortalFormLinks:
    """
    Attributes:
        bridge_id (str):
        forms (list[OutputPartnerPortalFormLink]):
    """

    bridge_id: str
    forms: list[OutputPartnerPortalFormLink]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        forms = []
        for forms_item_data in self.forms:
            forms_item = forms_item_data.to_dict()
            forms.append(forms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "forms": forms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_partner_portal_form_link import OutputPartnerPortalFormLink

        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        forms = []
        _forms = d.pop("forms")
        for forms_item_data in _forms:
            forms_item = OutputPartnerPortalFormLink.from_dict(forms_item_data)

            forms.append(forms_item)

        output_partner_portal_form_links = cls(
            bridge_id=bridge_id,
            forms=forms,
        )

        output_partner_portal_form_links.additional_properties = d
        return output_partner_portal_form_links

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
