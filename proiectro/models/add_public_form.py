from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddPublicForm")


@_attrs_define
class AddPublicForm:
    """A custom form published at its own address (PUBLIC_INBOUND.md Part E). The address is the last
    part of the link, lowercase letters, digits and dashes; left empty, it is made from the title.
    `lead_list` empty means no list.

        Attributes:
            custom_form (str):
            title (str):
            owner (str):
            slug (None | str | Unset):  Default: ''.
            intro (None | str | Unset):  Default: ''.
            lead_list (None | str | Unset):  Default: ''.
            phone_required (bool | None | Unset):  Default: False.
            company_required (bool | None | Unset):  Default: False.
            is_active (bool | None | Unset):  Default: False.
            thank_you_text (None | str | Unset):  Default: ''.
    """

    custom_form: str
    title: str
    owner: str
    slug: None | str | Unset = ""
    intro: None | str | Unset = ""
    lead_list: None | str | Unset = ""
    phone_required: bool | None | Unset = False
    company_required: bool | None | Unset = False
    is_active: bool | None | Unset = False
    thank_you_text: None | str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_form = self.custom_form

        title = self.title

        owner = self.owner

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        intro: None | str | Unset
        if isinstance(self.intro, Unset):
            intro = UNSET
        else:
            intro = self.intro

        lead_list: None | str | Unset
        if isinstance(self.lead_list, Unset):
            lead_list = UNSET
        else:
            lead_list = self.lead_list

        phone_required: bool | None | Unset
        if isinstance(self.phone_required, Unset):
            phone_required = UNSET
        else:
            phone_required = self.phone_required

        company_required: bool | None | Unset
        if isinstance(self.company_required, Unset):
            company_required = UNSET
        else:
            company_required = self.company_required

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        thank_you_text: None | str | Unset
        if isinstance(self.thank_you_text, Unset):
            thank_you_text = UNSET
        else:
            thank_you_text = self.thank_you_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_form": custom_form,
                "title": title,
                "owner": owner,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if intro is not UNSET:
            field_dict["intro"] = intro
        if lead_list is not UNSET:
            field_dict["lead_list"] = lead_list
        if phone_required is not UNSET:
            field_dict["phone_required"] = phone_required
        if company_required is not UNSET:
            field_dict["company_required"] = company_required
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if thank_you_text is not UNSET:
            field_dict["thank_you_text"] = thank_you_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_form = d.pop("custom_form")

        title = d.pop("title")

        owner = d.pop("owner")

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_intro(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro = _parse_intro(d.pop("intro", UNSET))

        def _parse_lead_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_list = _parse_lead_list(d.pop("lead_list", UNSET))

        def _parse_phone_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        phone_required = _parse_phone_required(d.pop("phone_required", UNSET))

        def _parse_company_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        company_required = _parse_company_required(d.pop("company_required", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_thank_you_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thank_you_text = _parse_thank_you_text(d.pop("thank_you_text", UNSET))

        add_public_form = cls(
            custom_form=custom_form,
            title=title,
            owner=owner,
            slug=slug,
            intro=intro,
            lead_list=lead_list,
            phone_required=phone_required,
            company_required=company_required,
            is_active=is_active,
            thank_you_text=thank_you_text,
        )

        add_public_form.additional_properties = d
        return add_public_form

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
