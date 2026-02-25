from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.close_external_support_request_resolution import (
    CloseExternalSupportRequestResolution,
)

T = TypeVar("T", bound="CloseExternalSupportRequest")


@_attrs_define
class CloseExternalSupportRequest:
    """
    Attributes:
        status_id (str):
        resolution (CloseExternalSupportRequestResolution):
        reason (str):
    """

    status_id: str
    resolution: CloseExternalSupportRequestResolution
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_id = self.status_id

        resolution = self.resolution.value

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_id": status_id,
                "resolution": resolution,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_id = d.pop("status_id")

        resolution = CloseExternalSupportRequestResolution(d.pop("resolution"))

        reason = d.pop("reason")

        close_external_support_request = cls(
            status_id=status_id,
            resolution=resolution,
            reason=reason,
        )

        close_external_support_request.additional_properties = d
        return close_external_support_request

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
