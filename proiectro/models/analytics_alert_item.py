from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsAlertItem")


@_attrs_define
class AnalyticsAlertItem:
    """Single alert item

    Attributes:
        id (str):
        severity (str):
        category (str):
        title (str):
        description (str):
        created_at (datetime.datetime):
        action_url (None | str | Unset):
        amount (float | None | str | Unset):
        currency (None | str | Unset):
        days_info (None | str | Unset):
    """

    id: str
    severity: str
    category: str
    title: str
    description: str
    created_at: datetime.datetime
    action_url: None | str | Unset = UNSET
    amount: float | None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    days_info: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        severity = self.severity

        category = self.category

        title = self.title

        description = self.description

        created_at = self.created_at.isoformat()

        action_url: None | str | Unset
        if isinstance(self.action_url, Unset):
            action_url = UNSET
        else:
            action_url = self.action_url

        amount: float | None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        days_info: None | str | Unset
        if isinstance(self.days_info, Unset):
            days_info = UNSET
        else:
            days_info = self.days_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "severity": severity,
                "category": category,
                "title": title,
                "description": description,
                "created_at": created_at,
            }
        )
        if action_url is not UNSET:
            field_dict["action_url"] = action_url
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if days_info is not UNSET:
            field_dict["days_info"] = days_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        severity = d.pop("severity")

        category = d.pop("category")

        title = d.pop("title")

        description = d.pop("description")

        created_at = isoparse(d.pop("created_at"))

        def _parse_action_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_url = _parse_action_url(d.pop("action_url", UNSET))

        def _parse_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_days_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        days_info = _parse_days_info(d.pop("days_info", UNSET))

        analytics_alert_item = cls(
            id=id,
            severity=severity,
            category=category,
            title=title,
            description=description,
            created_at=created_at,
            action_url=action_url,
            amount=amount,
            currency=currency,
            days_info=days_info,
        )

        analytics_alert_item.additional_properties = d
        return analytics_alert_item

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
