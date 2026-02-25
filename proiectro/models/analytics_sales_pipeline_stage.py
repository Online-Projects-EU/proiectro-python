from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSalesPipelineStage")


@_attrs_define
class AnalyticsSalesPipelineStage:
    """Single pipeline stage with deal distribution and velocity metrics

    Attributes:
        stage_id (str):
        stage_name (str):
        stage_type (str):
        stage_order (int):
        probability_percent (int):
        deal_count (int):
        total_value (float | str):
        weighted_value (float | str):
        avg_days_in_stage (int):
    """

    stage_id: str
    stage_name: str
    stage_type: str
    stage_order: int
    probability_percent: int
    deal_count: int
    total_value: float | str
    weighted_value: float | str
    avg_days_in_stage: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_id = self.stage_id

        stage_name = self.stage_name

        stage_type = self.stage_type

        stage_order = self.stage_order

        probability_percent = self.probability_percent

        deal_count = self.deal_count

        total_value: float | str
        total_value = self.total_value

        weighted_value: float | str
        weighted_value = self.weighted_value

        avg_days_in_stage = self.avg_days_in_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_id": stage_id,
                "stage_name": stage_name,
                "stage_type": stage_type,
                "stage_order": stage_order,
                "probability_percent": probability_percent,
                "deal_count": deal_count,
                "total_value": total_value,
                "weighted_value": weighted_value,
                "avg_days_in_stage": avg_days_in_stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_id = d.pop("stage_id")

        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        stage_order = d.pop("stage_order")

        probability_percent = d.pop("probability_percent")

        deal_count = d.pop("deal_count")

        def _parse_total_value(data: object) -> float | str:
            return cast(float | str, data)

        total_value = _parse_total_value(d.pop("total_value"))

        def _parse_weighted_value(data: object) -> float | str:
            return cast(float | str, data)

        weighted_value = _parse_weighted_value(d.pop("weighted_value"))

        avg_days_in_stage = d.pop("avg_days_in_stage")

        analytics_sales_pipeline_stage = cls(
            stage_id=stage_id,
            stage_name=stage_name,
            stage_type=stage_type,
            stage_order=stage_order,
            probability_percent=probability_percent,
            deal_count=deal_count,
            total_value=total_value,
            weighted_value=weighted_value,
            avg_days_in_stage=avg_days_in_stage,
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
