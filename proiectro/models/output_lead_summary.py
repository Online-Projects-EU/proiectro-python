from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_tag import OutputTag


T = TypeVar("T", bound="OutputLeadSummary")


@_attrs_define
class OutputLeadSummary:
    """Compact representation used in list/bucket views and the worklist.

    Attributes:
        id (str):
        name (str):
        status (str):
        status_label (str):
        source (str):
        source_label (str):
        company_name (str | Unset):  Default: ''.
        email (None | str | Unset):
        phone (str | Unset):  Default: ''.
        job_title (str | Unset):  Default: ''.
        owner_id (None | str | Unset):
        owner_name (None | str | Unset):
        owner_avatar_url (None | str | Unset):
        lead_list_id (None | str | Unset):
        lead_list_name (None | str | Unset):
        next_action_at (datetime.datetime | None | Unset):
        next_action_channel (str | Unset):  Default: ''.
        next_action_channel_label (str | Unset):  Default: ''.
        last_action_at (datetime.datetime | None | Unset):
        last_actor_name (None | str | Unset):
        last_actor_avatar_url (None | str | Unset):
        score (int | None | Unset):
        country (None | str | Unset):
        tags (list[OutputTag] | Unset):
        converted_at (datetime.datetime | None | Unset):
        converted_to_org_id (None | str | Unset):
        converted_to_org_name (None | str | Unset):
        closed_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    status: str
    status_label: str
    source: str
    source_label: str
    company_name: str | Unset = ""
    email: None | str | Unset = UNSET
    phone: str | Unset = ""
    job_title: str | Unset = ""
    owner_id: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_avatar_url: None | str | Unset = UNSET
    lead_list_id: None | str | Unset = UNSET
    lead_list_name: None | str | Unset = UNSET
    next_action_at: datetime.datetime | None | Unset = UNSET
    next_action_channel: str | Unset = ""
    next_action_channel_label: str | Unset = ""
    last_action_at: datetime.datetime | None | Unset = UNSET
    last_actor_name: None | str | Unset = UNSET
    last_actor_avatar_url: None | str | Unset = UNSET
    score: int | None | Unset = UNSET
    country: None | str | Unset = UNSET
    tags: list[OutputTag] | Unset = UNSET
    converted_at: datetime.datetime | None | Unset = UNSET
    converted_to_org_id: None | str | Unset = UNSET
    converted_to_org_name: None | str | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        status_label = self.status_label

        source = self.source

        source_label = self.source_label

        company_name = self.company_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone = self.phone

        job_title = self.job_title

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

        next_action_channel_label = self.next_action_channel_label

        last_action_at: None | str | Unset
        if isinstance(self.last_action_at, Unset):
            last_action_at = UNSET
        elif isinstance(self.last_action_at, datetime.datetime):
            last_action_at = self.last_action_at.isoformat()
        else:
            last_action_at = self.last_action_at

        last_actor_name: None | str | Unset
        if isinstance(self.last_actor_name, Unset):
            last_actor_name = UNSET
        else:
            last_actor_name = self.last_actor_name

        last_actor_avatar_url: None | str | Unset
        if isinstance(self.last_actor_avatar_url, Unset):
            last_actor_avatar_url = UNSET
        else:
            last_actor_avatar_url = self.last_actor_avatar_url

        score: int | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        converted_at: None | str | Unset
        if isinstance(self.converted_at, Unset):
            converted_at = UNSET
        elif isinstance(self.converted_at, datetime.datetime):
            converted_at = self.converted_at.isoformat()
        else:
            converted_at = self.converted_at

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

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "status_label": status_label,
                "source": source,
                "source_label": source_label,
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
        if next_action_channel_label is not UNSET:
            field_dict["next_action_channel_label"] = next_action_channel_label
        if last_action_at is not UNSET:
            field_dict["last_action_at"] = last_action_at
        if last_actor_name is not UNSET:
            field_dict["last_actor_name"] = last_actor_name
        if last_actor_avatar_url is not UNSET:
            field_dict["last_actor_avatar_url"] = last_actor_avatar_url
        if score is not UNSET:
            field_dict["score"] = score
        if country is not UNSET:
            field_dict["country"] = country
        if tags is not UNSET:
            field_dict["tags"] = tags
        if converted_at is not UNSET:
            field_dict["converted_at"] = converted_at
        if converted_to_org_id is not UNSET:
            field_dict["converted_to_org_id"] = converted_to_org_id
        if converted_to_org_name is not UNSET:
            field_dict["converted_to_org_name"] = converted_to_org_name
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tag import OutputTag

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status")

        status_label = d.pop("status_label")

        source = d.pop("source")

        source_label = d.pop("source_label")

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

        next_action_channel_label = d.pop("next_action_channel_label", UNSET)

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

        def _parse_last_actor_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_actor_name = _parse_last_actor_name(d.pop("last_actor_name", UNSET))

        def _parse_last_actor_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_actor_avatar_url = _parse_last_actor_avatar_url(
            d.pop("last_actor_avatar_url", UNSET)
        )

        def _parse_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[OutputTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = OutputTag.from_dict(tags_item_data)

                tags.append(tags_item)

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

        def _parse_converted_to_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        converted_to_org_id = _parse_converted_to_org_id(
            d.pop("converted_to_org_id", UNSET)
        )

        def _parse_converted_to_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        converted_to_org_name = _parse_converted_to_org_name(
            d.pop("converted_to_org_name", UNSET)
        )

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = isoparse(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        output_lead_summary = cls(
            id=id,
            name=name,
            status=status,
            status_label=status_label,
            source=source,
            source_label=source_label,
            company_name=company_name,
            email=email,
            phone=phone,
            job_title=job_title,
            owner_id=owner_id,
            owner_name=owner_name,
            owner_avatar_url=owner_avatar_url,
            lead_list_id=lead_list_id,
            lead_list_name=lead_list_name,
            next_action_at=next_action_at,
            next_action_channel=next_action_channel,
            next_action_channel_label=next_action_channel_label,
            last_action_at=last_action_at,
            last_actor_name=last_actor_name,
            last_actor_avatar_url=last_actor_avatar_url,
            score=score,
            country=country,
            tags=tags,
            converted_at=converted_at,
            converted_to_org_id=converted_to_org_id,
            converted_to_org_name=converted_to_org_name,
            closed_at=closed_at,
        )

        output_lead_summary.additional_properties = d
        return output_lead_summary

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
