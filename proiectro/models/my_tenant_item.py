from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MyTenantItem")



@_attrs_define
class MyTenantItem:
    """ Individual tenant/workspace the current user belongs to

        Attributes:
            id (str):
            name (str):
            path (str):
            logo_url (str):
            is_owner (bool):
            member_id (str):
     """

    id: str
    name: str
    path: str
    logo_url: str
    is_owner: bool
    member_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        path = self.path

        logo_url = self.logo_url

        is_owner = self.is_owner

        member_id = self.member_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "path": path,
            "logo_url": logo_url,
            "is_owner": is_owner,
            "member_id": member_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        path = d.pop("path")

        logo_url = d.pop("logo_url")

        is_owner = d.pop("is_owner")

        member_id = d.pop("member_id")

        my_tenant_item = cls(
            id=id,
            name=name,
            path=path,
            logo_url=logo_url,
            is_owner=is_owner,
            member_id=member_id,
        )


        my_tenant_item.additional_properties = d
        return my_tenant_item

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
