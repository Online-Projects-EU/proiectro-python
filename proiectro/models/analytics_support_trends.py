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
    from ..models.analytics_issue_type_item import AnalyticsIssueTypeItem
    from ..models.analytics_trend_month_item import AnalyticsTrendMonthItem
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsSupportTrends")


@_attrs_define
class AnalyticsSupportTrends:
    """Support trend analysis

    Attributes:
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
        monthly_trend (list[AnalyticsTrendMonthItem] | Unset):
        top_issue_types (list[AnalyticsIssueTypeItem] | Unset):
        total_created (int | Unset):  Default: 0.
        total_closed (int | Unset):  Default: 0.
        prev_total_created (int | None | Unset):
        prev_total_closed (int | None | Unset):
        created_change_pct (float | Literal['new'] | None | Unset):
        closed_change_pct (float | Literal['new'] | None | Unset):
    """

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
    monthly_trend: list[AnalyticsTrendMonthItem] | Unset = UNSET
    top_issue_types: list[AnalyticsIssueTypeItem] | Unset = UNSET
    total_created: int | Unset = 0
    total_closed: int | Unset = 0
    prev_total_created: int | None | Unset = UNSET
    prev_total_closed: int | None | Unset = UNSET
    created_change_pct: float | Literal["new"] | None | Unset = UNSET
    closed_change_pct: float | Literal["new"] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        monthly_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monthly_trend, Unset):
            monthly_trend = []
            for monthly_trend_item_data in self.monthly_trend:
                monthly_trend_item = monthly_trend_item_data.to_dict()
                monthly_trend.append(monthly_trend_item)

        top_issue_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_issue_types, Unset):
            top_issue_types = []
            for top_issue_types_item_data in self.top_issue_types:
                top_issue_types_item = top_issue_types_item_data.to_dict()
                top_issue_types.append(top_issue_types_item)

        total_created = self.total_created

        total_closed = self.total_closed

        prev_total_created: int | None | Unset
        if isinstance(self.prev_total_created, Unset):
            prev_total_created = UNSET
        else:
            prev_total_created = self.prev_total_created

        prev_total_closed: int | None | Unset
        if isinstance(self.prev_total_closed, Unset):
            prev_total_closed = UNSET
        else:
            prev_total_closed = self.prev_total_closed

        created_change_pct: float | Literal["new"] | None | Unset
        if isinstance(self.created_change_pct, Unset):
            created_change_pct = UNSET
        else:
            created_change_pct = self.created_change_pct

        closed_change_pct: float | Literal["new"] | None | Unset
        if isinstance(self.closed_change_pct, Unset):
            closed_change_pct = UNSET
        else:
            closed_change_pct = self.closed_change_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if monthly_trend is not UNSET:
            field_dict["monthly_trend"] = monthly_trend
        if top_issue_types is not UNSET:
            field_dict["top_issue_types"] = top_issue_types
        if total_created is not UNSET:
            field_dict["total_created"] = total_created
        if total_closed is not UNSET:
            field_dict["total_closed"] = total_closed
        if prev_total_created is not UNSET:
            field_dict["prev_total_created"] = prev_total_created
        if prev_total_closed is not UNSET:
            field_dict["prev_total_closed"] = prev_total_closed
        if created_change_pct is not UNSET:
            field_dict["created_change_pct"] = created_change_pct
        if closed_change_pct is not UNSET:
            field_dict["closed_change_pct"] = closed_change_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_issue_type_item import AnalyticsIssueTypeItem
        from ..models.analytics_trend_month_item import AnalyticsTrendMonthItem
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)
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

        _monthly_trend = d.pop("monthly_trend", UNSET)
        monthly_trend: list[AnalyticsTrendMonthItem] | Unset = UNSET
        if _monthly_trend is not UNSET:
            monthly_trend = []
            for monthly_trend_item_data in _monthly_trend:
                monthly_trend_item = AnalyticsTrendMonthItem.from_dict(
                    monthly_trend_item_data
                )

                monthly_trend.append(monthly_trend_item)

        _top_issue_types = d.pop("top_issue_types", UNSET)
        top_issue_types: list[AnalyticsIssueTypeItem] | Unset = UNSET
        if _top_issue_types is not UNSET:
            top_issue_types = []
            for top_issue_types_item_data in _top_issue_types:
                top_issue_types_item = AnalyticsIssueTypeItem.from_dict(
                    top_issue_types_item_data
                )

                top_issue_types.append(top_issue_types_item)

        total_created = d.pop("total_created", UNSET)

        total_closed = d.pop("total_closed", UNSET)

        def _parse_prev_total_created(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prev_total_created = _parse_prev_total_created(
            d.pop("prev_total_created", UNSET)
        )

        def _parse_prev_total_closed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prev_total_closed = _parse_prev_total_closed(d.pop("prev_total_closed", UNSET))

        def _parse_created_change_pct(
            data: object,
        ) -> float | Literal["new"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            created_change_pct_type_1 = cast(Literal["new"], data)
            if created_change_pct_type_1 != "new":
                raise ValueError(
                    f"created_change_pct_type_1 must match const 'new', got '{created_change_pct_type_1}'"
                )
            return created_change_pct_type_1
            return cast(float | Literal["new"] | None | Unset, data)

        created_change_pct = _parse_created_change_pct(
            d.pop("created_change_pct", UNSET)
        )

        def _parse_closed_change_pct(
            data: object,
        ) -> float | Literal["new"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            closed_change_pct_type_1 = cast(Literal["new"], data)
            if closed_change_pct_type_1 != "new":
                raise ValueError(
                    f"closed_change_pct_type_1 must match const 'new', got '{closed_change_pct_type_1}'"
                )
            return closed_change_pct_type_1
            return cast(float | Literal["new"] | None | Unset, data)

        closed_change_pct = _parse_closed_change_pct(d.pop("closed_change_pct", UNSET))

        analytics_support_trends = cls(
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
            monthly_trend=monthly_trend,
            top_issue_types=top_issue_types,
            total_created=total_created,
            total_closed=total_closed,
            prev_total_created=prev_total_created,
            prev_total_closed=prev_total_closed,
            created_change_pct=created_change_pct,
            closed_change_pct=closed_change_pct,
        )

        analytics_support_trends.additional_properties = d
        return analytics_support_trends

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
