from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditQueueRule")


@_attrs_define
class EditQueueRule:
    """Input schema for editing a queue routing rule

    Attributes:
        name (str):
        target_queue (str):
        description (None | str | Unset):  Default: ''.
        priority (int | Unset):  Default: 100.
        active (bool | Unset):  Default: True.
        request_type (None | str | Unset):
        request_severity (None | str | Unset):
    """

    name: str
    target_queue: str
    description: None | str | Unset = ""
    priority: int | Unset = 100
    active: bool | Unset = True
    request_type: None | str | Unset = UNSET
    request_severity: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        target_queue = self.target_queue

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority = self.priority

        active = self.active

        request_type: None | str | Unset
        if isinstance(self.request_type, Unset):
            request_type = UNSET
        else:
            request_type = self.request_type

        request_severity: None | str | Unset
        if isinstance(self.request_severity, Unset):
            request_severity = UNSET
        else:
            request_severity = self.request_severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "target_queue": target_queue,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if active is not UNSET:
            field_dict["active"] = active
        if request_type is not UNSET:
            field_dict["request_type"] = request_type
        if request_severity is not UNSET:
            field_dict["request_severity"] = request_severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        target_queue = d.pop("target_queue")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        priority = d.pop("priority", UNSET)

        active = d.pop("active", UNSET)

        def _parse_request_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_type = _parse_request_type(d.pop("request_type", UNSET))

        def _parse_request_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_severity = _parse_request_severity(d.pop("request_severity", UNSET))

        edit_queue_rule = cls(
            name=name,
            target_queue=target_queue,
            description=description,
            priority=priority,
            active=active,
            request_type=request_type,
            request_severity=request_severity,
        )

        edit_queue_rule.additional_properties = d
        return edit_queue_rule

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
