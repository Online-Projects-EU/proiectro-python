from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishShare")


@_attrs_define
class PublishShare:
    """Publishes the share and every item waiting in it. The expiry is the end of the day, in the
    organization's timezone, `expires_in_days` from now; `no_expiry` overrides it. With neither, the
    share keeps the expiry an earlier publication chose while it is still ahead, or gets the default.

        Attributes:
            expires_in_days (int | None | Unset):
            no_expiry (bool | None | Unset):
            confirm_link_retirement (bool | None | Unset):
            replace_link (bool | None | Unset):
    """

    expires_in_days: int | None | Unset = UNSET
    no_expiry: bool | None | Unset = UNSET
    confirm_link_retirement: bool | None | Unset = UNSET
    replace_link: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_in_days: int | None | Unset
        if isinstance(self.expires_in_days, Unset):
            expires_in_days = UNSET
        else:
            expires_in_days = self.expires_in_days

        no_expiry: bool | None | Unset
        if isinstance(self.no_expiry, Unset):
            no_expiry = UNSET
        else:
            no_expiry = self.no_expiry

        confirm_link_retirement: bool | None | Unset
        if isinstance(self.confirm_link_retirement, Unset):
            confirm_link_retirement = UNSET
        else:
            confirm_link_retirement = self.confirm_link_retirement

        replace_link: bool | None | Unset
        if isinstance(self.replace_link, Unset):
            replace_link = UNSET
        else:
            replace_link = self.replace_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_in_days is not UNSET:
            field_dict["expires_in_days"] = expires_in_days
        if no_expiry is not UNSET:
            field_dict["no_expiry"] = no_expiry
        if confirm_link_retirement is not UNSET:
            field_dict["confirm_link_retirement"] = confirm_link_retirement
        if replace_link is not UNSET:
            field_dict["replace_link"] = replace_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expires_in_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_in_days = _parse_expires_in_days(d.pop("expires_in_days", UNSET))

        def _parse_no_expiry(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        no_expiry = _parse_no_expiry(d.pop("no_expiry", UNSET))

        def _parse_confirm_link_retirement(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        confirm_link_retirement = _parse_confirm_link_retirement(
            d.pop("confirm_link_retirement", UNSET)
        )

        def _parse_replace_link(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        replace_link = _parse_replace_link(d.pop("replace_link", UNSET))

        publish_share = cls(
            expires_in_days=expires_in_days,
            no_expiry=no_expiry,
            confirm_link_retirement=confirm_link_retirement,
            replace_link=replace_link,
        )

        publish_share.additional_properties = d
        return publish_share

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
