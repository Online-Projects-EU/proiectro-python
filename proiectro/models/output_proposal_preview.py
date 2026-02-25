from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_proposal_preview_acceptance_info import (
        OutputProposalPreviewAcceptanceInfo,
    )
    from ..models.output_proposal_preview_company import OutputProposalPreviewCompany
    from ..models.output_proposal_preview_customer import OutputProposalPreviewCustomer
    from ..models.output_proposal_preview_executive_summary import (
        OutputProposalPreviewExecutiveSummary,
    )
    from ..models.output_proposal_preview_header import OutputProposalPreviewHeader
    from ..models.output_proposal_preview_investment_summary import (
        OutputProposalPreviewInvestmentSummary,
    )
    from ..models.output_proposal_preview_payment_schedule_item import (
        OutputProposalPreviewPaymentScheduleItem,
    )
    from ..models.output_proposal_preview_products_item import (
        OutputProposalPreviewProductsItem,
    )
    from ..models.output_proposal_preview_terms_conditions import (
        OutputProposalPreviewTermsConditions,
    )


T = TypeVar("T", bound="OutputProposalPreview")


@_attrs_define
class OutputProposalPreview:
    """Proposal preview with full proposal details for customer presentation

    Attributes:
        company (OutputProposalPreviewCompany):
        customer (OutputProposalPreviewCustomer):
        header (OutputProposalPreviewHeader):
        executive_summary (OutputProposalPreviewExecutiveSummary):
        products (list[OutputProposalPreviewProductsItem]):
        payment_schedule (list[OutputProposalPreviewPaymentScheduleItem]):
        investment_summary (OutputProposalPreviewInvestmentSummary):
        terms_conditions (OutputProposalPreviewTermsConditions):
        acceptance_info (OutputProposalPreviewAcceptanceInfo):
        generated_at (str):
        tenant_path (str):
        proposal_id (str):
        customer_org_id (None | str | Unset):
    """

    company: OutputProposalPreviewCompany
    customer: OutputProposalPreviewCustomer
    header: OutputProposalPreviewHeader
    executive_summary: OutputProposalPreviewExecutiveSummary
    products: list[OutputProposalPreviewProductsItem]
    payment_schedule: list[OutputProposalPreviewPaymentScheduleItem]
    investment_summary: OutputProposalPreviewInvestmentSummary
    terms_conditions: OutputProposalPreviewTermsConditions
    acceptance_info: OutputProposalPreviewAcceptanceInfo
    generated_at: str
    tenant_path: str
    proposal_id: str
    customer_org_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        customer = self.customer.to_dict()

        header = self.header.to_dict()

        executive_summary = self.executive_summary.to_dict()

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        payment_schedule = []
        for payment_schedule_item_data in self.payment_schedule:
            payment_schedule_item = payment_schedule_item_data.to_dict()
            payment_schedule.append(payment_schedule_item)

        investment_summary = self.investment_summary.to_dict()

        terms_conditions = self.terms_conditions.to_dict()

        acceptance_info = self.acceptance_info.to_dict()

        generated_at = self.generated_at

        tenant_path = self.tenant_path

        proposal_id = self.proposal_id

        customer_org_id: None | str | Unset
        if isinstance(self.customer_org_id, Unset):
            customer_org_id = UNSET
        else:
            customer_org_id = self.customer_org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "customer": customer,
                "header": header,
                "executive_summary": executive_summary,
                "products": products,
                "payment_schedule": payment_schedule,
                "investment_summary": investment_summary,
                "terms_conditions": terms_conditions,
                "acceptance_info": acceptance_info,
                "generated_at": generated_at,
                "tenant_path": tenant_path,
                "proposal_id": proposal_id,
            }
        )
        if customer_org_id is not UNSET:
            field_dict["customer_org_id"] = customer_org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_proposal_preview_acceptance_info import (
            OutputProposalPreviewAcceptanceInfo,
        )
        from ..models.output_proposal_preview_company import (
            OutputProposalPreviewCompany,
        )
        from ..models.output_proposal_preview_customer import (
            OutputProposalPreviewCustomer,
        )
        from ..models.output_proposal_preview_executive_summary import (
            OutputProposalPreviewExecutiveSummary,
        )
        from ..models.output_proposal_preview_header import OutputProposalPreviewHeader
        from ..models.output_proposal_preview_investment_summary import (
            OutputProposalPreviewInvestmentSummary,
        )
        from ..models.output_proposal_preview_payment_schedule_item import (
            OutputProposalPreviewPaymentScheduleItem,
        )
        from ..models.output_proposal_preview_products_item import (
            OutputProposalPreviewProductsItem,
        )
        from ..models.output_proposal_preview_terms_conditions import (
            OutputProposalPreviewTermsConditions,
        )

        d = dict(src_dict)
        company = OutputProposalPreviewCompany.from_dict(d.pop("company"))

        customer = OutputProposalPreviewCustomer.from_dict(d.pop("customer"))

        header = OutputProposalPreviewHeader.from_dict(d.pop("header"))

        executive_summary = OutputProposalPreviewExecutiveSummary.from_dict(
            d.pop("executive_summary")
        )

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = OutputProposalPreviewProductsItem.from_dict(
                products_item_data
            )

            products.append(products_item)

        payment_schedule = []
        _payment_schedule = d.pop("payment_schedule")
        for payment_schedule_item_data in _payment_schedule:
            payment_schedule_item = OutputProposalPreviewPaymentScheduleItem.from_dict(
                payment_schedule_item_data
            )

            payment_schedule.append(payment_schedule_item)

        investment_summary = OutputProposalPreviewInvestmentSummary.from_dict(
            d.pop("investment_summary")
        )

        terms_conditions = OutputProposalPreviewTermsConditions.from_dict(
            d.pop("terms_conditions")
        )

        acceptance_info = OutputProposalPreviewAcceptanceInfo.from_dict(
            d.pop("acceptance_info")
        )

        generated_at = d.pop("generated_at")

        tenant_path = d.pop("tenant_path")

        proposal_id = d.pop("proposal_id")

        def _parse_customer_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_org_id = _parse_customer_org_id(d.pop("customer_org_id", UNSET))

        output_proposal_preview = cls(
            company=company,
            customer=customer,
            header=header,
            executive_summary=executive_summary,
            products=products,
            payment_schedule=payment_schedule,
            investment_summary=investment_summary,
            terms_conditions=terms_conditions,
            acceptance_info=acceptance_info,
            generated_at=generated_at,
            tenant_path=tenant_path,
            proposal_id=proposal_id,
            customer_org_id=customer_org_id,
        )

        output_proposal_preview.additional_properties = d
        return output_proposal_preview

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
