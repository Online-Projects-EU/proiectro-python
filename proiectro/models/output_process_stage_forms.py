from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_process_stage_form import OutputProcessStageForm


T = TypeVar("T", bound="OutputProcessStageForms")


@_attrs_define
class OutputProcessStageForms:
    """
    Attributes:
        stage_id (str):
        forms (list[OutputProcessStageForm]):
    """

    stage_id: str
    forms: list[OutputProcessStageForm]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_id = self.stage_id

        forms = []
        for forms_item_data in self.forms:
            forms_item = forms_item_data.to_dict()
            forms.append(forms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_id": stage_id,
                "forms": forms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_process_stage_form import OutputProcessStageForm

        d = dict(src_dict)
        stage_id = d.pop("stage_id")

        forms = []
        _forms = d.pop("forms")
        for forms_item_data in _forms:
            forms_item = OutputProcessStageForm.from_dict(forms_item_data)

            forms.append(forms_item)

        output_process_stage_forms = cls(
            stage_id=stage_id,
            forms=forms,
        )

        output_process_stage_forms.additional_properties = d
        return output_process_stage_forms

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
