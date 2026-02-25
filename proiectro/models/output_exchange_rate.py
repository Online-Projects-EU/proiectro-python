from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputExchangeRate")


@_attrs_define
class OutputExchangeRate:
    """
    Attributes:
        id (str):
        base_currency_code (str):
        base_currency_name (str):
        base_currency_symbol (str):
        target_currency_code (str):
        target_currency_name (str):
        target_currency_symbol (str):
        rate (float | str):
        valid_from (datetime.datetime):
        source (str):
        created_at (datetime.datetime):
        created_by_name (str):
        is_active (bool):
        valid_until (datetime.datetime | None | Unset):
    """

    id: str
    base_currency_code: str
    base_currency_name: str
    base_currency_symbol: str
    target_currency_code: str
    target_currency_name: str
    target_currency_symbol: str
    rate: float | str
    valid_from: datetime.datetime
    source: str
    created_at: datetime.datetime
    created_by_name: str
    is_active: bool
    valid_until: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        base_currency_code = self.base_currency_code

        base_currency_name = self.base_currency_name

        base_currency_symbol = self.base_currency_symbol

        target_currency_code = self.target_currency_code

        target_currency_name = self.target_currency_name

        target_currency_symbol = self.target_currency_symbol

        rate: float | str
        rate = self.rate

        valid_from = self.valid_from.isoformat()

        source = self.source

        created_at = self.created_at.isoformat()

        created_by_name = self.created_by_name

        is_active = self.is_active

        valid_until: None | str | Unset
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        elif isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "base_currency_code": base_currency_code,
                "base_currency_name": base_currency_name,
                "base_currency_symbol": base_currency_symbol,
                "target_currency_code": target_currency_code,
                "target_currency_name": target_currency_name,
                "target_currency_symbol": target_currency_symbol,
                "rate": rate,
                "valid_from": valid_from,
                "source": source,
                "created_at": created_at,
                "created_by_name": created_by_name,
                "is_active": is_active,
            }
        )
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        base_currency_code = d.pop("base_currency_code")

        base_currency_name = d.pop("base_currency_name")

        base_currency_symbol = d.pop("base_currency_symbol")

        target_currency_code = d.pop("target_currency_code")

        target_currency_name = d.pop("target_currency_name")

        target_currency_symbol = d.pop("target_currency_symbol")

        def _parse_rate(data: object) -> float | str:
            return cast(float | str, data)

        rate = _parse_rate(d.pop("rate"))

        valid_from = isoparse(d.pop("valid_from"))

        source = d.pop("source")

        created_at = isoparse(d.pop("created_at"))

        created_by_name = d.pop("created_by_name")

        is_active = d.pop("is_active")

        def _parse_valid_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = isoparse(data)

                return valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_until = _parse_valid_until(d.pop("valid_until", UNSET))

        output_exchange_rate = cls(
            id=id,
            base_currency_code=base_currency_code,
            base_currency_name=base_currency_name,
            base_currency_symbol=base_currency_symbol,
            target_currency_code=target_currency_code,
            target_currency_name=target_currency_name,
            target_currency_symbol=target_currency_symbol,
            rate=rate,
            valid_from=valid_from,
            source=source,
            created_at=created_at,
            created_by_name=created_by_name,
            is_active=is_active,
            valid_until=valid_until,
        )

        output_exchange_rate.additional_properties = d
        return output_exchange_rate

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
