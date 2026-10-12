from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.fast_proposal_stage_option import FastProposalStageOption


T = TypeVar("T", bound="OutputFastProposalOptions")


@_attrs_define
class OutputFastProposalOptions:
    """What a client needs before offering the Fast Proposal form for one lead.

    `blockers` is the same list the web form shows instead of its fields: when it is not empty,
    submitting cannot succeed. `updated_at` is the lead's, for the submit's optimistic lock.

        Attributes:
            lead_id (str):
            updated_at (datetime.datetime):
            customer_name (str):
            has_customer_org (bool):
            currency_code (str):
            currency_symbol (str):
            stages (list[FastProposalStageOption]):
            blockers (list[str]):
    """

    lead_id: str
    updated_at: datetime.datetime
    customer_name: str
    has_customer_org: bool
    currency_code: str
    currency_symbol: str
    stages: list[FastProposalStageOption]
    blockers: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lead_id = self.lead_id

        updated_at = self.updated_at.isoformat()

        customer_name = self.customer_name

        has_customer_org = self.has_customer_org

        currency_code = self.currency_code

        currency_symbol = self.currency_symbol

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        blockers = self.blockers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lead_id": lead_id,
                "updated_at": updated_at,
                "customer_name": customer_name,
                "has_customer_org": has_customer_org,
                "currency_code": currency_code,
                "currency_symbol": currency_symbol,
                "stages": stages,
                "blockers": blockers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fast_proposal_stage_option import FastProposalStageOption

        d = dict(src_dict)
        lead_id = d.pop("lead_id")

        updated_at = isoparse(d.pop("updated_at"))

        customer_name = d.pop("customer_name")

        has_customer_org = d.pop("has_customer_org")

        currency_code = d.pop("currency_code")

        currency_symbol = d.pop("currency_symbol")

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = FastProposalStageOption.from_dict(stages_item_data)

            stages.append(stages_item)

        blockers = cast(list[str], d.pop("blockers"))

        output_fast_proposal_options = cls(
            lead_id=lead_id,
            updated_at=updated_at,
            customer_name=customer_name,
            has_customer_org=has_customer_org,
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            stages=stages,
            blockers=blockers,
        )

        output_fast_proposal_options.additional_properties = d
        return output_fast_proposal_options

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
