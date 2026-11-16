from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditPublicForm")


@_attrs_define
class EditPublicForm:
    """Every field may be left out to keep its stored value. `lead_list` empty means no list.

    Attributes:
        custom_form (None | str | Unset):
        title (None | str | Unset):
        slug (None | str | Unset):
        intro (None | str | Unset):
        owner (None | str | Unset):
        lead_list (None | str | Unset):
        phone_required (bool | None | Unset):
        company_required (bool | None | Unset):
        is_active (bool | None | Unset):
        thank_you_text (None | str | Unset):
    """

    custom_form: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    intro: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    lead_list: None | str | Unset = UNSET
    phone_required: bool | None | Unset = UNSET
    company_required: bool | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    thank_you_text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_form: None | str | Unset
        if isinstance(self.custom_form, Unset):
            custom_form = UNSET
        else:
            custom_form = self.custom_form

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

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
        field_dict.update({})
        if custom_form is not UNSET:
            field_dict["custom_form"] = custom_form
        if title is not UNSET:
            field_dict["title"] = title
        if slug is not UNSET:
            field_dict["slug"] = slug
        if intro is not UNSET:
            field_dict["intro"] = intro
        if owner is not UNSET:
            field_dict["owner"] = owner
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

        def _parse_custom_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_form = _parse_custom_form(d.pop("custom_form", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

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

        edit_public_form = cls(
            custom_form=custom_form,
            title=title,
            slug=slug,
            intro=intro,
            owner=owner,
            lead_list=lead_list,
            phone_required=phone_required,
            company_required=company_required,
            is_active=is_active,
            thank_you_text=thank_you_text,
        )

        edit_public_form.additional_properties = d
        return edit_public_form

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
