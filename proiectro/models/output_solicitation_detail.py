from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputSolicitationDetail")


@_attrs_define
class OutputSolicitationDetail:
    """Full details of an RFP received from a partner (solicitation)

    Attributes:
        id (str):
        rfp_id (str):
        name (str):
        description (str):
        category_display (str):
        currency_code (str):
        budget_min (float | None | str):
        budget_max (float | None | str):
        submission_deadline (str):
        status (str):
        status_display (str):
        issuer_name (str):
        bridge_id (str):
        publication_state (str):
        publication_state_display (str):
        published_at (str):
        viewed_at (None | str):
        intent_to_respond (bool | None):
        intent_declared_at (None | str):
        intent_note (str):
        is_winner (bool | Unset):  Default: False.
    """

    id: str
    rfp_id: str
    name: str
    description: str
    category_display: str
    currency_code: str
    budget_min: float | None | str
    budget_max: float | None | str
    submission_deadline: str
    status: str
    status_display: str
    issuer_name: str
    bridge_id: str
    publication_state: str
    publication_state_display: str
    published_at: str
    viewed_at: None | str
    intent_to_respond: bool | None
    intent_declared_at: None | str
    intent_note: str
    is_winner: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rfp_id = self.rfp_id

        name = self.name

        description = self.description

        category_display = self.category_display

        currency_code = self.currency_code

        budget_min: float | None | str
        budget_min = self.budget_min

        budget_max: float | None | str
        budget_max = self.budget_max

        submission_deadline = self.submission_deadline

        status = self.status

        status_display = self.status_display

        issuer_name = self.issuer_name

        bridge_id = self.bridge_id

        publication_state = self.publication_state

        publication_state_display = self.publication_state_display

        published_at = self.published_at

        viewed_at: None | str
        viewed_at = self.viewed_at

        intent_to_respond: bool | None
        intent_to_respond = self.intent_to_respond

        intent_declared_at: None | str
        intent_declared_at = self.intent_declared_at

        intent_note = self.intent_note

        is_winner = self.is_winner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rfp_id": rfp_id,
                "name": name,
                "description": description,
                "category_display": category_display,
                "currency_code": currency_code,
                "budget_min": budget_min,
                "budget_max": budget_max,
                "submission_deadline": submission_deadline,
                "status": status,
                "status_display": status_display,
                "issuer_name": issuer_name,
                "bridge_id": bridge_id,
                "publication_state": publication_state,
                "publication_state_display": publication_state_display,
                "published_at": published_at,
                "viewed_at": viewed_at,
                "intent_to_respond": intent_to_respond,
                "intent_declared_at": intent_declared_at,
                "intent_note": intent_note,
            }
        )
        if is_winner is not UNSET:
            field_dict["is_winner"] = is_winner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rfp_id = d.pop("rfp_id")

        name = d.pop("name")

        description = d.pop("description")

        category_display = d.pop("category_display")

        currency_code = d.pop("currency_code")

        def _parse_budget_min(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        budget_min = _parse_budget_min(d.pop("budget_min"))

        def _parse_budget_max(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        budget_max = _parse_budget_max(d.pop("budget_max"))

        submission_deadline = d.pop("submission_deadline")

        status = d.pop("status")

        status_display = d.pop("status_display")

        issuer_name = d.pop("issuer_name")

        bridge_id = d.pop("bridge_id")

        publication_state = d.pop("publication_state")

        publication_state_display = d.pop("publication_state_display")

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

        intent_note = d.pop("intent_note")

        is_winner = d.pop("is_winner", UNSET)

        output_solicitation_detail = cls(
            id=id,
            rfp_id=rfp_id,
            name=name,
            description=description,
            category_display=category_display,
            currency_code=currency_code,
            budget_min=budget_min,
            budget_max=budget_max,
            submission_deadline=submission_deadline,
            status=status,
            status_display=status_display,
            issuer_name=issuer_name,
            bridge_id=bridge_id,
            publication_state=publication_state,
            publication_state_display=publication_state_display,
            published_at=published_at,
            viewed_at=viewed_at,
            intent_to_respond=intent_to_respond,
            intent_declared_at=intent_declared_at,
            intent_note=intent_note,
            is_winner=is_winner,
        )

        output_solicitation_detail.additional_properties = d
        return output_solicitation_detail

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
