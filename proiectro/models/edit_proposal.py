from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_proposal_pricing_strategy_type_0 import (
    EditProposalPricingStrategyType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditProposal")


@_attrs_define
class EditProposal:
    """
    Attributes:
        name (str):
        description (str):
        customer (str):
        owner (str):
        proposal_currency (str):
        internal_code (None | str | Unset):
        rfp_publication (None | str | Unset):
        pricing_strategy (EditProposalPricingStrategyType0 | None | Unset):  Default:
            EditProposalPricingStrategyType0.PRODUCT_PRICES.
        pricing_adjustment_percent (float | str | Unset):  Default: 0.0.
        pricing_adjustment_amount (float | str | Unset):  Default: 0.0.
        target_margin_percent (float | str | Unset):  Default: 30.0.
        minimum_margin_percent (float | str | Unset):  Default: 20.0.
        proposal_valid_since (None | str | Unset):
        proposal_valid_until (None | str | Unset):
        project_start_date (None | str | Unset):
        project_end_date (None | str | Unset):
        project_enable_booking_management (bool | None | Unset):
        project_enable_resource_management (bool | None | Unset):
        project_enable_effort_management (bool | None | Unset):
        project_enable_financial_management (bool | None | Unset):
        project_enable_schedule_management (bool | None | Unset):
        project_enable_earned_value_management (bool | None | Unset):
        wbsconfiguration (None | str | Unset):
    """

    name: str
    description: str
    customer: str
    owner: str
    proposal_currency: str
    internal_code: None | str | Unset = UNSET
    rfp_publication: None | str | Unset = UNSET
    pricing_strategy: EditProposalPricingStrategyType0 | None | Unset = (
        EditProposalPricingStrategyType0.PRODUCT_PRICES
    )
    pricing_adjustment_percent: float | str | Unset = 0.0
    pricing_adjustment_amount: float | str | Unset = 0.0
    target_margin_percent: float | str | Unset = 30.0
    minimum_margin_percent: float | str | Unset = 20.0
    proposal_valid_since: None | str | Unset = UNSET
    proposal_valid_until: None | str | Unset = UNSET
    project_start_date: None | str | Unset = UNSET
    project_end_date: None | str | Unset = UNSET
    project_enable_booking_management: bool | None | Unset = UNSET
    project_enable_resource_management: bool | None | Unset = UNSET
    project_enable_effort_management: bool | None | Unset = UNSET
    project_enable_financial_management: bool | None | Unset = UNSET
    project_enable_schedule_management: bool | None | Unset = UNSET
    project_enable_earned_value_management: bool | None | Unset = UNSET
    wbsconfiguration: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        customer = self.customer

        owner = self.owner

        proposal_currency = self.proposal_currency

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        rfp_publication: None | str | Unset
        if isinstance(self.rfp_publication, Unset):
            rfp_publication = UNSET
        else:
            rfp_publication = self.rfp_publication

        pricing_strategy: None | str | Unset
        if isinstance(self.pricing_strategy, Unset):
            pricing_strategy = UNSET
        elif isinstance(self.pricing_strategy, EditProposalPricingStrategyType0):
            pricing_strategy = self.pricing_strategy.value
        else:
            pricing_strategy = self.pricing_strategy

        pricing_adjustment_percent: float | str | Unset
        if isinstance(self.pricing_adjustment_percent, Unset):
            pricing_adjustment_percent = UNSET
        else:
            pricing_adjustment_percent = self.pricing_adjustment_percent

        pricing_adjustment_amount: float | str | Unset
        if isinstance(self.pricing_adjustment_amount, Unset):
            pricing_adjustment_amount = UNSET
        else:
            pricing_adjustment_amount = self.pricing_adjustment_amount

        target_margin_percent: float | str | Unset
        if isinstance(self.target_margin_percent, Unset):
            target_margin_percent = UNSET
        else:
            target_margin_percent = self.target_margin_percent

        minimum_margin_percent: float | str | Unset
        if isinstance(self.minimum_margin_percent, Unset):
            minimum_margin_percent = UNSET
        else:
            minimum_margin_percent = self.minimum_margin_percent

        proposal_valid_since: None | str | Unset
        if isinstance(self.proposal_valid_since, Unset):
            proposal_valid_since = UNSET
        else:
            proposal_valid_since = self.proposal_valid_since

        proposal_valid_until: None | str | Unset
        if isinstance(self.proposal_valid_until, Unset):
            proposal_valid_until = UNSET
        else:
            proposal_valid_until = self.proposal_valid_until

        project_start_date: None | str | Unset
        if isinstance(self.project_start_date, Unset):
            project_start_date = UNSET
        else:
            project_start_date = self.project_start_date

        project_end_date: None | str | Unset
        if isinstance(self.project_end_date, Unset):
            project_end_date = UNSET
        else:
            project_end_date = self.project_end_date

        project_enable_booking_management: bool | None | Unset
        if isinstance(self.project_enable_booking_management, Unset):
            project_enable_booking_management = UNSET
        else:
            project_enable_booking_management = self.project_enable_booking_management

        project_enable_resource_management: bool | None | Unset
        if isinstance(self.project_enable_resource_management, Unset):
            project_enable_resource_management = UNSET
        else:
            project_enable_resource_management = self.project_enable_resource_management

        project_enable_effort_management: bool | None | Unset
        if isinstance(self.project_enable_effort_management, Unset):
            project_enable_effort_management = UNSET
        else:
            project_enable_effort_management = self.project_enable_effort_management

        project_enable_financial_management: bool | None | Unset
        if isinstance(self.project_enable_financial_management, Unset):
            project_enable_financial_management = UNSET
        else:
            project_enable_financial_management = (
                self.project_enable_financial_management
            )

        project_enable_schedule_management: bool | None | Unset
        if isinstance(self.project_enable_schedule_management, Unset):
            project_enable_schedule_management = UNSET
        else:
            project_enable_schedule_management = self.project_enable_schedule_management

        project_enable_earned_value_management: bool | None | Unset
        if isinstance(self.project_enable_earned_value_management, Unset):
            project_enable_earned_value_management = UNSET
        else:
            project_enable_earned_value_management = (
                self.project_enable_earned_value_management
            )

        wbsconfiguration: None | str | Unset
        if isinstance(self.wbsconfiguration, Unset):
            wbsconfiguration = UNSET
        else:
            wbsconfiguration = self.wbsconfiguration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "customer": customer,
                "owner": owner,
                "proposal_currency": proposal_currency,
            }
        )
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if rfp_publication is not UNSET:
            field_dict["rfp_publication"] = rfp_publication
        if pricing_strategy is not UNSET:
            field_dict["pricing_strategy"] = pricing_strategy
        if pricing_adjustment_percent is not UNSET:
            field_dict["pricing_adjustment_percent"] = pricing_adjustment_percent
        if pricing_adjustment_amount is not UNSET:
            field_dict["pricing_adjustment_amount"] = pricing_adjustment_amount
        if target_margin_percent is not UNSET:
            field_dict["target_margin_percent"] = target_margin_percent
        if minimum_margin_percent is not UNSET:
            field_dict["minimum_margin_percent"] = minimum_margin_percent
        if proposal_valid_since is not UNSET:
            field_dict["proposal_valid_since"] = proposal_valid_since
        if proposal_valid_until is not UNSET:
            field_dict["proposal_valid_until"] = proposal_valid_until
        if project_start_date is not UNSET:
            field_dict["project_start_date"] = project_start_date
        if project_end_date is not UNSET:
            field_dict["project_end_date"] = project_end_date
        if project_enable_booking_management is not UNSET:
            field_dict["project_enable_booking_management"] = (
                project_enable_booking_management
            )
        if project_enable_resource_management is not UNSET:
            field_dict["project_enable_resource_management"] = (
                project_enable_resource_management
            )
        if project_enable_effort_management is not UNSET:
            field_dict["project_enable_effort_management"] = (
                project_enable_effort_management
            )
        if project_enable_financial_management is not UNSET:
            field_dict["project_enable_financial_management"] = (
                project_enable_financial_management
            )
        if project_enable_schedule_management is not UNSET:
            field_dict["project_enable_schedule_management"] = (
                project_enable_schedule_management
            )
        if project_enable_earned_value_management is not UNSET:
            field_dict["project_enable_earned_value_management"] = (
                project_enable_earned_value_management
            )
        if wbsconfiguration is not UNSET:
            field_dict["wbsconfiguration"] = wbsconfiguration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        customer = d.pop("customer")

        owner = d.pop("owner")

        proposal_currency = d.pop("proposal_currency")

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_rfp_publication(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rfp_publication = _parse_rfp_publication(d.pop("rfp_publication", UNSET))

        def _parse_pricing_strategy(
            data: object,
        ) -> EditProposalPricingStrategyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pricing_strategy_type_0 = EditProposalPricingStrategyType0(data)

                return pricing_strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditProposalPricingStrategyType0 | None | Unset, data)

        pricing_strategy = _parse_pricing_strategy(d.pop("pricing_strategy", UNSET))

        def _parse_pricing_adjustment_percent(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        pricing_adjustment_percent = _parse_pricing_adjustment_percent(
            d.pop("pricing_adjustment_percent", UNSET)
        )

        def _parse_pricing_adjustment_amount(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        pricing_adjustment_amount = _parse_pricing_adjustment_amount(
            d.pop("pricing_adjustment_amount", UNSET)
        )

        def _parse_target_margin_percent(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        target_margin_percent = _parse_target_margin_percent(
            d.pop("target_margin_percent", UNSET)
        )

        def _parse_minimum_margin_percent(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        minimum_margin_percent = _parse_minimum_margin_percent(
            d.pop("minimum_margin_percent", UNSET)
        )

        def _parse_proposal_valid_since(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposal_valid_since = _parse_proposal_valid_since(
            d.pop("proposal_valid_since", UNSET)
        )

        def _parse_proposal_valid_until(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposal_valid_until = _parse_proposal_valid_until(
            d.pop("proposal_valid_until", UNSET)
        )

        def _parse_project_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_start_date = _parse_project_start_date(
            d.pop("project_start_date", UNSET)
        )

        def _parse_project_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_end_date = _parse_project_end_date(d.pop("project_end_date", UNSET))

        def _parse_project_enable_booking_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_booking_management = _parse_project_enable_booking_management(
            d.pop("project_enable_booking_management", UNSET)
        )

        def _parse_project_enable_resource_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_resource_management = _parse_project_enable_resource_management(
            d.pop("project_enable_resource_management", UNSET)
        )

        def _parse_project_enable_effort_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_effort_management = _parse_project_enable_effort_management(
            d.pop("project_enable_effort_management", UNSET)
        )

        def _parse_project_enable_financial_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_financial_management = (
            _parse_project_enable_financial_management(
                d.pop("project_enable_financial_management", UNSET)
            )
        )

        def _parse_project_enable_schedule_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_schedule_management = _parse_project_enable_schedule_management(
            d.pop("project_enable_schedule_management", UNSET)
        )

        def _parse_project_enable_earned_value_management(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        project_enable_earned_value_management = (
            _parse_project_enable_earned_value_management(
                d.pop("project_enable_earned_value_management", UNSET)
            )
        )

        def _parse_wbsconfiguration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wbsconfiguration = _parse_wbsconfiguration(d.pop("wbsconfiguration", UNSET))

        edit_proposal = cls(
            name=name,
            description=description,
            customer=customer,
            owner=owner,
            proposal_currency=proposal_currency,
            internal_code=internal_code,
            rfp_publication=rfp_publication,
            pricing_strategy=pricing_strategy,
            pricing_adjustment_percent=pricing_adjustment_percent,
            pricing_adjustment_amount=pricing_adjustment_amount,
            target_margin_percent=target_margin_percent,
            minimum_margin_percent=minimum_margin_percent,
            proposal_valid_since=proposal_valid_since,
            proposal_valid_until=proposal_valid_until,
            project_start_date=project_start_date,
            project_end_date=project_end_date,
            project_enable_booking_management=project_enable_booking_management,
            project_enable_resource_management=project_enable_resource_management,
            project_enable_effort_management=project_enable_effort_management,
            project_enable_financial_management=project_enable_financial_management,
            project_enable_schedule_management=project_enable_schedule_management,
            project_enable_earned_value_management=project_enable_earned_value_management,
            wbsconfiguration=wbsconfiguration,
        )

        edit_proposal.additional_properties = d
        return edit_proposal

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
