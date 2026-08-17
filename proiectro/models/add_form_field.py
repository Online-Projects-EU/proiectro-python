from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.add_form_field_field_type import AddFormFieldFieldType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AddFormField")



@_attrs_define
class AddFormField:
    """ 
        Attributes:
            name (str):
            label (str):
            field_type (AddFormFieldFieldType):
            step_id (None | str | Unset):
            sequence (int | Unset):  Default: 0.
            required (bool | Unset):  Default: False.
            is_summary_field (bool | Unset):  Default: False.
            is_personal_data (bool | Unset):  Default: False.
            placeholder (None | str | Unset):  Default: ''.
            help_text (None | str | Unset):  Default: ''.
            choices (list[str] | None | Unset):
            min_length (int | None | Unset):
            max_length (int | None | Unset):
            min_value (float | None | str | Unset):
            max_value (float | None | str | Unset):
            scale_min (int | None | Unset):
            scale_max (int | None | Unset):
     """

    name: str
    label: str
    field_type: AddFormFieldFieldType
    step_id: None | str | Unset = UNSET
    sequence: int | Unset = 0
    required: bool | Unset = False
    is_summary_field: bool | Unset = False
    is_personal_data: bool | Unset = False
    placeholder: None | str | Unset = ''
    help_text: None | str | Unset = ''
    choices: list[str] | None | Unset = UNSET
    min_length: int | None | Unset = UNSET
    max_length: int | None | Unset = UNSET
    min_value: float | None | str | Unset = UNSET
    max_value: float | None | str | Unset = UNSET
    scale_min: int | None | Unset = UNSET
    scale_max: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        field_type = self.field_type.value

        step_id: None | str | Unset
        if isinstance(self.step_id, Unset):
            step_id = UNSET
        else:
            step_id = self.step_id

        sequence = self.sequence

        required = self.required

        is_summary_field = self.is_summary_field

        is_personal_data = self.is_personal_data

        placeholder: None | str | Unset
        if isinstance(self.placeholder, Unset):
            placeholder = UNSET
        else:
            placeholder = self.placeholder

        help_text: None | str | Unset
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

        choices: list[str] | None | Unset
        if isinstance(self.choices, Unset):
            choices = UNSET
        elif isinstance(self.choices, list):
            choices = self.choices


        else:
            choices = self.choices

        min_length: int | None | Unset
        if isinstance(self.min_length, Unset):
            min_length = UNSET
        else:
            min_length = self.min_length

        max_length: int | None | Unset
        if isinstance(self.max_length, Unset):
            max_length = UNSET
        else:
            max_length = self.max_length

        min_value: float | None | str | Unset
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        max_value: float | None | str | Unset
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        scale_min: int | None | Unset
        if isinstance(self.scale_min, Unset):
            scale_min = UNSET
        else:
            scale_min = self.scale_min

        scale_max: int | None | Unset
        if isinstance(self.scale_max, Unset):
            scale_max = UNSET
        else:
            scale_max = self.scale_max


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "label": label,
            "field_type": field_type,
        })
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if required is not UNSET:
            field_dict["required"] = required
        if is_summary_field is not UNSET:
            field_dict["is_summary_field"] = is_summary_field
        if is_personal_data is not UNSET:
            field_dict["is_personal_data"] = is_personal_data
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if help_text is not UNSET:
            field_dict["help_text"] = help_text
        if choices is not UNSET:
            field_dict["choices"] = choices
        if min_length is not UNSET:
            field_dict["min_length"] = min_length
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if scale_min is not UNSET:
            field_dict["scale_min"] = scale_min
        if scale_max is not UNSET:
            field_dict["scale_max"] = scale_max

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        label = d.pop("label")

        field_type = AddFormFieldFieldType(d.pop("field_type"))




        def _parse_step_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_id = _parse_step_id(d.pop("step_id", UNSET))


        sequence = d.pop("sequence", UNSET)

        required = d.pop("required", UNSET)

        is_summary_field = d.pop("is_summary_field", UNSET)

        is_personal_data = d.pop("is_personal_data", UNSET)

        def _parse_placeholder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        placeholder = _parse_placeholder(d.pop("placeholder", UNSET))


        def _parse_help_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        help_text = _parse_help_text(d.pop("help_text", UNSET))


        def _parse_choices(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                choices_type_0 = cast(list[str], data)

                return choices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        choices = _parse_choices(d.pop("choices", UNSET))


        def _parse_min_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_length = _parse_min_length(d.pop("min_length", UNSET))


        def _parse_max_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length = _parse_max_length(d.pop("max_length", UNSET))


        def _parse_min_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))


        def _parse_max_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))


        def _parse_scale_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scale_min = _parse_scale_min(d.pop("scale_min", UNSET))


        def _parse_scale_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scale_max = _parse_scale_max(d.pop("scale_max", UNSET))


        add_form_field = cls(
            name=name,
            label=label,
            field_type=field_type,
            step_id=step_id,
            sequence=sequence,
            required=required,
            is_summary_field=is_summary_field,
            is_personal_data=is_personal_data,
            placeholder=placeholder,
            help_text=help_text,
            choices=choices,
            min_length=min_length,
            max_length=max_length,
            min_value=min_value,
            max_value=max_value,
            scale_min=scale_min,
            scale_max=scale_max,
        )


        add_form_field.additional_properties = d
        return add_form_field

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
