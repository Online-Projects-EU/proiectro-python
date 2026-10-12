from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_custom_form import OutputCustomForm


T = TypeVar("T", bound="OutputCustomForms")


@_attrs_define
class OutputCustomForms:
    """
    Attributes:
        custom_forms (list[OutputCustomForm]):
        total_count (int | Unset):  Default: 0.
    """

    custom_forms: list[OutputCustomForm]
    total_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_forms = []
        for custom_forms_item_data in self.custom_forms:
            custom_forms_item = custom_forms_item_data.to_dict()
            custom_forms.append(custom_forms_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_forms": custom_forms,
            }
        )
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_custom_form import OutputCustomForm

        d = dict(src_dict)
        custom_forms = []
        _custom_forms = d.pop("custom_forms")
        for custom_forms_item_data in _custom_forms:
            custom_forms_item = OutputCustomForm.from_dict(custom_forms_item_data)

            custom_forms.append(custom_forms_item)

        total_count = d.pop("total_count", UNSET)

        output_custom_forms = cls(
            custom_forms=custom_forms,
            total_count=total_count,
        )

        output_custom_forms.additional_properties = d
        return output_custom_forms

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
