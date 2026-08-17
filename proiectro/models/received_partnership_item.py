from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ReceivedPartnershipItem")



@_attrs_define
class ReceivedPartnershipItem:
    """ Single received partnership invitation item

        Attributes:
            bridge_id (str):
            inviter_tenant_name (str):
            inviter_admin_name (str):
            inviter_admin_email (str):
            invitation_message (None | str | Unset):
            invited_at (datetime.datetime | None | Unset):
     """

    bridge_id: str
    inviter_tenant_name: str
    inviter_admin_name: str
    inviter_admin_email: str
    invitation_message: None | str | Unset = UNSET
    invited_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        inviter_tenant_name = self.inviter_tenant_name

        inviter_admin_name = self.inviter_admin_name

        inviter_admin_email = self.inviter_admin_email

        invitation_message: None | str | Unset
        if isinstance(self.invitation_message, Unset):
            invitation_message = UNSET
        else:
            invitation_message = self.invitation_message

        invited_at: None | str | Unset
        if isinstance(self.invited_at, Unset):
            invited_at = UNSET
        elif isinstance(self.invited_at, datetime.datetime):
            invited_at = self.invited_at.isoformat()
        else:
            invited_at = self.invited_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "bridge_id": bridge_id,
            "inviter_tenant_name": inviter_tenant_name,
            "inviter_admin_name": inviter_admin_name,
            "inviter_admin_email": inviter_admin_email,
        })
        if invitation_message is not UNSET:
            field_dict["invitation_message"] = invitation_message
        if invited_at is not UNSET:
            field_dict["invited_at"] = invited_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        inviter_tenant_name = d.pop("inviter_tenant_name")

        inviter_admin_name = d.pop("inviter_admin_name")

        inviter_admin_email = d.pop("inviter_admin_email")

        def _parse_invitation_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invitation_message = _parse_invitation_message(d.pop("invitation_message", UNSET))


        def _parse_invited_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invited_at_type_0 = isoparse(data)



                return invited_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        invited_at = _parse_invited_at(d.pop("invited_at", UNSET))


        received_partnership_item = cls(
            bridge_id=bridge_id,
            inviter_tenant_name=inviter_tenant_name,
            inviter_admin_name=inviter_admin_name,
            inviter_admin_email=inviter_admin_email,
            invitation_message=invitation_message,
            invited_at=invited_at,
        )


        received_partnership_item.additional_properties = d
        return received_partnership_item

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
