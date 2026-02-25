from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="SalesKPIs")


@_attrs_define
class SalesKPIs:
    """Sales KPIs - Pipeline health and deal flow status.

    Shows 4 key metrics:
    1. Win Rate - effectiveness of converting deals
    2. Average Deal Size - quality indicator
    3. Sales Velocity - compound metric of pipeline health
    4. Revenue Won - bottom-line result for the period

    Plus supporting pipeline and deal breakdown data.

        Attributes:
            win_rate_percent (float | str):
            win_rate_benchmark (float | str):
            win_rate_status (str):
            deals_won_period (int):
            deals_lost_period (int):
            avg_deal_size (float | str):
            avg_deal_size_status (str):
            largest_deal_value (float | str):
            smallest_deal_value (float | str):
            sales_velocity (float | str):
            sales_velocity_status (str):
            avg_sales_cycle_days (int):
            revenue_won_period (float | str):
            revenue_won_previous (float | str):
            revenue_won_trend (str):
            pipeline_total_value (float | str):
            pipeline_weighted_value (float | str):
            pipeline_status (str):
            deals_in_discovery (int):
            deals_in_proposal (int):
            deals_in_negotiation (int):
            deals_closing_soon (int):
            total_active_deals (int):
            new_deals_this_period (int):
            stalled_deals (int):
            deals_status (str):
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
    """

    win_rate_percent: float | str
    win_rate_benchmark: float | str
    win_rate_status: str
    deals_won_period: int
    deals_lost_period: int
    avg_deal_size: float | str
    avg_deal_size_status: str
    largest_deal_value: float | str
    smallest_deal_value: float | str
    sales_velocity: float | str
    sales_velocity_status: str
    avg_sales_cycle_days: int
    revenue_won_period: float | str
    revenue_won_previous: float | str
    revenue_won_trend: str
    pipeline_total_value: float | str
    pipeline_weighted_value: float | str
    pipeline_status: str
    deals_in_discovery: int
    deals_in_proposal: int
    deals_in_negotiation: int
    deals_closing_soon: int
    total_active_deals: int
    new_deals_this_period: int
    stalled_deals: int
    deals_status: str
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        win_rate_percent: float | str
        win_rate_percent = self.win_rate_percent

        win_rate_benchmark: float | str
        win_rate_benchmark = self.win_rate_benchmark

        win_rate_status = self.win_rate_status

        deals_won_period = self.deals_won_period

        deals_lost_period = self.deals_lost_period

        avg_deal_size: float | str
        avg_deal_size = self.avg_deal_size

        avg_deal_size_status = self.avg_deal_size_status

        largest_deal_value: float | str
        largest_deal_value = self.largest_deal_value

        smallest_deal_value: float | str
        smallest_deal_value = self.smallest_deal_value

        sales_velocity: float | str
        sales_velocity = self.sales_velocity

        sales_velocity_status = self.sales_velocity_status

        avg_sales_cycle_days = self.avg_sales_cycle_days

        revenue_won_period: float | str
        revenue_won_period = self.revenue_won_period

        revenue_won_previous: float | str
        revenue_won_previous = self.revenue_won_previous

        revenue_won_trend = self.revenue_won_trend

        pipeline_total_value: float | str
        pipeline_total_value = self.pipeline_total_value

        pipeline_weighted_value: float | str
        pipeline_weighted_value = self.pipeline_weighted_value

        pipeline_status = self.pipeline_status

        deals_in_discovery = self.deals_in_discovery

        deals_in_proposal = self.deals_in_proposal

        deals_in_negotiation = self.deals_in_negotiation

        deals_closing_soon = self.deals_closing_soon

        total_active_deals = self.total_active_deals

        new_deals_this_period = self.new_deals_this_period

        stalled_deals = self.stalled_deals

        deals_status = self.deals_status

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "win_rate_percent": win_rate_percent,
                "win_rate_benchmark": win_rate_benchmark,
                "win_rate_status": win_rate_status,
                "deals_won_period": deals_won_period,
                "deals_lost_period": deals_lost_period,
                "avg_deal_size": avg_deal_size,
                "avg_deal_size_status": avg_deal_size_status,
                "largest_deal_value": largest_deal_value,
                "smallest_deal_value": smallest_deal_value,
                "sales_velocity": sales_velocity,
                "sales_velocity_status": sales_velocity_status,
                "avg_sales_cycle_days": avg_sales_cycle_days,
                "revenue_won_period": revenue_won_period,
                "revenue_won_previous": revenue_won_previous,
                "revenue_won_trend": revenue_won_trend,
                "pipeline_total_value": pipeline_total_value,
                "pipeline_weighted_value": pipeline_weighted_value,
                "pipeline_status": pipeline_status,
                "deals_in_discovery": deals_in_discovery,
                "deals_in_proposal": deals_in_proposal,
                "deals_in_negotiation": deals_in_negotiation,
                "deals_closing_soon": deals_closing_soon,
                "total_active_deals": total_active_deals,
                "new_deals_this_period": new_deals_this_period,
                "stalled_deals": stalled_deals,
                "deals_status": deals_status,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_win_rate_percent(data: object) -> float | str:
            return cast(float | str, data)

        win_rate_percent = _parse_win_rate_percent(d.pop("win_rate_percent"))

        def _parse_win_rate_benchmark(data: object) -> float | str:
            return cast(float | str, data)

        win_rate_benchmark = _parse_win_rate_benchmark(d.pop("win_rate_benchmark"))

        win_rate_status = d.pop("win_rate_status")

        deals_won_period = d.pop("deals_won_period")

        deals_lost_period = d.pop("deals_lost_period")

        def _parse_avg_deal_size(data: object) -> float | str:
            return cast(float | str, data)

        avg_deal_size = _parse_avg_deal_size(d.pop("avg_deal_size"))

        avg_deal_size_status = d.pop("avg_deal_size_status")

        def _parse_largest_deal_value(data: object) -> float | str:
            return cast(float | str, data)

        largest_deal_value = _parse_largest_deal_value(d.pop("largest_deal_value"))

        def _parse_smallest_deal_value(data: object) -> float | str:
            return cast(float | str, data)

        smallest_deal_value = _parse_smallest_deal_value(d.pop("smallest_deal_value"))

        def _parse_sales_velocity(data: object) -> float | str:
            return cast(float | str, data)

        sales_velocity = _parse_sales_velocity(d.pop("sales_velocity"))

        sales_velocity_status = d.pop("sales_velocity_status")

        avg_sales_cycle_days = d.pop("avg_sales_cycle_days")

        def _parse_revenue_won_period(data: object) -> float | str:
            return cast(float | str, data)

        revenue_won_period = _parse_revenue_won_period(d.pop("revenue_won_period"))

        def _parse_revenue_won_previous(data: object) -> float | str:
            return cast(float | str, data)

        revenue_won_previous = _parse_revenue_won_previous(
            d.pop("revenue_won_previous")
        )

        revenue_won_trend = d.pop("revenue_won_trend")

        def _parse_pipeline_total_value(data: object) -> float | str:
            return cast(float | str, data)

        pipeline_total_value = _parse_pipeline_total_value(
            d.pop("pipeline_total_value")
        )

        def _parse_pipeline_weighted_value(data: object) -> float | str:
            return cast(float | str, data)

        pipeline_weighted_value = _parse_pipeline_weighted_value(
            d.pop("pipeline_weighted_value")
        )

        pipeline_status = d.pop("pipeline_status")

        deals_in_discovery = d.pop("deals_in_discovery")

        deals_in_proposal = d.pop("deals_in_proposal")

        deals_in_negotiation = d.pop("deals_in_negotiation")

        deals_closing_soon = d.pop("deals_closing_soon")

        total_active_deals = d.pop("total_active_deals")

        new_deals_this_period = d.pop("new_deals_this_period")

        stalled_deals = d.pop("stalled_deals")

        deals_status = d.pop("deals_status")

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

        sales_kp_is = cls(
            win_rate_percent=win_rate_percent,
            win_rate_benchmark=win_rate_benchmark,
            win_rate_status=win_rate_status,
            deals_won_period=deals_won_period,
            deals_lost_period=deals_lost_period,
            avg_deal_size=avg_deal_size,
            avg_deal_size_status=avg_deal_size_status,
            largest_deal_value=largest_deal_value,
            smallest_deal_value=smallest_deal_value,
            sales_velocity=sales_velocity,
            sales_velocity_status=sales_velocity_status,
            avg_sales_cycle_days=avg_sales_cycle_days,
            revenue_won_period=revenue_won_period,
            revenue_won_previous=revenue_won_previous,
            revenue_won_trend=revenue_won_trend,
            pipeline_total_value=pipeline_total_value,
            pipeline_weighted_value=pipeline_weighted_value,
            pipeline_status=pipeline_status,
            deals_in_discovery=deals_in_discovery,
            deals_in_proposal=deals_in_proposal,
            deals_in_negotiation=deals_in_negotiation,
            deals_closing_soon=deals_closing_soon,
            total_active_deals=total_active_deals,
            new_deals_this_period=new_deals_this_period,
            stalled_deals=stalled_deals,
            deals_status=deals_status,
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
        )

        sales_kp_is.additional_properties = d
        return sales_kp_is

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
