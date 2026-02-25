from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputRFPPublicationItem")


@_attrs_define
class OutputRFPPublicationItem:
    """Single publication entry for RFP detail view

    Attributes:
        id (str):
        partner_name (str):
        bridge_id (str):
        state (str):
        state_display (str):
        published_at (str):
        viewed_at (None | str):
        intent_to_respond (bool | None):
        intent_declared_at (None | str):
        is_shortlisted (bool):
        is_winner (bool):
        has_proposal (bool | Unset):  Default: False.
        proposal_id (None | str | Unset):
        has_proposal_grant (bool | Unset):  Default: False.
    """

    id: str
    partner_name: str
    bridge_id: str
    state: str
    state_display: str
    published_at: str
    viewed_at: None | str
    intent_to_respond: bool | None
    intent_declared_at: None | str
    is_shortlisted: bool
    is_winner: bool
    has_proposal: bool | Unset = False
    proposal_id: None | str | Unset = UNSET
    has_proposal_grant: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        partner_name = self.partner_name

        bridge_id = self.bridge_id

        state = self.state

        state_display = self.state_display

        published_at = self.published_at

        viewed_at: None | str
        viewed_at = self.viewed_at

        intent_to_respond: bool | None
        intent_to_respond = self.intent_to_respond

        intent_declared_at: None | str
        intent_declared_at = self.intent_declared_at

        is_shortlisted = self.is_shortlisted

        is_winner = self.is_winner

        has_proposal = self.has_proposal

        proposal_id: None | str | Unset
        if isinstance(self.proposal_id, Unset):
            proposal_id = UNSET
        else:
            proposal_id = self.proposal_id

        has_proposal_grant = self.has_proposal_grant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "partner_name": partner_name,
                "bridge_id": bridge_id,
                "state": state,
                "state_display": state_display,
                "published_at": published_at,
                "viewed_at": viewed_at,
                "intent_to_respond": intent_to_respond,
                "intent_declared_at": intent_declared_at,
                "is_shortlisted": is_shortlisted,
                "is_winner": is_winner,
            }
        )
        if has_proposal is not UNSET:
            field_dict["has_proposal"] = has_proposal
        if proposal_id is not UNSET:
            field_dict["proposal_id"] = proposal_id
        if has_proposal_grant is not UNSET:
            field_dict["has_proposal_grant"] = has_proposal_grant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        partner_name = d.pop("partner_name")

        bridge_id = d.pop("bridge_id")

        state = d.pop("state")

        state_display = d.pop("state_display")

        published_at = d.pop("published_at")

        def _parse_viewed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        viewed_at = _parse_viewed_at(d.pop("viewed_at"))

        def _parse_intent_to_respond(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        intent_to_respond = _parse_intent_to_respond(d.pop("intent_to_respond"))

        def _parse_intent_declared_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        intent_declared_at = _parse_intent_declared_at(d.pop("intent_declared_at"))

        is_shortlisted = d.pop("is_shortlisted")

        is_winner = d.pop("is_winner")

        has_proposal = d.pop("has_proposal", UNSET)

        def _parse_proposal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposal_id = _parse_proposal_id(d.pop("proposal_id", UNSET))

        has_proposal_grant = d.pop("has_proposal_grant", UNSET)

        output_rfp_publication_item = cls(
            id=id,
            partner_name=partner_name,
            bridge_id=bridge_id,
            state=state,
            state_display=state_display,
            published_at=published_at,
            viewed_at=viewed_at,
            intent_to_respond=intent_to_respond,
            intent_declared_at=intent_declared_at,
            is_shortlisted=is_shortlisted,
            is_winner=is_winner,
            has_proposal=has_proposal,
            proposal_id=proposal_id,
            has_proposal_grant=has_proposal_grant,
        )

        output_rfp_publication_item.additional_properties = d
        return output_rfp_publication_item

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
