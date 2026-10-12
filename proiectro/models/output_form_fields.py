from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_form_field import OutputFormField
    from ..models.output_form_fields_steps_item import OutputFormFieldsStepsItem


T = TypeVar("T", bound="OutputFormFields")


@_attrs_define
class OutputFormFields:
    """
    Attributes:
        version_id (str):
        fields (list[OutputFormField]):
        steps (list[OutputFormFieldsStepsItem] | Unset):
        is_locked (bool | Unset):  Default: False.
    """

    version_id: str
    fields: list[OutputFormField]
    steps: list[OutputFormFieldsStepsItem] | Unset = UNSET
    is_locked: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_id = self.version_id

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        is_locked = self.is_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version_id": version_id,
                "fields": fields,
            }
        )
        if steps is not UNSET:
            field_dict["steps"] = steps
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_form_field import OutputFormField
        from ..models.output_form_fields_steps_item import OutputFormFieldsStepsItem

        d = dict(src_dict)
        version_id = d.pop("version_id")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = OutputFormField.from_dict(fields_item_data)

            fields.append(fields_item)

        _steps = d.pop("steps", UNSET)
        steps: list[OutputFormFieldsStepsItem] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = OutputFormFieldsStepsItem.from_dict(steps_item_data)

                steps.append(steps_item)

        is_locked = d.pop("is_locked", UNSET)

        output_form_fields = cls(
            version_id=version_id,
            fields=fields,
            steps=steps,
            is_locked=is_locked,
        )

        output_form_fields.additional_properties = d
        return output_form_fields

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
