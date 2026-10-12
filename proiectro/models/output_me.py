from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputMe")


@_attrs_define
class OutputMe:
    """Current authenticated user info (for API key validation / Zapier auth test)

    Attributes:
        id (str):
        email (str):
        name (str):
        tenant_id (str):
        tenant_name (str):
        tenant_path (str):
    """

    id: str
    email: str
    name: str
    tenant_id: str
    tenant_name: str
    tenant_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        tenant_id = self.tenant_id

        tenant_name = self.tenant_name

        tenant_path = self.tenant_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "name": name,
                "tenant_id": tenant_id,
                "tenant_name": tenant_name,
                "tenant_path": tenant_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        tenant_id = d.pop("tenant_id")

        tenant_name = d.pop("tenant_name")

        tenant_path = d.pop("tenant_path")

        output_me = cls(
            id=id,
            email=email,
            name=name,
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            tenant_path=tenant_path,
        )

        output_me.additional_properties = d
        return output_me

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
