from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_ar_customer_item import AnalyticsARCustomerItem
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsFinancialAging")


@_attrs_define
class AnalyticsFinancialAging:
    """AR/AP aging analysis

    Attributes:
        ar_total (float | str):
        ar_current (float | str):
        ar_30_days (float | str):
        ar_60_days (float | str):
        ar_90_plus_days (float | str):
        ap_total (float | str):
        ap_current (float | str):
        ap_30_days (float | str):
        ap_60_days (float | str):
        ap_90_plus_days (float | str):
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
        ar_by_customer (list[AnalyticsARCustomerItem] | Unset):
    """

    ar_total: float | str
    ar_current: float | str
    ar_30_days: float | str
    ar_60_days: float | str
    ar_90_plus_days: float | str
    ap_total: float | str
    ap_current: float | str
    ap_30_days: float | str
    ap_60_days: float | str
    ap_90_plus_days: float | str
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
    ar_by_customer: list[AnalyticsARCustomerItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ar_total: float | str
        ar_total = self.ar_total

        ar_current: float | str
        ar_current = self.ar_current

        ar_30_days: float | str
        ar_30_days = self.ar_30_days

        ar_60_days: float | str
        ar_60_days = self.ar_60_days

        ar_90_plus_days: float | str
        ar_90_plus_days = self.ar_90_plus_days

        ap_total: float | str
        ap_total = self.ap_total

        ap_current: float | str
        ap_current = self.ap_current

        ap_30_days: float | str
        ap_30_days = self.ap_30_days

        ap_60_days: float | str
        ap_60_days = self.ap_60_days

        ap_90_plus_days: float | str
        ap_90_plus_days = self.ap_90_plus_days

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

        ar_by_customer: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ar_by_customer, Unset):
            ar_by_customer = []
            for ar_by_customer_item_data in self.ar_by_customer:
                ar_by_customer_item = ar_by_customer_item_data.to_dict()
                ar_by_customer.append(ar_by_customer_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ar_total": ar_total,
                "ar_current": ar_current,
                "ar_30_days": ar_30_days,
                "ar_60_days": ar_60_days,
                "ar_90_plus_days": ar_90_plus_days,
                "ap_total": ap_total,
                "ap_current": ap_current,
                "ap_30_days": ap_30_days,
                "ap_60_days": ap_60_days,
                "ap_90_plus_days": ap_90_plus_days,
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
        if ar_by_customer is not UNSET:
            field_dict["ar_by_customer"] = ar_by_customer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_ar_customer_item import AnalyticsARCustomerItem
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_ar_total(data: object) -> float | str:
            return cast(float | str, data)

        ar_total = _parse_ar_total(d.pop("ar_total"))

        def _parse_ar_current(data: object) -> float | str:
            return cast(float | str, data)

        ar_current = _parse_ar_current(d.pop("ar_current"))

        def _parse_ar_30_days(data: object) -> float | str:
            return cast(float | str, data)

        ar_30_days = _parse_ar_30_days(d.pop("ar_30_days"))

        def _parse_ar_60_days(data: object) -> float | str:
            return cast(float | str, data)

        ar_60_days = _parse_ar_60_days(d.pop("ar_60_days"))

        def _parse_ar_90_plus_days(data: object) -> float | str:
            return cast(float | str, data)

        ar_90_plus_days = _parse_ar_90_plus_days(d.pop("ar_90_plus_days"))

        def _parse_ap_total(data: object) -> float | str:
            return cast(float | str, data)

        ap_total = _parse_ap_total(d.pop("ap_total"))

        def _parse_ap_current(data: object) -> float | str:
            return cast(float | str, data)

        ap_current = _parse_ap_current(d.pop("ap_current"))

        def _parse_ap_30_days(data: object) -> float | str:
            return cast(float | str, data)

        ap_30_days = _parse_ap_30_days(d.pop("ap_30_days"))

        def _parse_ap_60_days(data: object) -> float | str:
            return cast(float | str, data)

        ap_60_days = _parse_ap_60_days(d.pop("ap_60_days"))

        def _parse_ap_90_plus_days(data: object) -> float | str:
            return cast(float | str, data)

        ap_90_plus_days = _parse_ap_90_plus_days(d.pop("ap_90_plus_days"))

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

        _ar_by_customer = d.pop("ar_by_customer", UNSET)
        ar_by_customer: list[AnalyticsARCustomerItem] | Unset = UNSET
        if _ar_by_customer is not UNSET:
            ar_by_customer = []
            for ar_by_customer_item_data in _ar_by_customer:
                ar_by_customer_item = AnalyticsARCustomerItem.from_dict(
                    ar_by_customer_item_data
                )

                ar_by_customer.append(ar_by_customer_item)

        analytics_financial_aging = cls(
            ar_total=ar_total,
            ar_current=ar_current,
            ar_30_days=ar_30_days,
            ar_60_days=ar_60_days,
            ar_90_plus_days=ar_90_plus_days,
            ap_total=ap_total,
            ap_current=ap_current,
            ap_30_days=ap_30_days,
            ap_60_days=ap_60_days,
            ap_90_plus_days=ap_90_plus_days,
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
            ar_by_customer=ar_by_customer,
        )

        analytics_financial_aging.additional_properties = d
        return analytics_financial_aging

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
