from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditMemberPreferences")


@_attrs_define
class EditMemberPreferences:
    """
    Attributes:
        nickname (str):
        work_email (None | str | Unset):
        work_email_alternative (None | str | Unset): Email address visible to customers in their portal
        work_phone (None | str | Unset):
        work_phone_alternative (None | str | Unset): Phone number visible to customers in their portal
        territory (None | str | Unset):
    """

    nickname: str
    work_email: None | str | Unset = UNSET
    work_email_alternative: None | str | Unset = UNSET
    work_phone: None | str | Unset = UNSET
    work_phone_alternative: None | str | Unset = UNSET
    territory: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nickname = self.nickname

        work_email: None | str | Unset
        if isinstance(self.work_email, Unset):
            work_email = UNSET
        else:
            work_email = self.work_email

        work_email_alternative: None | str | Unset
        if isinstance(self.work_email_alternative, Unset):
            work_email_alternative = UNSET
        else:
            work_email_alternative = self.work_email_alternative

        work_phone: None | str | Unset
        if isinstance(self.work_phone, Unset):
            work_phone = UNSET
        else:
            work_phone = self.work_phone

        work_phone_alternative: None | str | Unset
        if isinstance(self.work_phone_alternative, Unset):
            work_phone_alternative = UNSET
        else:
            work_phone_alternative = self.work_phone_alternative

        territory: None | str | Unset
        if isinstance(self.territory, Unset):
            territory = UNSET
        else:
            territory = self.territory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nickname": nickname,
            }
        )
        if work_email is not UNSET:
            field_dict["work_email"] = work_email
        if work_email_alternative is not UNSET:
            field_dict["work_email_alternative"] = work_email_alternative
        if work_phone is not UNSET:
            field_dict["work_phone"] = work_phone
        if work_phone_alternative is not UNSET:
            field_dict["work_phone_alternative"] = work_phone_alternative
        if territory is not UNSET:
            field_dict["territory"] = territory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nickname = d.pop("nickname")

        def _parse_work_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_email = _parse_work_email(d.pop("work_email", UNSET))

        def _parse_work_email_alternative(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_email_alternative = _parse_work_email_alternative(
            d.pop("work_email_alternative", UNSET)
        )

        def _parse_work_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_phone = _parse_work_phone(d.pop("work_phone", UNSET))

        def _parse_work_phone_alternative(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_phone_alternative = _parse_work_phone_alternative(
            d.pop("work_phone_alternative", UNSET)
        )

        def _parse_territory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        territory = _parse_territory(d.pop("territory", UNSET))

        edit_member_preferences = cls(
            nickname=nickname,
            work_email=work_email,
            work_email_alternative=work_email_alternative,
            work_phone=work_phone,
            work_phone_alternative=work_phone_alternative,
            territory=territory,
        )

        edit_member_preferences.additional_properties = d
        return edit_member_preferences

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
