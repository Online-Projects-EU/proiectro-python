from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_sales_forecast_bucket import AnalyticsSalesForecastBucket
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsSalesForecast")


@_attrs_define
class AnalyticsSalesForecast:
    """Sales forecast - aggregated across all funnels.

    Projects future revenue based on current pipeline deals weighted by
    stage probability. Deals are grouped by expected close date into
    time buckets (monthly for short horizons, quarterly for long).

    Note: Comparisons (YoY, PoP) are not applicable to forecasts since
    forecasts are projections, not historical data.

        Attributes:
            total_pipeline_value (float | str):
            total_weighted_value (float | str):
            total_best_case (float | str):
            total_worst_case (float | str):
            total_deals (int):
            avg_deal_size (float | str):
            avg_sales_cycle_days (int):
            granularity (str):
            currency (str):
            period (str | Unset):  Default: 'YTD'.
            temporal_type (str | Unset):  Default: 'snapshot'.
            generated_at (str | Unset):  Default: ''.
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
            buckets (list[AnalyticsSalesForecastBucket] | Unset):
            deals_without_close_date (int | Unset):  Default: 0.
            value_without_close_date (float | str | Unset):  Default: 0.0.
            weighted_value_explanation (str | Unset):  Default: ''.
    """

    total_pipeline_value: float | str
    total_weighted_value: float | str
    total_best_case: float | str
    total_worst_case: float | str
    total_deals: int
    avg_deal_size: float | str
    avg_sales_cycle_days: int
    granularity: str
    currency: str
    period: str | Unset = "YTD"
    temporal_type: str | Unset = "snapshot"
    generated_at: str | Unset = ""
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
    buckets: list[AnalyticsSalesForecastBucket] | Unset = UNSET
    deals_without_close_date: int | Unset = 0
    value_without_close_date: float | str | Unset = 0.0
    weighted_value_explanation: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_pipeline_value: float | str
        total_pipeline_value = self.total_pipeline_value

        total_weighted_value: float | str
        total_weighted_value = self.total_weighted_value

        total_best_case: float | str
        total_best_case = self.total_best_case

        total_worst_case: float | str
        total_worst_case = self.total_worst_case

        total_deals = self.total_deals

        avg_deal_size: float | str
        avg_deal_size = self.avg_deal_size

        avg_sales_cycle_days = self.avg_sales_cycle_days

        granularity = self.granularity

        currency = self.currency

        period = self.period

        temporal_type = self.temporal_type

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

        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        deals_without_close_date = self.deals_without_close_date

        value_without_close_date: float | str | Unset
        if isinstance(self.value_without_close_date, Unset):
            value_without_close_date = UNSET
        else:
            value_without_close_date = self.value_without_close_date

        weighted_value_explanation = self.weighted_value_explanation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_pipeline_value": total_pipeline_value,
                "total_weighted_value": total_weighted_value,
                "total_best_case": total_best_case,
                "total_worst_case": total_worst_case,
                "total_deals": total_deals,
                "avg_deal_size": avg_deal_size,
                "avg_sales_cycle_days": avg_sales_cycle_days,
                "granularity": granularity,
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
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if deals_without_close_date is not UNSET:
            field_dict["deals_without_close_date"] = deals_without_close_date
        if value_without_close_date is not UNSET:
            field_dict["value_without_close_date"] = value_without_close_date
        if weighted_value_explanation is not UNSET:
            field_dict["weighted_value_explanation"] = weighted_value_explanation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_sales_forecast_bucket import (
            AnalyticsSalesForecastBucket,
        )
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_total_pipeline_value(data: object) -> float | str:
            return cast(float | str, data)

        total_pipeline_value = _parse_total_pipeline_value(
            d.pop("total_pipeline_value")
        )

        def _parse_total_weighted_value(data: object) -> float | str:
            return cast(float | str, data)

        total_weighted_value = _parse_total_weighted_value(
            d.pop("total_weighted_value")
        )

        def _parse_total_best_case(data: object) -> float | str:
            return cast(float | str, data)

        total_best_case = _parse_total_best_case(d.pop("total_best_case"))

        def _parse_total_worst_case(data: object) -> float | str:
            return cast(float | str, data)

        total_worst_case = _parse_total_worst_case(d.pop("total_worst_case"))

        total_deals = d.pop("total_deals")

        def _parse_avg_deal_size(data: object) -> float | str:
            return cast(float | str, data)

        avg_deal_size = _parse_avg_deal_size(d.pop("avg_deal_size"))

        avg_sales_cycle_days = d.pop("avg_sales_cycle_days")

        granularity = d.pop("granularity")

        currency = d.pop("currency")

        period = d.pop("period", UNSET)

        temporal_type = d.pop("temporal_type", UNSET)

        generated_at = d.pop("generated_at", UNSET)

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

        _buckets = d.pop("buckets", UNSET)
        buckets: list[AnalyticsSalesForecastBucket] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = AnalyticsSalesForecastBucket.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        deals_without_close_date = d.pop("deals_without_close_date", UNSET)

        def _parse_value_without_close_date(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        value_without_close_date = _parse_value_without_close_date(
            d.pop("value_without_close_date", UNSET)
        )

        weighted_value_explanation = d.pop("weighted_value_explanation", UNSET)

        analytics_sales_forecast = cls(
            total_pipeline_value=total_pipeline_value,
            total_weighted_value=total_weighted_value,
            total_best_case=total_best_case,
            total_worst_case=total_worst_case,
            total_deals=total_deals,
            avg_deal_size=avg_deal_size,
            avg_sales_cycle_days=avg_sales_cycle_days,
            granularity=granularity,
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
            buckets=buckets,
            deals_without_close_date=deals_without_close_date,
            value_without_close_date=value_without_close_date,
            weighted_value_explanation=weighted_value_explanation,
        )

        analytics_sales_forecast.additional_properties = d
        return analytics_sales_forecast

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
