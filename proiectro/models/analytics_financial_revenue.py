from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_revenue_category_item import AnalyticsRevenueCategoryItem
    from ..models.analytics_revenue_month_item import AnalyticsRevenueMonthItem
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsFinancialRevenue")


@_attrs_define
class AnalyticsFinancialRevenue:
    """Revenue analysis

    Attributes:
        total_revenue (float | str):
        recurring_revenue (float | str):
        one_time_revenue (float | str):
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
        revenue_by_category (list[AnalyticsRevenueCategoryItem] | Unset):
        monthly_trend (list[AnalyticsRevenueMonthItem] | Unset):
        prev_total_revenue (float | None | str | Unset):
        prev_recurring_revenue (float | None | str | Unset):
        prev_one_time_revenue (float | None | str | Unset):
        total_change_pct (float | Literal['new'] | None | str | Unset):
        recurring_change_pct (float | Literal['new'] | None | str | Unset):
        one_time_change_pct (float | Literal['new'] | None | str | Unset):
    """

    total_revenue: float | str
    recurring_revenue: float | str
    one_time_revenue: float | str
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
    revenue_by_category: list[AnalyticsRevenueCategoryItem] | Unset = UNSET
    monthly_trend: list[AnalyticsRevenueMonthItem] | Unset = UNSET
    prev_total_revenue: float | None | str | Unset = UNSET
    prev_recurring_revenue: float | None | str | Unset = UNSET
    prev_one_time_revenue: float | None | str | Unset = UNSET
    total_change_pct: float | Literal["new"] | None | str | Unset = UNSET
    recurring_change_pct: float | Literal["new"] | None | str | Unset = UNSET
    one_time_change_pct: float | Literal["new"] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_revenue: float | str
        total_revenue = self.total_revenue

        recurring_revenue: float | str
        recurring_revenue = self.recurring_revenue

        one_time_revenue: float | str
        one_time_revenue = self.one_time_revenue

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

        revenue_by_category: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.revenue_by_category, Unset):
            revenue_by_category = []
            for revenue_by_category_item_data in self.revenue_by_category:
                revenue_by_category_item = revenue_by_category_item_data.to_dict()
                revenue_by_category.append(revenue_by_category_item)

        monthly_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monthly_trend, Unset):
            monthly_trend = []
            for monthly_trend_item_data in self.monthly_trend:
                monthly_trend_item = monthly_trend_item_data.to_dict()
                monthly_trend.append(monthly_trend_item)

        prev_total_revenue: float | None | str | Unset
        if isinstance(self.prev_total_revenue, Unset):
            prev_total_revenue = UNSET
        else:
            prev_total_revenue = self.prev_total_revenue

        prev_recurring_revenue: float | None | str | Unset
        if isinstance(self.prev_recurring_revenue, Unset):
            prev_recurring_revenue = UNSET
        else:
            prev_recurring_revenue = self.prev_recurring_revenue

        prev_one_time_revenue: float | None | str | Unset
        if isinstance(self.prev_one_time_revenue, Unset):
            prev_one_time_revenue = UNSET
        else:
            prev_one_time_revenue = self.prev_one_time_revenue

        total_change_pct: float | Literal["new"] | None | str | Unset
        if isinstance(self.total_change_pct, Unset):
            total_change_pct = UNSET
        else:
            total_change_pct = self.total_change_pct

        recurring_change_pct: float | Literal["new"] | None | str | Unset
        if isinstance(self.recurring_change_pct, Unset):
            recurring_change_pct = UNSET
        else:
            recurring_change_pct = self.recurring_change_pct

        one_time_change_pct: float | Literal["new"] | None | str | Unset
        if isinstance(self.one_time_change_pct, Unset):
            one_time_change_pct = UNSET
        else:
            one_time_change_pct = self.one_time_change_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_revenue": total_revenue,
                "recurring_revenue": recurring_revenue,
                "one_time_revenue": one_time_revenue,
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
        if revenue_by_category is not UNSET:
            field_dict["revenue_by_category"] = revenue_by_category
        if monthly_trend is not UNSET:
            field_dict["monthly_trend"] = monthly_trend
        if prev_total_revenue is not UNSET:
            field_dict["prev_total_revenue"] = prev_total_revenue
        if prev_recurring_revenue is not UNSET:
            field_dict["prev_recurring_revenue"] = prev_recurring_revenue
        if prev_one_time_revenue is not UNSET:
            field_dict["prev_one_time_revenue"] = prev_one_time_revenue
        if total_change_pct is not UNSET:
            field_dict["total_change_pct"] = total_change_pct
        if recurring_change_pct is not UNSET:
            field_dict["recurring_change_pct"] = recurring_change_pct
        if one_time_change_pct is not UNSET:
            field_dict["one_time_change_pct"] = one_time_change_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_revenue_category_item import (
            AnalyticsRevenueCategoryItem,
        )
        from ..models.analytics_revenue_month_item import AnalyticsRevenueMonthItem
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_total_revenue(data: object) -> float | str:
            return cast(float | str, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue"))

        def _parse_recurring_revenue(data: object) -> float | str:
            return cast(float | str, data)

        recurring_revenue = _parse_recurring_revenue(d.pop("recurring_revenue"))

        def _parse_one_time_revenue(data: object) -> float | str:
            return cast(float | str, data)

        one_time_revenue = _parse_one_time_revenue(d.pop("one_time_revenue"))

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

        _revenue_by_category = d.pop("revenue_by_category", UNSET)
        revenue_by_category: list[AnalyticsRevenueCategoryItem] | Unset = UNSET
        if _revenue_by_category is not UNSET:
            revenue_by_category = []
            for revenue_by_category_item_data in _revenue_by_category:
                revenue_by_category_item = AnalyticsRevenueCategoryItem.from_dict(
                    revenue_by_category_item_data
                )

                revenue_by_category.append(revenue_by_category_item)

        _monthly_trend = d.pop("monthly_trend", UNSET)
        monthly_trend: list[AnalyticsRevenueMonthItem] | Unset = UNSET
        if _monthly_trend is not UNSET:
            monthly_trend = []
            for monthly_trend_item_data in _monthly_trend:
                monthly_trend_item = AnalyticsRevenueMonthItem.from_dict(
                    monthly_trend_item_data
                )

                monthly_trend.append(monthly_trend_item)

        def _parse_prev_total_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_total_revenue = _parse_prev_total_revenue(
            d.pop("prev_total_revenue", UNSET)
        )

        def _parse_prev_recurring_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_recurring_revenue = _parse_prev_recurring_revenue(
            d.pop("prev_recurring_revenue", UNSET)
        )

        def _parse_prev_one_time_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_one_time_revenue = _parse_prev_one_time_revenue(
            d.pop("prev_one_time_revenue", UNSET)
        )

        def _parse_total_change_pct(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            total_change_pct_type_2 = cast(Literal["new"], data)
            if total_change_pct_type_2 != "new":
                raise ValueError(
                    f"total_change_pct_type_2 must match const 'new', got '{total_change_pct_type_2}'"
                )
            return total_change_pct_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        total_change_pct = _parse_total_change_pct(d.pop("total_change_pct", UNSET))

        def _parse_recurring_change_pct(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            recurring_change_pct_type_2 = cast(Literal["new"], data)
            if recurring_change_pct_type_2 != "new":
                raise ValueError(
                    f"recurring_change_pct_type_2 must match const 'new', got '{recurring_change_pct_type_2}'"
                )
            return recurring_change_pct_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        recurring_change_pct = _parse_recurring_change_pct(
            d.pop("recurring_change_pct", UNSET)
        )

        def _parse_one_time_change_pct(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            one_time_change_pct_type_2 = cast(Literal["new"], data)
            if one_time_change_pct_type_2 != "new":
                raise ValueError(
                    f"one_time_change_pct_type_2 must match const 'new', got '{one_time_change_pct_type_2}'"
                )
            return one_time_change_pct_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        one_time_change_pct = _parse_one_time_change_pct(
            d.pop("one_time_change_pct", UNSET)
        )

        analytics_financial_revenue = cls(
            total_revenue=total_revenue,
            recurring_revenue=recurring_revenue,
            one_time_revenue=one_time_revenue,
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
            revenue_by_category=revenue_by_category,
            monthly_trend=monthly_trend,
            prev_total_revenue=prev_total_revenue,
            prev_recurring_revenue=prev_recurring_revenue,
            prev_one_time_revenue=prev_one_time_revenue,
            total_change_pct=total_change_pct,
            recurring_change_pct=recurring_change_pct,
            one_time_change_pct=one_time_change_pct,
        )

        analytics_financial_revenue.additional_properties = d
        return analytics_financial_revenue

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
