from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddContactToOrg")


@_attrs_define
class AddContactToOrg:
    """
    Attributes:
        contact_info_first_name (str):
        contact_info_last_name (str):
        contact_info_email (str):
        contact_info_phone (str):
        contact_info_address (str):
        contact_info_job_title (str):
    """

    contact_info_first_name: str
    contact_info_last_name: str
    contact_info_email: str
    contact_info_phone: str
    contact_info_address: str
    contact_info_job_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_info_first_name = self.contact_info_first_name

        contact_info_last_name = self.contact_info_last_name

        contact_info_email = self.contact_info_email

        contact_info_phone = self.contact_info_phone

        contact_info_address = self.contact_info_address

        contact_info_job_title = self.contact_info_job_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact_info_first_name": contact_info_first_name,
                "contact_info_last_name": contact_info_last_name,
                "contact_info_email": contact_info_email,
                "contact_info_phone": contact_info_phone,
                "contact_info_address": contact_info_address,
                "contact_info_job_title": contact_info_job_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_info_first_name = d.pop("contact_info_first_name")

        contact_info_last_name = d.pop("contact_info_last_name")

        contact_info_email = d.pop("contact_info_email")

        contact_info_phone = d.pop("contact_info_phone")

        contact_info_address = d.pop("contact_info_address")

        contact_info_job_title = d.pop("contact_info_job_title")

        add_contact_to_org = cls(
            contact_info_first_name=contact_info_first_name,
            contact_info_last_name=contact_info_last_name,
            contact_info_email=contact_info_email,
            contact_info_phone=contact_info_phone,
            contact_info_address=contact_info_address,
            contact_info_job_title=contact_info_job_title,
        )

        add_contact_to_org.additional_properties = d
        return add_contact_to_org

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
