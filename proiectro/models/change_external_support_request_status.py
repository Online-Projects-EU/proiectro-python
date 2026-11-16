from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeExternalSupportRequestStatus")


@_attrs_define
class ChangeExternalSupportRequestStatus:
    """
    Attributes:
        status_id (str):
        reason (str):
        send_email (bool | Unset):  Default: False.
    """

    status_id: str
    reason: str
    send_email: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_id = self.status_id

        reason = self.reason

        send_email = self.send_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_id": status_id,
                "reason": reason,
            }
        )
        if send_email is not UNSET:
            field_dict["send_email"] = send_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_id = d.pop("status_id")

        reason = d.pop("reason")

        send_email = d.pop("send_email", UNSET)

        change_external_support_request_status = cls(
            status_id=status_id,
            reason=reason,
            send_email=send_email,
        )

        change_external_support_request_status.additional_properties = d
        return change_external_support_request_status

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
