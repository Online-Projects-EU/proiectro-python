from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeProposalStage")


@_attrs_define
class ChangeProposalStage:
    """
    Attributes:
        i_have_followed_the_instructions (bool | None | Unset):
        contact_id (None | str | Unset):
        rejection_reason (None | str | Unset):
    """

    i_have_followed_the_instructions: bool | None | Unset = UNSET
    contact_id: None | str | Unset = UNSET
    rejection_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        i_have_followed_the_instructions: bool | None | Unset
        if isinstance(self.i_have_followed_the_instructions, Unset):
            i_have_followed_the_instructions = UNSET
        else:
            i_have_followed_the_instructions = self.i_have_followed_the_instructions

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = self.contact_id

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if i_have_followed_the_instructions is not UNSET:
            field_dict["i_have_followed_the_instructions"] = (
                i_have_followed_the_instructions
            )
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if rejection_reason is not UNSET:
            field_dict["rejection_reason"] = rejection_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_i_have_followed_the_instructions(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        i_have_followed_the_instructions = _parse_i_have_followed_the_instructions(
            d.pop("i_have_followed_the_instructions", UNSET)
        )

        def _parse_contact_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_id = _parse_contact_id(d.pop("contact_id", UNSET))

        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason", UNSET))

        change_proposal_stage = cls(
            i_have_followed_the_instructions=i_have_followed_the_instructions,
            contact_id=contact_id,
            rejection_reason=rejection_reason,
        )

        change_proposal_stage.additional_properties = d
        return change_proposal_stage

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
