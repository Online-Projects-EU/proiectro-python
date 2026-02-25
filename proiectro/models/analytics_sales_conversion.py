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
    from ..models.analytics_sales_conversion_funnel_summary import (
        AnalyticsSalesConversionFunnelSummary,
    )
    from ..models.analytics_sales_conversion_stage import AnalyticsSalesConversionStage
    from ..models.compare_option import CompareOption
    from ..models.horizon_option import HorizonOption


T = TypeVar("T", bound="AnalyticsSalesConversion")


@_attrs_define
class AnalyticsSalesConversion:
    """Sales conversion funnel analysis with overall summary and per-funnel detail.

    Shows:
    - Overall conversion metrics across all funnels
    - Per-funnel tabs with stage-by-stage conversion rates
    - Detailed stage metrics including drop-off analysis

        Attributes:
            overall_conversion_rate (float | str):
            total_deals_created (int):
            total_deals_won (int):
            total_deals_lost (int):
            total_deals_open (int):
            avg_sales_cycle_days (int):
            win_rate (float | str):
            funnel_id (str):
            funnel_name (str):
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
            prev_conversion_rate (float | None | str | Unset):
            prev_win_rate (float | None | str | Unset):
            conversion_rate_change (float | Literal['new'] | None | str | Unset):
            win_rate_change (float | Literal['new'] | None | str | Unset):
            available_funnels (list[AnalyticsSalesConversionFunnelSummary] | Unset):
            stages (list[AnalyticsSalesConversionStage] | Unset):
            bottleneck_stage (None | str | Unset):
            fastest_stage (None | str | Unset):
    """

    overall_conversion_rate: float | str
    total_deals_created: int
    total_deals_won: int
    total_deals_lost: int
    total_deals_open: int
    avg_sales_cycle_days: int
    win_rate: float | str
    funnel_id: str
    funnel_name: str
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
    prev_conversion_rate: float | None | str | Unset = UNSET
    prev_win_rate: float | None | str | Unset = UNSET
    conversion_rate_change: float | Literal["new"] | None | str | Unset = UNSET
    win_rate_change: float | Literal["new"] | None | str | Unset = UNSET
    available_funnels: list[AnalyticsSalesConversionFunnelSummary] | Unset = UNSET
    stages: list[AnalyticsSalesConversionStage] | Unset = UNSET
    bottleneck_stage: None | str | Unset = UNSET
    fastest_stage: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overall_conversion_rate: float | str
        overall_conversion_rate = self.overall_conversion_rate

        total_deals_created = self.total_deals_created

        total_deals_won = self.total_deals_won

        total_deals_lost = self.total_deals_lost

        total_deals_open = self.total_deals_open

        avg_sales_cycle_days = self.avg_sales_cycle_days

        win_rate: float | str
        win_rate = self.win_rate

        funnel_id = self.funnel_id

        funnel_name = self.funnel_name

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

        prev_conversion_rate: float | None | str | Unset
        if isinstance(self.prev_conversion_rate, Unset):
            prev_conversion_rate = UNSET
        else:
            prev_conversion_rate = self.prev_conversion_rate

        prev_win_rate: float | None | str | Unset
        if isinstance(self.prev_win_rate, Unset):
            prev_win_rate = UNSET
        else:
            prev_win_rate = self.prev_win_rate

        conversion_rate_change: float | Literal["new"] | None | str | Unset
        if isinstance(self.conversion_rate_change, Unset):
            conversion_rate_change = UNSET
        else:
            conversion_rate_change = self.conversion_rate_change

        win_rate_change: float | Literal["new"] | None | str | Unset
        if isinstance(self.win_rate_change, Unset):
            win_rate_change = UNSET
        else:
            win_rate_change = self.win_rate_change

        available_funnels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_funnels, Unset):
            available_funnels = []
            for available_funnels_item_data in self.available_funnels:
                available_funnels_item = available_funnels_item_data.to_dict()
                available_funnels.append(available_funnels_item)

        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        bottleneck_stage: None | str | Unset
        if isinstance(self.bottleneck_stage, Unset):
            bottleneck_stage = UNSET
        else:
            bottleneck_stage = self.bottleneck_stage

        fastest_stage: None | str | Unset
        if isinstance(self.fastest_stage, Unset):
            fastest_stage = UNSET
        else:
            fastest_stage = self.fastest_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overall_conversion_rate": overall_conversion_rate,
                "total_deals_created": total_deals_created,
                "total_deals_won": total_deals_won,
                "total_deals_lost": total_deals_lost,
                "total_deals_open": total_deals_open,
                "avg_sales_cycle_days": avg_sales_cycle_days,
                "win_rate": win_rate,
                "funnel_id": funnel_id,
                "funnel_name": funnel_name,
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
        if prev_conversion_rate is not UNSET:
            field_dict["prev_conversion_rate"] = prev_conversion_rate
        if prev_win_rate is not UNSET:
            field_dict["prev_win_rate"] = prev_win_rate
        if conversion_rate_change is not UNSET:
            field_dict["conversion_rate_change"] = conversion_rate_change
        if win_rate_change is not UNSET:
            field_dict["win_rate_change"] = win_rate_change
        if available_funnels is not UNSET:
            field_dict["available_funnels"] = available_funnels
        if stages is not UNSET:
            field_dict["stages"] = stages
        if bottleneck_stage is not UNSET:
            field_dict["bottleneck_stage"] = bottleneck_stage
        if fastest_stage is not UNSET:
            field_dict["fastest_stage"] = fastest_stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_sales_conversion_funnel_summary import (
            AnalyticsSalesConversionFunnelSummary,
        )
        from ..models.analytics_sales_conversion_stage import (
            AnalyticsSalesConversionStage,
        )
        from ..models.compare_option import CompareOption
        from ..models.horizon_option import HorizonOption

        d = dict(src_dict)

        def _parse_overall_conversion_rate(data: object) -> float | str:
            return cast(float | str, data)

        overall_conversion_rate = _parse_overall_conversion_rate(
            d.pop("overall_conversion_rate")
        )

        total_deals_created = d.pop("total_deals_created")

        total_deals_won = d.pop("total_deals_won")

        total_deals_lost = d.pop("total_deals_lost")

        total_deals_open = d.pop("total_deals_open")

        avg_sales_cycle_days = d.pop("avg_sales_cycle_days")

        def _parse_win_rate(data: object) -> float | str:
            return cast(float | str, data)

        win_rate = _parse_win_rate(d.pop("win_rate"))

        funnel_id = d.pop("funnel_id")

        funnel_name = d.pop("funnel_name")

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

        def _parse_prev_conversion_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_conversion_rate = _parse_prev_conversion_rate(
            d.pop("prev_conversion_rate", UNSET)
        )

        def _parse_prev_win_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_win_rate = _parse_prev_win_rate(d.pop("prev_win_rate", UNSET))

        def _parse_conversion_rate_change(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            conversion_rate_change_type_2 = cast(Literal["new"], data)
            if conversion_rate_change_type_2 != "new":
                raise ValueError(
                    f"conversion_rate_change_type_2 must match const 'new', got '{conversion_rate_change_type_2}'"
                )
            return conversion_rate_change_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        conversion_rate_change = _parse_conversion_rate_change(
            d.pop("conversion_rate_change", UNSET)
        )

        def _parse_win_rate_change(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            win_rate_change_type_2 = cast(Literal["new"], data)
            if win_rate_change_type_2 != "new":
                raise ValueError(
                    f"win_rate_change_type_2 must match const 'new', got '{win_rate_change_type_2}'"
                )
            return win_rate_change_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        win_rate_change = _parse_win_rate_change(d.pop("win_rate_change", UNSET))

        _available_funnels = d.pop("available_funnels", UNSET)
        available_funnels: list[AnalyticsSalesConversionFunnelSummary] | Unset = UNSET
        if _available_funnels is not UNSET:
            available_funnels = []
            for available_funnels_item_data in _available_funnels:
                available_funnels_item = (
                    AnalyticsSalesConversionFunnelSummary.from_dict(
                        available_funnels_item_data
                    )
                )

                available_funnels.append(available_funnels_item)

        _stages = d.pop("stages", UNSET)
        stages: list[AnalyticsSalesConversionStage] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = AnalyticsSalesConversionStage.from_dict(stages_item_data)

                stages.append(stages_item)

        def _parse_bottleneck_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bottleneck_stage = _parse_bottleneck_stage(d.pop("bottleneck_stage", UNSET))

        def _parse_fastest_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fastest_stage = _parse_fastest_stage(d.pop("fastest_stage", UNSET))

        analytics_sales_conversion = cls(
            overall_conversion_rate=overall_conversion_rate,
            total_deals_created=total_deals_created,
            total_deals_won=total_deals_won,
            total_deals_lost=total_deals_lost,
            total_deals_open=total_deals_open,
            avg_sales_cycle_days=avg_sales_cycle_days,
            win_rate=win_rate,
            funnel_id=funnel_id,
            funnel_name=funnel_name,
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
            prev_conversion_rate=prev_conversion_rate,
            prev_win_rate=prev_win_rate,
            conversion_rate_change=conversion_rate_change,
            win_rate_change=win_rate_change,
            available_funnels=available_funnels,
            stages=stages,
            bottleneck_stage=bottleneck_stage,
            fastest_stage=fastest_stage,
        )

        analytics_sales_conversion.additional_properties = d
        return analytics_sales_conversion

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
