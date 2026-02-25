from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkPaymentPaid")


@_attrs_define
class MarkPaymentPaid:
    """
    Attributes:
        paid_date (str):
        payment_integration_id (None | str | Unset):
    """

    paid_date: str
    payment_integration_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paid_date = self.paid_date

        payment_integration_id: None | str | Unset
        if isinstance(self.payment_integration_id, Unset):
            payment_integration_id = UNSET
        else:
            payment_integration_id = self.payment_integration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paid_date": paid_date,
            }
        )
        if payment_integration_id is not UNSET:
            field_dict["payment_integration_id"] = payment_integration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paid_date = d.pop("paid_date")

        def _parse_payment_integration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_integration_id = _parse_payment_integration_id(
            d.pop("payment_integration_id", UNSET)
        )

        mark_payment_paid = cls(
            paid_date=paid_date,
            payment_integration_id=payment_integration_id,
        )

        mark_payment_paid.additional_properties = d
        return mark_payment_paid

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
