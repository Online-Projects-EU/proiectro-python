from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_exchange_rate import OutputExchangeRate


T = TypeVar("T", bound="OutputExchangeRates")


@_attrs_define
class OutputExchangeRates:
    """
    Attributes:
        exchange_rates (list[OutputExchangeRate]):
    """

    exchange_rates: list[OutputExchangeRate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_rates = []
        for exchange_rates_item_data in self.exchange_rates:
            exchange_rates_item = exchange_rates_item_data.to_dict()
            exchange_rates.append(exchange_rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exchange_rates": exchange_rates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_exchange_rate import OutputExchangeRate

        d = dict(src_dict)
        exchange_rates = []
        _exchange_rates = d.pop("exchange_rates")
        for exchange_rates_item_data in _exchange_rates:
            exchange_rates_item = OutputExchangeRate.from_dict(exchange_rates_item_data)

            exchange_rates.append(exchange_rates_item)

        output_exchange_rates = cls(
            exchange_rates=exchange_rates,
        )

        output_exchange_rates.additional_properties = d
        return output_exchange_rates

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
