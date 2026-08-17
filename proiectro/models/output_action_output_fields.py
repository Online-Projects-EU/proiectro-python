from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.output_action_output_fields_fields import OutputActionOutputFieldsFields





T = TypeVar("T", bound="OutputActionOutputFields")



@_attrs_define
class OutputActionOutputFields:
    """ Output: available output fields for an action type.

        Attributes:
            fields (OutputActionOutputFieldsFields):
     """

    fields: OutputActionOutputFieldsFields
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.output_action_output_fields_fields import OutputActionOutputFieldsFields
        fields = self.fields.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fields": fields,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_action_output_fields_fields import OutputActionOutputFieldsFields
        d = dict(src_dict)
        fields = OutputActionOutputFieldsFields.from_dict(d.pop("fields"))




        output_action_output_fields = cls(
            fields=fields,
        )


        output_action_output_fields.additional_properties = d
        return output_action_output_fields

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
