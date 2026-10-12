from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FastProposal")


@_attrs_define
class FastProposal:
    """Turn a claimed lead into a priced proposal in one step.

    The worker's phone call *is* the offer, so there is no draft and no send step: the customer
    organization, the proposal and its single priced line are created together, and the proposal
    lands in a stage from which the deal can go straight to won or lost.

    Currency is deliberately absent. It is not a decision the person filing the call should be
    making, so the workspace default is applied server-side; a client that supplies one is ignored.

        Attributes:
            customer_name (str):
            sales_stage (str):
            product_name (str):
            amount (float | str):
            updated_at (datetime.datetime):
            planned_end (None | str | Unset):
    """

    customer_name: str
    sales_stage: str
    product_name: str
    amount: float | str
    updated_at: datetime.datetime
    planned_end: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_name = self.customer_name

        sales_stage = self.sales_stage

        product_name = self.product_name

        amount: float | str
        amount = self.amount

        updated_at = self.updated_at.isoformat()

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        else:
            planned_end = self.planned_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_name": customer_name,
                "sales_stage": sales_stage,
                "product_name": product_name,
                "amount": amount,
                "updated_at": updated_at,
            }
        )
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_name = d.pop("customer_name")

        sales_stage = d.pop("sales_stage")

        product_name = d.pop("product_name")

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_planned_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        fast_proposal = cls(
            customer_name=customer_name,
            sales_stage=sales_stage,
            product_name=product_name,
            amount=amount,
            updated_at=updated_at,
            planned_end=planned_end,
        )

        fast_proposal.additional_properties = d
        return fast_proposal

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
