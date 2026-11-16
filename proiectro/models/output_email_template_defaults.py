from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_email_template_default import OutputEmailTemplateDefault


T = TypeVar("T", bound="OutputEmailTemplateDefaults")


@_attrs_define
class OutputEmailTemplateDefaults:
    """
    Attributes:
        purposes (list[OutputEmailTemplateDefault] | Unset):
    """

    purposes: list[OutputEmailTemplateDefault] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purposes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.purposes, Unset):
            purposes = []
            for purposes_item_data in self.purposes:
                purposes_item = purposes_item_data.to_dict()
                purposes.append(purposes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purposes is not UNSET:
            field_dict["purposes"] = purposes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_email_template_default import OutputEmailTemplateDefault

        d = dict(src_dict)
        _purposes = d.pop("purposes", UNSET)
        purposes: list[OutputEmailTemplateDefault] | Unset = UNSET
        if _purposes is not UNSET:
            purposes = []
            for purposes_item_data in _purposes:
                purposes_item = OutputEmailTemplateDefault.from_dict(purposes_item_data)

                purposes.append(purposes_item)

        output_email_template_defaults = cls(
            purposes=purposes,
        )

        output_email_template_defaults.additional_properties = d
        return output_email_template_defaults

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
