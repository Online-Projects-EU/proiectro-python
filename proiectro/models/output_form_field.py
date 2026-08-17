from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.output_form_field_options_type_0 import OutputFormFieldOptionsType0





T = TypeVar("T", bound="OutputFormField")



@_attrs_define
class OutputFormField:
    """ 
        Attributes:
            id (str):
            step_id (str):
            form_version_id (str):
            name (str):
            label (str):
            field_type (str):
            sequence (int):
            required (bool):
            is_summary_field (bool):
            is_personal_data (bool):
            placeholder (str | Unset):  Default: ''.
            help_text (str | Unset):  Default: ''.
            options (None | OutputFormFieldOptionsType0 | Unset):
     """

    id: str
    step_id: str
    form_version_id: str
    name: str
    label: str
    field_type: str
    sequence: int
    required: bool
    is_summary_field: bool
    is_personal_data: bool
    placeholder: str | Unset = ''
    help_text: str | Unset = ''
    options: None | OutputFormFieldOptionsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.output_form_field_options_type_0 import OutputFormFieldOptionsType0
        id = self.id

        step_id = self.step_id

        form_version_id = self.form_version_id

        name = self.name

        label = self.label

        field_type = self.field_type

        sequence = self.sequence

        required = self.required

        is_summary_field = self.is_summary_field

        is_personal_data = self.is_personal_data

        placeholder = self.placeholder

        help_text = self.help_text

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, OutputFormFieldOptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "step_id": step_id,
            "form_version_id": form_version_id,
            "name": name,
            "label": label,
            "field_type": field_type,
            "sequence": sequence,
            "required": required,
            "is_summary_field": is_summary_field,
            "is_personal_data": is_personal_data,
        })
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if help_text is not UNSET:
            field_dict["help_text"] = help_text
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_form_field_options_type_0 import OutputFormFieldOptionsType0
        d = dict(src_dict)
        id = d.pop("id")

        step_id = d.pop("step_id")

        form_version_id = d.pop("form_version_id")

        name = d.pop("name")

        label = d.pop("label")

        field_type = d.pop("field_type")

        sequence = d.pop("sequence")

        required = d.pop("required")

        is_summary_field = d.pop("is_summary_field")

        is_personal_data = d.pop("is_personal_data")

        placeholder = d.pop("placeholder", UNSET)

        help_text = d.pop("help_text", UNSET)

        def _parse_options(data: object) -> None | OutputFormFieldOptionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = OutputFormFieldOptionsType0.from_dict(data)



                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputFormFieldOptionsType0 | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        output_form_field = cls(
            id=id,
            step_id=step_id,
            form_version_id=form_version_id,
            name=name,
            label=label,
            field_type=field_type,
            sequence=sequence,
            required=required,
            is_summary_field=is_summary_field,
            is_personal_data=is_personal_data,
            placeholder=placeholder,
            help_text=help_text,
            options=options,
        )


        output_form_field.additional_properties = d
        return output_form_field

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
