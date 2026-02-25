from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsSalesConversionStage")


@_attrs_define
class AnalyticsSalesConversionStage:
    """Single conversion stage with transition metrics

    Attributes:
        stage_id (str):
        stage_name (str):
        stage_type (str):
        stage_order (int):
        deals_entered (int):
        deals_advanced (int):
        deals_lost (int):
        deals_stalled (int):
        conversion_rate (float | str):
        avg_days_in_stage (int):
        prev_conversion_rate (float | None | str | Unset):
        conversion_rate_change (float | Literal['new'] | None | str | Unset):
    """

    stage_id: str
    stage_name: str
    stage_type: str
    stage_order: int
    deals_entered: int
    deals_advanced: int
    deals_lost: int
    deals_stalled: int
    conversion_rate: float | str
    avg_days_in_stage: int
    prev_conversion_rate: float | None | str | Unset = UNSET
    conversion_rate_change: float | Literal["new"] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_id = self.stage_id

        stage_name = self.stage_name

        stage_type = self.stage_type

        stage_order = self.stage_order

        deals_entered = self.deals_entered

        deals_advanced = self.deals_advanced

        deals_lost = self.deals_lost

        deals_stalled = self.deals_stalled

        conversion_rate: float | str
        conversion_rate = self.conversion_rate

        avg_days_in_stage = self.avg_days_in_stage

        prev_conversion_rate: float | None | str | Unset
        if isinstance(self.prev_conversion_rate, Unset):
            prev_conversion_rate = UNSET
        else:
            prev_conversion_rate = self.prev_conversion_rate

        conversion_rate_change: float | Literal["new"] | None | str | Unset
        if isinstance(self.conversion_rate_change, Unset):
            conversion_rate_change = UNSET
        else:
            conversion_rate_change = self.conversion_rate_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_id": stage_id,
                "stage_name": stage_name,
                "stage_type": stage_type,
                "stage_order": stage_order,
                "deals_entered": deals_entered,
                "deals_advanced": deals_advanced,
                "deals_lost": deals_lost,
                "deals_stalled": deals_stalled,
                "conversion_rate": conversion_rate,
                "avg_days_in_stage": avg_days_in_stage,
            }
        )
        if prev_conversion_rate is not UNSET:
            field_dict["prev_conversion_rate"] = prev_conversion_rate
        if conversion_rate_change is not UNSET:
            field_dict["conversion_rate_change"] = conversion_rate_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_id = d.pop("stage_id")

        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        stage_order = d.pop("stage_order")

        deals_entered = d.pop("deals_entered")

        deals_advanced = d.pop("deals_advanced")

        deals_lost = d.pop("deals_lost")

        deals_stalled = d.pop("deals_stalled")

        def _parse_conversion_rate(data: object) -> float | str:
            return cast(float | str, data)

        conversion_rate = _parse_conversion_rate(d.pop("conversion_rate"))

        avg_days_in_stage = d.pop("avg_days_in_stage")

        def _parse_prev_conversion_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_conversion_rate = _parse_prev_conversion_rate(
            d.pop("prev_conversion_rate", UNSET)
        )

        def _parse_conversion_rate_change(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            conversion_rate_change_type_2 = cast(Literal["new"], data)
            if conversion_rate_change_type_2 != "new":
                raise ValueError(
                    f"conversion_rate_change_type_2 must match const 'new', got '{conversion_rate_change_type_2}'"
                )
            return conversion_rate_change_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        conversion_rate_change = _parse_conversion_rate_change(
            d.pop("conversion_rate_change", UNSET)
        )

        analytics_sales_conversion_stage = cls(
            stage_id=stage_id,
            stage_name=stage_name,
            stage_type=stage_type,
            stage_order=stage_order,
            deals_entered=deals_entered,
            deals_advanced=deals_advanced,
            deals_lost=deals_lost,
            deals_stalled=deals_stalled,
            conversion_rate=conversion_rate,
            avg_days_in_stage=avg_days_in_stage,
            prev_conversion_rate=prev_conversion_rate,
            conversion_rate_change=conversion_rate_change,
        )

        analytics_sales_conversion_stage.additional_properties = d
        return analytics_sales_conversion_stage

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
