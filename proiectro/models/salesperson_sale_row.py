from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SalespersonSaleRow")


@_attrs_define
class SalespersonSaleRow:
    """One won deal on the salesperson page.

    Attributes:
        value (float | str):
        currency (str):
        project_id (str):
        project_name (str):
        approved_at (datetime.datetime | None | Unset):
        customer_id (None | str | Unset):
        customer_name (None | str | Unset):
        lead_id (None | str | Unset):
        lead_name (None | str | Unset):
        lead_count (int | Unset):  Default: 0.
    """

    value: float | str
    currency: str
    project_id: str
    project_name: str
    approved_at: datetime.datetime | None | Unset = UNSET
    customer_id: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    lead_id: None | str | Unset = UNSET
    lead_name: None | str | Unset = UNSET
    lead_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: float | str
        value = self.value

        currency = self.currency

        project_id = self.project_id

        project_name = self.project_name

        approved_at: None | str | Unset
        if isinstance(self.approved_at, Unset):
            approved_at = UNSET
        elif isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        lead_id: None | str | Unset
        if isinstance(self.lead_id, Unset):
            lead_id = UNSET
        else:
            lead_id = self.lead_id

        lead_name: None | str | Unset
        if isinstance(self.lead_name, Unset):
            lead_name = UNSET
        else:
            lead_name = self.lead_name

        lead_count = self.lead_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "currency": currency,
                "project_id": project_id,
                "project_name": project_name,
            }
        )
        if approved_at is not UNSET:
            field_dict["approved_at"] = approved_at
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if lead_id is not UNSET:
            field_dict["lead_id"] = lead_id
        if lead_name is not UNSET:
            field_dict["lead_name"] = lead_name
        if lead_count is not UNSET:
            field_dict["lead_count"] = lead_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_value(data: object) -> float | str:
            return cast(float | str, data)

        value = _parse_value(d.pop("value"))

        currency = d.pop("currency")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        def _parse_approved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = isoparse(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approved_at = _parse_approved_at(d.pop("approved_at", UNSET))

        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        def _parse_lead_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_id = _parse_lead_id(d.pop("lead_id", UNSET))

        def _parse_lead_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_name = _parse_lead_name(d.pop("lead_name", UNSET))

        lead_count = d.pop("lead_count", UNSET)

        salesperson_sale_row = cls(
            value=value,
            currency=currency,
            project_id=project_id,
            project_name=project_name,
            approved_at=approved_at,
            customer_id=customer_id,
            customer_name=customer_name,
            lead_id=lead_id,
            lead_name=lead_name,
            lead_count=lead_count,
        )

        salesperson_sale_row.additional_properties = d
        return salesperson_sale_row

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
