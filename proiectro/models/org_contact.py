from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgContact")


@_attrs_define
class OrgContact:
    """
    Attributes:
        id (str):
        first_name (str):
        last_name (str):
        email (str):
        phone (str):
        address (str):
        job_title (str):
        customer_portal_access (bool):
        customer_portal_invitation (None | str | Unset):
    """

    id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    job_title: str
    customer_portal_access: bool
    customer_portal_invitation: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone = self.phone

        address = self.address

        job_title = self.job_title

        customer_portal_access = self.customer_portal_access

        customer_portal_invitation: None | str | Unset
        if isinstance(self.customer_portal_invitation, Unset):
            customer_portal_invitation = UNSET
        else:
            customer_portal_invitation = self.customer_portal_invitation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone,
                "address": address,
                "job_title": job_title,
                "customer_portal_access": customer_portal_access,
            }
        )
        if customer_portal_invitation is not UNSET:
            field_dict["customer_portal_invitation"] = customer_portal_invitation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        phone = d.pop("phone")

        address = d.pop("address")

        job_title = d.pop("job_title")

        customer_portal_access = d.pop("customer_portal_access")

        def _parse_customer_portal_invitation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_portal_invitation = _parse_customer_portal_invitation(
            d.pop("customer_portal_invitation", UNSET)
        )

        org_contact = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            job_title=job_title,
            customer_portal_access=customer_portal_access,
            customer_portal_invitation=customer_portal_invitation,
        )

        org_contact.additional_properties = d
        return org_contact

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
