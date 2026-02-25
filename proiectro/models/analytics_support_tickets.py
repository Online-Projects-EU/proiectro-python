from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_ticket_category_item import AnalyticsTicketCategoryItem
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsSupportTickets")


@_attrs_define
class AnalyticsSupportTickets:
    """Support ticket volume and distribution analysis - Internal and External sections

    Attributes:
        internal_total (int):
        internal_open (int):
        internal_closed (int):
        external_total (int):
        external_open (int):
        external_closed (int):
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
        internal_by_status (list[AnalyticsTicketCategoryItem] | Unset):
        internal_by_severity (list[AnalyticsTicketCategoryItem] | Unset):
        internal_by_type (list[AnalyticsTicketCategoryItem] | Unset):
        internal_by_queue (list[AnalyticsTicketCategoryItem] | Unset):
        external_by_status (list[AnalyticsTicketCategoryItem] | Unset):
        external_by_severity (list[AnalyticsTicketCategoryItem] | Unset):
        external_by_type (list[AnalyticsTicketCategoryItem] | Unset):
        external_by_queue (list[AnalyticsTicketCategoryItem] | Unset):
    """

    internal_total: int
    internal_open: int
    internal_closed: int
    external_total: int
    external_open: int
    external_closed: int
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
    internal_by_status: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    internal_by_severity: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    internal_by_type: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    internal_by_queue: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    external_by_status: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    external_by_severity: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    external_by_type: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    external_by_queue: list[AnalyticsTicketCategoryItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internal_total = self.internal_total

        internal_open = self.internal_open

        internal_closed = self.internal_closed

        external_total = self.external_total

        external_open = self.external_open

        external_closed = self.external_closed

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

        internal_by_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.internal_by_status, Unset):
            internal_by_status = []
            for internal_by_status_item_data in self.internal_by_status:
                internal_by_status_item = internal_by_status_item_data.to_dict()
                internal_by_status.append(internal_by_status_item)

        internal_by_severity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.internal_by_severity, Unset):
            internal_by_severity = []
            for internal_by_severity_item_data in self.internal_by_severity:
                internal_by_severity_item = internal_by_severity_item_data.to_dict()
                internal_by_severity.append(internal_by_severity_item)

        internal_by_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.internal_by_type, Unset):
            internal_by_type = []
            for internal_by_type_item_data in self.internal_by_type:
                internal_by_type_item = internal_by_type_item_data.to_dict()
                internal_by_type.append(internal_by_type_item)

        internal_by_queue: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.internal_by_queue, Unset):
            internal_by_queue = []
            for internal_by_queue_item_data in self.internal_by_queue:
                internal_by_queue_item = internal_by_queue_item_data.to_dict()
                internal_by_queue.append(internal_by_queue_item)

        external_by_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_by_status, Unset):
            external_by_status = []
            for external_by_status_item_data in self.external_by_status:
                external_by_status_item = external_by_status_item_data.to_dict()
                external_by_status.append(external_by_status_item)

        external_by_severity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_by_severity, Unset):
            external_by_severity = []
            for external_by_severity_item_data in self.external_by_severity:
                external_by_severity_item = external_by_severity_item_data.to_dict()
                external_by_severity.append(external_by_severity_item)

        external_by_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_by_type, Unset):
            external_by_type = []
            for external_by_type_item_data in self.external_by_type:
                external_by_type_item = external_by_type_item_data.to_dict()
                external_by_type.append(external_by_type_item)

        external_by_queue: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_by_queue, Unset):
            external_by_queue = []
            for external_by_queue_item_data in self.external_by_queue:
                external_by_queue_item = external_by_queue_item_data.to_dict()
                external_by_queue.append(external_by_queue_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internal_total": internal_total,
                "internal_open": internal_open,
                "internal_closed": internal_closed,
                "external_total": external_total,
                "external_open": external_open,
                "external_closed": external_closed,
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
        if internal_by_status is not UNSET:
            field_dict["internal_by_status"] = internal_by_status
        if internal_by_severity is not UNSET:
            field_dict["internal_by_severity"] = internal_by_severity
        if internal_by_type is not UNSET:
            field_dict["internal_by_type"] = internal_by_type
        if internal_by_queue is not UNSET:
            field_dict["internal_by_queue"] = internal_by_queue
        if external_by_status is not UNSET:
            field_dict["external_by_status"] = external_by_status
        if external_by_severity is not UNSET:
            field_dict["external_by_severity"] = external_by_severity
        if external_by_type is not UNSET:
            field_dict["external_by_type"] = external_by_type
        if external_by_queue is not UNSET:
            field_dict["external_by_queue"] = external_by_queue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_ticket_category_item import AnalyticsTicketCategoryItem
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)
        internal_total = d.pop("internal_total")

        internal_open = d.pop("internal_open")

        internal_closed = d.pop("internal_closed")

        external_total = d.pop("external_total")

        external_open = d.pop("external_open")

        external_closed = d.pop("external_closed")

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

        _internal_by_status = d.pop("internal_by_status", UNSET)
        internal_by_status: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _internal_by_status is not UNSET:
            internal_by_status = []
            for internal_by_status_item_data in _internal_by_status:
                internal_by_status_item = AnalyticsTicketCategoryItem.from_dict(
                    internal_by_status_item_data
                )

                internal_by_status.append(internal_by_status_item)

        _internal_by_severity = d.pop("internal_by_severity", UNSET)
        internal_by_severity: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _internal_by_severity is not UNSET:
            internal_by_severity = []
            for internal_by_severity_item_data in _internal_by_severity:
                internal_by_severity_item = AnalyticsTicketCategoryItem.from_dict(
                    internal_by_severity_item_data
                )

                internal_by_severity.append(internal_by_severity_item)

        _internal_by_type = d.pop("internal_by_type", UNSET)
        internal_by_type: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _internal_by_type is not UNSET:
            internal_by_type = []
            for internal_by_type_item_data in _internal_by_type:
                internal_by_type_item = AnalyticsTicketCategoryItem.from_dict(
                    internal_by_type_item_data
                )

                internal_by_type.append(internal_by_type_item)

        _internal_by_queue = d.pop("internal_by_queue", UNSET)
        internal_by_queue: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _internal_by_queue is not UNSET:
            internal_by_queue = []
            for internal_by_queue_item_data in _internal_by_queue:
                internal_by_queue_item = AnalyticsTicketCategoryItem.from_dict(
                    internal_by_queue_item_data
                )

                internal_by_queue.append(internal_by_queue_item)

        _external_by_status = d.pop("external_by_status", UNSET)
        external_by_status: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _external_by_status is not UNSET:
            external_by_status = []
            for external_by_status_item_data in _external_by_status:
                external_by_status_item = AnalyticsTicketCategoryItem.from_dict(
                    external_by_status_item_data
                )

                external_by_status.append(external_by_status_item)

        _external_by_severity = d.pop("external_by_severity", UNSET)
        external_by_severity: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _external_by_severity is not UNSET:
            external_by_severity = []
            for external_by_severity_item_data in _external_by_severity:
                external_by_severity_item = AnalyticsTicketCategoryItem.from_dict(
                    external_by_severity_item_data
                )

                external_by_severity.append(external_by_severity_item)

        _external_by_type = d.pop("external_by_type", UNSET)
        external_by_type: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _external_by_type is not UNSET:
            external_by_type = []
            for external_by_type_item_data in _external_by_type:
                external_by_type_item = AnalyticsTicketCategoryItem.from_dict(
                    external_by_type_item_data
                )

                external_by_type.append(external_by_type_item)

        _external_by_queue = d.pop("external_by_queue", UNSET)
        external_by_queue: list[AnalyticsTicketCategoryItem] | Unset = UNSET
        if _external_by_queue is not UNSET:
            external_by_queue = []
            for external_by_queue_item_data in _external_by_queue:
                external_by_queue_item = AnalyticsTicketCategoryItem.from_dict(
                    external_by_queue_item_data
                )

                external_by_queue.append(external_by_queue_item)

        analytics_support_tickets = cls(
            internal_total=internal_total,
            internal_open=internal_open,
            internal_closed=internal_closed,
            external_total=external_total,
            external_open=external_open,
            external_closed=external_closed,
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
            internal_by_status=internal_by_status,
            internal_by_severity=internal_by_severity,
            internal_by_type=internal_by_type,
            internal_by_queue=internal_by_queue,
            external_by_status=external_by_status,
            external_by_severity=external_by_severity,
            external_by_type=external_by_type,
            external_by_queue=external_by_queue,
        )

        analytics_support_tickets.additional_properties = d
        return analytics_support_tickets

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
