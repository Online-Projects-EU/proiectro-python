from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funnel_stage_schema import FunnelStageSchema
    from ..models.tenant_funnel_overview_avg_deal_size_by_currency_type_0 import (
        TenantFunnelOverviewAvgDealSizeByCurrencyType0,
    )
    from ..models.tenant_funnel_overview_currency_symbols_type_0 import (
        TenantFunnelOverviewCurrencySymbolsType0,
    )
    from ..models.tenant_funnel_overview_deal_count_by_currency_type_0 import (
        TenantFunnelOverviewDealCountByCurrencyType0,
    )
    from ..models.tenant_funnel_overview_pipeline_by_currency_type_0 import (
        TenantFunnelOverviewPipelineByCurrencyType0,
    )


T = TypeVar("T", bound="TenantFunnelOverview")


@_attrs_define
class TenantFunnelOverview:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        stages (list[FunnelStageSchema]):
        total_pipeline_value (float | str):
        total_deals (int):
        average_deal_size (float | str):
        average_days_per_stage (float | str):
        currency_symbol (str):
        pipeline_by_currency (None | TenantFunnelOverviewPipelineByCurrencyType0 | Unset):
        avg_deal_size_by_currency (None | TenantFunnelOverviewAvgDealSizeByCurrencyType0 | Unset):
        currency_symbols (None | TenantFunnelOverviewCurrencySymbolsType0 | Unset):
        deal_count_by_currency (None | TenantFunnelOverviewDealCountByCurrencyType0 | Unset):
        has_mixed_currencies (bool | None | Unset):  Default: False.
    """

    id: str
    name: str
    description: str
    stages: list[FunnelStageSchema]
    total_pipeline_value: float | str
    total_deals: int
    average_deal_size: float | str
    average_days_per_stage: float | str
    currency_symbol: str
    pipeline_by_currency: None | TenantFunnelOverviewPipelineByCurrencyType0 | Unset = (
        UNSET
    )
    avg_deal_size_by_currency: (
        None | TenantFunnelOverviewAvgDealSizeByCurrencyType0 | Unset
    ) = UNSET
    currency_symbols: None | TenantFunnelOverviewCurrencySymbolsType0 | Unset = UNSET
    deal_count_by_currency: (
        None | TenantFunnelOverviewDealCountByCurrencyType0 | Unset
    ) = UNSET
    has_mixed_currencies: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tenant_funnel_overview_avg_deal_size_by_currency_type_0 import (
            TenantFunnelOverviewAvgDealSizeByCurrencyType0,
        )
        from ..models.tenant_funnel_overview_currency_symbols_type_0 import (
            TenantFunnelOverviewCurrencySymbolsType0,
        )
        from ..models.tenant_funnel_overview_deal_count_by_currency_type_0 import (
            TenantFunnelOverviewDealCountByCurrencyType0,
        )
        from ..models.tenant_funnel_overview_pipeline_by_currency_type_0 import (
            TenantFunnelOverviewPipelineByCurrencyType0,
        )

        id = self.id

        name = self.name

        description = self.description

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        total_pipeline_value: float | str
        total_pipeline_value = self.total_pipeline_value

        total_deals = self.total_deals

        average_deal_size: float | str
        average_deal_size = self.average_deal_size

        average_days_per_stage: float | str
        average_days_per_stage = self.average_days_per_stage

        currency_symbol = self.currency_symbol

        pipeline_by_currency: dict[str, Any] | None | Unset
        if isinstance(self.pipeline_by_currency, Unset):
            pipeline_by_currency = UNSET
        elif isinstance(
            self.pipeline_by_currency, TenantFunnelOverviewPipelineByCurrencyType0
        ):
            pipeline_by_currency = self.pipeline_by_currency.to_dict()
        else:
            pipeline_by_currency = self.pipeline_by_currency

        avg_deal_size_by_currency: dict[str, Any] | None | Unset
        if isinstance(self.avg_deal_size_by_currency, Unset):
            avg_deal_size_by_currency = UNSET
        elif isinstance(
            self.avg_deal_size_by_currency,
            TenantFunnelOverviewAvgDealSizeByCurrencyType0,
        ):
            avg_deal_size_by_currency = self.avg_deal_size_by_currency.to_dict()
        else:
            avg_deal_size_by_currency = self.avg_deal_size_by_currency

        currency_symbols: dict[str, Any] | None | Unset
        if isinstance(self.currency_symbols, Unset):
            currency_symbols = UNSET
        elif isinstance(
            self.currency_symbols, TenantFunnelOverviewCurrencySymbolsType0
        ):
            currency_symbols = self.currency_symbols.to_dict()
        else:
            currency_symbols = self.currency_symbols

        deal_count_by_currency: dict[str, Any] | None | Unset
        if isinstance(self.deal_count_by_currency, Unset):
            deal_count_by_currency = UNSET
        elif isinstance(
            self.deal_count_by_currency, TenantFunnelOverviewDealCountByCurrencyType0
        ):
            deal_count_by_currency = self.deal_count_by_currency.to_dict()
        else:
            deal_count_by_currency = self.deal_count_by_currency

        has_mixed_currencies: bool | None | Unset
        if isinstance(self.has_mixed_currencies, Unset):
            has_mixed_currencies = UNSET
        else:
            has_mixed_currencies = self.has_mixed_currencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "stages": stages,
                "total_pipeline_value": total_pipeline_value,
                "total_deals": total_deals,
                "average_deal_size": average_deal_size,
                "average_days_per_stage": average_days_per_stage,
                "currency_symbol": currency_symbol,
            }
        )
        if pipeline_by_currency is not UNSET:
            field_dict["pipeline_by_currency"] = pipeline_by_currency
        if avg_deal_size_by_currency is not UNSET:
            field_dict["avg_deal_size_by_currency"] = avg_deal_size_by_currency
        if currency_symbols is not UNSET:
            field_dict["currency_symbols"] = currency_symbols
        if deal_count_by_currency is not UNSET:
            field_dict["deal_count_by_currency"] = deal_count_by_currency
        if has_mixed_currencies is not UNSET:
            field_dict["has_mixed_currencies"] = has_mixed_currencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.funnel_stage_schema import FunnelStageSchema
        from ..models.tenant_funnel_overview_avg_deal_size_by_currency_type_0 import (
            TenantFunnelOverviewAvgDealSizeByCurrencyType0,
        )
        from ..models.tenant_funnel_overview_currency_symbols_type_0 import (
            TenantFunnelOverviewCurrencySymbolsType0,
        )
        from ..models.tenant_funnel_overview_deal_count_by_currency_type_0 import (
            TenantFunnelOverviewDealCountByCurrencyType0,
        )
        from ..models.tenant_funnel_overview_pipeline_by_currency_type_0 import (
            TenantFunnelOverviewPipelineByCurrencyType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = FunnelStageSchema.from_dict(stages_item_data)

            stages.append(stages_item)

        def _parse_total_pipeline_value(data: object) -> float | str:
            return cast(float | str, data)

        total_pipeline_value = _parse_total_pipeline_value(
            d.pop("total_pipeline_value")
        )

        total_deals = d.pop("total_deals")

        def _parse_average_deal_size(data: object) -> float | str:
            return cast(float | str, data)

        average_deal_size = _parse_average_deal_size(d.pop("average_deal_size"))

        def _parse_average_days_per_stage(data: object) -> float | str:
            return cast(float | str, data)

        average_days_per_stage = _parse_average_days_per_stage(
            d.pop("average_days_per_stage")
        )

        currency_symbol = d.pop("currency_symbol")

        def _parse_pipeline_by_currency(
            data: object,
        ) -> None | TenantFunnelOverviewPipelineByCurrencyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pipeline_by_currency_type_0 = (
                    TenantFunnelOverviewPipelineByCurrencyType0.from_dict(data)
                )

                return pipeline_by_currency_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TenantFunnelOverviewPipelineByCurrencyType0 | Unset, data
            )

        pipeline_by_currency = _parse_pipeline_by_currency(
            d.pop("pipeline_by_currency", UNSET)
        )

        def _parse_avg_deal_size_by_currency(
            data: object,
        ) -> None | TenantFunnelOverviewAvgDealSizeByCurrencyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                avg_deal_size_by_currency_type_0 = (
                    TenantFunnelOverviewAvgDealSizeByCurrencyType0.from_dict(data)
                )

                return avg_deal_size_by_currency_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TenantFunnelOverviewAvgDealSizeByCurrencyType0 | Unset, data
            )

        avg_deal_size_by_currency = _parse_avg_deal_size_by_currency(
            d.pop("avg_deal_size_by_currency", UNSET)
        )

        def _parse_currency_symbols(
            data: object,
        ) -> None | TenantFunnelOverviewCurrencySymbolsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                currency_symbols_type_0 = (
                    TenantFunnelOverviewCurrencySymbolsType0.from_dict(data)
                )

                return currency_symbols_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TenantFunnelOverviewCurrencySymbolsType0 | Unset, data)

        currency_symbols = _parse_currency_symbols(d.pop("currency_symbols", UNSET))

        def _parse_deal_count_by_currency(
            data: object,
        ) -> None | TenantFunnelOverviewDealCountByCurrencyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deal_count_by_currency_type_0 = (
                    TenantFunnelOverviewDealCountByCurrencyType0.from_dict(data)
                )

                return deal_count_by_currency_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | TenantFunnelOverviewDealCountByCurrencyType0 | Unset, data
            )

        deal_count_by_currency = _parse_deal_count_by_currency(
            d.pop("deal_count_by_currency", UNSET)
        )

        def _parse_has_mixed_currencies(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_mixed_currencies = _parse_has_mixed_currencies(
            d.pop("has_mixed_currencies", UNSET)
        )

        tenant_funnel_overview = cls(
            id=id,
            name=name,
            description=description,
            stages=stages,
            total_pipeline_value=total_pipeline_value,
            total_deals=total_deals,
            average_deal_size=average_deal_size,
            average_days_per_stage=average_days_per_stage,
            currency_symbol=currency_symbol,
            pipeline_by_currency=pipeline_by_currency,
            avg_deal_size_by_currency=avg_deal_size_by_currency,
            currency_symbols=currency_symbols,
            deal_count_by_currency=deal_count_by_currency,
            has_mixed_currencies=has_mixed_currencies,
        )

        tenant_funnel_overview.additional_properties = d
        return tenant_funnel_overview

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
