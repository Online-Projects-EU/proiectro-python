from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

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
            revenue_status (str):
            gross_margin_target (float | str):
            gross_margin_status (str):
            margin_trend_direction (str):
            ar_status (str):
            dso_target (int):
            dso_status (str):
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
            uncovered_currencies (list[str] | Unset):
            total_revenue (float | None | str | Unset):
            revenue_growth_percent (float | None | str | Unset): A percentage, or "new" when the prior period had nothing to
                compare against.
            recurring_revenue (float | None | str | Unset):
            one_time_revenue (float | None | str | Unset):
            gross_margin_percent (float | None | str | Unset):
            outstanding_ar (float | None | str | Unset):
            ar_current (float | None | str | Unset):
            ar_overdue (float | None | str | Unset):
            ar_overdue_30_plus (float | None | str | Unset):
            ar_nothing_outstanding (bool | Unset):  Default: False.
            ar_at_risk_percent (float | None | str | Unset):
            dso_days (int | None | Unset):
            dso_industry_benchmark (int | None | Unset):
    """

    revenue_status: str
    gross_margin_target: float | str
    gross_margin_status: str
    margin_trend_direction: str
    ar_status: str
    dso_target: int
    dso_status: str
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
    uncovered_currencies: list[str] | Unset = UNSET
    total_revenue: float | None | str | Unset = UNSET
    revenue_growth_percent: float | None | str | Unset = UNSET
    recurring_revenue: float | None | str | Unset = UNSET
    one_time_revenue: float | None | str | Unset = UNSET
    gross_margin_percent: float | None | str | Unset = UNSET
    outstanding_ar: float | None | str | Unset = UNSET
    ar_current: float | None | str | Unset = UNSET
    ar_overdue: float | None | str | Unset = UNSET
    ar_overdue_30_plus: float | None | str | Unset = UNSET
    ar_nothing_outstanding: bool | Unset = False
    ar_at_risk_percent: float | None | str | Unset = UNSET
    dso_days: int | None | Unset = UNSET
    dso_industry_benchmark: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revenue_status = self.revenue_status

        gross_margin_target: float | str
        gross_margin_target = self.gross_margin_target

        gross_margin_status = self.gross_margin_status

        margin_trend_direction = self.margin_trend_direction

        ar_status = self.ar_status

        dso_target = self.dso_target

        dso_status = self.dso_status

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

        uncovered_currencies: list[str] | Unset = UNSET
        if not isinstance(self.uncovered_currencies, Unset):
            uncovered_currencies = self.uncovered_currencies

        total_revenue: float | None | str | Unset
        if isinstance(self.total_revenue, Unset):
            total_revenue = UNSET
        else:
            total_revenue = self.total_revenue

        revenue_growth_percent: float | None | str | Unset
        if isinstance(self.revenue_growth_percent, Unset):
            revenue_growth_percent = UNSET
        else:
            revenue_growth_percent = self.revenue_growth_percent

        recurring_revenue: float | None | str | Unset
        if isinstance(self.recurring_revenue, Unset):
            recurring_revenue = UNSET
        else:
            recurring_revenue = self.recurring_revenue

        one_time_revenue: float | None | str | Unset
        if isinstance(self.one_time_revenue, Unset):
            one_time_revenue = UNSET
        else:
            one_time_revenue = self.one_time_revenue

        gross_margin_percent: float | None | str | Unset
        if isinstance(self.gross_margin_percent, Unset):
            gross_margin_percent = UNSET
        else:
            gross_margin_percent = self.gross_margin_percent

        outstanding_ar: float | None | str | Unset
        if isinstance(self.outstanding_ar, Unset):
            outstanding_ar = UNSET
        else:
            outstanding_ar = self.outstanding_ar

        ar_current: float | None | str | Unset
        if isinstance(self.ar_current, Unset):
            ar_current = UNSET
        else:
            ar_current = self.ar_current

        ar_overdue: float | None | str | Unset
        if isinstance(self.ar_overdue, Unset):
            ar_overdue = UNSET
        else:
            ar_overdue = self.ar_overdue

        ar_overdue_30_plus: float | None | str | Unset
        if isinstance(self.ar_overdue_30_plus, Unset):
            ar_overdue_30_plus = UNSET
        else:
            ar_overdue_30_plus = self.ar_overdue_30_plus

        ar_nothing_outstanding = self.ar_nothing_outstanding

        ar_at_risk_percent: float | None | str | Unset
        if isinstance(self.ar_at_risk_percent, Unset):
            ar_at_risk_percent = UNSET
        else:
            ar_at_risk_percent = self.ar_at_risk_percent

        dso_days: int | None | Unset
        if isinstance(self.dso_days, Unset):
            dso_days = UNSET
        else:
            dso_days = self.dso_days

        dso_industry_benchmark: int | None | Unset
        if isinstance(self.dso_industry_benchmark, Unset):
            dso_industry_benchmark = UNSET
        else:
            dso_industry_benchmark = self.dso_industry_benchmark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revenue_status": revenue_status,
                "gross_margin_target": gross_margin_target,
                "gross_margin_status": gross_margin_status,
                "margin_trend_direction": margin_trend_direction,
                "ar_status": ar_status,
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
        if uncovered_currencies is not UNSET:
            field_dict["uncovered_currencies"] = uncovered_currencies
        if total_revenue is not UNSET:
            field_dict["total_revenue"] = total_revenue
        if revenue_growth_percent is not UNSET:
            field_dict["revenue_growth_percent"] = revenue_growth_percent
        if recurring_revenue is not UNSET:
            field_dict["recurring_revenue"] = recurring_revenue
        if one_time_revenue is not UNSET:
            field_dict["one_time_revenue"] = one_time_revenue
        if gross_margin_percent is not UNSET:
            field_dict["gross_margin_percent"] = gross_margin_percent
        if outstanding_ar is not UNSET:
            field_dict["outstanding_ar"] = outstanding_ar
        if ar_current is not UNSET:
            field_dict["ar_current"] = ar_current
        if ar_overdue is not UNSET:
            field_dict["ar_overdue"] = ar_overdue
        if ar_overdue_30_plus is not UNSET:
            field_dict["ar_overdue_30_plus"] = ar_overdue_30_plus
        if ar_nothing_outstanding is not UNSET:
            field_dict["ar_nothing_outstanding"] = ar_nothing_outstanding
        if ar_at_risk_percent is not UNSET:
            field_dict["ar_at_risk_percent"] = ar_at_risk_percent
        if dso_days is not UNSET:
            field_dict["dso_days"] = dso_days
        if dso_industry_benchmark is not UNSET:
            field_dict["dso_industry_benchmark"] = dso_industry_benchmark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)
        revenue_status = d.pop("revenue_status")

        def _parse_gross_margin_target(data: object) -> float | str:
            return cast(float | str, data)

        gross_margin_target = _parse_gross_margin_target(d.pop("gross_margin_target"))

        gross_margin_status = d.pop("gross_margin_status")

        margin_trend_direction = d.pop("margin_trend_direction")

        ar_status = d.pop("ar_status")

        dso_target = d.pop("dso_target")

        dso_status = d.pop("dso_status")

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

        uncovered_currencies = cast(list[str], d.pop("uncovered_currencies", UNSET))

        def _parse_total_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue", UNSET))

        def _parse_revenue_growth_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        revenue_growth_percent = _parse_revenue_growth_percent(
            d.pop("revenue_growth_percent", UNSET)
        )

        def _parse_recurring_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        recurring_revenue = _parse_recurring_revenue(d.pop("recurring_revenue", UNSET))

        def _parse_one_time_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        one_time_revenue = _parse_one_time_revenue(d.pop("one_time_revenue", UNSET))

        def _parse_gross_margin_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        gross_margin_percent = _parse_gross_margin_percent(
            d.pop("gross_margin_percent", UNSET)
        )

        def _parse_outstanding_ar(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        outstanding_ar = _parse_outstanding_ar(d.pop("outstanding_ar", UNSET))

        def _parse_ar_current(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        ar_current = _parse_ar_current(d.pop("ar_current", UNSET))

        def _parse_ar_overdue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        ar_overdue = _parse_ar_overdue(d.pop("ar_overdue", UNSET))

        def _parse_ar_overdue_30_plus(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        ar_overdue_30_plus = _parse_ar_overdue_30_plus(
            d.pop("ar_overdue_30_plus", UNSET)
        )

        ar_nothing_outstanding = d.pop("ar_nothing_outstanding", UNSET)

        def _parse_ar_at_risk_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        ar_at_risk_percent = _parse_ar_at_risk_percent(
            d.pop("ar_at_risk_percent", UNSET)
        )

        def _parse_dso_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dso_days = _parse_dso_days(d.pop("dso_days", UNSET))

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
            revenue_status=revenue_status,
            gross_margin_target=gross_margin_target,
            gross_margin_status=gross_margin_status,
            margin_trend_direction=margin_trend_direction,
            ar_status=ar_status,
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
            uncovered_currencies=uncovered_currencies,
            total_revenue=total_revenue,
            revenue_growth_percent=revenue_growth_percent,
            recurring_revenue=recurring_revenue,
            one_time_revenue=one_time_revenue,
            gross_margin_percent=gross_margin_percent,
            outstanding_ar=outstanding_ar,
            ar_current=ar_current,
            ar_overdue=ar_overdue,
            ar_overdue_30_plus=ar_overdue_30_plus,
            ar_nothing_outstanding=ar_nothing_outstanding,
            ar_at_risk_percent=ar_at_risk_percent,
            dso_days=dso_days,
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
