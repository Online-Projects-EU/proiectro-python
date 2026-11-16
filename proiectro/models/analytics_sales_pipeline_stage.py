from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsSalesPipelineStage")


@_attrs_define
class AnalyticsSalesPipelineStage:
    """Single pipeline stage with deal distribution and velocity metrics

    Attributes:
        stage_id (str):
        stage_name (str):
        stage_type (str):
        stage_order (int):
        deal_count (int):
        avg_days_in_stage (int):
        probability_percent (float | None | str | Unset):
        probability_low (float | None | str | Unset):
        probability_high (float | None | str | Unset):
        outcomes_known (int | Unset):  Default: 0.
        outcomes_won (int | Unset):  Default: 0.
        outcomes_lost (int | Unset):  Default: 0.
        outcomes_slower_than_usual (int | Unset):  Default: 0.
        outcomes_needed (int | Unset):  Default: 0.
        deals_still_moving (int | Unset):  Default: 0.
        usual_stay_days (int | None | Unset):
        stays_counted (int | Unset):  Default: 0.
        stays_needed (int | Unset):  Default: 0.
        total_value (float | None | str | Unset):
        weighted_value (float | None | str | Unset):
        deals_slower_than_usual (int | Unset):  Default: 0.
        value_slower_than_usual (float | None | str | Unset):
    """

    stage_id: str
    stage_name: str
    stage_type: str
    stage_order: int
    deal_count: int
    avg_days_in_stage: int
    probability_percent: float | None | str | Unset = UNSET
    probability_low: float | None | str | Unset = UNSET
    probability_high: float | None | str | Unset = UNSET
    outcomes_known: int | Unset = 0
    outcomes_won: int | Unset = 0
    outcomes_lost: int | Unset = 0
    outcomes_slower_than_usual: int | Unset = 0
    outcomes_needed: int | Unset = 0
    deals_still_moving: int | Unset = 0
    usual_stay_days: int | None | Unset = UNSET
    stays_counted: int | Unset = 0
    stays_needed: int | Unset = 0
    total_value: float | None | str | Unset = UNSET
    weighted_value: float | None | str | Unset = UNSET
    deals_slower_than_usual: int | Unset = 0
    value_slower_than_usual: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_id = self.stage_id

        stage_name = self.stage_name

        stage_type = self.stage_type

        stage_order = self.stage_order

        deal_count = self.deal_count

        avg_days_in_stage = self.avg_days_in_stage

        probability_percent: float | None | str | Unset
        if isinstance(self.probability_percent, Unset):
            probability_percent = UNSET
        else:
            probability_percent = self.probability_percent

        probability_low: float | None | str | Unset
        if isinstance(self.probability_low, Unset):
            probability_low = UNSET
        else:
            probability_low = self.probability_low

        probability_high: float | None | str | Unset
        if isinstance(self.probability_high, Unset):
            probability_high = UNSET
        else:
            probability_high = self.probability_high

        outcomes_known = self.outcomes_known

        outcomes_won = self.outcomes_won

        outcomes_lost = self.outcomes_lost

        outcomes_slower_than_usual = self.outcomes_slower_than_usual

        outcomes_needed = self.outcomes_needed

        deals_still_moving = self.deals_still_moving

        usual_stay_days: int | None | Unset
        if isinstance(self.usual_stay_days, Unset):
            usual_stay_days = UNSET
        else:
            usual_stay_days = self.usual_stay_days

        stays_counted = self.stays_counted

        stays_needed = self.stays_needed

        total_value: float | None | str | Unset
        if isinstance(self.total_value, Unset):
            total_value = UNSET
        else:
            total_value = self.total_value

        weighted_value: float | None | str | Unset
        if isinstance(self.weighted_value, Unset):
            weighted_value = UNSET
        else:
            weighted_value = self.weighted_value

        deals_slower_than_usual = self.deals_slower_than_usual

        value_slower_than_usual: float | None | str | Unset
        if isinstance(self.value_slower_than_usual, Unset):
            value_slower_than_usual = UNSET
        else:
            value_slower_than_usual = self.value_slower_than_usual

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_id": stage_id,
                "stage_name": stage_name,
                "stage_type": stage_type,
                "stage_order": stage_order,
                "deal_count": deal_count,
                "avg_days_in_stage": avg_days_in_stage,
            }
        )
        if probability_percent is not UNSET:
            field_dict["probability_percent"] = probability_percent
        if probability_low is not UNSET:
            field_dict["probability_low"] = probability_low
        if probability_high is not UNSET:
            field_dict["probability_high"] = probability_high
        if outcomes_known is not UNSET:
            field_dict["outcomes_known"] = outcomes_known
        if outcomes_won is not UNSET:
            field_dict["outcomes_won"] = outcomes_won
        if outcomes_lost is not UNSET:
            field_dict["outcomes_lost"] = outcomes_lost
        if outcomes_slower_than_usual is not UNSET:
            field_dict["outcomes_slower_than_usual"] = outcomes_slower_than_usual
        if outcomes_needed is not UNSET:
            field_dict["outcomes_needed"] = outcomes_needed
        if deals_still_moving is not UNSET:
            field_dict["deals_still_moving"] = deals_still_moving
        if usual_stay_days is not UNSET:
            field_dict["usual_stay_days"] = usual_stay_days
        if stays_counted is not UNSET:
            field_dict["stays_counted"] = stays_counted
        if stays_needed is not UNSET:
            field_dict["stays_needed"] = stays_needed
        if total_value is not UNSET:
            field_dict["total_value"] = total_value
        if weighted_value is not UNSET:
            field_dict["weighted_value"] = weighted_value
        if deals_slower_than_usual is not UNSET:
            field_dict["deals_slower_than_usual"] = deals_slower_than_usual
        if value_slower_than_usual is not UNSET:
            field_dict["value_slower_than_usual"] = value_slower_than_usual

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_id = d.pop("stage_id")

        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        stage_order = d.pop("stage_order")

        deal_count = d.pop("deal_count")

        avg_days_in_stage = d.pop("avg_days_in_stage")

        def _parse_probability_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        probability_percent = _parse_probability_percent(
            d.pop("probability_percent", UNSET)
        )

        def _parse_probability_low(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        probability_low = _parse_probability_low(d.pop("probability_low", UNSET))

        def _parse_probability_high(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        probability_high = _parse_probability_high(d.pop("probability_high", UNSET))

        outcomes_known = d.pop("outcomes_known", UNSET)

        outcomes_won = d.pop("outcomes_won", UNSET)

        outcomes_lost = d.pop("outcomes_lost", UNSET)

        outcomes_slower_than_usual = d.pop("outcomes_slower_than_usual", UNSET)

        outcomes_needed = d.pop("outcomes_needed", UNSET)

        deals_still_moving = d.pop("deals_still_moving", UNSET)

        def _parse_usual_stay_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        usual_stay_days = _parse_usual_stay_days(d.pop("usual_stay_days", UNSET))

        stays_counted = d.pop("stays_counted", UNSET)

        stays_needed = d.pop("stays_needed", UNSET)

        def _parse_total_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_value = _parse_total_value(d.pop("total_value", UNSET))

        def _parse_weighted_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        weighted_value = _parse_weighted_value(d.pop("weighted_value", UNSET))

        deals_slower_than_usual = d.pop("deals_slower_than_usual", UNSET)

        def _parse_value_slower_than_usual(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        value_slower_than_usual = _parse_value_slower_than_usual(
            d.pop("value_slower_than_usual", UNSET)
        )

        analytics_sales_pipeline_stage = cls(
            stage_id=stage_id,
            stage_name=stage_name,
            stage_type=stage_type,
            stage_order=stage_order,
            deal_count=deal_count,
            avg_days_in_stage=avg_days_in_stage,
            probability_percent=probability_percent,
            probability_low=probability_low,
            probability_high=probability_high,
            outcomes_known=outcomes_known,
            outcomes_won=outcomes_won,
            outcomes_lost=outcomes_lost,
            outcomes_slower_than_usual=outcomes_slower_than_usual,
            outcomes_needed=outcomes_needed,
            deals_still_moving=deals_still_moving,
            usual_stay_days=usual_stay_days,
            stays_counted=stays_counted,
            stays_needed=stays_needed,
            total_value=total_value,
            weighted_value=weighted_value,
            deals_slower_than_usual=deals_slower_than_usual,
            value_slower_than_usual=value_slower_than_usual,
        )

        analytics_sales_pipeline_stage.additional_properties = d
        return analytics_sales_pipeline_stage

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
