from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomationAction")


@_attrs_define
class AutomationAction:
    """An available action as returned by the automation_actions endpoint.

    Attributes:
        action_id (str):
        name (str):
        category (str):
        fields (str | Unset):  Default: '[]'.
        form_url (None | str | Unset):
    """

    action_id: str
    name: str
    category: str
    fields: str | Unset = "[]"
    form_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_id = self.action_id

        name = self.name

        category = self.category

        fields = self.fields

        form_url: None | str | Unset
        if isinstance(self.form_url, Unset):
            form_url = UNSET
        else:
            form_url = self.form_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_id": action_id,
                "name": name,
                "category": category,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if form_url is not UNSET:
            field_dict["form_url"] = form_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_id = d.pop("action_id")

        name = d.pop("name")

        category = d.pop("category")

        fields = d.pop("fields", UNSET)

        def _parse_form_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_url = _parse_form_url(d.pop("form_url", UNSET))

        automation_action = cls(
            action_id=action_id,
            name=name,
            category=category,
            fields=fields,
            form_url=form_url,
        )

        automation_action.additional_properties = d
        return automation_action

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
