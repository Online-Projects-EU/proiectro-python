from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_tenant_portal_settings_portal_orders_payment_terms_type_0 import (
    EditTenantPortalSettingsPortalOrdersPaymentTermsType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTenantPortalSettings")


@_attrs_define
class EditTenantPortalSettings:
    """Schema for updating customer portal customization settings.

    Attributes:
        portal_top_message (None | str | Unset):
        portal_bottom_message (None | str | Unset):
        use_portal_menu_background_color (bool | None | Unset):
        use_portal_menu_link_color (bool | None | Unset):
        use_portal_menu_divider_color (bool | None | Unset):
        use_portal_logo_background_color (bool | None | Unset):
        use_portal_background_color (bool | None | Unset):
        use_portal_button_color (bool | None | Unset):
        use_portal_icon_color (bool | None | Unset):
        portal_menu_background_color (None | str | Unset):
        portal_menu_link_color (None | str | Unset):
        portal_menu_divider_color (None | str | Unset):
        portal_logo_background_color (None | str | Unset):
        portal_background_color (None | str | Unset):
        portal_button_color (None | str | Unset):
        portal_icon_color (None | str | Unset):
        portal_order_funnel (None | str | Unset):
        portal_orders_auto_accept (bool | None | Unset):
        portal_orders_payment_terms (EditTenantPortalSettingsPortalOrdersPaymentTermsType0 | None | Unset):
        portal_orders_payment_days (int | None | Unset):
        portal_orders_new_org_default (bool | None | Unset):
        portal_quote_requests_new_org_default (bool | None | Unset):
        portal_orders_new_bridge_default (bool | None | Unset):
        portal_new_org_price_list (None | str | Unset):
        portal_new_bridge_price_list (None | str | Unset):
        portal_quote_requests_new_bridge_default (bool | None | Unset):
        portal_quote_funnel (None | str | Unset):
    """

    portal_top_message: None | str | Unset = UNSET
    portal_bottom_message: None | str | Unset = UNSET
    use_portal_menu_background_color: bool | None | Unset = UNSET
    use_portal_menu_link_color: bool | None | Unset = UNSET
    use_portal_menu_divider_color: bool | None | Unset = UNSET
    use_portal_logo_background_color: bool | None | Unset = UNSET
    use_portal_background_color: bool | None | Unset = UNSET
    use_portal_button_color: bool | None | Unset = UNSET
    use_portal_icon_color: bool | None | Unset = UNSET
    portal_menu_background_color: None | str | Unset = UNSET
    portal_menu_link_color: None | str | Unset = UNSET
    portal_menu_divider_color: None | str | Unset = UNSET
    portal_logo_background_color: None | str | Unset = UNSET
    portal_background_color: None | str | Unset = UNSET
    portal_button_color: None | str | Unset = UNSET
    portal_icon_color: None | str | Unset = UNSET
    portal_order_funnel: None | str | Unset = UNSET
    portal_orders_auto_accept: bool | None | Unset = UNSET
    portal_orders_payment_terms: (
        EditTenantPortalSettingsPortalOrdersPaymentTermsType0 | None | Unset
    ) = UNSET
    portal_orders_payment_days: int | None | Unset = UNSET
    portal_orders_new_org_default: bool | None | Unset = UNSET
    portal_quote_requests_new_org_default: bool | None | Unset = UNSET
    portal_orders_new_bridge_default: bool | None | Unset = UNSET
    portal_new_org_price_list: None | str | Unset = UNSET
    portal_new_bridge_price_list: None | str | Unset = UNSET
    portal_quote_requests_new_bridge_default: bool | None | Unset = UNSET
    portal_quote_funnel: None | str | Unset = UNSET
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

        use_portal_menu_background_color: bool | None | Unset
        if isinstance(self.use_portal_menu_background_color, Unset):
            use_portal_menu_background_color = UNSET
        else:
            use_portal_menu_background_color = self.use_portal_menu_background_color

        use_portal_menu_link_color: bool | None | Unset
        if isinstance(self.use_portal_menu_link_color, Unset):
            use_portal_menu_link_color = UNSET
        else:
            use_portal_menu_link_color = self.use_portal_menu_link_color

        use_portal_menu_divider_color: bool | None | Unset
        if isinstance(self.use_portal_menu_divider_color, Unset):
            use_portal_menu_divider_color = UNSET
        else:
            use_portal_menu_divider_color = self.use_portal_menu_divider_color

        use_portal_logo_background_color: bool | None | Unset
        if isinstance(self.use_portal_logo_background_color, Unset):
            use_portal_logo_background_color = UNSET
        else:
            use_portal_logo_background_color = self.use_portal_logo_background_color

        use_portal_background_color: bool | None | Unset
        if isinstance(self.use_portal_background_color, Unset):
            use_portal_background_color = UNSET
        else:
            use_portal_background_color = self.use_portal_background_color

        use_portal_button_color: bool | None | Unset
        if isinstance(self.use_portal_button_color, Unset):
            use_portal_button_color = UNSET
        else:
            use_portal_button_color = self.use_portal_button_color

        use_portal_icon_color: bool | None | Unset
        if isinstance(self.use_portal_icon_color, Unset):
            use_portal_icon_color = UNSET
        else:
            use_portal_icon_color = self.use_portal_icon_color

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

        portal_order_funnel: None | str | Unset
        if isinstance(self.portal_order_funnel, Unset):
            portal_order_funnel = UNSET
        else:
            portal_order_funnel = self.portal_order_funnel

        portal_orders_auto_accept: bool | None | Unset
        if isinstance(self.portal_orders_auto_accept, Unset):
            portal_orders_auto_accept = UNSET
        else:
            portal_orders_auto_accept = self.portal_orders_auto_accept

        portal_orders_payment_terms: None | str | Unset
        if isinstance(self.portal_orders_payment_terms, Unset):
            portal_orders_payment_terms = UNSET
        elif isinstance(
            self.portal_orders_payment_terms,
            EditTenantPortalSettingsPortalOrdersPaymentTermsType0,
        ):
            portal_orders_payment_terms = self.portal_orders_payment_terms.value
        else:
            portal_orders_payment_terms = self.portal_orders_payment_terms

        portal_orders_payment_days: int | None | Unset
        if isinstance(self.portal_orders_payment_days, Unset):
            portal_orders_payment_days = UNSET
        else:
            portal_orders_payment_days = self.portal_orders_payment_days

        portal_orders_new_org_default: bool | None | Unset
        if isinstance(self.portal_orders_new_org_default, Unset):
            portal_orders_new_org_default = UNSET
        else:
            portal_orders_new_org_default = self.portal_orders_new_org_default

        portal_quote_requests_new_org_default: bool | None | Unset
        if isinstance(self.portal_quote_requests_new_org_default, Unset):
            portal_quote_requests_new_org_default = UNSET
        else:
            portal_quote_requests_new_org_default = (
                self.portal_quote_requests_new_org_default
            )

        portal_orders_new_bridge_default: bool | None | Unset
        if isinstance(self.portal_orders_new_bridge_default, Unset):
            portal_orders_new_bridge_default = UNSET
        else:
            portal_orders_new_bridge_default = self.portal_orders_new_bridge_default

        portal_new_org_price_list: None | str | Unset
        if isinstance(self.portal_new_org_price_list, Unset):
            portal_new_org_price_list = UNSET
        else:
            portal_new_org_price_list = self.portal_new_org_price_list

        portal_new_bridge_price_list: None | str | Unset
        if isinstance(self.portal_new_bridge_price_list, Unset):
            portal_new_bridge_price_list = UNSET
        else:
            portal_new_bridge_price_list = self.portal_new_bridge_price_list

        portal_quote_requests_new_bridge_default: bool | None | Unset
        if isinstance(self.portal_quote_requests_new_bridge_default, Unset):
            portal_quote_requests_new_bridge_default = UNSET
        else:
            portal_quote_requests_new_bridge_default = (
                self.portal_quote_requests_new_bridge_default
            )

        portal_quote_funnel: None | str | Unset
        if isinstance(self.portal_quote_funnel, Unset):
            portal_quote_funnel = UNSET
        else:
            portal_quote_funnel = self.portal_quote_funnel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portal_top_message is not UNSET:
            field_dict["portal_top_message"] = portal_top_message
        if portal_bottom_message is not UNSET:
            field_dict["portal_bottom_message"] = portal_bottom_message
        if use_portal_menu_background_color is not UNSET:
            field_dict["use_portal_menu_background_color"] = (
                use_portal_menu_background_color
            )
        if use_portal_menu_link_color is not UNSET:
            field_dict["use_portal_menu_link_color"] = use_portal_menu_link_color
        if use_portal_menu_divider_color is not UNSET:
            field_dict["use_portal_menu_divider_color"] = use_portal_menu_divider_color
        if use_portal_logo_background_color is not UNSET:
            field_dict["use_portal_logo_background_color"] = (
                use_portal_logo_background_color
            )
        if use_portal_background_color is not UNSET:
            field_dict["use_portal_background_color"] = use_portal_background_color
        if use_portal_button_color is not UNSET:
            field_dict["use_portal_button_color"] = use_portal_button_color
        if use_portal_icon_color is not UNSET:
            field_dict["use_portal_icon_color"] = use_portal_icon_color
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
        if portal_order_funnel is not UNSET:
            field_dict["portal_order_funnel"] = portal_order_funnel
        if portal_orders_auto_accept is not UNSET:
            field_dict["portal_orders_auto_accept"] = portal_orders_auto_accept
        if portal_orders_payment_terms is not UNSET:
            field_dict["portal_orders_payment_terms"] = portal_orders_payment_terms
        if portal_orders_payment_days is not UNSET:
            field_dict["portal_orders_payment_days"] = portal_orders_payment_days
        if portal_orders_new_org_default is not UNSET:
            field_dict["portal_orders_new_org_default"] = portal_orders_new_org_default
        if portal_quote_requests_new_org_default is not UNSET:
            field_dict["portal_quote_requests_new_org_default"] = (
                portal_quote_requests_new_org_default
            )
        if portal_orders_new_bridge_default is not UNSET:
            field_dict["portal_orders_new_bridge_default"] = (
                portal_orders_new_bridge_default
            )
        if portal_new_org_price_list is not UNSET:
            field_dict["portal_new_org_price_list"] = portal_new_org_price_list
        if portal_new_bridge_price_list is not UNSET:
            field_dict["portal_new_bridge_price_list"] = portal_new_bridge_price_list
        if portal_quote_requests_new_bridge_default is not UNSET:
            field_dict["portal_quote_requests_new_bridge_default"] = (
                portal_quote_requests_new_bridge_default
            )
        if portal_quote_funnel is not UNSET:
            field_dict["portal_quote_funnel"] = portal_quote_funnel

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

        def _parse_use_portal_menu_background_color(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_portal_menu_background_color = _parse_use_portal_menu_background_color(
            d.pop("use_portal_menu_background_color", UNSET)
        )

        def _parse_use_portal_menu_link_color(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_portal_menu_link_color = _parse_use_portal_menu_link_color(
            d.pop("use_portal_menu_link_color", UNSET)
        )

        def _parse_use_portal_menu_divider_color(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_portal_menu_divider_color = _parse_use_portal_menu_divider_color(
            d.pop("use_portal_menu_divider_color", UNSET)
        )

        def _parse_use_portal_logo_background_color(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_portal_logo_background_color = _parse_use_portal_logo_background_color(
            d.pop("use_portal_logo_background_color", UNSET)
        )

        def _parse_use_portal_background_color(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_portal_background_color = _parse_use_portal_background_color(
            d.pop("use_portal_background_color", UNSET)
        )

        def _parse_use_portal_button_color(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_portal_button_color = _parse_use_portal_button_color(
            d.pop("use_portal_button_color", UNSET)
        )

        def _parse_use_portal_icon_color(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_portal_icon_color = _parse_use_portal_icon_color(
            d.pop("use_portal_icon_color", UNSET)
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

        def _parse_portal_order_funnel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_order_funnel = _parse_portal_order_funnel(
            d.pop("portal_order_funnel", UNSET)
        )

        def _parse_portal_orders_auto_accept(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_orders_auto_accept = _parse_portal_orders_auto_accept(
            d.pop("portal_orders_auto_accept", UNSET)
        )

        def _parse_portal_orders_payment_terms(
            data: object,
        ) -> EditTenantPortalSettingsPortalOrdersPaymentTermsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                portal_orders_payment_terms_type_0 = (
                    EditTenantPortalSettingsPortalOrdersPaymentTermsType0(data)
                )

                return portal_orders_payment_terms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EditTenantPortalSettingsPortalOrdersPaymentTermsType0 | None | Unset,
                data,
            )

        portal_orders_payment_terms = _parse_portal_orders_payment_terms(
            d.pop("portal_orders_payment_terms", UNSET)
        )

        def _parse_portal_orders_payment_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        portal_orders_payment_days = _parse_portal_orders_payment_days(
            d.pop("portal_orders_payment_days", UNSET)
        )

        def _parse_portal_orders_new_org_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_orders_new_org_default = _parse_portal_orders_new_org_default(
            d.pop("portal_orders_new_org_default", UNSET)
        )

        def _parse_portal_quote_requests_new_org_default(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_quote_requests_new_org_default = (
            _parse_portal_quote_requests_new_org_default(
                d.pop("portal_quote_requests_new_org_default", UNSET)
            )
        )

        def _parse_portal_orders_new_bridge_default(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_orders_new_bridge_default = _parse_portal_orders_new_bridge_default(
            d.pop("portal_orders_new_bridge_default", UNSET)
        )

        def _parse_portal_new_org_price_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_new_org_price_list = _parse_portal_new_org_price_list(
            d.pop("portal_new_org_price_list", UNSET)
        )

        def _parse_portal_new_bridge_price_list(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_new_bridge_price_list = _parse_portal_new_bridge_price_list(
            d.pop("portal_new_bridge_price_list", UNSET)
        )

        def _parse_portal_quote_requests_new_bridge_default(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        portal_quote_requests_new_bridge_default = (
            _parse_portal_quote_requests_new_bridge_default(
                d.pop("portal_quote_requests_new_bridge_default", UNSET)
            )
        )

        def _parse_portal_quote_funnel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_quote_funnel = _parse_portal_quote_funnel(
            d.pop("portal_quote_funnel", UNSET)
        )

        edit_tenant_portal_settings = cls(
            portal_top_message=portal_top_message,
            portal_bottom_message=portal_bottom_message,
            use_portal_menu_background_color=use_portal_menu_background_color,
            use_portal_menu_link_color=use_portal_menu_link_color,
            use_portal_menu_divider_color=use_portal_menu_divider_color,
            use_portal_logo_background_color=use_portal_logo_background_color,
            use_portal_background_color=use_portal_background_color,
            use_portal_button_color=use_portal_button_color,
            use_portal_icon_color=use_portal_icon_color,
            portal_menu_background_color=portal_menu_background_color,
            portal_menu_link_color=portal_menu_link_color,
            portal_menu_divider_color=portal_menu_divider_color,
            portal_logo_background_color=portal_logo_background_color,
            portal_background_color=portal_background_color,
            portal_button_color=portal_button_color,
            portal_icon_color=portal_icon_color,
            portal_order_funnel=portal_order_funnel,
            portal_orders_auto_accept=portal_orders_auto_accept,
            portal_orders_payment_terms=portal_orders_payment_terms,
            portal_orders_payment_days=portal_orders_payment_days,
            portal_orders_new_org_default=portal_orders_new_org_default,
            portal_quote_requests_new_org_default=portal_quote_requests_new_org_default,
            portal_orders_new_bridge_default=portal_orders_new_bridge_default,
            portal_new_org_price_list=portal_new_org_price_list,
            portal_new_bridge_price_list=portal_new_bridge_price_list,
            portal_quote_requests_new_bridge_default=portal_quote_requests_new_bridge_default,
            portal_quote_funnel=portal_quote_funnel,
        )

        edit_tenant_portal_settings.additional_properties = d
        return edit_tenant_portal_settings

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
