from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="FinancialKPIs")


@_attrs_define
class FinancialKPIs:
    """Financial KPIs - Revenue, margins, and receivables health.

    Shows: Revenue with growth rate, Margin health, AR aging summary, DSO status.

        Attributes:
            total_revenue (float | str):
            revenue_growth_percent (float | str):
            revenue_status (str):
            recurring_revenue (float | str):
            one_time_revenue (float | str):
            gross_margin_percent (float | str):
            gross_margin_target (float | str):
            gross_margin_status (str):
            margin_trend_direction (str):
            outstanding_ar (float | str):
            ar_current (float | str):
            ar_overdue (float | str):
            ar_overdue_30_plus (float | str):
            ar_status (str):
            ar_at_risk_percent (float | str):
            dso_days (int):
            dso_target (int):
            dso_status (str):
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
            dso_industry_benchmark (int | None | Unset):
    """

    total_revenue: float | str
    revenue_growth_percent: float | str
    revenue_status: str
    recurring_revenue: float | str
    one_time_revenue: float | str
    gross_margin_percent: float | str
    gross_margin_target: float | str
    gross_margin_status: str
    margin_trend_direction: str
    outstanding_ar: float | str
    ar_current: float | str
    ar_overdue: float | str
    ar_overdue_30_plus: float | str
    ar_status: str
    ar_at_risk_percent: float | str
    dso_days: int
    dso_target: int
    dso_status: str
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
    dso_industry_benchmark: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_revenue: float | str
        total_revenue = self.total_revenue

        revenue_growth_percent: float | str
        revenue_growth_percent = self.revenue_growth_percent

        revenue_status = self.revenue_status

        recurring_revenue: float | str
        recurring_revenue = self.recurring_revenue

        one_time_revenue: float | str
        one_time_revenue = self.one_time_revenue

        gross_margin_percent: float | str
        gross_margin_percent = self.gross_margin_percent

        gross_margin_target: float | str
        gross_margin_target = self.gross_margin_target

        gross_margin_status = self.gross_margin_status

        margin_trend_direction = self.margin_trend_direction

        outstanding_ar: float | str
        outstanding_ar = self.outstanding_ar

        ar_current: float | str
        ar_current = self.ar_current

        ar_overdue: float | str
        ar_overdue = self.ar_overdue

        ar_overdue_30_plus: float | str
        ar_overdue_30_plus = self.ar_overdue_30_plus

        ar_status = self.ar_status

        ar_at_risk_percent: float | str
        ar_at_risk_percent = self.ar_at_risk_percent

        dso_days = self.dso_days

        dso_target = self.dso_target

        dso_status = self.dso_status

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

        dso_industry_benchmark: int | None | Unset
        if isinstance(self.dso_industry_benchmark, Unset):
            dso_industry_benchmark = UNSET
        else:
            dso_industry_benchmark = self.dso_industry_benchmark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_revenue": total_revenue,
                "revenue_growth_percent": revenue_growth_percent,
                "revenue_status": revenue_status,
                "recurring_revenue": recurring_revenue,
                "one_time_revenue": one_time_revenue,
                "gross_margin_percent": gross_margin_percent,
                "gross_margin_target": gross_margin_target,
                "gross_margin_status": gross_margin_status,
                "margin_trend_direction": margin_trend_direction,
                "outstanding_ar": outstanding_ar,
                "ar_current": ar_current,
                "ar_overdue": ar_overdue,
                "ar_overdue_30_plus": ar_overdue_30_plus,
                "ar_status": ar_status,
                "ar_at_risk_percent": ar_at_risk_percent,
                "dso_days": dso_days,
                "dso_target": dso_target,
                "dso_status": dso_status,
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
        if dso_industry_benchmark is not UNSET:
            field_dict["dso_industry_benchmark"] = dso_industry_benchmark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_total_revenue(data: object) -> float | str:
            return cast(float | str, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue"))

        def _parse_revenue_growth_percent(data: object) -> float | str:
            return cast(float | str, data)

        revenue_growth_percent = _parse_revenue_growth_percent(
            d.pop("revenue_growth_percent")
        )

        revenue_status = d.pop("revenue_status")

        def _parse_recurring_revenue(data: object) -> float | str:
            return cast(float | str, data)

        recurring_revenue = _parse_recurring_revenue(d.pop("recurring_revenue"))

        def _parse_one_time_revenue(data: object) -> float | str:
            return cast(float | str, data)

        one_time_revenue = _parse_one_time_revenue(d.pop("one_time_revenue"))

        def _parse_gross_margin_percent(data: object) -> float | str:
            return cast(float | str, data)

        gross_margin_percent = _parse_gross_margin_percent(
            d.pop("gross_margin_percent")
        )

        def _parse_gross_margin_target(data: object) -> float | str:
            return cast(float | str, data)

        gross_margin_target = _parse_gross_margin_target(d.pop("gross_margin_target"))

        gross_margin_status = d.pop("gross_margin_status")

        margin_trend_direction = d.pop("margin_trend_direction")

        def _parse_outstanding_ar(data: object) -> float | str:
            return cast(float | str, data)

        outstanding_ar = _parse_outstanding_ar(d.pop("outstanding_ar"))

        def _parse_ar_current(data: object) -> float | str:
            return cast(float | str, data)

        ar_current = _parse_ar_current(d.pop("ar_current"))

        def _parse_ar_overdue(data: object) -> float | str:
            return cast(float | str, data)

        ar_overdue = _parse_ar_overdue(d.pop("ar_overdue"))

        def _parse_ar_overdue_30_plus(data: object) -> float | str:
            return cast(float | str, data)

        ar_overdue_30_plus = _parse_ar_overdue_30_plus(d.pop("ar_overdue_30_plus"))

        ar_status = d.pop("ar_status")

        def _parse_ar_at_risk_percent(data: object) -> float | str:
            return cast(float | str, data)

        ar_at_risk_percent = _parse_ar_at_risk_percent(d.pop("ar_at_risk_percent"))

        dso_days = d.pop("dso_days")

        dso_target = d.pop("dso_target")

        dso_status = d.pop("dso_status")

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

        def _parse_dso_industry_benchmark(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dso_industry_benchmark = _parse_dso_industry_benchmark(
            d.pop("dso_industry_benchmark", UNSET)
        )

        financial_kp_is = cls(
            total_revenue=total_revenue,
            revenue_growth_percent=revenue_growth_percent,
            revenue_status=revenue_status,
            recurring_revenue=recurring_revenue,
            one_time_revenue=one_time_revenue,
            gross_margin_percent=gross_margin_percent,
            gross_margin_target=gross_margin_target,
            gross_margin_status=gross_margin_status,
            margin_trend_direction=margin_trend_direction,
            outstanding_ar=outstanding_ar,
            ar_current=ar_current,
            ar_overdue=ar_overdue,
            ar_overdue_30_plus=ar_overdue_30_plus,
            ar_status=ar_status,
            ar_at_risk_percent=ar_at_risk_percent,
            dso_days=dso_days,
            dso_target=dso_target,
            dso_status=dso_status,
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
            dso_industry_benchmark=dso_industry_benchmark,
        )

        financial_kp_is.additional_properties = d
        return financial_kp_is

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
