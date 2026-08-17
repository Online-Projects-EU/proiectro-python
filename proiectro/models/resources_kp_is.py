from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.compare_option import CompareOption
  from ..models.horizon_option import HorizonOption





T = TypeVar("T", bound="ResourcesKPIs")



@_attrs_define
class ResourcesKPIs:
    """ Resources KPIs - equipment utilization and capacity health over the next `horizon_days`.

    "Resource" is the Resource model: equipment, vehicles, rooms. Every figure comes from
    ResourceBooking measured against each resource's weekly Availability.

    Billable/non-billable percentages and the skills-gap counts are GONE: the product models
    neither (WorkLog has no billable flag, and there is no Skill model), so they could only ever
    have been invented — which is exactly what the old implementation did.

        Attributes:
            horizon_days (int):
            utilization_percent (float | str):
            utilization_target_low (float | str):
            utilization_target_high (float | str):
            utilization_target_band (float | str):
            utilization_status (str):
            total_capacity_hours (float | str):
            allocated_hours (float | str):
            available_hours (float | str):
            capacity_status (str):
            weeks_of_capacity (float | str):
            total_resources (int):
            resources_overallocated (int):
            resources_underallocated (int):
            resources_optimal (int):
            resources_scheduled (int):
            resources_unscheduled (int):
            fleet_status (str):
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
     """

    horizon_days: int
    utilization_percent: float | str
    utilization_target_low: float | str
    utilization_target_high: float | str
    utilization_target_band: float | str
    utilization_status: str
    total_capacity_hours: float | str
    allocated_hours: float | str
    available_hours: float | str
    capacity_status: str
    weeks_of_capacity: float | str
    total_resources: int
    resources_overallocated: int
    resources_underallocated: int
    resources_optimal: int
    resources_scheduled: int
    resources_unscheduled: int
    fleet_status: str
    period: str | Unset = 'YTD'
    temporal_type: str | Unset = 'snapshot'
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption
        horizon_days = self.horizon_days

        utilization_percent: float | str
        utilization_percent = self.utilization_percent

        utilization_target_low: float | str
        utilization_target_low = self.utilization_target_low

        utilization_target_high: float | str
        utilization_target_high = self.utilization_target_high

        utilization_target_band: float | str
        utilization_target_band = self.utilization_target_band

        utilization_status = self.utilization_status

        total_capacity_hours: float | str
        total_capacity_hours = self.total_capacity_hours

        allocated_hours: float | str
        allocated_hours = self.allocated_hours

        available_hours: float | str
        available_hours = self.available_hours

        capacity_status = self.capacity_status

        weeks_of_capacity: float | str
        weeks_of_capacity = self.weeks_of_capacity

        total_resources = self.total_resources

        resources_overallocated = self.resources_overallocated

        resources_underallocated = self.resources_underallocated

        resources_optimal = self.resources_optimal

        resources_scheduled = self.resources_scheduled

        resources_unscheduled = self.resources_unscheduled

        fleet_status = self.fleet_status

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "horizon_days": horizon_days,
            "utilization_percent": utilization_percent,
            "utilization_target_low": utilization_target_low,
            "utilization_target_high": utilization_target_high,
            "utilization_target_band": utilization_target_band,
            "utilization_status": utilization_status,
            "total_capacity_hours": total_capacity_hours,
            "allocated_hours": allocated_hours,
            "available_hours": available_hours,
            "capacity_status": capacity_status,
            "weeks_of_capacity": weeks_of_capacity,
            "total_resources": total_resources,
            "resources_overallocated": resources_overallocated,
            "resources_underallocated": resources_underallocated,
            "resources_optimal": resources_optimal,
            "resources_scheduled": resources_scheduled,
            "resources_unscheduled": resources_unscheduled,
            "fleet_status": fleet_status,
        })
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
        horizon_days = d.pop("horizon_days")

        def _parse_utilization_percent(data: object) -> float | str:
            return cast(float | str, data)

        utilization_percent = _parse_utilization_percent(d.pop("utilization_percent"))


        def _parse_utilization_target_low(data: object) -> float | str:
            return cast(float | str, data)

        utilization_target_low = _parse_utilization_target_low(d.pop("utilization_target_low"))


        def _parse_utilization_target_high(data: object) -> float | str:
            return cast(float | str, data)

        utilization_target_high = _parse_utilization_target_high(d.pop("utilization_target_high"))


        def _parse_utilization_target_band(data: object) -> float | str:
            return cast(float | str, data)

        utilization_target_band = _parse_utilization_target_band(d.pop("utilization_target_band"))


        utilization_status = d.pop("utilization_status")

        def _parse_total_capacity_hours(data: object) -> float | str:
            return cast(float | str, data)

        total_capacity_hours = _parse_total_capacity_hours(d.pop("total_capacity_hours"))


        def _parse_allocated_hours(data: object) -> float | str:
            return cast(float | str, data)

        allocated_hours = _parse_allocated_hours(d.pop("allocated_hours"))


        def _parse_available_hours(data: object) -> float | str:
            return cast(float | str, data)

        available_hours = _parse_available_hours(d.pop("available_hours"))


        capacity_status = d.pop("capacity_status")

        def _parse_weeks_of_capacity(data: object) -> float | str:
            return cast(float | str, data)

        weeks_of_capacity = _parse_weeks_of_capacity(d.pop("weeks_of_capacity"))


        total_resources = d.pop("total_resources")

        resources_overallocated = d.pop("resources_overallocated")

        resources_underallocated = d.pop("resources_underallocated")

        resources_optimal = d.pop("resources_optimal")

        resources_scheduled = d.pop("resources_scheduled")

        resources_unscheduled = d.pop("resources_unscheduled")

        fleet_status = d.pop("fleet_status")

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
                for horizon_options_type_0_item_data in (_horizon_options_type_0):
                    horizon_options_type_0_item = HorizonOption.from_dict(horizon_options_type_0_item_data)



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
                for compare_options_type_0_item_data in (_compare_options_type_0):
                    compare_options_type_0_item = CompareOption.from_dict(compare_options_type_0_item_data)



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

        filter_severity_label = _parse_filter_severity_label(d.pop("filter_severity_label", UNSET))


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

        filter_category_label = _parse_filter_category_label(d.pop("filter_category_label", UNSET))


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


        resources_kp_is = cls(
            horizon_days=horizon_days,
            utilization_percent=utilization_percent,
            utilization_target_low=utilization_target_low,
            utilization_target_high=utilization_target_high,
            utilization_target_band=utilization_target_band,
            utilization_status=utilization_status,
            total_capacity_hours=total_capacity_hours,
            allocated_hours=allocated_hours,
            available_hours=available_hours,
            capacity_status=capacity_status,
            weeks_of_capacity=weeks_of_capacity,
            total_resources=total_resources,
            resources_overallocated=resources_overallocated,
            resources_underallocated=resources_underallocated,
            resources_optimal=resources_optimal,
            resources_scheduled=resources_scheduled,
            resources_unscheduled=resources_unscheduled,
            fleet_status=fleet_status,
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


        resources_kp_is.additional_properties = d
        return resources_kp_is

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
