from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_payment_schedule_block_payment_type import (
    AddPaymentScheduleBlockPaymentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddPaymentScheduleBlock")


@_attrs_define
class AddPaymentScheduleBlock:
    """
    Attributes:
        name (str):
        description (str):
        payment_type (AddPaymentScheduleBlockPaymentType):
        internal_code (None | str | Unset):
        sequence_no (int | None | Unset):
    """

    name: str
    description: str
    payment_type: AddPaymentScheduleBlockPaymentType
    internal_code: None | str | Unset = UNSET
    sequence_no: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        payment_type = self.payment_type.value

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        sequence_no: int | None | Unset
        if isinstance(self.sequence_no, Unset):
            sequence_no = UNSET
        else:
            sequence_no = self.sequence_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "payment_type": payment_type,
            }
        )
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if sequence_no is not UNSET:
            field_dict["sequence_no"] = sequence_no

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        payment_type = AddPaymentScheduleBlockPaymentType(d.pop("payment_type"))

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_sequence_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence_no = _parse_sequence_no(d.pop("sequence_no", UNSET))

        add_payment_schedule_block = cls(
            name=name,
            description=description,
            payment_type=payment_type,
            internal_code=internal_code,
            sequence_no=sequence_no,
        )

        add_payment_schedule_block.additional_properties = d
        return add_payment_schedule_block

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
