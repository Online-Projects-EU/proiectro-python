from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.my_pending_invitation import MyPendingInvitation
  from ..models.my_tenant_item import MyTenantItem





T = TypeVar("T", bound="OutputMyTenants")



@_attrs_define
class OutputMyTenants:
    """ Cross-tenant list of workspaces the current user belongs to (active memberships only)

        Attributes:
            tenants (list[MyTenantItem]):
            invitations (list[MyPendingInvitation]):
            total_count (int):
     """

    tenants: list[MyTenantItem]
    invitations: list[MyPendingInvitation]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.my_pending_invitation import MyPendingInvitation
        from ..models.my_tenant_item import MyTenantItem
        tenants = []
        for tenants_item_data in self.tenants:
            tenants_item = tenants_item_data.to_dict()
            tenants.append(tenants_item)



        invitations = []
        for invitations_item_data in self.invitations:
            invitations_item = invitations_item_data.to_dict()
            invitations.append(invitations_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tenants": tenants,
            "invitations": invitations,
            "total_count": total_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_pending_invitation import MyPendingInvitation
        from ..models.my_tenant_item import MyTenantItem
        d = dict(src_dict)
        tenants = []
        _tenants = d.pop("tenants")
        for tenants_item_data in (_tenants):
            tenants_item = MyTenantItem.from_dict(tenants_item_data)



            tenants.append(tenants_item)


        invitations = []
        _invitations = d.pop("invitations")
        for invitations_item_data in (_invitations):
            invitations_item = MyPendingInvitation.from_dict(invitations_item_data)



            invitations.append(invitations_item)


        total_count = d.pop("total_count")

        output_my_tenants = cls(
            tenants=tenants,
            invitations=invitations,
            total_count=total_count,
        )


        output_my_tenants.additional_properties = d
        return output_my_tenants

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
