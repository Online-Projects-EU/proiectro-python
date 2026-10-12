from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tenant_role import TenantRole


T = TypeVar("T", bound="TenantRoles")


@_attrs_define
class TenantRoles:
    """
    Attributes:
        roles (list[TenantRole]):
    """

    roles: list[TenantRole]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_role import TenantRole

        d = dict(src_dict)
        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = TenantRole.from_dict(roles_item_data)

            roles.append(roles_item)

        tenant_roles = cls(
            roles=roles,
        )

        tenant_roles.additional_properties = d
        return tenant_roles

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
