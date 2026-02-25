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
    from ..models.analytics_margin_item import AnalyticsMarginItem
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsFinancialMargins")


@_attrs_define
class AnalyticsFinancialMargins:
    """Margin analytics

    Attributes:
        gross_margin_percent (float | str):
        contribution_margin_percent (float | str):
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
        margins_by_product (list[AnalyticsMarginItem] | Unset):
        margins_by_customer (list[AnalyticsMarginItem] | Unset):
        prev_gross_margin_pct (float | None | str | Unset):
        prev_contribution_margin_pct (float | None | str | Unset):
        gross_margin_change_pp (float | Literal['new'] | None | str | Unset):
        contribution_margin_change_pp (float | Literal['new'] | None | str | Unset):
    """

    gross_margin_percent: float | str
    contribution_margin_percent: float | str
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
    margins_by_product: list[AnalyticsMarginItem] | Unset = UNSET
    margins_by_customer: list[AnalyticsMarginItem] | Unset = UNSET
    prev_gross_margin_pct: float | None | str | Unset = UNSET
    prev_contribution_margin_pct: float | None | str | Unset = UNSET
    gross_margin_change_pp: float | Literal["new"] | None | str | Unset = UNSET
    contribution_margin_change_pp: float | Literal["new"] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gross_margin_percent: float | str
        gross_margin_percent = self.gross_margin_percent

        contribution_margin_percent: float | str
        contribution_margin_percent = self.contribution_margin_percent

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

        margins_by_product: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.margins_by_product, Unset):
            margins_by_product = []
            for margins_by_product_item_data in self.margins_by_product:
                margins_by_product_item = margins_by_product_item_data.to_dict()
                margins_by_product.append(margins_by_product_item)

        margins_by_customer: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.margins_by_customer, Unset):
            margins_by_customer = []
            for margins_by_customer_item_data in self.margins_by_customer:
                margins_by_customer_item = margins_by_customer_item_data.to_dict()
                margins_by_customer.append(margins_by_customer_item)

        prev_gross_margin_pct: float | None | str | Unset
        if isinstance(self.prev_gross_margin_pct, Unset):
            prev_gross_margin_pct = UNSET
        else:
            prev_gross_margin_pct = self.prev_gross_margin_pct

        prev_contribution_margin_pct: float | None | str | Unset
        if isinstance(self.prev_contribution_margin_pct, Unset):
            prev_contribution_margin_pct = UNSET
        else:
            prev_contribution_margin_pct = self.prev_contribution_margin_pct

        gross_margin_change_pp: float | Literal["new"] | None | str | Unset
        if isinstance(self.gross_margin_change_pp, Unset):
            gross_margin_change_pp = UNSET
        else:
            gross_margin_change_pp = self.gross_margin_change_pp

        contribution_margin_change_pp: float | Literal["new"] | None | str | Unset
        if isinstance(self.contribution_margin_change_pp, Unset):
            contribution_margin_change_pp = UNSET
        else:
            contribution_margin_change_pp = self.contribution_margin_change_pp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gross_margin_percent": gross_margin_percent,
                "contribution_margin_percent": contribution_margin_percent,
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
        if margins_by_product is not UNSET:
            field_dict["margins_by_product"] = margins_by_product
        if margins_by_customer is not UNSET:
            field_dict["margins_by_customer"] = margins_by_customer
        if prev_gross_margin_pct is not UNSET:
            field_dict["prev_gross_margin_pct"] = prev_gross_margin_pct
        if prev_contribution_margin_pct is not UNSET:
            field_dict["prev_contribution_margin_pct"] = prev_contribution_margin_pct
        if gross_margin_change_pp is not UNSET:
            field_dict["gross_margin_change_pp"] = gross_margin_change_pp
        if contribution_margin_change_pp is not UNSET:
            field_dict["contribution_margin_change_pp"] = contribution_margin_change_pp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_margin_item import AnalyticsMarginItem
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_gross_margin_percent(data: object) -> float | str:
            return cast(float | str, data)

        gross_margin_percent = _parse_gross_margin_percent(
            d.pop("gross_margin_percent")
        )

        def _parse_contribution_margin_percent(data: object) -> float | str:
            return cast(float | str, data)

        contribution_margin_percent = _parse_contribution_margin_percent(
            d.pop("contribution_margin_percent")
        )

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

        _margins_by_product = d.pop("margins_by_product", UNSET)
        margins_by_product: list[AnalyticsMarginItem] | Unset = UNSET
        if _margins_by_product is not UNSET:
            margins_by_product = []
            for margins_by_product_item_data in _margins_by_product:
                margins_by_product_item = AnalyticsMarginItem.from_dict(
                    margins_by_product_item_data
                )

                margins_by_product.append(margins_by_product_item)

        _margins_by_customer = d.pop("margins_by_customer", UNSET)
        margins_by_customer: list[AnalyticsMarginItem] | Unset = UNSET
        if _margins_by_customer is not UNSET:
            margins_by_customer = []
            for margins_by_customer_item_data in _margins_by_customer:
                margins_by_customer_item = AnalyticsMarginItem.from_dict(
                    margins_by_customer_item_data
                )

                margins_by_customer.append(margins_by_customer_item)

        def _parse_prev_gross_margin_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_gross_margin_pct = _parse_prev_gross_margin_pct(
            d.pop("prev_gross_margin_pct", UNSET)
        )

        def _parse_prev_contribution_margin_pct(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_contribution_margin_pct = _parse_prev_contribution_margin_pct(
            d.pop("prev_contribution_margin_pct", UNSET)
        )

        def _parse_gross_margin_change_pp(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            gross_margin_change_pp_type_2 = cast(Literal["new"], data)
            if gross_margin_change_pp_type_2 != "new":
                raise ValueError(
                    f"gross_margin_change_pp_type_2 must match const 'new', got '{gross_margin_change_pp_type_2}'"
                )
            return gross_margin_change_pp_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        gross_margin_change_pp = _parse_gross_margin_change_pp(
            d.pop("gross_margin_change_pp", UNSET)
        )

        def _parse_contribution_margin_change_pp(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            contribution_margin_change_pp_type_2 = cast(Literal["new"], data)
            if contribution_margin_change_pp_type_2 != "new":
                raise ValueError(
                    f"contribution_margin_change_pp_type_2 must match const 'new', got '{contribution_margin_change_pp_type_2}'"
                )
            return contribution_margin_change_pp_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        contribution_margin_change_pp = _parse_contribution_margin_change_pp(
            d.pop("contribution_margin_change_pp", UNSET)
        )

        analytics_financial_margins = cls(
            gross_margin_percent=gross_margin_percent,
            contribution_margin_percent=contribution_margin_percent,
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
            margins_by_product=margins_by_product,
            margins_by_customer=margins_by_customer,
            prev_gross_margin_pct=prev_gross_margin_pct,
            prev_contribution_margin_pct=prev_contribution_margin_pct,
            gross_margin_change_pp=gross_margin_change_pp,
            contribution_margin_change_pp=contribution_margin_change_pp,
        )

        analytics_financial_margins.additional_properties = d
        return analytics_financial_margins

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
