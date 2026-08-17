from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="OutputLead")



@_attrs_define
class OutputLead:
    """ Lead detail page payload.

        Attributes:
            id (str):
            name (str):
            source (str):
            source_label (str):
            status (str):
            status_label (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            company_name (str | Unset):  Default: ''.
            email (None | str | Unset):
            phone (str | Unset):  Default: ''.
            job_title (str | Unset):  Default: ''.
            source_note (str | Unset):  Default: ''.
            owner_id (None | str | Unset):
            owner_name (None | str | Unset):
            owner_avatar_url (None | str | Unset):
            lead_list_id (None | str | Unset):
            lead_list_name (None | str | Unset):
            next_action_at (datetime.datetime | None | Unset):
            next_action_channel (str | Unset):  Default: ''.
            next_action_note (str | Unset):  Default: ''.
            last_action_at (datetime.datetime | None | Unset):
            notes (str | Unset):  Default: ''.
            profile_url (str | Unset):  Default: ''.
            company_url (str | Unset):  Default: ''.
            country (None | str | Unset):
            score (int | None | Unset):
            converted_to_org_id (None | str | Unset):
            converted_to_org_name (None | str | Unset):
            converted_at (datetime.datetime | None | Unset):
            created_by_name (None | str | Unset):
     """

    id: str
    name: str
    source: str
    source_label: str
    status: str
    status_label: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    company_name: str | Unset = ''
    email: None | str | Unset = UNSET
    phone: str | Unset = ''
    job_title: str | Unset = ''
    source_note: str | Unset = ''
    owner_id: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_avatar_url: None | str | Unset = UNSET
    lead_list_id: None | str | Unset = UNSET
    lead_list_name: None | str | Unset = UNSET
    next_action_at: datetime.datetime | None | Unset = UNSET
    next_action_channel: str | Unset = ''
    next_action_note: str | Unset = ''
    last_action_at: datetime.datetime | None | Unset = UNSET
    notes: str | Unset = ''
    profile_url: str | Unset = ''
    company_url: str | Unset = ''
    country: None | str | Unset = UNSET
    score: int | None | Unset = UNSET
    converted_to_org_id: None | str | Unset = UNSET
    converted_to_org_name: None | str | Unset = UNSET
    converted_at: datetime.datetime | None | Unset = UNSET
    created_by_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        source = self.source

        source_label = self.source_label

        status = self.status

        status_label = self.status_label

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        company_name = self.company_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone = self.phone

        job_title = self.job_title

        source_note = self.source_note

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_avatar_url: None | str | Unset
        if isinstance(self.owner_avatar_url, Unset):
            owner_avatar_url = UNSET
        else:
            owner_avatar_url = self.owner_avatar_url

        lead_list_id: None | str | Unset
        if isinstance(self.lead_list_id, Unset):
            lead_list_id = UNSET
        else:
            lead_list_id = self.lead_list_id

        lead_list_name: None | str | Unset
        if isinstance(self.lead_list_name, Unset):
            lead_list_name = UNSET
        else:
            lead_list_name = self.lead_list_name

        next_action_at: None | str | Unset
        if isinstance(self.next_action_at, Unset):
            next_action_at = UNSET
        elif isinstance(self.next_action_at, datetime.datetime):
            next_action_at = self.next_action_at.isoformat()
        else:
            next_action_at = self.next_action_at

        next_action_channel = self.next_action_channel

        next_action_note = self.next_action_note

        last_action_at: None | str | Unset
        if isinstance(self.last_action_at, Unset):
            last_action_at = UNSET
        elif isinstance(self.last_action_at, datetime.datetime):
            last_action_at = self.last_action_at.isoformat()
        else:
            last_action_at = self.last_action_at

        notes = self.notes

        profile_url = self.profile_url

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

        converted_to_org_id: None | str | Unset
        if isinstance(self.converted_to_org_id, Unset):
            converted_to_org_id = UNSET
        else:
            converted_to_org_id = self.converted_to_org_id

        converted_to_org_name: None | str | Unset
        if isinstance(self.converted_to_org_name, Unset):
            converted_to_org_name = UNSET
        else:
            converted_to_org_name = self.converted_to_org_name

        converted_at: None | str | Unset
        if isinstance(self.converted_at, Unset):
            converted_at = UNSET
        elif isinstance(self.converted_at, datetime.datetime):
            converted_at = self.converted_at.isoformat()
        else:
            converted_at = self.converted_at

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "source": source,
            "source_label": source_label,
            "status": status,
            "status_label": status_label,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if source_note is not UNSET:
            field_dict["source_note"] = source_note
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if owner_avatar_url is not UNSET:
            field_dict["owner_avatar_url"] = owner_avatar_url
        if lead_list_id is not UNSET:
            field_dict["lead_list_id"] = lead_list_id
        if lead_list_name is not UNSET:
            field_dict["lead_list_name"] = lead_list_name
        if next_action_at is not UNSET:
            field_dict["next_action_at"] = next_action_at
        if next_action_channel is not UNSET:
            field_dict["next_action_channel"] = next_action_channel
        if next_action_note is not UNSET:
            field_dict["next_action_note"] = next_action_note
        if last_action_at is not UNSET:
            field_dict["last_action_at"] = last_action_at
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
        if converted_to_org_id is not UNSET:
            field_dict["converted_to_org_id"] = converted_to_org_id
        if converted_to_org_name is not UNSET:
            field_dict["converted_to_org_name"] = converted_to_org_name
        if converted_at is not UNSET:
            field_dict["converted_at"] = converted_at
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        source = d.pop("source")

        source_label = d.pop("source_label")

        status = d.pop("status")

        status_label = d.pop("status_label")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        company_name = d.pop("company_name", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        phone = d.pop("phone", UNSET)

        job_title = d.pop("job_title", UNSET)

        source_note = d.pop("source_note", UNSET)

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))


        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))


        def _parse_owner_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_avatar_url = _parse_owner_avatar_url(d.pop("owner_avatar_url", UNSET))


        def _parse_lead_list_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_list_id = _parse_lead_list_id(d.pop("lead_list_id", UNSET))


        def _parse_lead_list_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_list_name = _parse_lead_list_name(d.pop("lead_list_name", UNSET))


        def _parse_next_action_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_action_at_type_0 = isoparse(data)



                return next_action_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_action_at = _parse_next_action_at(d.pop("next_action_at", UNSET))


        next_action_channel = d.pop("next_action_channel", UNSET)

        next_action_note = d.pop("next_action_note", UNSET)

        def _parse_last_action_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_action_at_type_0 = isoparse(data)



                return last_action_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_action_at = _parse_last_action_at(d.pop("last_action_at", UNSET))


        notes = d.pop("notes", UNSET)

        profile_url = d.pop("profile_url", UNSET)

        company_url = d.pop("company_url", UNSET)

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


        def _parse_converted_to_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        converted_to_org_id = _parse_converted_to_org_id(d.pop("converted_to_org_id", UNSET))


        def _parse_converted_to_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        converted_to_org_name = _parse_converted_to_org_name(d.pop("converted_to_org_name", UNSET))


        def _parse_converted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                converted_at_type_0 = isoparse(data)



                return converted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        converted_at = _parse_converted_at(d.pop("converted_at", UNSET))


        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("created_by_name", UNSET))


        output_lead = cls(
            id=id,
            name=name,
            source=source,
            source_label=source_label,
            status=status,
            status_label=status_label,
            created_at=created_at,
            updated_at=updated_at,
            company_name=company_name,
            email=email,
            phone=phone,
            job_title=job_title,
            source_note=source_note,
            owner_id=owner_id,
            owner_name=owner_name,
            owner_avatar_url=owner_avatar_url,
            lead_list_id=lead_list_id,
            lead_list_name=lead_list_name,
            next_action_at=next_action_at,
            next_action_channel=next_action_channel,
            next_action_note=next_action_note,
            last_action_at=last_action_at,
            notes=notes,
            profile_url=profile_url,
            company_url=company_url,
            country=country,
            score=score,
            converted_to_org_id=converted_to_org_id,
            converted_to_org_name=converted_to_org_name,
            converted_at=converted_at,
            created_by_name=created_by_name,
        )


        output_lead.additional_properties = d
        return output_lead

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
