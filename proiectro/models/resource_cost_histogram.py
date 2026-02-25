from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ResourceCostHistogram")


@_attrs_define
class ResourceCostHistogram:
    """
    Attributes:
        effective_start_datetime (datetime.datetime):
        currency (str):
        value (str):
        name (str):
    """

    effective_start_datetime: datetime.datetime
    currency: str
    value: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_start_datetime = self.effective_start_datetime.isoformat()

        currency = self.currency

        value = self.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effective_start_datetime": effective_start_datetime,
                "currency": currency,
                "value": value,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        effective_start_datetime = isoparse(d.pop("effective_start_datetime"))

        currency = d.pop("currency")

        value = d.pop("value")

        name = d.pop("name")

        resource_cost_histogram = cls(
            effective_start_datetime=effective_start_datetime,
            currency=currency,
            value=value,
            name=name,
        )

        resource_cost_histogram.additional_properties = d
        return resource_cost_histogram

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
