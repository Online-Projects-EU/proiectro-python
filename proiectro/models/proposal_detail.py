from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposalDetail")


@_attrs_define
class ProposalDetail:
    """
    Attributes:
        id (str):
        name (str):
        customer (str):
        customer_id (str):
        created_at (datetime.datetime):
        internal_costs (float | str):
        external_value (float | str):
        margin (float | str):
        margin_percent (float | str):
        currency (str):
        currency_symbol (str):
        owner_name (str):
        days_in_stage (int):
        product_count (int):
        days_since_last_activity (int):
        last_activity (datetime.datetime | None | Unset):
        transitions (list[list[Any]] | None | Unset):
        funnel_name (None | str | Unset):
        funnel_id (None | str | Unset):
    """

    id: str
    name: str
    customer: str
    customer_id: str
    created_at: datetime.datetime
    internal_costs: float | str
    external_value: float | str
    margin: float | str
    margin_percent: float | str
    currency: str
    currency_symbol: str
    owner_name: str
    days_in_stage: int
    product_count: int
    days_since_last_activity: int
    last_activity: datetime.datetime | None | Unset = UNSET
    transitions: list[list[Any]] | None | Unset = UNSET
    funnel_name: None | str | Unset = UNSET
    funnel_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        customer = self.customer

        customer_id = self.customer_id

        created_at = self.created_at.isoformat()

        internal_costs: float | str
        internal_costs = self.internal_costs

        external_value: float | str
        external_value = self.external_value

        margin: float | str
        margin = self.margin

        margin_percent: float | str
        margin_percent = self.margin_percent

        currency = self.currency

        currency_symbol = self.currency_symbol

        owner_name = self.owner_name

        days_in_stage = self.days_in_stage

        product_count = self.product_count

        days_since_last_activity = self.days_since_last_activity

        last_activity: None | str | Unset
        if isinstance(self.last_activity, Unset):
            last_activity = UNSET
        elif isinstance(self.last_activity, datetime.datetime):
            last_activity = self.last_activity.isoformat()
        else:
            last_activity = self.last_activity

        transitions: list[list[Any]] | None | Unset
        if isinstance(self.transitions, Unset):
            transitions = UNSET
        elif isinstance(self.transitions, list):
            transitions = []
            for transitions_type_0_item_data in self.transitions:
                transitions_type_0_item = transitions_type_0_item_data

                transitions.append(transitions_type_0_item)

        else:
            transitions = self.transitions

        funnel_name: None | str | Unset
        if isinstance(self.funnel_name, Unset):
            funnel_name = UNSET
        else:
            funnel_name = self.funnel_name

        funnel_id: None | str | Unset
        if isinstance(self.funnel_id, Unset):
            funnel_id = UNSET
        else:
            funnel_id = self.funnel_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "customer": customer,
                "customer_id": customer_id,
                "created_at": created_at,
                "internal_costs": internal_costs,
                "external_value": external_value,
                "margin": margin,
                "margin_percent": margin_percent,
                "currency": currency,
                "currency_symbol": currency_symbol,
                "owner_name": owner_name,
                "days_in_stage": days_in_stage,
                "product_count": product_count,
                "days_since_last_activity": days_since_last_activity,
            }
        )
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity
        if transitions is not UNSET:
            field_dict["transitions"] = transitions
        if funnel_name is not UNSET:
            field_dict["funnel_name"] = funnel_name
        if funnel_id is not UNSET:
            field_dict["funnel_id"] = funnel_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        customer = d.pop("customer")

        customer_id = d.pop("customer_id")

        created_at = isoparse(d.pop("created_at"))

        def _parse_internal_costs(data: object) -> float | str:
            return cast(float | str, data)

        internal_costs = _parse_internal_costs(d.pop("internal_costs"))

        def _parse_external_value(data: object) -> float | str:
            return cast(float | str, data)

        external_value = _parse_external_value(d.pop("external_value"))

        def _parse_margin(data: object) -> float | str:
            return cast(float | str, data)

        margin = _parse_margin(d.pop("margin"))

        def _parse_margin_percent(data: object) -> float | str:
            return cast(float | str, data)

        margin_percent = _parse_margin_percent(d.pop("margin_percent"))

        currency = d.pop("currency")

        currency_symbol = d.pop("currency_symbol")

        owner_name = d.pop("owner_name")

        days_in_stage = d.pop("days_in_stage")

        product_count = d.pop("product_count")

        days_since_last_activity = d.pop("days_since_last_activity")

        def _parse_last_activity(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_type_0 = isoparse(data)

                return last_activity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity = _parse_last_activity(d.pop("last_activity", UNSET))

        def _parse_transitions(data: object) -> list[list[Any]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transitions_type_0 = []
                _transitions_type_0 = data
                for transitions_type_0_item_data in _transitions_type_0:
                    transitions_type_0_item = cast(
                        list[Any], transitions_type_0_item_data
                    )

                    transitions_type_0.append(transitions_type_0_item)

                return transitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[Any]] | None | Unset, data)

        transitions = _parse_transitions(d.pop("transitions", UNSET))

        def _parse_funnel_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funnel_name = _parse_funnel_name(d.pop("funnel_name", UNSET))

        def _parse_funnel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funnel_id = _parse_funnel_id(d.pop("funnel_id", UNSET))

        proposal_detail = cls(
            id=id,
            name=name,
            customer=customer,
            customer_id=customer_id,
            created_at=created_at,
            internal_costs=internal_costs,
            external_value=external_value,
            margin=margin,
            margin_percent=margin_percent,
            currency=currency,
            currency_symbol=currency_symbol,
            owner_name=owner_name,
            days_in_stage=days_in_stage,
            product_count=product_count,
            days_since_last_activity=days_since_last_activity,
            last_activity=last_activity,
            transitions=transitions,
            funnel_name=funnel_name,
            funnel_id=funnel_id,
        )

        proposal_detail.additional_properties = d
        return proposal_detail

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
