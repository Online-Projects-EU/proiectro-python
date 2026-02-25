from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBridge")


@_attrs_define
class CreateBridge:
    """Input schema for creating a tenant bridge (partnership) invitation

    Attributes:
        partner_identifier (str):
        grant_rfp_create (bool | None | Unset):  Default: False.
        grant_proposal_view (bool | None | Unset):  Default: False.
        grant_proposal_accept (bool | None | Unset):  Default: False.
        grant_project_view (bool | None | Unset):  Default: False.
        grant_product_view (bool | None | Unset):  Default: False.
        grant_product_accept (bool | None | Unset):  Default: False.
        grant_product_reject (bool | None | Unset):  Default: False.
        grant_payment_view (bool | None | Unset):  Default: False.
        grant_support_use (bool | None | Unset):  Default: False.
        invitation_message (None | str | Unset):
    """

    partner_identifier: str
    grant_rfp_create: bool | None | Unset = False
    grant_proposal_view: bool | None | Unset = False
    grant_proposal_accept: bool | None | Unset = False
    grant_project_view: bool | None | Unset = False
    grant_product_view: bool | None | Unset = False
    grant_product_accept: bool | None | Unset = False
    grant_product_reject: bool | None | Unset = False
    grant_payment_view: bool | None | Unset = False
    grant_support_use: bool | None | Unset = False
    invitation_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partner_identifier = self.partner_identifier

        grant_rfp_create: bool | None | Unset
        if isinstance(self.grant_rfp_create, Unset):
            grant_rfp_create = UNSET
        else:
            grant_rfp_create = self.grant_rfp_create

        grant_proposal_view: bool | None | Unset
        if isinstance(self.grant_proposal_view, Unset):
            grant_proposal_view = UNSET
        else:
            grant_proposal_view = self.grant_proposal_view

        grant_proposal_accept: bool | None | Unset
        if isinstance(self.grant_proposal_accept, Unset):
            grant_proposal_accept = UNSET
        else:
            grant_proposal_accept = self.grant_proposal_accept

        grant_project_view: bool | None | Unset
        if isinstance(self.grant_project_view, Unset):
            grant_project_view = UNSET
        else:
            grant_project_view = self.grant_project_view

        grant_product_view: bool | None | Unset
        if isinstance(self.grant_product_view, Unset):
            grant_product_view = UNSET
        else:
            grant_product_view = self.grant_product_view

        grant_product_accept: bool | None | Unset
        if isinstance(self.grant_product_accept, Unset):
            grant_product_accept = UNSET
        else:
            grant_product_accept = self.grant_product_accept

        grant_product_reject: bool | None | Unset
        if isinstance(self.grant_product_reject, Unset):
            grant_product_reject = UNSET
        else:
            grant_product_reject = self.grant_product_reject

        grant_payment_view: bool | None | Unset
        if isinstance(self.grant_payment_view, Unset):
            grant_payment_view = UNSET
        else:
            grant_payment_view = self.grant_payment_view

        grant_support_use: bool | None | Unset
        if isinstance(self.grant_support_use, Unset):
            grant_support_use = UNSET
        else:
            grant_support_use = self.grant_support_use

        invitation_message: None | str | Unset
        if isinstance(self.invitation_message, Unset):
            invitation_message = UNSET
        else:
            invitation_message = self.invitation_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partner_identifier": partner_identifier,
            }
        )
        if grant_rfp_create is not UNSET:
            field_dict["grant_rfp_create"] = grant_rfp_create
        if grant_proposal_view is not UNSET:
            field_dict["grant_proposal_view"] = grant_proposal_view
        if grant_proposal_accept is not UNSET:
            field_dict["grant_proposal_accept"] = grant_proposal_accept
        if grant_project_view is not UNSET:
            field_dict["grant_project_view"] = grant_project_view
        if grant_product_view is not UNSET:
            field_dict["grant_product_view"] = grant_product_view
        if grant_product_accept is not UNSET:
            field_dict["grant_product_accept"] = grant_product_accept
        if grant_product_reject is not UNSET:
            field_dict["grant_product_reject"] = grant_product_reject
        if grant_payment_view is not UNSET:
            field_dict["grant_payment_view"] = grant_payment_view
        if grant_support_use is not UNSET:
            field_dict["grant_support_use"] = grant_support_use
        if invitation_message is not UNSET:
            field_dict["invitation_message"] = invitation_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partner_identifier = d.pop("partner_identifier")

        def _parse_grant_rfp_create(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_rfp_create = _parse_grant_rfp_create(d.pop("grant_rfp_create", UNSET))

        def _parse_grant_proposal_view(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_proposal_view = _parse_grant_proposal_view(
            d.pop("grant_proposal_view", UNSET)
        )

        def _parse_grant_proposal_accept(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_proposal_accept = _parse_grant_proposal_accept(
            d.pop("grant_proposal_accept", UNSET)
        )

        def _parse_grant_project_view(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_project_view = _parse_grant_project_view(
            d.pop("grant_project_view", UNSET)
        )

        def _parse_grant_product_view(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_product_view = _parse_grant_product_view(
            d.pop("grant_product_view", UNSET)
        )

        def _parse_grant_product_accept(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_product_accept = _parse_grant_product_accept(
            d.pop("grant_product_accept", UNSET)
        )

        def _parse_grant_product_reject(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_product_reject = _parse_grant_product_reject(
            d.pop("grant_product_reject", UNSET)
        )

        def _parse_grant_payment_view(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_payment_view = _parse_grant_payment_view(
            d.pop("grant_payment_view", UNSET)
        )

        def _parse_grant_support_use(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_support_use = _parse_grant_support_use(d.pop("grant_support_use", UNSET))

        def _parse_invitation_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invitation_message = _parse_invitation_message(
            d.pop("invitation_message", UNSET)
        )

        create_bridge = cls(
            partner_identifier=partner_identifier,
            grant_rfp_create=grant_rfp_create,
            grant_proposal_view=grant_proposal_view,
            grant_proposal_accept=grant_proposal_accept,
            grant_project_view=grant_project_view,
            grant_product_view=grant_product_view,
            grant_product_accept=grant_product_accept,
            grant_product_reject=grant_product_reject,
            grant_payment_view=grant_payment_view,
            grant_support_use=grant_support_use,
            invitation_message=invitation_message,
        )

        create_bridge.additional_properties = d
        return create_bridge

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
