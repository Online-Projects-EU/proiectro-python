from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BridgeAdminContact")


@_attrs_define
class BridgeAdminContact:
    """Contact info for a tenant admin in a bridge

    Attributes:
        name (str):
        email (str):
        work_email (None | str | Unset):
        work_phone (None | str | Unset):
    """

    name: str
    email: str
    work_email: None | str | Unset = UNSET
    work_phone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        work_email: None | str | Unset
        if isinstance(self.work_email, Unset):
            work_email = UNSET
        else:
            work_email = self.work_email

        work_phone: None | str | Unset
        if isinstance(self.work_phone, Unset):
            work_phone = UNSET
        else:
            work_phone = self.work_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
            }
        )
        if work_email is not UNSET:
            field_dict["work_email"] = work_email
        if work_phone is not UNSET:
            field_dict["work_phone"] = work_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        def _parse_work_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_email = _parse_work_email(d.pop("work_email", UNSET))

        def _parse_work_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_phone = _parse_work_phone(d.pop("work_phone", UNSET))

        bridge_admin_contact = cls(
            name=name,
            email=email,
            work_email=work_email,
            work_phone=work_phone,
        )

        bridge_admin_contact.additional_properties = d
        return bridge_admin_contact

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
