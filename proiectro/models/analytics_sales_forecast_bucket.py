from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsSalesForecastBucket")


@_attrs_define
class AnalyticsSalesForecastBucket:
    """Single time bucket (month or quarter) in sales forecast

    Attributes:
        label (str):
        sublabel (str):
        deal_count (int):
        pipeline_value (float | None | str | Unset):
        weighted_value (float | None | str | Unset):
        best_case (float | None | str | Unset):
        worst_case (float | None | str | Unset):
    """

    label: str
    sublabel: str
    deal_count: int
    pipeline_value: float | None | str | Unset = UNSET
    weighted_value: float | None | str | Unset = UNSET
    best_case: float | None | str | Unset = UNSET
    worst_case: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        sublabel = self.sublabel

        deal_count = self.deal_count

        pipeline_value: float | None | str | Unset
        if isinstance(self.pipeline_value, Unset):
            pipeline_value = UNSET
        else:
            pipeline_value = self.pipeline_value

        weighted_value: float | None | str | Unset
        if isinstance(self.weighted_value, Unset):
            weighted_value = UNSET
        else:
            weighted_value = self.weighted_value

        best_case: float | None | str | Unset
        if isinstance(self.best_case, Unset):
            best_case = UNSET
        else:
            best_case = self.best_case

        worst_case: float | None | str | Unset
        if isinstance(self.worst_case, Unset):
            worst_case = UNSET
        else:
            worst_case = self.worst_case

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "sublabel": sublabel,
                "deal_count": deal_count,
            }
        )
        if pipeline_value is not UNSET:
            field_dict["pipeline_value"] = pipeline_value
        if weighted_value is not UNSET:
            field_dict["weighted_value"] = weighted_value
        if best_case is not UNSET:
            field_dict["best_case"] = best_case
        if worst_case is not UNSET:
            field_dict["worst_case"] = worst_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        sublabel = d.pop("sublabel")

        deal_count = d.pop("deal_count")

        def _parse_pipeline_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pipeline_value = _parse_pipeline_value(d.pop("pipeline_value", UNSET))

        def _parse_weighted_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        weighted_value = _parse_weighted_value(d.pop("weighted_value", UNSET))

        def _parse_best_case(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        best_case = _parse_best_case(d.pop("best_case", UNSET))

        def _parse_worst_case(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        worst_case = _parse_worst_case(d.pop("worst_case", UNSET))

        analytics_sales_forecast_bucket = cls(
            label=label,
            sublabel=sublabel,
            deal_count=deal_count,
            pipeline_value=pipeline_value,
            weighted_value=weighted_value,
            best_case=best_case,
            worst_case=worst_case,
        )

        analytics_sales_forecast_bucket.additional_properties = d
        return analytics_sales_forecast_bucket

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
