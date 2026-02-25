from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputTenantPortalSettings")


@_attrs_define
class OutputTenantPortalSettings:
    """Output schema for tenant customer portal settings (GET endpoint).

    Attributes:
        portal_top_message (None | str | Unset):
        portal_bottom_message (None | str | Unset):
        portal_menu_background_color (None | str | Unset):
        portal_menu_link_color (None | str | Unset):
        portal_menu_divider_color (None | str | Unset):
        portal_logo_background_color (None | str | Unset):
        portal_background_color (None | str | Unset):
        portal_button_color (None | str | Unset):
        portal_icon_color (None | str | Unset):
    """

    portal_top_message: None | str | Unset = UNSET
    portal_bottom_message: None | str | Unset = UNSET
    portal_menu_background_color: None | str | Unset = UNSET
    portal_menu_link_color: None | str | Unset = UNSET
    portal_menu_divider_color: None | str | Unset = UNSET
    portal_logo_background_color: None | str | Unset = UNSET
    portal_background_color: None | str | Unset = UNSET
    portal_button_color: None | str | Unset = UNSET
    portal_icon_color: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        portal_top_message: None | str | Unset
        if isinstance(self.portal_top_message, Unset):
            portal_top_message = UNSET
        else:
            portal_top_message = self.portal_top_message

        portal_bottom_message: None | str | Unset
        if isinstance(self.portal_bottom_message, Unset):
            portal_bottom_message = UNSET
        else:
            portal_bottom_message = self.portal_bottom_message

        portal_menu_background_color: None | str | Unset
        if isinstance(self.portal_menu_background_color, Unset):
            portal_menu_background_color = UNSET
        else:
            portal_menu_background_color = self.portal_menu_background_color

        portal_menu_link_color: None | str | Unset
        if isinstance(self.portal_menu_link_color, Unset):
            portal_menu_link_color = UNSET
        else:
            portal_menu_link_color = self.portal_menu_link_color

        portal_menu_divider_color: None | str | Unset
        if isinstance(self.portal_menu_divider_color, Unset):
            portal_menu_divider_color = UNSET
        else:
            portal_menu_divider_color = self.portal_menu_divider_color

        portal_logo_background_color: None | str | Unset
        if isinstance(self.portal_logo_background_color, Unset):
            portal_logo_background_color = UNSET
        else:
            portal_logo_background_color = self.portal_logo_background_color

        portal_background_color: None | str | Unset
        if isinstance(self.portal_background_color, Unset):
            portal_background_color = UNSET
        else:
            portal_background_color = self.portal_background_color

        portal_button_color: None | str | Unset
        if isinstance(self.portal_button_color, Unset):
            portal_button_color = UNSET
        else:
            portal_button_color = self.portal_button_color

        portal_icon_color: None | str | Unset
        if isinstance(self.portal_icon_color, Unset):
            portal_icon_color = UNSET
        else:
            portal_icon_color = self.portal_icon_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portal_top_message is not UNSET:
            field_dict["portal_top_message"] = portal_top_message
        if portal_bottom_message is not UNSET:
            field_dict["portal_bottom_message"] = portal_bottom_message
        if portal_menu_background_color is not UNSET:
            field_dict["portal_menu_background_color"] = portal_menu_background_color
        if portal_menu_link_color is not UNSET:
            field_dict["portal_menu_link_color"] = portal_menu_link_color
        if portal_menu_divider_color is not UNSET:
            field_dict["portal_menu_divider_color"] = portal_menu_divider_color
        if portal_logo_background_color is not UNSET:
            field_dict["portal_logo_background_color"] = portal_logo_background_color
        if portal_background_color is not UNSET:
            field_dict["portal_background_color"] = portal_background_color
        if portal_button_color is not UNSET:
            field_dict["portal_button_color"] = portal_button_color
        if portal_icon_color is not UNSET:
            field_dict["portal_icon_color"] = portal_icon_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_portal_top_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_top_message = _parse_portal_top_message(
            d.pop("portal_top_message", UNSET)
        )

        def _parse_portal_bottom_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_bottom_message = _parse_portal_bottom_message(
            d.pop("portal_bottom_message", UNSET)
        )

        def _parse_portal_menu_background_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_menu_background_color = _parse_portal_menu_background_color(
            d.pop("portal_menu_background_color", UNSET)
        )

        def _parse_portal_menu_link_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_menu_link_color = _parse_portal_menu_link_color(
            d.pop("portal_menu_link_color", UNSET)
        )

        def _parse_portal_menu_divider_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_menu_divider_color = _parse_portal_menu_divider_color(
            d.pop("portal_menu_divider_color", UNSET)
        )

        def _parse_portal_logo_background_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_logo_background_color = _parse_portal_logo_background_color(
            d.pop("portal_logo_background_color", UNSET)
        )

        def _parse_portal_background_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_background_color = _parse_portal_background_color(
            d.pop("portal_background_color", UNSET)
        )

        def _parse_portal_button_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_button_color = _parse_portal_button_color(
            d.pop("portal_button_color", UNSET)
        )

        def _parse_portal_icon_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_icon_color = _parse_portal_icon_color(d.pop("portal_icon_color", UNSET))

        output_tenant_portal_settings = cls(
            portal_top_message=portal_top_message,
            portal_bottom_message=portal_bottom_message,
            portal_menu_background_color=portal_menu_background_color,
            portal_menu_link_color=portal_menu_link_color,
            portal_menu_divider_color=portal_menu_divider_color,
            portal_logo_background_color=portal_logo_background_color,
            portal_background_color=portal_background_color,
            portal_button_color=portal_button_color,
            portal_icon_color=portal_icon_color,
        )

        output_tenant_portal_settings.additional_properties = d
        return output_tenant_portal_settings

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
