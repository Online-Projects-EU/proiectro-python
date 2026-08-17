from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MyPendingInvitation")



@_attrs_define
class MyPendingInvitation:
    """ Individual pending invitation for the current user

        Attributes:
            id (str):
            tenant_name (str):
            invited_by (None | str | Unset):
     """

    id: str
    tenant_name: str
    invited_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_name = self.tenant_name

        invited_by: None | str | Unset
        if isinstance(self.invited_by, Unset):
            invited_by = UNSET
        else:
            invited_by = self.invited_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "tenant_name": tenant_name,
        })
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        tenant_name = d.pop("tenant_name")

        def _parse_invited_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invited_by = _parse_invited_by(d.pop("invited_by", UNSET))


        my_pending_invitation = cls(
            id=id,
            tenant_name=tenant_name,
            invited_by=invited_by,
        )


        my_pending_invitation.additional_properties = d
        return my_pending_invitation

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
