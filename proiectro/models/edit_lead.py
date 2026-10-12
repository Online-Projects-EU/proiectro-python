from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.edit_lead_source import EditLeadSource
from ..models.edit_lead_status import EditLeadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditLead")


@_attrs_define
class EditLead:
    """
    Attributes:
        name (str):
        updated_at (datetime.datetime):
        company_name (None | str | Unset):  Default: ''.
        email (None | str | Unset):
        phone (None | str | Unset):  Default: ''.
        job_title (None | str | Unset):  Default: ''.
        source (EditLeadSource | Unset):  Default: EditLeadSource.OTHER.
        source_note (None | str | Unset):  Default: ''.
        status (EditLeadStatus | Unset):  Default: EditLeadStatus.NEW.
        owner (None | str | Unset):
        lead_list (None | str | Unset):
        next_action_at (None | str | Unset):
        next_action_channel (None | str | Unset):  Default: ''.
        next_action_note (None | str | Unset):  Default: ''.
        notes (None | str | Unset):  Default: ''.
        profile_url (None | str | Unset):  Default: ''.
        company_url (None | str | Unset):  Default: ''.
        country (None | str | Unset):
        score (int | None | Unset):
    """

    name: str
    updated_at: datetime.datetime
    company_name: None | str | Unset = ""
    email: None | str | Unset = UNSET
    phone: None | str | Unset = ""
    job_title: None | str | Unset = ""
    source: EditLeadSource | Unset = EditLeadSource.OTHER
    source_note: None | str | Unset = ""
    status: EditLeadStatus | Unset = EditLeadStatus.NEW
    owner: None | str | Unset = UNSET
    lead_list: None | str | Unset = UNSET
    next_action_at: None | str | Unset = UNSET
    next_action_channel: None | str | Unset = ""
    next_action_note: None | str | Unset = ""
    notes: None | str | Unset = ""
    profile_url: None | str | Unset = ""
    company_url: None | str | Unset = ""
    country: None | str | Unset = UNSET
    score: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        updated_at = self.updated_at.isoformat()

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        source_note: None | str | Unset
        if isinstance(self.source_note, Unset):
            source_note = UNSET
        else:
            source_note = self.source_note

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        lead_list: None | str | Unset
        if isinstance(self.lead_list, Unset):
            lead_list = UNSET
        else:
            lead_list = self.lead_list

        next_action_at: None | str | Unset
        if isinstance(self.next_action_at, Unset):
            next_action_at = UNSET
        else:
            next_action_at = self.next_action_at

        next_action_channel: None | str | Unset
        if isinstance(self.next_action_channel, Unset):
            next_action_channel = UNSET
        else:
            next_action_channel = self.next_action_channel

        next_action_note: None | str | Unset
        if isinstance(self.next_action_note, Unset):
            next_action_note = UNSET
        else:
            next_action_note = self.next_action_note

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        profile_url: None | str | Unset
        if isinstance(self.profile_url, Unset):
            profile_url = UNSET
        else:
            profile_url = self.profile_url

        company_url: None | str | Unset
        if isinstance(self.company_url, Unset):
            company_url = UNSET
        else:
            company_url = self.company_url

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        score: int | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "updated_at": updated_at,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if source is not UNSET:
            field_dict["source"] = source
        if source_note is not UNSET:
            field_dict["source_note"] = source_note
        if status is not UNSET:
            field_dict["status"] = status
        if owner is not UNSET:
            field_dict["owner"] = owner
        if lead_list is not UNSET:
            field_dict["lead_list"] = lead_list
        if next_action_at is not UNSET:
            field_dict["next_action_at"] = next_action_at
        if next_action_channel is not UNSET:
            field_dict["next_action_channel"] = next_action_channel
        if next_action_note is not UNSET:
            field_dict["next_action_note"] = next_action_note
        if notes is not UNSET:
            field_dict["notes"] = notes
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url
        if company_url is not UNSET:
            field_dict["company_url"] = company_url
        if country is not UNSET:
            field_dict["country"] = country
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("job_title", UNSET))

        _source = d.pop("source", UNSET)
        source: EditLeadSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = EditLeadSource(_source)

        def _parse_source_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_note = _parse_source_note(d.pop("source_note", UNSET))

        _status = d.pop("status", UNSET)
        status: EditLeadStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EditLeadStatus(_status)

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_lead_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_list = _parse_lead_list(d.pop("lead_list", UNSET))

        def _parse_next_action_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_action_at = _parse_next_action_at(d.pop("next_action_at", UNSET))

        def _parse_next_action_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_action_channel = _parse_next_action_channel(
            d.pop("next_action_channel", UNSET)
        )

        def _parse_next_action_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_action_note = _parse_next_action_note(d.pop("next_action_note", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_profile_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_url = _parse_profile_url(d.pop("profile_url", UNSET))

        def _parse_company_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_url = _parse_company_url(d.pop("company_url", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        edit_lead = cls(
            name=name,
            updated_at=updated_at,
            company_name=company_name,
            email=email,
            phone=phone,
            job_title=job_title,
            source=source,
            source_note=source_note,
            status=status,
            owner=owner,
            lead_list=lead_list,
            next_action_at=next_action_at,
            next_action_channel=next_action_channel,
            next_action_note=next_action_note,
            notes=notes,
            profile_url=profile_url,
            company_url=company_url,
            country=country,
            score=score,
        )

        edit_lead.additional_properties = d
        return edit_lead

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
