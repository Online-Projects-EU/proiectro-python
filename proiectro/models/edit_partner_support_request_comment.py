from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EditPartnerSupportRequestComment")


@_attrs_define
class EditPartnerSupportRequestComment:
    """Input schema for partner editing comment (IDs in URL path)

    Attributes:
        bridge_id (str):
        content (str):
    """

    bridge_id: str
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        content = d.pop("content")

        edit_partner_support_request_comment = cls(
            bridge_id=bridge_id,
            content=content,
        )

        edit_partner_support_request_comment.additional_properties = d
        return edit_partner_support_request_comment

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
