from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funnel_won_proposals_currency_breakdown_type_0 import (
        FunnelWonProposalsCurrencyBreakdownType0,
    )
    from ..models.proposal_detail import ProposalDetail


T = TypeVar("T", bound="FunnelWonProposals")


@_attrs_define
class FunnelWonProposals:
    """
    Attributes:
        proposals (list[ProposalDetail]):
        funnel_name (str):
        funnel_id (str):
        total_value (float | str):
        total_count (int):
        currency_symbol (str):
        has_mixed_currencies (bool):
        stage_type (str):
        currency_breakdown (FunnelWonProposalsCurrencyBreakdownType0 | None | Unset):
    """

    proposals: list[ProposalDetail]
    funnel_name: str
    funnel_id: str
    total_value: float | str
    total_count: int
    currency_symbol: str
    has_mixed_currencies: bool
    stage_type: str
    currency_breakdown: FunnelWonProposalsCurrencyBreakdownType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.funnel_won_proposals_currency_breakdown_type_0 import (
            FunnelWonProposalsCurrencyBreakdownType0,
        )

        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        funnel_name = self.funnel_name

        funnel_id = self.funnel_id

        total_value: float | str
        total_value = self.total_value

        total_count = self.total_count

        currency_symbol = self.currency_symbol

        has_mixed_currencies = self.has_mixed_currencies

        stage_type = self.stage_type

        currency_breakdown: dict[str, Any] | None | Unset
        if isinstance(self.currency_breakdown, Unset):
            currency_breakdown = UNSET
        elif isinstance(
            self.currency_breakdown, FunnelWonProposalsCurrencyBreakdownType0
        ):
            currency_breakdown = self.currency_breakdown.to_dict()
        else:
            currency_breakdown = self.currency_breakdown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposals": proposals,
                "funnel_name": funnel_name,
                "funnel_id": funnel_id,
                "total_value": total_value,
                "total_count": total_count,
                "currency_symbol": currency_symbol,
                "has_mixed_currencies": has_mixed_currencies,
                "stage_type": stage_type,
            }
        )
        if currency_breakdown is not UNSET:
            field_dict["currency_breakdown"] = currency_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.funnel_won_proposals_currency_breakdown_type_0 import (
            FunnelWonProposalsCurrencyBreakdownType0,
        )
        from ..models.proposal_detail import ProposalDetail

        d = dict(src_dict)
        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = ProposalDetail.from_dict(proposals_item_data)

            proposals.append(proposals_item)

        funnel_name = d.pop("funnel_name")

        funnel_id = d.pop("funnel_id")

        def _parse_total_value(data: object) -> float | str:
            return cast(float | str, data)

        total_value = _parse_total_value(d.pop("total_value"))

        total_count = d.pop("total_count")

        currency_symbol = d.pop("currency_symbol")

        has_mixed_currencies = d.pop("has_mixed_currencies")

        stage_type = d.pop("stage_type")

        def _parse_currency_breakdown(
            data: object,
        ) -> FunnelWonProposalsCurrencyBreakdownType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                currency_breakdown_type_0 = (
                    FunnelWonProposalsCurrencyBreakdownType0.from_dict(data)
                )

                return currency_breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FunnelWonProposalsCurrencyBreakdownType0 | None | Unset, data)

        currency_breakdown = _parse_currency_breakdown(
            d.pop("currency_breakdown", UNSET)
        )

        funnel_won_proposals = cls(
            proposals=proposals,
            funnel_name=funnel_name,
            funnel_id=funnel_id,
            total_value=total_value,
            total_count=total_count,
            currency_symbol=currency_symbol,
            has_mixed_currencies=has_mixed_currencies,
            stage_type=stage_type,
            currency_breakdown=currency_breakdown,
        )

        funnel_won_proposals.additional_properties = d
        return funnel_won_proposals

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
