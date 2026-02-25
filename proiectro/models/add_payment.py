from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddPayment")


@_attrs_define
class AddPayment:
    """
    Attributes:
        payment_schedule_block_id (str):
        name (str):
        due_date (str):
        amount (float | str):
        product_id (None | str | Unset):
        internal_code (None | str | Unset):
        payment_integration_id (None | str | Unset):
    """

    payment_schedule_block_id: str
    name: str
    due_date: str
    amount: float | str
    product_id: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    payment_integration_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_schedule_block_id = self.payment_schedule_block_id

        name = self.name

        due_date = self.due_date

        amount: float | str
        amount = self.amount

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        payment_integration_id: None | str | Unset
        if isinstance(self.payment_integration_id, Unset):
            payment_integration_id = UNSET
        else:
            payment_integration_id = self.payment_integration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payment_schedule_block_id": payment_schedule_block_id,
                "name": name,
                "due_date": due_date,
                "amount": amount,
            }
        )
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if payment_integration_id is not UNSET:
            field_dict["payment_integration_id"] = payment_integration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_schedule_block_id = d.pop("payment_schedule_block_id")

        name = d.pop("name")

        due_date = d.pop("due_date")

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_payment_integration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_integration_id = _parse_payment_integration_id(
            d.pop("payment_integration_id", UNSET)
        )

        add_payment = cls(
            payment_schedule_block_id=payment_schedule_block_id,
            name=name,
            due_date=due_date,
            amount=amount,
            product_id=product_id,
            internal_code=internal_code,
            payment_integration_id=payment_integration_id,
        )

        add_payment.additional_properties = d
        return add_payment

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
