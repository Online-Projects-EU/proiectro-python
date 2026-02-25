from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GuideStep")


@_attrs_define
class GuideStep:
    """A single step in a guidance campaign.

    Attributes:
        code (str):
        name (str):
        description (str):
        required (bool):
        status (str):
        action_url (None | str | Unset):
        action_label (None | str | Unset):
    """

    code: str
    name: str
    description: str
    required: bool
    status: str
    action_url: None | str | Unset = UNSET
    action_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        description = self.description

        required = self.required

        status = self.status

        action_url: None | str | Unset
        if isinstance(self.action_url, Unset):
            action_url = UNSET
        else:
            action_url = self.action_url

        action_label: None | str | Unset
        if isinstance(self.action_label, Unset):
            action_label = UNSET
        else:
            action_label = self.action_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "description": description,
                "required": required,
                "status": status,
            }
        )
        if action_url is not UNSET:
            field_dict["action_url"] = action_url
        if action_label is not UNSET:
            field_dict["action_label"] = action_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        description = d.pop("description")

        required = d.pop("required")

        status = d.pop("status")

        def _parse_action_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_url = _parse_action_url(d.pop("action_url", UNSET))

        def _parse_action_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_label = _parse_action_label(d.pop("action_label", UNSET))

        guide_step = cls(
            code=code,
            name=name,
            description=description,
            required=required,
            status=status,
            action_url=action_url,
            action_label=action_label,
        )

        guide_step.additional_properties = d
        return guide_step

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
