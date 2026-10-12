from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_payment_schedule_block_payment_type_type_0 import (
    EditPaymentScheduleBlockPaymentTypeType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditPaymentScheduleBlock")


@_attrs_define
class EditPaymentScheduleBlock:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        payment_type (EditPaymentScheduleBlockPaymentTypeType0 | None | Unset):
        internal_code (None | str | Unset):
        sequence_no (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    payment_type: EditPaymentScheduleBlockPaymentTypeType0 | None | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    sequence_no: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        payment_type: None | str | Unset
        if isinstance(self.payment_type, Unset):
            payment_type = UNSET
        elif isinstance(self.payment_type, EditPaymentScheduleBlockPaymentTypeType0):
            payment_type = self.payment_type.value
        else:
            payment_type = self.payment_type

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if sequence_no is not UNSET:
            field_dict["sequence_no"] = sequence_no

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_payment_type(
            data: object,
        ) -> EditPaymentScheduleBlockPaymentTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_type_type_0 = EditPaymentScheduleBlockPaymentTypeType0(data)

                return payment_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditPaymentScheduleBlockPaymentTypeType0 | None | Unset, data)

        payment_type = _parse_payment_type(d.pop("payment_type", UNSET))

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

        edit_payment_schedule_block = cls(
            name=name,
            description=description,
            payment_type=payment_type,
            internal_code=internal_code,
            sequence_no=sequence_no,
        )

        edit_payment_schedule_block.additional_properties = d
        return edit_payment_schedule_block

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
