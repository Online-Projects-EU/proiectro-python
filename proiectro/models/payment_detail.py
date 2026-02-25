from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentDetail")


@_attrs_define
class PaymentDetail:
    """
    Attributes:
        id (str):
        name (str):
        due_date (str):
        amount (float | str):
        currency_symbol (str):
        paid (bool):
        block_id (str):
        block_name (str):
        block_type (str):
        project_id (str):
        internal_code (None | str | Unset):
        paid_date (None | str | Unset):
        payment_integration_id (None | str | Unset):
        product_id (None | str | Unset):
        product_name (None | str | Unset):
    """

    id: str
    name: str
    due_date: str
    amount: float | str
    currency_symbol: str
    paid: bool
    block_id: str
    block_name: str
    block_type: str
    project_id: str
    internal_code: None | str | Unset = UNSET
    paid_date: None | str | Unset = UNSET
    payment_integration_id: None | str | Unset = UNSET
    product_id: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        due_date = self.due_date

        amount: float | str
        amount = self.amount

        currency_symbol = self.currency_symbol

        paid = self.paid

        block_id = self.block_id

        block_name = self.block_name

        block_type = self.block_type

        project_id = self.project_id

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        paid_date: None | str | Unset
        if isinstance(self.paid_date, Unset):
            paid_date = UNSET
        else:
            paid_date = self.paid_date

        payment_integration_id: None | str | Unset
        if isinstance(self.payment_integration_id, Unset):
            payment_integration_id = UNSET
        else:
            payment_integration_id = self.payment_integration_id

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "due_date": due_date,
                "amount": amount,
                "currency_symbol": currency_symbol,
                "paid": paid,
                "block_id": block_id,
                "block_name": block_name,
                "block_type": block_type,
                "project_id": project_id,
            }
        )
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if paid_date is not UNSET:
            field_dict["paid_date"] = paid_date
        if payment_integration_id is not UNSET:
            field_dict["payment_integration_id"] = payment_integration_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        due_date = d.pop("due_date")

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        currency_symbol = d.pop("currency_symbol")

        paid = d.pop("paid")

        block_id = d.pop("block_id")

        block_name = d.pop("block_name")

        block_type = d.pop("block_type")

        project_id = d.pop("project_id")

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_paid_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paid_date = _parse_paid_date(d.pop("paid_date", UNSET))

        def _parse_payment_integration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_integration_id = _parse_payment_integration_id(
            d.pop("payment_integration_id", UNSET)
        )

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))

        payment_detail = cls(
            id=id,
            name=name,
            due_date=due_date,
            amount=amount,
            currency_symbol=currency_symbol,
            paid=paid,
            block_id=block_id,
            block_name=block_name,
            block_type=block_type,
            project_id=project_id,
            internal_code=internal_code,
            paid_date=paid_date,
            payment_integration_id=payment_integration_id,
            product_id=product_id,
            product_name=product_name,
        )

        payment_detail.additional_properties = d
        return payment_detail

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
