from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputApiKeyGrant")


@_attrs_define
class OutputApiKeyGrant:
    """One permission an API key is limited to, and whether the key can use it right now.

    `state` is `usable`, `needs_operation` (the key lacks the operation the permission is for),
    or `not_held` (the key's owner no longer has the permission). `operation` is the permission's
    own operation: create, read, update, delete, or `all` for a whole area or a feature switch.

        Attributes:
            name (str):
            group (str):
            operation (str):
            covers_area (bool):
            state (str):
    """

    name: str
    group: str
    operation: str
    covers_area: bool
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        group = self.group

        operation = self.operation

        covers_area = self.covers_area

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "group": group,
                "operation": operation,
                "covers_area": covers_area,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        group = d.pop("group")

        operation = d.pop("operation")

        covers_area = d.pop("covers_area")

        state = d.pop("state")

        output_api_key_grant = cls(
            name=name,
            group=group,
            operation=operation,
            covers_area=covers_area,
            state=state,
        )

        output_api_key_grant.additional_properties = d
        return output_api_key_grant

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
