from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttachPartnerPortalForm")



@_attrs_define
class AttachPartnerPortalForm:
    """ 
        Attributes:
            custom_form_id (str):
            display_order (int | Unset):  Default: 0.
     """

    custom_form_id: str
    display_order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        custom_form_id = self.custom_form_id

        display_order = self.display_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "custom_form_id": custom_form_id,
        })
        if display_order is not UNSET:
            field_dict["display_order"] = display_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_form_id = d.pop("custom_form_id")

        display_order = d.pop("display_order", UNSET)

        attach_partner_portal_form = cls(
            custom_form_id=custom_form_id,
            display_order=display_order,
        )


        attach_partner_portal_form.additional_properties = d
        return attach_partner_portal_form

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
