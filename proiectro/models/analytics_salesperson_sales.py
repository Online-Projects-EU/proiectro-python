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
    from ..models.sales_series_point import SalesSeriesPoint
    from ..models.salesperson_sale_row import SalespersonSaleRow
    from ..models.target_attainment_entry import TargetAttainmentEntry


T = TypeVar("T", bound="AnalyticsSalespersonSales")


@_attrs_define
class AnalyticsSalespersonSales:
    """One salesperson's won deals for a period, with the same KPIs the dashboard shows.

    Attributes:
        member_id (str):
        member_name (str):
        deals_won (int):
        deals_lost (int):
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
        avatar_url (None | str | Unset):
        is_self (bool | Unset):  Default: False.
        total_revenue (float | None | str | Unset):
        win_rate (float | None | str | Unset):
        avg_deal_size (float | None | str | Unset):
        prev_revenue (float | None | str | Unset):
        revenue_change_pct (float | None | str | Unset): A percentage, or "new" when the prior period had nothing to
            compare against.
        rows (list[SalespersonSaleRow] | Unset):
        uncovered_currencies (list[str] | Unset):
        series (list[SalesSeriesPoint] | Unset):
        series_previous (list[SalesSeriesPoint] | Unset):
        window_start (datetime.date | None | Unset):
        window_end (datetime.date | None | Unset):
        previous_start (datetime.date | None | Unset):
        previous_end (datetime.date | None | Unset):
        attainment (list[TargetAttainmentEntry] | Unset):
    """

    member_id: str
    member_name: str
    deals_won: int
    deals_lost: int
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
    avatar_url: None | str | Unset = UNSET
    is_self: bool | Unset = False
    total_revenue: float | None | str | Unset = UNSET
    win_rate: float | None | str | Unset = UNSET
    avg_deal_size: float | None | str | Unset = UNSET
    prev_revenue: float | None | str | Unset = UNSET
    revenue_change_pct: float | None | str | Unset = UNSET
    rows: list[SalespersonSaleRow] | Unset = UNSET
    uncovered_currencies: list[str] | Unset = UNSET
    series: list[SalesSeriesPoint] | Unset = UNSET
    series_previous: list[SalesSeriesPoint] | Unset = UNSET
    window_start: datetime.date | None | Unset = UNSET
    window_end: datetime.date | None | Unset = UNSET
    previous_start: datetime.date | None | Unset = UNSET
    previous_end: datetime.date | None | Unset = UNSET
    attainment: list[TargetAttainmentEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_id = self.member_id

        member_name = self.member_name

        deals_won = self.deals_won

        deals_lost = self.deals_lost

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

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        is_self = self.is_self

        total_revenue: float | None | str | Unset
        if isinstance(self.total_revenue, Unset):
            total_revenue = UNSET
        else:
            total_revenue = self.total_revenue

        win_rate: float | None | str | Unset
        if isinstance(self.win_rate, Unset):
            win_rate = UNSET
        else:
            win_rate = self.win_rate

        avg_deal_size: float | None | str | Unset
        if isinstance(self.avg_deal_size, Unset):
            avg_deal_size = UNSET
        else:
            avg_deal_size = self.avg_deal_size

        prev_revenue: float | None | str | Unset
        if isinstance(self.prev_revenue, Unset):
            prev_revenue = UNSET
        else:
            prev_revenue = self.prev_revenue

        revenue_change_pct: float | None | str | Unset
        if isinstance(self.revenue_change_pct, Unset):
            revenue_change_pct = UNSET
        else:
            revenue_change_pct = self.revenue_change_pct

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        uncovered_currencies: list[str] | Unset = UNSET
        if not isinstance(self.uncovered_currencies, Unset):
            uncovered_currencies = self.uncovered_currencies

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        series_previous: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series_previous, Unset):
            series_previous = []
            for series_previous_item_data in self.series_previous:
                series_previous_item = series_previous_item_data.to_dict()
                series_previous.append(series_previous_item)

        window_start: None | str | Unset
        if isinstance(self.window_start, Unset):
            window_start = UNSET
        elif isinstance(self.window_start, datetime.date):
            window_start = self.window_start.isoformat()
        else:
            window_start = self.window_start

        window_end: None | str | Unset
        if isinstance(self.window_end, Unset):
            window_end = UNSET
        elif isinstance(self.window_end, datetime.date):
            window_end = self.window_end.isoformat()
        else:
            window_end = self.window_end

        previous_start: None | str | Unset
        if isinstance(self.previous_start, Unset):
            previous_start = UNSET
        elif isinstance(self.previous_start, datetime.date):
            previous_start = self.previous_start.isoformat()
        else:
            previous_start = self.previous_start

        previous_end: None | str | Unset
        if isinstance(self.previous_end, Unset):
            previous_end = UNSET
        elif isinstance(self.previous_end, datetime.date):
            previous_end = self.previous_end.isoformat()
        else:
            previous_end = self.previous_end

        attainment: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attainment, Unset):
            attainment = []
            for attainment_item_data in self.attainment:
                attainment_item = attainment_item_data.to_dict()
                attainment.append(attainment_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member_id": member_id,
                "member_name": member_name,
                "deals_won": deals_won,
                "deals_lost": deals_lost,
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
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if is_self is not UNSET:
            field_dict["is_self"] = is_self
        if total_revenue is not UNSET:
            field_dict["total_revenue"] = total_revenue
        if win_rate is not UNSET:
            field_dict["win_rate"] = win_rate
        if avg_deal_size is not UNSET:
            field_dict["avg_deal_size"] = avg_deal_size
        if prev_revenue is not UNSET:
            field_dict["prev_revenue"] = prev_revenue
        if revenue_change_pct is not UNSET:
            field_dict["revenue_change_pct"] = revenue_change_pct
        if rows is not UNSET:
            field_dict["rows"] = rows
        if uncovered_currencies is not UNSET:
            field_dict["uncovered_currencies"] = uncovered_currencies
        if series is not UNSET:
            field_dict["series"] = series
        if series_previous is not UNSET:
            field_dict["series_previous"] = series_previous
        if window_start is not UNSET:
            field_dict["window_start"] = window_start
        if window_end is not UNSET:
            field_dict["window_end"] = window_end
        if previous_start is not UNSET:
            field_dict["previous_start"] = previous_start
        if previous_end is not UNSET:
            field_dict["previous_end"] = previous_end
        if attainment is not UNSET:
            field_dict["attainment"] = attainment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption
        from ..models.sales_series_point import SalesSeriesPoint
        from ..models.salesperson_sale_row import SalespersonSaleRow
        from ..models.target_attainment_entry import TargetAttainmentEntry

        d = dict(src_dict)
        member_id = d.pop("member_id")

        member_name = d.pop("member_name")

        deals_won = d.pop("deals_won")

        deals_lost = d.pop("deals_lost")

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

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        is_self = d.pop("is_self", UNSET)

        def _parse_total_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue", UNSET))

        def _parse_win_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        win_rate = _parse_win_rate(d.pop("win_rate", UNSET))

        def _parse_avg_deal_size(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        avg_deal_size = _parse_avg_deal_size(d.pop("avg_deal_size", UNSET))

        def _parse_prev_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_revenue = _parse_prev_revenue(d.pop("prev_revenue", UNSET))

        def _parse_revenue_change_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        revenue_change_pct = _parse_revenue_change_pct(
            d.pop("revenue_change_pct", UNSET)
        )

        _rows = d.pop("rows", UNSET)
        rows: list[SalespersonSaleRow] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = SalespersonSaleRow.from_dict(rows_item_data)

                rows.append(rows_item)

        uncovered_currencies = cast(list[str], d.pop("uncovered_currencies", UNSET))

        _series = d.pop("series", UNSET)
        series: list[SalesSeriesPoint] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = SalesSeriesPoint.from_dict(series_item_data)

                series.append(series_item)

        _series_previous = d.pop("series_previous", UNSET)
        series_previous: list[SalesSeriesPoint] | Unset = UNSET
        if _series_previous is not UNSET:
            series_previous = []
            for series_previous_item_data in _series_previous:
                series_previous_item = SalesSeriesPoint.from_dict(
                    series_previous_item_data
                )

                series_previous.append(series_previous_item)

        def _parse_window_start(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_start_type_0 = isoparse(data).date()

                return window_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        window_start = _parse_window_start(d.pop("window_start", UNSET))

        def _parse_window_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_end_type_0 = isoparse(data).date()

                return window_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        window_end = _parse_window_end(d.pop("window_end", UNSET))

        def _parse_previous_start(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_start_type_0 = isoparse(data).date()

                return previous_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        previous_start = _parse_previous_start(d.pop("previous_start", UNSET))

        def _parse_previous_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_end_type_0 = isoparse(data).date()

                return previous_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        previous_end = _parse_previous_end(d.pop("previous_end", UNSET))

        _attainment = d.pop("attainment", UNSET)
        attainment: list[TargetAttainmentEntry] | Unset = UNSET
        if _attainment is not UNSET:
            attainment = []
            for attainment_item_data in _attainment:
                attainment_item = TargetAttainmentEntry.from_dict(attainment_item_data)

                attainment.append(attainment_item)

        analytics_salesperson_sales = cls(
            member_id=member_id,
            member_name=member_name,
            deals_won=deals_won,
            deals_lost=deals_lost,
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
            avatar_url=avatar_url,
            is_self=is_self,
            total_revenue=total_revenue,
            win_rate=win_rate,
            avg_deal_size=avg_deal_size,
            prev_revenue=prev_revenue,
            revenue_change_pct=revenue_change_pct,
            rows=rows,
            uncovered_currencies=uncovered_currencies,
            series=series,
            series_previous=series_previous,
            window_start=window_start,
            window_end=window_end,
            previous_start=previous_start,
            previous_end=previous_end,
            attainment=attainment,
        )

        analytics_salesperson_sales.additional_properties = d
        return analytics_salesperson_sales

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
