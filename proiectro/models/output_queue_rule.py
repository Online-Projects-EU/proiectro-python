from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputQueueRule")


@_attrs_define
class OutputQueueRule:
    """Output schema for a single queue rule

    Attributes:
        id (str):
        name (str):
        description (str):
        priority (int):
        active (bool):
        internal (bool):
        target_queue_name (str):
        target_queue_active (bool):
        specificity_score (int):
        target_queue_id (None | str | Unset):
        request_type_id (None | str | Unset):
        request_type_name (None | str | Unset):
        request_severity_id (None | str | Unset):
        request_severity_name (None | str | Unset):
    """

    id: str
    name: str
    description: str
    priority: int
    active: bool
    internal: bool
    target_queue_name: str
    target_queue_active: bool
    specificity_score: int
    target_queue_id: None | str | Unset = UNSET
    request_type_id: None | str | Unset = UNSET
    request_type_name: None | str | Unset = UNSET
    request_severity_id: None | str | Unset = UNSET
    request_severity_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        priority = self.priority

        active = self.active

        internal = self.internal

        target_queue_name = self.target_queue_name

        target_queue_active = self.target_queue_active

        specificity_score = self.specificity_score

        target_queue_id: None | str | Unset
        if isinstance(self.target_queue_id, Unset):
            target_queue_id = UNSET
        else:
            target_queue_id = self.target_queue_id

        request_type_id: None | str | Unset
        if isinstance(self.request_type_id, Unset):
            request_type_id = UNSET
        else:
            request_type_id = self.request_type_id

        request_type_name: None | str | Unset
        if isinstance(self.request_type_name, Unset):
            request_type_name = UNSET
        else:
            request_type_name = self.request_type_name

        request_severity_id: None | str | Unset
        if isinstance(self.request_severity_id, Unset):
            request_severity_id = UNSET
        else:
            request_severity_id = self.request_severity_id

        request_severity_name: None | str | Unset
        if isinstance(self.request_severity_name, Unset):
            request_severity_name = UNSET
        else:
            request_severity_name = self.request_severity_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "priority": priority,
                "active": active,
                "internal": internal,
                "target_queue_name": target_queue_name,
                "target_queue_active": target_queue_active,
                "specificity_score": specificity_score,
            }
        )
        if target_queue_id is not UNSET:
            field_dict["target_queue_id"] = target_queue_id
        if request_type_id is not UNSET:
            field_dict["request_type_id"] = request_type_id
        if request_type_name is not UNSET:
            field_dict["request_type_name"] = request_type_name
        if request_severity_id is not UNSET:
            field_dict["request_severity_id"] = request_severity_id
        if request_severity_name is not UNSET:
            field_dict["request_severity_name"] = request_severity_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        priority = d.pop("priority")

        active = d.pop("active")

        internal = d.pop("internal")

        target_queue_name = d.pop("target_queue_name")

        target_queue_active = d.pop("target_queue_active")

        specificity_score = d.pop("specificity_score")

        def _parse_target_queue_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_queue_id = _parse_target_queue_id(d.pop("target_queue_id", UNSET))

        def _parse_request_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_type_id = _parse_request_type_id(d.pop("request_type_id", UNSET))

        def _parse_request_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_type_name = _parse_request_type_name(d.pop("request_type_name", UNSET))

        def _parse_request_severity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_severity_id = _parse_request_severity_id(
            d.pop("request_severity_id", UNSET)
        )

        def _parse_request_severity_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_severity_name = _parse_request_severity_name(
            d.pop("request_severity_name", UNSET)
        )

        output_queue_rule = cls(
            id=id,
            name=name,
            description=description,
            priority=priority,
            active=active,
            internal=internal,
            target_queue_name=target_queue_name,
            target_queue_active=target_queue_active,
            specificity_score=specificity_score,
            target_queue_id=target_queue_id,
            request_type_id=request_type_id,
            request_type_name=request_type_name,
            request_severity_id=request_severity_id,
            request_severity_name=request_severity_name,
        )

        output_queue_rule.additional_properties = d
        return output_queue_rule

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
