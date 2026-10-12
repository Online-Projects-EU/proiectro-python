from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_billable_source import OutputBillableSource


T = TypeVar("T", bound="OutputBillableSourceList")


@_attrs_define
class OutputBillableSourceList:
    """Payload for the per-source-type picker list endpoints.

    Attributes:
        sources (list[OutputBillableSource]):
        payment_id (str):
        currency_symbol (str):
    """

    sources: list[OutputBillableSource]
    payment_id: str
    currency_symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        payment_id = self.payment_id

        currency_symbol = self.currency_symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sources": sources,
                "payment_id": payment_id,
                "currency_symbol": currency_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_billable_source import OutputBillableSource

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = OutputBillableSource.from_dict(sources_item_data)

            sources.append(sources_item)

        payment_id = d.pop("payment_id")

        currency_symbol = d.pop("currency_symbol")

        output_billable_source_list = cls(
            sources=sources,
            payment_id=payment_id,
            currency_symbol=currency_symbol,
        )

        output_billable_source_list.additional_properties = d
        return output_billable_source_list

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
