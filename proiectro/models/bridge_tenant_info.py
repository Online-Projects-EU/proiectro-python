from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_admin_contact import BridgeAdminContact


T = TypeVar("T", bound="BridgeTenantInfo")


@_attrs_define
class BridgeTenantInfo:
    """Tenant information in a bridge context

    Attributes:
        id (str):
        name (str):
        admin (BridgeAdminContact | None | Unset):
        manager (BridgeAdminContact | None | Unset):
    """

    id: str
    name: str
    admin: BridgeAdminContact | None | Unset = UNSET
    manager: BridgeAdminContact | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bridge_admin_contact import BridgeAdminContact

        id = self.id

        name = self.name

        admin: dict[str, Any] | None | Unset
        if isinstance(self.admin, Unset):
            admin = UNSET
        elif isinstance(self.admin, BridgeAdminContact):
            admin = self.admin.to_dict()
        else:
            admin = self.admin

        manager: dict[str, Any] | None | Unset
        if isinstance(self.manager, Unset):
            manager = UNSET
        elif isinstance(self.manager, BridgeAdminContact):
            manager = self.manager.to_dict()
        else:
            manager = self.manager

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if admin is not UNSET:
            field_dict["admin"] = admin
        if manager is not UNSET:
            field_dict["manager"] = manager

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bridge_admin_contact import BridgeAdminContact

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_admin(data: object) -> BridgeAdminContact | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                admin_type_0 = BridgeAdminContact.from_dict(data)

                return admin_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BridgeAdminContact | None | Unset, data)

        admin = _parse_admin(d.pop("admin", UNSET))

        def _parse_manager(data: object) -> BridgeAdminContact | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manager_type_0 = BridgeAdminContact.from_dict(data)

                return manager_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BridgeAdminContact | None | Unset, data)

        manager = _parse_manager(d.pop("manager", UNSET))

        bridge_tenant_info = cls(
            id=id,
            name=name,
            admin=admin,
            manager=manager,
        )

        bridge_tenant_info.additional_properties = d
        return bridge_tenant_info

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
