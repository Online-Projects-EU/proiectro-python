from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_schedule_block_amount import PaymentScheduleBlockAmount


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
        payment_count (int | Unset):  Default: 0.
        amounts (list[PaymentScheduleBlockAmount] | Unset):
        next_due_date (datetime.date | None | Unset):
    """

    id: str
    name: str
    description: str
    payment_type: str
    payment_type_display: str
    sequence_no: int
    project_id: str
    internal_code: None | str | Unset = UNSET
    payment_count: int | Unset = 0
    amounts: list[PaymentScheduleBlockAmount] | Unset = UNSET
    next_due_date: datetime.date | None | Unset = UNSET
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

        payment_count = self.payment_count

        amounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = []
            for amounts_item_data in self.amounts:
                amounts_item = amounts_item_data.to_dict()
                amounts.append(amounts_item)

        next_due_date: None | str | Unset
        if isinstance(self.next_due_date, Unset):
            next_due_date = UNSET
        elif isinstance(self.next_due_date, datetime.date):
            next_due_date = self.next_due_date.isoformat()
        else:
            next_due_date = self.next_due_date

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
        if payment_count is not UNSET:
            field_dict["payment_count"] = payment_count
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if next_due_date is not UNSET:
            field_dict["next_due_date"] = next_due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_schedule_block_amount import PaymentScheduleBlockAmount

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

        payment_count = d.pop("payment_count", UNSET)

        _amounts = d.pop("amounts", UNSET)
        amounts: list[PaymentScheduleBlockAmount] | Unset = UNSET
        if _amounts is not UNSET:
            amounts = []
            for amounts_item_data in _amounts:
                amounts_item = PaymentScheduleBlockAmount.from_dict(amounts_item_data)

                amounts.append(amounts_item)

        def _parse_next_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_due_date_type_0 = isoparse(data).date()

                return next_due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        next_due_date = _parse_next_due_date(d.pop("next_due_date", UNSET))

        payment_schedule_block_detail = cls(
            id=id,
            name=name,
            description=description,
            payment_type=payment_type,
            payment_type_display=payment_type_display,
            sequence_no=sequence_no,
            project_id=project_id,
            internal_code=internal_code,
            payment_count=payment_count,
            amounts=amounts,
            next_due_date=next_due_date,
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
