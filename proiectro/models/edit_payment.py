from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditPayment")


@_attrs_define
class EditPayment:
    """
    Attributes:
        name (None | str | Unset):
        internal_code (None | str | Unset):
        due_date (None | str | Unset):
        amount (float | None | str | Unset):
        product_id (None | str | Unset):
        payment_integration_id (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    due_date: None | str | Unset = UNSET
    amount: float | None | str | Unset = UNSET
    product_id: None | str | Unset = UNSET
    payment_integration_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        amount: float | None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        payment_integration_id: None | str | Unset
        if isinstance(self.payment_integration_id, Unset):
            payment_integration_id = UNSET
        else:
            payment_integration_id = self.payment_integration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if payment_integration_id is not UNSET:
            field_dict["payment_integration_id"] = payment_integration_id

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

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_payment_integration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_integration_id = _parse_payment_integration_id(
            d.pop("payment_integration_id", UNSET)
        )

        edit_payment = cls(
            name=name,
            internal_code=internal_code,
            due_date=due_date,
            amount=amount,
            product_id=product_id,
            payment_integration_id=payment_integration_id,
        )

        edit_payment.additional_properties = d
        return edit_payment

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
