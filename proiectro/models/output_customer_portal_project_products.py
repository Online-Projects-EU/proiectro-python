from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.customer_portal_project_product_item import (
        CustomerPortalProjectProductItem,
    )
    from ..models.output_customer_portal_project_products_escalation_item import (
        OutputCustomerPortalProjectProductsEscalationItem,
    )
    from ..models.output_customer_portal_project_products_org import (
        OutputCustomerPortalProjectProductsOrg,
    )
    from ..models.output_customer_portal_project_products_payments_item import (
        OutputCustomerPortalProjectProductsPaymentsItem,
    )
    from ..models.output_customer_portal_project_products_project import (
        OutputCustomerPortalProjectProductsProject,
    )


T = TypeVar("T", bound="OutputCustomerPortalProjectProducts")


@_attrs_define
class OutputCustomerPortalProjectProducts:
    """Customer portal project products view

    Attributes:
        products (list[CustomerPortalProjectProductItem]):
        payments (list[OutputCustomerPortalProjectProductsPaymentsItem]):
        escalation (list[OutputCustomerPortalProjectProductsEscalationItem]):
        project (OutputCustomerPortalProjectProductsProject):
        org (OutputCustomerPortalProjectProductsOrg):
    """

    products: list[CustomerPortalProjectProductItem]
    payments: list[OutputCustomerPortalProjectProductsPaymentsItem]
    escalation: list[OutputCustomerPortalProjectProductsEscalationItem]
    project: OutputCustomerPortalProjectProductsProject
    org: OutputCustomerPortalProjectProductsOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        project = self.project.to_dict()

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "payments": payments,
                "escalation": escalation,
                "project": project,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_portal_project_product_item import (
            CustomerPortalProjectProductItem,
        )
        from ..models.output_customer_portal_project_products_escalation_item import (
            OutputCustomerPortalProjectProductsEscalationItem,
        )
        from ..models.output_customer_portal_project_products_org import (
            OutputCustomerPortalProjectProductsOrg,
        )
        from ..models.output_customer_portal_project_products_payments_item import (
            OutputCustomerPortalProjectProductsPaymentsItem,
        )
        from ..models.output_customer_portal_project_products_project import (
            OutputCustomerPortalProjectProductsProject,
        )

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = CustomerPortalProjectProductItem.from_dict(
                products_item_data
            )

            products.append(products_item)

        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = OutputCustomerPortalProjectProductsPaymentsItem.from_dict(
                payments_item_data
            )

            payments.append(payments_item)

        escalation = []
        _escalation = d.pop("escalation")
        for escalation_item_data in _escalation:
            escalation_item = (
                OutputCustomerPortalProjectProductsEscalationItem.from_dict(
                    escalation_item_data
                )
            )

            escalation.append(escalation_item)

        project = OutputCustomerPortalProjectProductsProject.from_dict(d.pop("project"))

        org = OutputCustomerPortalProjectProductsOrg.from_dict(d.pop("org"))

        output_customer_portal_project_products = cls(
            products=products,
            payments=payments,
            escalation=escalation,
            project=project,
            org=org,
        )

        output_customer_portal_project_products.additional_properties = d
        return output_customer_portal_project_products

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
