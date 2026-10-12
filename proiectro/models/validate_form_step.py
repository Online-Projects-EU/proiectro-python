from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.validate_form_step_data import ValidateFormStepData


T = TypeVar("T", bound="ValidateFormStep")


@_attrs_define
class ValidateFormStep:
    """
    Attributes:
        step_id (str):
        data (ValidateFormStepData):
    """

    step_id: str
    data: ValidateFormStepData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_id = self.step_id

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step_id": step_id,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_form_step_data import ValidateFormStepData

        d = dict(src_dict)
        step_id = d.pop("step_id")

        data = ValidateFormStepData.from_dict(d.pop("data"))

        validate_form_step = cls(
            step_id=step_id,
            data=data,
        )

        validate_form_step.additional_properties = d
        return validate_form_step

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
