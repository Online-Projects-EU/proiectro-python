from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputEmailTemplateDefault")


@_attrs_define
class OutputEmailTemplateDefault:
    """One kind of email and the template it uses by default, if any.

    Attributes:
        purpose (str):
        name (str):
        group (str | Unset):  Default: ''.
        template_id (None | str | Unset):
        template_name (str | Unset):  Default: ''.
    """

    purpose: str
    name: str
    group: str | Unset = ""
    template_id: None | str | Unset = UNSET
    template_name: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purpose = self.purpose

        name = self.name

        group = self.group

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        template_name = self.template_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purpose": purpose,
                "name": name,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if template_name is not UNSET:
            field_dict["template_name"] = template_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        purpose = d.pop("purpose")

        name = d.pop("name")

        group = d.pop("group", UNSET)

        def _parse_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_id = _parse_template_id(d.pop("template_id", UNSET))

        template_name = d.pop("template_name", UNSET)

        output_email_template_default = cls(
            purpose=purpose,
            name=name,
            group=group,
            template_id=template_id,
            template_name=template_name,
        )

        output_email_template_default.additional_properties = d
        return output_email_template_default

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
