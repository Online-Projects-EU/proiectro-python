from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_work_item_stage_form import OutputWorkItemStageForm


T = TypeVar("T", bound="OutputWorkItemStageForms")


@_attrs_define
class OutputWorkItemStageForms:
    """
    Attributes:
        item_id (str):
        forms (list[OutputWorkItemStageForm]):
        has_blocking (bool | Unset):  Default: False.
        can_fill (bool | Unset):  Default: False.
        fill_locked_reason (str | Unset):  Default: ''.
    """

    item_id: str
    forms: list[OutputWorkItemStageForm]
    has_blocking: bool | Unset = False
    can_fill: bool | Unset = False
    fill_locked_reason: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        forms = []
        for forms_item_data in self.forms:
            forms_item = forms_item_data.to_dict()
            forms.append(forms_item)

        has_blocking = self.has_blocking

        can_fill = self.can_fill

        fill_locked_reason = self.fill_locked_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "forms": forms,
            }
        )
        if has_blocking is not UNSET:
            field_dict["has_blocking"] = has_blocking
        if can_fill is not UNSET:
            field_dict["can_fill"] = can_fill
        if fill_locked_reason is not UNSET:
            field_dict["fill_locked_reason"] = fill_locked_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_work_item_stage_form import OutputWorkItemStageForm

        d = dict(src_dict)
        item_id = d.pop("item_id")

        forms = []
        _forms = d.pop("forms")
        for forms_item_data in _forms:
            forms_item = OutputWorkItemStageForm.from_dict(forms_item_data)

            forms.append(forms_item)

        has_blocking = d.pop("has_blocking", UNSET)

        can_fill = d.pop("can_fill", UNSET)

        fill_locked_reason = d.pop("fill_locked_reason", UNSET)

        output_work_item_stage_forms = cls(
            item_id=item_id,
            forms=forms,
            has_blocking=has_blocking,
            can_fill=can_fill,
            fill_locked_reason=fill_locked_reason,
        )

        output_work_item_stage_forms.additional_properties = d
        return output_work_item_stage_forms

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
