from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgProposalDetails")


@_attrs_define
class OrgProposalDetails:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        funnel (str):
        stage (str):
        stage_type (str):
        created_at (datetime.datetime):
        internal_costs (float | str):
        external_value (float | str):
        currency (str):
        currency_symbol (str):
        owner_name (str):
        pricing_strategy (str):
        pricing_adjustment_percent (float | None | str | Unset):
        pricing_adjustment_amount (float | None | str | Unset):
        target_margin_percent (float | None | str | Unset):
        minimum_margin_percent (float | None | str | Unset):
    """

    id: str
    name: str
    description: str
    funnel: str
    stage: str
    stage_type: str
    created_at: datetime.datetime
    internal_costs: float | str
    external_value: float | str
    currency: str
    currency_symbol: str
    owner_name: str
    pricing_strategy: str
    pricing_adjustment_percent: float | None | str | Unset = UNSET
    pricing_adjustment_amount: float | None | str | Unset = UNSET
    target_margin_percent: float | None | str | Unset = UNSET
    minimum_margin_percent: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        funnel = self.funnel

        stage = self.stage

        stage_type = self.stage_type

        created_at = self.created_at.isoformat()

        internal_costs: float | str
        internal_costs = self.internal_costs

        external_value: float | str
        external_value = self.external_value

        currency = self.currency

        currency_symbol = self.currency_symbol

        owner_name = self.owner_name

        pricing_strategy = self.pricing_strategy

        pricing_adjustment_percent: float | None | str | Unset
        if isinstance(self.pricing_adjustment_percent, Unset):
            pricing_adjustment_percent = UNSET
        else:
            pricing_adjustment_percent = self.pricing_adjustment_percent

        pricing_adjustment_amount: float | None | str | Unset
        if isinstance(self.pricing_adjustment_amount, Unset):
            pricing_adjustment_amount = UNSET
        else:
            pricing_adjustment_amount = self.pricing_adjustment_amount

        target_margin_percent: float | None | str | Unset
        if isinstance(self.target_margin_percent, Unset):
            target_margin_percent = UNSET
        else:
            target_margin_percent = self.target_margin_percent

        minimum_margin_percent: float | None | str | Unset
        if isinstance(self.minimum_margin_percent, Unset):
            minimum_margin_percent = UNSET
        else:
            minimum_margin_percent = self.minimum_margin_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "funnel": funnel,
                "stage": stage,
                "stage_type": stage_type,
                "created_at": created_at,
                "internal_costs": internal_costs,
                "external_value": external_value,
                "currency": currency,
                "currency_symbol": currency_symbol,
                "owner_name": owner_name,
                "pricing_strategy": pricing_strategy,
            }
        )
        if pricing_adjustment_percent is not UNSET:
            field_dict["pricing_adjustment_percent"] = pricing_adjustment_percent
        if pricing_adjustment_amount is not UNSET:
            field_dict["pricing_adjustment_amount"] = pricing_adjustment_amount
        if target_margin_percent is not UNSET:
            field_dict["target_margin_percent"] = target_margin_percent
        if minimum_margin_percent is not UNSET:
            field_dict["minimum_margin_percent"] = minimum_margin_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        funnel = d.pop("funnel")

        stage = d.pop("stage")

        stage_type = d.pop("stage_type")

        created_at = isoparse(d.pop("created_at"))

        def _parse_internal_costs(data: object) -> float | str:
            return cast(float | str, data)

        internal_costs = _parse_internal_costs(d.pop("internal_costs"))

        def _parse_external_value(data: object) -> float | str:
            return cast(float | str, data)

        external_value = _parse_external_value(d.pop("external_value"))

        currency = d.pop("currency")

        currency_symbol = d.pop("currency_symbol")

        owner_name = d.pop("owner_name")

        pricing_strategy = d.pop("pricing_strategy")

        def _parse_pricing_adjustment_percent(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pricing_adjustment_percent = _parse_pricing_adjustment_percent(
            d.pop("pricing_adjustment_percent", UNSET)
        )

        def _parse_pricing_adjustment_amount(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pricing_adjustment_amount = _parse_pricing_adjustment_amount(
            d.pop("pricing_adjustment_amount", UNSET)
        )

        def _parse_target_margin_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        target_margin_percent = _parse_target_margin_percent(
            d.pop("target_margin_percent", UNSET)
        )

        def _parse_minimum_margin_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        minimum_margin_percent = _parse_minimum_margin_percent(
            d.pop("minimum_margin_percent", UNSET)
        )

        org_proposal_details = cls(
            id=id,
            name=name,
            description=description,
            funnel=funnel,
            stage=stage,
            stage_type=stage_type,
            created_at=created_at,
            internal_costs=internal_costs,
            external_value=external_value,
            currency=currency,
            currency_symbol=currency_symbol,
            owner_name=owner_name,
            pricing_strategy=pricing_strategy,
            pricing_adjustment_percent=pricing_adjustment_percent,
            pricing_adjustment_amount=pricing_adjustment_amount,
            target_margin_percent=target_margin_percent,
            minimum_margin_percent=minimum_margin_percent,
        )

        org_proposal_details.additional_properties = d
        return org_proposal_details

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
