from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_summary import InboundSummary


T = TypeVar("T", bound="SalesActivityContent")


@_attrs_define
class SalesActivityContent:
    """
    Attributes:
        activity_type (str):
        activity_icon (str):
        author_id (str):
        author_name (str):
        author_avatar_url (str):
        description (str):
        author_email (None | str | Unset):
        author_phone (None | str | Unset):
        org_id (None | str | Unset):
        org_name (None | str | Unset):
        proposal_id (None | str | Unset):
        proposal_name (None | str | Unset):
        addable_contacts (list[str] | Unset):
        inbound (InboundSummary | None | Unset):
    """

    activity_type: str
    activity_icon: str
    author_id: str
    author_name: str
    author_avatar_url: str
    description: str
    author_email: None | str | Unset = UNSET
    author_phone: None | str | Unset = UNSET
    org_id: None | str | Unset = UNSET
    org_name: None | str | Unset = UNSET
    proposal_id: None | str | Unset = UNSET
    proposal_name: None | str | Unset = UNSET
    addable_contacts: list[str] | Unset = UNSET
    inbound: InboundSummary | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inbound_summary import InboundSummary

        activity_type = self.activity_type

        activity_icon = self.activity_icon

        author_id = self.author_id

        author_name = self.author_name

        author_avatar_url = self.author_avatar_url

        description = self.description

        author_email: None | str | Unset
        if isinstance(self.author_email, Unset):
            author_email = UNSET
        else:
            author_email = self.author_email

        author_phone: None | str | Unset
        if isinstance(self.author_phone, Unset):
            author_phone = UNSET
        else:
            author_phone = self.author_phone

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        else:
            org_id = self.org_id

        org_name: None | str | Unset
        if isinstance(self.org_name, Unset):
            org_name = UNSET
        else:
            org_name = self.org_name

        proposal_id: None | str | Unset
        if isinstance(self.proposal_id, Unset):
            proposal_id = UNSET
        else:
            proposal_id = self.proposal_id

        proposal_name: None | str | Unset
        if isinstance(self.proposal_name, Unset):
            proposal_name = UNSET
        else:
            proposal_name = self.proposal_name

        addable_contacts: list[str] | Unset = UNSET
        if not isinstance(self.addable_contacts, Unset):
            addable_contacts = self.addable_contacts

        inbound: dict[str, Any] | None | Unset
        if isinstance(self.inbound, Unset):
            inbound = UNSET
        elif isinstance(self.inbound, InboundSummary):
            inbound = self.inbound.to_dict()
        else:
            inbound = self.inbound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity_type": activity_type,
                "activity_icon": activity_icon,
                "author_id": author_id,
                "author_name": author_name,
                "author_avatar_url": author_avatar_url,
                "description": description,
            }
        )
        if author_email is not UNSET:
            field_dict["author_email"] = author_email
        if author_phone is not UNSET:
            field_dict["author_phone"] = author_phone
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if org_name is not UNSET:
            field_dict["org_name"] = org_name
        if proposal_id is not UNSET:
            field_dict["proposal_id"] = proposal_id
        if proposal_name is not UNSET:
            field_dict["proposal_name"] = proposal_name
        if addable_contacts is not UNSET:
            field_dict["addable_contacts"] = addable_contacts
        if inbound is not UNSET:
            field_dict["inbound"] = inbound

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbound_summary import InboundSummary

        d = dict(src_dict)
        activity_type = d.pop("activity_type")

        activity_icon = d.pop("activity_icon")

        author_id = d.pop("author_id")

        author_name = d.pop("author_name")

        author_avatar_url = d.pop("author_avatar_url")

        description = d.pop("description")

        def _parse_author_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_email = _parse_author_email(d.pop("author_email", UNSET))

        def _parse_author_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_phone = _parse_author_phone(d.pop("author_phone", UNSET))

        def _parse_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_name = _parse_org_name(d.pop("org_name", UNSET))

        def _parse_proposal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposal_id = _parse_proposal_id(d.pop("proposal_id", UNSET))

        def _parse_proposal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposal_name = _parse_proposal_name(d.pop("proposal_name", UNSET))

        addable_contacts = cast(list[str], d.pop("addable_contacts", UNSET))

        def _parse_inbound(data: object) -> InboundSummary | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inbound_type_0 = InboundSummary.from_dict(data)

                return inbound_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InboundSummary | None | Unset, data)

        inbound = _parse_inbound(d.pop("inbound", UNSET))

        sales_activity_content = cls(
            activity_type=activity_type,
            activity_icon=activity_icon,
            author_id=author_id,
            author_name=author_name,
            author_avatar_url=author_avatar_url,
            description=description,
            author_email=author_email,
            author_phone=author_phone,
            org_id=org_id,
            org_name=org_name,
            proposal_id=proposal_id,
            proposal_name=proposal_name,
            addable_contacts=addable_contacts,
            inbound=inbound,
        )

        sales_activity_content.additional_properties = d
        return sales_activity_content

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
