from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_portal_project_product_item import (
        PartnerPortalProjectProductItem,
    )
    from ..models.partner_portal_project_products_escalation_item import (
        PartnerPortalProjectProductsEscalationItem,
    )
    from ..models.partner_portal_project_products_payments_item import (
        PartnerPortalProjectProductsPaymentsItem,
    )
    from ..models.partner_portal_project_products_project import (
        PartnerPortalProjectProductsProject,
    )


T = TypeVar("T", bound="PartnerPortalProjectProducts")


@_attrs_define
class PartnerPortalProjectProducts:
    """Partner portal project products view with tabs

    Attributes:
        bridge_id (str):
        project_id (str):
        project (PartnerPortalProjectProductsProject):
        products (list[PartnerPortalProjectProductItem]):
        payments (list[PartnerPortalProjectProductsPaymentsItem]):
        escalation (list[PartnerPortalProjectProductsEscalationItem]):
        grant_given_by_partner (bool | Unset):  Default: True.
        grant_label (None | str | Unset):
    """

    bridge_id: str
    project_id: str
    project: PartnerPortalProjectProductsProject
    products: list[PartnerPortalProjectProductItem]
    payments: list[PartnerPortalProjectProductsPaymentsItem]
    escalation: list[PartnerPortalProjectProductsEscalationItem]
    grant_given_by_partner: bool | Unset = True
    grant_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        project_id = self.project_id

        project = self.project.to_dict()

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        escalation = []
        for escalation_item_data in self.escalation:
            escalation_item = escalation_item_data.to_dict()
            escalation.append(escalation_item)

        grant_given_by_partner = self.grant_given_by_partner

        grant_label: None | str | Unset
        if isinstance(self.grant_label, Unset):
            grant_label = UNSET
        else:
            grant_label = self.grant_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "project_id": project_id,
                "project": project,
                "products": products,
                "payments": payments,
                "escalation": escalation,
            }
        )
        if grant_given_by_partner is not UNSET:
            field_dict["grant_given_by_partner"] = grant_given_by_partner
        if grant_label is not UNSET:
            field_dict["grant_label"] = grant_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_portal_project_product_item import (
            PartnerPortalProjectProductItem,
        )
        from ..models.partner_portal_project_products_escalation_item import (
            PartnerPortalProjectProductsEscalationItem,
        )
        from ..models.partner_portal_project_products_payments_item import (
            PartnerPortalProjectProductsPaymentsItem,
        )
        from ..models.partner_portal_project_products_project import (
            PartnerPortalProjectProductsProject,
        )

        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        project_id = d.pop("project_id")

        project = PartnerPortalProjectProductsProject.from_dict(d.pop("project"))

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = PartnerPortalProjectProductItem.from_dict(
                products_item_data
            )

            products.append(products_item)

        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = PartnerPortalProjectProductsPaymentsItem.from_dict(
                payments_item_data
            )

            payments.append(payments_item)

        escalation = []
        _escalation = d.pop("escalation")
        for escalation_item_data in _escalation:
            escalation_item = PartnerPortalProjectProductsEscalationItem.from_dict(
                escalation_item_data
            )

            escalation.append(escalation_item)

        grant_given_by_partner = d.pop("grant_given_by_partner", UNSET)

        def _parse_grant_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grant_label = _parse_grant_label(d.pop("grant_label", UNSET))

        partner_portal_project_products = cls(
            bridge_id=bridge_id,
            project_id=project_id,
            project=project,
            products=products,
            payments=payments,
            escalation=escalation,
            grant_given_by_partner=grant_given_by_partner,
            grant_label=grant_label,
        )

        partner_portal_project_products.additional_properties = d
        return partner_portal_project_products

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
