from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FunnelStageSchema")


@_attrs_define
class FunnelStageSchema:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        is_lead (bool):
        proposal_count (int):
        total_value (float | str):
        average_deal_size (float | str):
        average_days_in_stage (float | str):
        total_value_symbol (str):
        currency_breakdown (None | str | Unset):
    """

    id: str
    name: str
    description: str
    is_lead: bool
    proposal_count: int
    total_value: float | str
    average_deal_size: float | str
    average_days_in_stage: float | str
    total_value_symbol: str
    currency_breakdown: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_lead = self.is_lead

        proposal_count = self.proposal_count

        total_value: float | str
        total_value = self.total_value

        average_deal_size: float | str
        average_deal_size = self.average_deal_size

        average_days_in_stage: float | str
        average_days_in_stage = self.average_days_in_stage

        total_value_symbol = self.total_value_symbol

        currency_breakdown: None | str | Unset
        if isinstance(self.currency_breakdown, Unset):
            currency_breakdown = UNSET
        else:
            currency_breakdown = self.currency_breakdown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "is_lead": is_lead,
                "proposal_count": proposal_count,
                "total_value": total_value,
                "average_deal_size": average_deal_size,
                "average_days_in_stage": average_days_in_stage,
                "total_value_symbol": total_value_symbol,
            }
        )
        if currency_breakdown is not UNSET:
            field_dict["currency_breakdown"] = currency_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_lead = d.pop("is_lead")

        proposal_count = d.pop("proposal_count")

        def _parse_total_value(data: object) -> float | str:
            return cast(float | str, data)

        total_value = _parse_total_value(d.pop("total_value"))

        def _parse_average_deal_size(data: object) -> float | str:
            return cast(float | str, data)

        average_deal_size = _parse_average_deal_size(d.pop("average_deal_size"))

        def _parse_average_days_in_stage(data: object) -> float | str:
            return cast(float | str, data)

        average_days_in_stage = _parse_average_days_in_stage(
            d.pop("average_days_in_stage")
        )

        total_value_symbol = d.pop("total_value_symbol")

        def _parse_currency_breakdown(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_breakdown = _parse_currency_breakdown(
            d.pop("currency_breakdown", UNSET)
        )

        funnel_stage_schema = cls(
            id=id,
            name=name,
            description=description,
            is_lead=is_lead,
            proposal_count=proposal_count,
            total_value=total_value,
            average_deal_size=average_deal_size,
            average_days_in_stage=average_days_in_stage,
            total_value_symbol=total_value_symbol,
            currency_breakdown=currency_breakdown,
        )

        funnel_stage_schema.additional_properties = d
        return funnel_stage_schema

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
