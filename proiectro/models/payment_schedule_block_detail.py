from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentScheduleBlockDetail")


@_attrs_define
class PaymentScheduleBlockDetail:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        payment_type (str):
        payment_type_display (str):
        sequence_no (int):
        project_id (str):
        internal_code (None | str | Unset):
    """

    id: str
    name: str
    description: str
    payment_type: str
    payment_type_display: str
    sequence_no: int
    project_id: str
    internal_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        payment_type = self.payment_type

        payment_type_display = self.payment_type_display

        sequence_no = self.sequence_no

        project_id = self.project_id

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "payment_type": payment_type,
                "payment_type_display": payment_type_display,
                "sequence_no": sequence_no,
                "project_id": project_id,
            }
        )
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        payment_type = d.pop("payment_type")

        payment_type_display = d.pop("payment_type_display")

        sequence_no = d.pop("sequence_no")

        project_id = d.pop("project_id")

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        payment_schedule_block_detail = cls(
            id=id,
            name=name,
            description=description,
            payment_type=payment_type,
            payment_type_display=payment_type_display,
            sequence_no=sequence_no,
            project_id=project_id,
            internal_code=internal_code,
        )

        payment_schedule_block_detail.additional_properties = d
        return payment_schedule_block_detail

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
