from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_utilization_item import AnalyticsUtilizationItem
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsResourcesUtilization")


@_attrs_define
class AnalyticsResourcesUtilization:
    """Equipment utilization over the selected period, with an optional previous-period compare.

    Attributes:
        total_booked_hours (float | str):
        total_available_hours (float | str):
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
        overall_utilization_rate (float | None | str | Unset):
        previous_utilization_rate (float | None | str | Unset):
        utilization_change_percent (float | None | str | Unset):
        utilization_trend (str | Unset):  Default: 'neutral'.
        utilization_by_resource (list[AnalyticsUtilizationItem] | Unset):
        utilization_by_category (list[AnalyticsUtilizationItem] | Unset):
    """

    total_booked_hours: float | str
    total_available_hours: float | str
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
    overall_utilization_rate: float | None | str | Unset = UNSET
    previous_utilization_rate: float | None | str | Unset = UNSET
    utilization_change_percent: float | None | str | Unset = UNSET
    utilization_trend: str | Unset = "neutral"
    utilization_by_resource: list[AnalyticsUtilizationItem] | Unset = UNSET
    utilization_by_category: list[AnalyticsUtilizationItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_booked_hours: float | str
        total_booked_hours = self.total_booked_hours

        total_available_hours: float | str
        total_available_hours = self.total_available_hours

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

        overall_utilization_rate: float | None | str | Unset
        if isinstance(self.overall_utilization_rate, Unset):
            overall_utilization_rate = UNSET
        else:
            overall_utilization_rate = self.overall_utilization_rate

        previous_utilization_rate: float | None | str | Unset
        if isinstance(self.previous_utilization_rate, Unset):
            previous_utilization_rate = UNSET
        else:
            previous_utilization_rate = self.previous_utilization_rate

        utilization_change_percent: float | None | str | Unset
        if isinstance(self.utilization_change_percent, Unset):
            utilization_change_percent = UNSET
        else:
            utilization_change_percent = self.utilization_change_percent

        utilization_trend = self.utilization_trend

        utilization_by_resource: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.utilization_by_resource, Unset):
            utilization_by_resource = []
            for utilization_by_resource_item_data in self.utilization_by_resource:
                utilization_by_resource_item = (
                    utilization_by_resource_item_data.to_dict()
                )
                utilization_by_resource.append(utilization_by_resource_item)

        utilization_by_category: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.utilization_by_category, Unset):
            utilization_by_category = []
            for utilization_by_category_item_data in self.utilization_by_category:
                utilization_by_category_item = (
                    utilization_by_category_item_data.to_dict()
                )
                utilization_by_category.append(utilization_by_category_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_booked_hours": total_booked_hours,
                "total_available_hours": total_available_hours,
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
        if overall_utilization_rate is not UNSET:
            field_dict["overall_utilization_rate"] = overall_utilization_rate
        if previous_utilization_rate is not UNSET:
            field_dict["previous_utilization_rate"] = previous_utilization_rate
        if utilization_change_percent is not UNSET:
            field_dict["utilization_change_percent"] = utilization_change_percent
        if utilization_trend is not UNSET:
            field_dict["utilization_trend"] = utilization_trend
        if utilization_by_resource is not UNSET:
            field_dict["utilization_by_resource"] = utilization_by_resource
        if utilization_by_category is not UNSET:
            field_dict["utilization_by_category"] = utilization_by_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_utilization_item import AnalyticsUtilizationItem
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_total_booked_hours(data: object) -> float | str:
            return cast(float | str, data)

        total_booked_hours = _parse_total_booked_hours(d.pop("total_booked_hours"))

        def _parse_total_available_hours(data: object) -> float | str:
            return cast(float | str, data)

        total_available_hours = _parse_total_available_hours(
            d.pop("total_available_hours")
        )

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

        def _parse_overall_utilization_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        overall_utilization_rate = _parse_overall_utilization_rate(
            d.pop("overall_utilization_rate", UNSET)
        )

        def _parse_previous_utilization_rate(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        previous_utilization_rate = _parse_previous_utilization_rate(
            d.pop("previous_utilization_rate", UNSET)
        )

        def _parse_utilization_change_percent(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        utilization_change_percent = _parse_utilization_change_percent(
            d.pop("utilization_change_percent", UNSET)
        )

        utilization_trend = d.pop("utilization_trend", UNSET)

        _utilization_by_resource = d.pop("utilization_by_resource", UNSET)
        utilization_by_resource: list[AnalyticsUtilizationItem] | Unset = UNSET
        if _utilization_by_resource is not UNSET:
            utilization_by_resource = []
            for utilization_by_resource_item_data in _utilization_by_resource:
                utilization_by_resource_item = AnalyticsUtilizationItem.from_dict(
                    utilization_by_resource_item_data
                )

                utilization_by_resource.append(utilization_by_resource_item)

        _utilization_by_category = d.pop("utilization_by_category", UNSET)
        utilization_by_category: list[AnalyticsUtilizationItem] | Unset = UNSET
        if _utilization_by_category is not UNSET:
            utilization_by_category = []
            for utilization_by_category_item_data in _utilization_by_category:
                utilization_by_category_item = AnalyticsUtilizationItem.from_dict(
                    utilization_by_category_item_data
                )

                utilization_by_category.append(utilization_by_category_item)

        analytics_resources_utilization = cls(
            total_booked_hours=total_booked_hours,
            total_available_hours=total_available_hours,
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
            overall_utilization_rate=overall_utilization_rate,
            previous_utilization_rate=previous_utilization_rate,
            utilization_change_percent=utilization_change_percent,
            utilization_trend=utilization_trend,
            utilization_by_resource=utilization_by_resource,
            utilization_by_category=utilization_by_category,
        )

        analytics_resources_utilization.additional_properties = d
        return analytics_resources_utilization

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
