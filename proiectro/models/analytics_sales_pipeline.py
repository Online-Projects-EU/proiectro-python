from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_sales_funnel import AnalyticsSalesFunnel
    from ..models.analytics_sales_pipeline_stage import AnalyticsSalesPipelineStage
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption
    from ..models.stage_not_measured_yet import StageNotMeasuredYet


T = TypeVar("T", bound="AnalyticsSalesPipeline")


@_attrs_define
class AnalyticsSalesPipeline:
    """Sales pipeline analysis for a specific funnel.

    Weighted Value Explanation:
    Weighted pipeline value multiplies the open value in each stage by that
    stage's win probability, measured from the workspace's own deals. A deal
    worth 100K in a stage where 60% of the deals with a known outcome were
    won contributes 60K. A stage with too few known outcomes has no win
    probability yet, and the weighted total waits for every stage that holds
    a deal to weigh: `weighted_waiting_on` lists them. A deal sitting in its
    stage longer than is usual there is set aside: it stays in the pipeline
    total and is reported in `value_slower_than_usual` instead of being weighed.

        Attributes:
            funnel_id (str):
            funnel_name (str):
            total_deals (int):
            currency (str):
            period (str | Unset):  Default: 'YTD'.
            temporal_type (str | Unset):  Default: 'snapshot'.
            generated_at (datetime.datetime | None | Unset):
            period_label (None | str | Unset):
            horizon (None | str | Unset):
            horizon_label (None | str | Unset):
            horizon_options (list[HorizonOption] | None | Unset):
            compare (None | str | Unset):
            compare_label (None | str | Unset):
            compare_options (list[CompareOption] | None | Unset):
            filter_severity (None | str | Unset):
            filter_severity_label (None | str | Unset):
            filter_category (None | str | Unset):
            filter_category_label (None | str | Unset):
            filter_type (None | str | Unset):
            filter_type_label (None | str | Unset):
            available_funnels (list[AnalyticsSalesFunnel] | Unset):
            total_pipeline_value (float | None | str | Unset):
            weighted_pipeline_value (float | None | str | Unset):
            weighted_waiting_on (list[StageNotMeasuredYet] | Unset):
            deals_slower_than_usual (int | Unset):  Default: 0.
            value_slower_than_usual (float | None | str | Unset):
            uncovered_currencies (list[str] | Unset):
            coverage_percent (float | None | str | Unset):
            stages (list[AnalyticsSalesPipelineStage] | Unset):
            weighted_value_explanation (str | Unset):  Default: ''.
    """

    funnel_id: str
    funnel_name: str
    total_deals: int
    currency: str
    period: str | Unset = "YTD"
    temporal_type: str | Unset = "snapshot"
    generated_at: datetime.datetime | None | Unset = UNSET
    period_label: None | str | Unset = UNSET
    horizon: None | str | Unset = UNSET
    horizon_label: None | str | Unset = UNSET
    horizon_options: list[HorizonOption] | None | Unset = UNSET
    compare: None | str | Unset = UNSET
    compare_label: None | str | Unset = UNSET
    compare_options: list[CompareOption] | None | Unset = UNSET
    filter_severity: None | str | Unset = UNSET
    filter_severity_label: None | str | Unset = UNSET
    filter_category: None | str | Unset = UNSET
    filter_category_label: None | str | Unset = UNSET
    filter_type: None | str | Unset = UNSET
    filter_type_label: None | str | Unset = UNSET
    available_funnels: list[AnalyticsSalesFunnel] | Unset = UNSET
    total_pipeline_value: float | None | str | Unset = UNSET
    weighted_pipeline_value: float | None | str | Unset = UNSET
    weighted_waiting_on: list[StageNotMeasuredYet] | Unset = UNSET
    deals_slower_than_usual: int | Unset = 0
    value_slower_than_usual: float | None | str | Unset = UNSET
    uncovered_currencies: list[str] | Unset = UNSET
    coverage_percent: float | None | str | Unset = UNSET
    stages: list[AnalyticsSalesPipelineStage] | Unset = UNSET
    weighted_value_explanation: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funnel_id = self.funnel_id

        funnel_name = self.funnel_name

        total_deals = self.total_deals

        currency = self.currency

        period = self.period

        temporal_type = self.temporal_type

        generated_at: None | str | Unset
        if isinstance(self.generated_at, Unset):
            generated_at = UNSET
        elif isinstance(self.generated_at, datetime.datetime):
            generated_at = self.generated_at.isoformat()
        else:
            generated_at = self.generated_at

        period_label: None | str | Unset
        if isinstance(self.period_label, Unset):
            period_label = UNSET
        else:
            period_label = self.period_label

        horizon: None | str | Unset
        if isinstance(self.horizon, Unset):
            horizon = UNSET
        else:
            horizon = self.horizon

        horizon_label: None | str | Unset
        if isinstance(self.horizon_label, Unset):
            horizon_label = UNSET
        else:
            horizon_label = self.horizon_label

        horizon_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.horizon_options, Unset):
            horizon_options = UNSET
        elif isinstance(self.horizon_options, list):
            horizon_options = []
            for horizon_options_type_0_item_data in self.horizon_options:
                horizon_options_type_0_item = horizon_options_type_0_item_data.to_dict()
                horizon_options.append(horizon_options_type_0_item)

        else:
            horizon_options = self.horizon_options

        compare: None | str | Unset
        if isinstance(self.compare, Unset):
            compare = UNSET
        else:
            compare = self.compare

        compare_label: None | str | Unset
        if isinstance(self.compare_label, Unset):
            compare_label = UNSET
        else:
            compare_label = self.compare_label

        compare_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.compare_options, Unset):
            compare_options = UNSET
        elif isinstance(self.compare_options, list):
            compare_options = []
            for compare_options_type_0_item_data in self.compare_options:
                compare_options_type_0_item = compare_options_type_0_item_data.to_dict()
                compare_options.append(compare_options_type_0_item)

        else:
            compare_options = self.compare_options

        filter_severity: None | str | Unset
        if isinstance(self.filter_severity, Unset):
            filter_severity = UNSET
        else:
            filter_severity = self.filter_severity

        filter_severity_label: None | str | Unset
        if isinstance(self.filter_severity_label, Unset):
            filter_severity_label = UNSET
        else:
            filter_severity_label = self.filter_severity_label

        filter_category: None | str | Unset
        if isinstance(self.filter_category, Unset):
            filter_category = UNSET
        else:
            filter_category = self.filter_category

        filter_category_label: None | str | Unset
        if isinstance(self.filter_category_label, Unset):
            filter_category_label = UNSET
        else:
            filter_category_label = self.filter_category_label

        filter_type: None | str | Unset
        if isinstance(self.filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = self.filter_type

        filter_type_label: None | str | Unset
        if isinstance(self.filter_type_label, Unset):
            filter_type_label = UNSET
        else:
            filter_type_label = self.filter_type_label

        available_funnels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_funnels, Unset):
            available_funnels = []
            for available_funnels_item_data in self.available_funnels:
                available_funnels_item = available_funnels_item_data.to_dict()
                available_funnels.append(available_funnels_item)

        total_pipeline_value: float | None | str | Unset
        if isinstance(self.total_pipeline_value, Unset):
            total_pipeline_value = UNSET
        else:
            total_pipeline_value = self.total_pipeline_value

        weighted_pipeline_value: float | None | str | Unset
        if isinstance(self.weighted_pipeline_value, Unset):
            weighted_pipeline_value = UNSET
        else:
            weighted_pipeline_value = self.weighted_pipeline_value

        weighted_waiting_on: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.weighted_waiting_on, Unset):
            weighted_waiting_on = []
            for weighted_waiting_on_item_data in self.weighted_waiting_on:
                weighted_waiting_on_item = weighted_waiting_on_item_data.to_dict()
                weighted_waiting_on.append(weighted_waiting_on_item)

        deals_slower_than_usual = self.deals_slower_than_usual

        value_slower_than_usual: float | None | str | Unset
        if isinstance(self.value_slower_than_usual, Unset):
            value_slower_than_usual = UNSET
        else:
            value_slower_than_usual = self.value_slower_than_usual

        uncovered_currencies: list[str] | Unset = UNSET
        if not isinstance(self.uncovered_currencies, Unset):
            uncovered_currencies = self.uncovered_currencies

        coverage_percent: float | None | str | Unset
        if isinstance(self.coverage_percent, Unset):
            coverage_percent = UNSET
        else:
            coverage_percent = self.coverage_percent

        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        weighted_value_explanation = self.weighted_value_explanation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "funnel_id": funnel_id,
                "funnel_name": funnel_name,
                "total_deals": total_deals,
                "currency": currency,
            }
        )
        if period is not UNSET:
            field_dict["period"] = period
        if temporal_type is not UNSET:
            field_dict["temporal_type"] = temporal_type
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if period_label is not UNSET:
            field_dict["period_label"] = period_label
        if horizon is not UNSET:
            field_dict["horizon"] = horizon
        if horizon_label is not UNSET:
            field_dict["horizon_label"] = horizon_label
        if horizon_options is not UNSET:
            field_dict["horizon_options"] = horizon_options
        if compare is not UNSET:
            field_dict["compare"] = compare
        if compare_label is not UNSET:
            field_dict["compare_label"] = compare_label
        if compare_options is not UNSET:
            field_dict["compare_options"] = compare_options
        if filter_severity is not UNSET:
            field_dict["filter_severity"] = filter_severity
        if filter_severity_label is not UNSET:
            field_dict["filter_severity_label"] = filter_severity_label
        if filter_category is not UNSET:
            field_dict["filter_category"] = filter_category
        if filter_category_label is not UNSET:
            field_dict["filter_category_label"] = filter_category_label
        if filter_type is not UNSET:
            field_dict["filter_type"] = filter_type
        if filter_type_label is not UNSET:
            field_dict["filter_type_label"] = filter_type_label
        if available_funnels is not UNSET:
            field_dict["available_funnels"] = available_funnels
        if total_pipeline_value is not UNSET:
            field_dict["total_pipeline_value"] = total_pipeline_value
        if weighted_pipeline_value is not UNSET:
            field_dict["weighted_pipeline_value"] = weighted_pipeline_value
        if weighted_waiting_on is not UNSET:
            field_dict["weighted_waiting_on"] = weighted_waiting_on
        if deals_slower_than_usual is not UNSET:
            field_dict["deals_slower_than_usual"] = deals_slower_than_usual
        if value_slower_than_usual is not UNSET:
            field_dict["value_slower_than_usual"] = value_slower_than_usual
        if uncovered_currencies is not UNSET:
            field_dict["uncovered_currencies"] = uncovered_currencies
        if coverage_percent is not UNSET:
            field_dict["coverage_percent"] = coverage_percent
        if stages is not UNSET:
            field_dict["stages"] = stages
        if weighted_value_explanation is not UNSET:
            field_dict["weighted_value_explanation"] = weighted_value_explanation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_sales_funnel import AnalyticsSalesFunnel
        from ..models.analytics_sales_pipeline_stage import AnalyticsSalesPipelineStage
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption
        from ..models.stage_not_measured_yet import StageNotMeasuredYet

        d = dict(src_dict)
        funnel_id = d.pop("funnel_id")

        funnel_name = d.pop("funnel_name")

        total_deals = d.pop("total_deals")

        currency = d.pop("currency")

        period = d.pop("period", UNSET)

        temporal_type = d.pop("temporal_type", UNSET)

        def _parse_generated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generated_at_type_0 = isoparse(data)

                return generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        generated_at = _parse_generated_at(d.pop("generated_at", UNSET))

        def _parse_period_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_label = _parse_period_label(d.pop("period_label", UNSET))

        def _parse_horizon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        horizon = _parse_horizon(d.pop("horizon", UNSET))

        def _parse_horizon_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        horizon_label = _parse_horizon_label(d.pop("horizon_label", UNSET))

        def _parse_horizon_options(data: object) -> list[HorizonOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                horizon_options_type_0 = []
                _horizon_options_type_0 = data
                for horizon_options_type_0_item_data in _horizon_options_type_0:
                    horizon_options_type_0_item = HorizonOption.from_dict(
                        horizon_options_type_0_item_data
                    )

                    horizon_options_type_0.append(horizon_options_type_0_item)

                return horizon_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HorizonOption] | None | Unset, data)

        horizon_options = _parse_horizon_options(d.pop("horizon_options", UNSET))

        def _parse_compare(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compare = _parse_compare(d.pop("compare", UNSET))

        def _parse_compare_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compare_label = _parse_compare_label(d.pop("compare_label", UNSET))

        def _parse_compare_options(data: object) -> list[CompareOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compare_options_type_0 = []
                _compare_options_type_0 = data
                for compare_options_type_0_item_data in _compare_options_type_0:
                    compare_options_type_0_item = CompareOption.from_dict(
                        compare_options_type_0_item_data
                    )

                    compare_options_type_0.append(compare_options_type_0_item)

                return compare_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompareOption] | None | Unset, data)

        compare_options = _parse_compare_options(d.pop("compare_options", UNSET))

        def _parse_filter_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_severity = _parse_filter_severity(d.pop("filter_severity", UNSET))

        def _parse_filter_severity_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_severity_label = _parse_filter_severity_label(
            d.pop("filter_severity_label", UNSET)
        )

        def _parse_filter_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_category = _parse_filter_category(d.pop("filter_category", UNSET))

        def _parse_filter_category_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_category_label = _parse_filter_category_label(
            d.pop("filter_category_label", UNSET)
        )

        def _parse_filter_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_type = _parse_filter_type(d.pop("filter_type", UNSET))

        def _parse_filter_type_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_type_label = _parse_filter_type_label(d.pop("filter_type_label", UNSET))

        _available_funnels = d.pop("available_funnels", UNSET)
        available_funnels: list[AnalyticsSalesFunnel] | Unset = UNSET
        if _available_funnels is not UNSET:
            available_funnels = []
            for available_funnels_item_data in _available_funnels:
                available_funnels_item = AnalyticsSalesFunnel.from_dict(
                    available_funnels_item_data
                )

                available_funnels.append(available_funnels_item)

        def _parse_total_pipeline_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_pipeline_value = _parse_total_pipeline_value(
            d.pop("total_pipeline_value", UNSET)
        )

        def _parse_weighted_pipeline_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        weighted_pipeline_value = _parse_weighted_pipeline_value(
            d.pop("weighted_pipeline_value", UNSET)
        )

        _weighted_waiting_on = d.pop("weighted_waiting_on", UNSET)
        weighted_waiting_on: list[StageNotMeasuredYet] | Unset = UNSET
        if _weighted_waiting_on is not UNSET:
            weighted_waiting_on = []
            for weighted_waiting_on_item_data in _weighted_waiting_on:
                weighted_waiting_on_item = StageNotMeasuredYet.from_dict(
                    weighted_waiting_on_item_data
                )

                weighted_waiting_on.append(weighted_waiting_on_item)

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

        uncovered_currencies = cast(list[str], d.pop("uncovered_currencies", UNSET))

        def _parse_coverage_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        coverage_percent = _parse_coverage_percent(d.pop("coverage_percent", UNSET))

        _stages = d.pop("stages", UNSET)
        stages: list[AnalyticsSalesPipelineStage] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = AnalyticsSalesPipelineStage.from_dict(stages_item_data)

                stages.append(stages_item)

        weighted_value_explanation = d.pop("weighted_value_explanation", UNSET)

        analytics_sales_pipeline = cls(
            funnel_id=funnel_id,
            funnel_name=funnel_name,
            total_deals=total_deals,
            currency=currency,
            period=period,
            temporal_type=temporal_type,
            generated_at=generated_at,
            period_label=period_label,
            horizon=horizon,
            horizon_label=horizon_label,
            horizon_options=horizon_options,
            compare=compare,
            compare_label=compare_label,
            compare_options=compare_options,
            filter_severity=filter_severity,
            filter_severity_label=filter_severity_label,
            filter_category=filter_category,
            filter_category_label=filter_category_label,
            filter_type=filter_type,
            filter_type_label=filter_type_label,
            available_funnels=available_funnels,
            total_pipeline_value=total_pipeline_value,
            weighted_pipeline_value=weighted_pipeline_value,
            weighted_waiting_on=weighted_waiting_on,
            deals_slower_than_usual=deals_slower_than_usual,
            value_slower_than_usual=value_slower_than_usual,
            uncovered_currencies=uncovered_currencies,
            coverage_percent=coverage_percent,
            stages=stages,
            weighted_value_explanation=weighted_value_explanation,
        )

        analytics_sales_pipeline.additional_properties = d
        return analytics_sales_pipeline

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
