from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.output_share_proposal_state import OutputShareProposalState
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputShareProposal")


@_attrs_define
class OutputShareProposal:
    """
    Attributes:
        id (str):
        proposal_id (str):
        name (str):
        state (OutputShareProposalState):
        added_at (datetime.datetime):
        sent_at (datetime.datetime | None | Unset):
        proposal_sent_at (datetime.datetime | None | Unset):
        published (bool | Unset):  Default: False.
        added_by (None | str | Unset):
    """

    id: str
    proposal_id: str
    name: str
    state: OutputShareProposalState
    added_at: datetime.datetime
    sent_at: datetime.datetime | None | Unset = UNSET
    proposal_sent_at: datetime.datetime | None | Unset = UNSET
    published: bool | Unset = False
    added_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        proposal_id = self.proposal_id

        name = self.name

        state = self.state.value

        added_at = self.added_at.isoformat()

        sent_at: None | str | Unset
        if isinstance(self.sent_at, Unset):
            sent_at = UNSET
        elif isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        proposal_sent_at: None | str | Unset
        if isinstance(self.proposal_sent_at, Unset):
            proposal_sent_at = UNSET
        elif isinstance(self.proposal_sent_at, datetime.datetime):
            proposal_sent_at = self.proposal_sent_at.isoformat()
        else:
            proposal_sent_at = self.proposal_sent_at

        published = self.published

        added_by: None | str | Unset
        if isinstance(self.added_by, Unset):
            added_by = UNSET
        else:
            added_by = self.added_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "proposal_id": proposal_id,
                "name": name,
                "state": state,
                "added_at": added_at,
            }
        )
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if proposal_sent_at is not UNSET:
            field_dict["proposal_sent_at"] = proposal_sent_at
        if published is not UNSET:
            field_dict["published"] = published
        if added_by is not UNSET:
            field_dict["added_by"] = added_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        proposal_id = d.pop("proposal_id")

        name = d.pop("name")

        state = OutputShareProposalState(d.pop("state"))

        added_at = isoparse(d.pop("added_at"))

        def _parse_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = isoparse(data)

                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sent_at = _parse_sent_at(d.pop("sent_at", UNSET))

        def _parse_proposal_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proposal_sent_at_type_0 = isoparse(data)

                return proposal_sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        proposal_sent_at = _parse_proposal_sent_at(d.pop("proposal_sent_at", UNSET))

        published = d.pop("published", UNSET)

        def _parse_added_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by = _parse_added_by(d.pop("added_by", UNSET))

        output_share_proposal = cls(
            id=id,
            proposal_id=proposal_id,
            name=name,
            state=state,
            added_at=added_at,
            sent_at=sent_at,
            proposal_sent_at=proposal_sent_at,
            published=published,
            added_by=added_by,
        )

        output_share_proposal.additional_properties = d
        return output_share_proposal

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
