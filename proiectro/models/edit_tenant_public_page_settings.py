from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTenantPublicPageSettings")


@_attrs_define
class EditTenantPublicPageSettings:
    """The workspace's public page (plans/PUBLIC_INBOUND.md C3). An omitted key keeps the stored
    value; an empty lead list or questions form means none.

        Attributes:
            published (bool | None | Unset):
            description (None | str | Unset):
            show_prices (bool | None | Unset):
            show_forms (bool | None | Unset):
            lead_owner (None | str | Unset):
            lead_list (None | str | Unset):
            phone_required (bool | None | Unset):
            company_required (bool | None | Unset):
            custom_form (None | str | Unset):
            privacy_notice (None | str | Unset):
    """

    published: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    show_prices: bool | None | Unset = UNSET
    show_forms: bool | None | Unset = UNSET
    lead_owner: None | str | Unset = UNSET
    lead_list: None | str | Unset = UNSET
    phone_required: bool | None | Unset = UNSET
    company_required: bool | None | Unset = UNSET
    custom_form: None | str | Unset = UNSET
    privacy_notice: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        published: bool | None | Unset
        if isinstance(self.published, Unset):
            published = UNSET
        else:
            published = self.published

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        show_prices: bool | None | Unset
        if isinstance(self.show_prices, Unset):
            show_prices = UNSET
        else:
            show_prices = self.show_prices

        show_forms: bool | None | Unset
        if isinstance(self.show_forms, Unset):
            show_forms = UNSET
        else:
            show_forms = self.show_forms

        lead_owner: None | str | Unset
        if isinstance(self.lead_owner, Unset):
            lead_owner = UNSET
        else:
            lead_owner = self.lead_owner

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

        custom_form: None | str | Unset
        if isinstance(self.custom_form, Unset):
            custom_form = UNSET
        else:
            custom_form = self.custom_form

        privacy_notice: None | str | Unset
        if isinstance(self.privacy_notice, Unset):
            privacy_notice = UNSET
        else:
            privacy_notice = self.privacy_notice

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if published is not UNSET:
            field_dict["published"] = published
        if description is not UNSET:
            field_dict["description"] = description
        if show_prices is not UNSET:
            field_dict["show_prices"] = show_prices
        if show_forms is not UNSET:
            field_dict["show_forms"] = show_forms
        if lead_owner is not UNSET:
            field_dict["lead_owner"] = lead_owner
        if lead_list is not UNSET:
            field_dict["lead_list"] = lead_list
        if phone_required is not UNSET:
            field_dict["phone_required"] = phone_required
        if company_required is not UNSET:
            field_dict["company_required"] = company_required
        if custom_form is not UNSET:
            field_dict["custom_form"] = custom_form
        if privacy_notice is not UNSET:
            field_dict["privacy_notice"] = privacy_notice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_published(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        published = _parse_published(d.pop("published", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_show_prices(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_prices = _parse_show_prices(d.pop("show_prices", UNSET))

        def _parse_show_forms(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_forms = _parse_show_forms(d.pop("show_forms", UNSET))

        def _parse_lead_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_owner = _parse_lead_owner(d.pop("lead_owner", UNSET))

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

        def _parse_custom_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_form = _parse_custom_form(d.pop("custom_form", UNSET))

        def _parse_privacy_notice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        privacy_notice = _parse_privacy_notice(d.pop("privacy_notice", UNSET))

        edit_tenant_public_page_settings = cls(
            published=published,
            description=description,
            show_prices=show_prices,
            show_forms=show_forms,
            lead_owner=lead_owner,
            lead_list=lead_list,
            phone_required=phone_required,
            company_required=company_required,
            custom_form=custom_form,
            privacy_notice=privacy_notice,
        )

        edit_tenant_public_page_settings.additional_properties = d
        return edit_tenant_public_page_settings

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
