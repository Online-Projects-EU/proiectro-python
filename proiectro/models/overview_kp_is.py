from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="OverviewKPIs")


@_attrs_define
class OverviewKPIs:
    """Executive KPIs for Overview - one metric per business domain.

    Covers all 4 business domains with real database-backed metrics:
    - Customers: Acquisition and growth
    - Sales: Won revenue (closed deals)
    - Delivery: Active project workload
    - Support: Ticket backlog health

    Designed for quick business health assessment with trend indicators.

        Attributes:
            currency (str):
            new_customers (int):
            new_customers_previous (int):
            new_customers_trend (str):
            total_active_customers (int):
            won_revenue (float | str):
            won_revenue_previous (float | str):
            won_revenue_trend (str):
            won_deals_count (int):
            active_projects (int):
            projects_started (int):
            projects_started_previous (int):
            projects_trend (str):
            open_tickets (int):
            tickets_opened (int):
            tickets_closed (int):
            tickets_net_change (int):
            tickets_previous_net (int):
            tickets_trend (str):
            tickets_status (str):
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
            new_customers_change_percent (float | None | str | Unset):
            won_revenue_change_percent (float | None | str | Unset):
            projects_started_change_percent (float | None | str | Unset):
    """

    currency: str
    new_customers: int
    new_customers_previous: int
    new_customers_trend: str
    total_active_customers: int
    won_revenue: float | str
    won_revenue_previous: float | str
    won_revenue_trend: str
    won_deals_count: int
    active_projects: int
    projects_started: int
    projects_started_previous: int
    projects_trend: str
    open_tickets: int
    tickets_opened: int
    tickets_closed: int
    tickets_net_change: int
    tickets_previous_net: int
    tickets_trend: str
    tickets_status: str
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
    new_customers_change_percent: float | None | str | Unset = UNSET
    won_revenue_change_percent: float | None | str | Unset = UNSET
    projects_started_change_percent: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        new_customers = self.new_customers

        new_customers_previous = self.new_customers_previous

        new_customers_trend = self.new_customers_trend

        total_active_customers = self.total_active_customers

        won_revenue: float | str
        won_revenue = self.won_revenue

        won_revenue_previous: float | str
        won_revenue_previous = self.won_revenue_previous

        won_revenue_trend = self.won_revenue_trend

        won_deals_count = self.won_deals_count

        active_projects = self.active_projects

        projects_started = self.projects_started

        projects_started_previous = self.projects_started_previous

        projects_trend = self.projects_trend

        open_tickets = self.open_tickets

        tickets_opened = self.tickets_opened

        tickets_closed = self.tickets_closed

        tickets_net_change = self.tickets_net_change

        tickets_previous_net = self.tickets_previous_net

        tickets_trend = self.tickets_trend

        tickets_status = self.tickets_status

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

        new_customers_change_percent: float | None | str | Unset
        if isinstance(self.new_customers_change_percent, Unset):
            new_customers_change_percent = UNSET
        else:
            new_customers_change_percent = self.new_customers_change_percent

        won_revenue_change_percent: float | None | str | Unset
        if isinstance(self.won_revenue_change_percent, Unset):
            won_revenue_change_percent = UNSET
        else:
            won_revenue_change_percent = self.won_revenue_change_percent

        projects_started_change_percent: float | None | str | Unset
        if isinstance(self.projects_started_change_percent, Unset):
            projects_started_change_percent = UNSET
        else:
            projects_started_change_percent = self.projects_started_change_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "new_customers": new_customers,
                "new_customers_previous": new_customers_previous,
                "new_customers_trend": new_customers_trend,
                "total_active_customers": total_active_customers,
                "won_revenue": won_revenue,
                "won_revenue_previous": won_revenue_previous,
                "won_revenue_trend": won_revenue_trend,
                "won_deals_count": won_deals_count,
                "active_projects": active_projects,
                "projects_started": projects_started,
                "projects_started_previous": projects_started_previous,
                "projects_trend": projects_trend,
                "open_tickets": open_tickets,
                "tickets_opened": tickets_opened,
                "tickets_closed": tickets_closed,
                "tickets_net_change": tickets_net_change,
                "tickets_previous_net": tickets_previous_net,
                "tickets_trend": tickets_trend,
                "tickets_status": tickets_status,
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
        if new_customers_change_percent is not UNSET:
            field_dict["new_customers_change_percent"] = new_customers_change_percent
        if won_revenue_change_percent is not UNSET:
            field_dict["won_revenue_change_percent"] = won_revenue_change_percent
        if projects_started_change_percent is not UNSET:
            field_dict["projects_started_change_percent"] = (
                projects_started_change_percent
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)
        currency = d.pop("currency")

        new_customers = d.pop("new_customers")

        new_customers_previous = d.pop("new_customers_previous")

        new_customers_trend = d.pop("new_customers_trend")

        total_active_customers = d.pop("total_active_customers")

        def _parse_won_revenue(data: object) -> float | str:
            return cast(float | str, data)

        won_revenue = _parse_won_revenue(d.pop("won_revenue"))

        def _parse_won_revenue_previous(data: object) -> float | str:
            return cast(float | str, data)

        won_revenue_previous = _parse_won_revenue_previous(
            d.pop("won_revenue_previous")
        )

        won_revenue_trend = d.pop("won_revenue_trend")

        won_deals_count = d.pop("won_deals_count")

        active_projects = d.pop("active_projects")

        projects_started = d.pop("projects_started")

        projects_started_previous = d.pop("projects_started_previous")

        projects_trend = d.pop("projects_trend")

        open_tickets = d.pop("open_tickets")

        tickets_opened = d.pop("tickets_opened")

        tickets_closed = d.pop("tickets_closed")

        tickets_net_change = d.pop("tickets_net_change")

        tickets_previous_net = d.pop("tickets_previous_net")

        tickets_trend = d.pop("tickets_trend")

        tickets_status = d.pop("tickets_status")

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

        def _parse_new_customers_change_percent(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        new_customers_change_percent = _parse_new_customers_change_percent(
            d.pop("new_customers_change_percent", UNSET)
        )

        def _parse_won_revenue_change_percent(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        won_revenue_change_percent = _parse_won_revenue_change_percent(
            d.pop("won_revenue_change_percent", UNSET)
        )

        def _parse_projects_started_change_percent(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        projects_started_change_percent = _parse_projects_started_change_percent(
            d.pop("projects_started_change_percent", UNSET)
        )

        overview_kp_is = cls(
            currency=currency,
            new_customers=new_customers,
            new_customers_previous=new_customers_previous,
            new_customers_trend=new_customers_trend,
            total_active_customers=total_active_customers,
            won_revenue=won_revenue,
            won_revenue_previous=won_revenue_previous,
            won_revenue_trend=won_revenue_trend,
            won_deals_count=won_deals_count,
            active_projects=active_projects,
            projects_started=projects_started,
            projects_started_previous=projects_started_previous,
            projects_trend=projects_trend,
            open_tickets=open_tickets,
            tickets_opened=tickets_opened,
            tickets_closed=tickets_closed,
            tickets_net_change=tickets_net_change,
            tickets_previous_net=tickets_previous_net,
            tickets_trend=tickets_trend,
            tickets_status=tickets_status,
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
            new_customers_change_percent=new_customers_change_percent,
            won_revenue_change_percent=won_revenue_change_percent,
            projects_started_change_percent=projects_started_change_percent,
        )

        overview_kp_is.additional_properties = d
        return overview_kp_is

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
