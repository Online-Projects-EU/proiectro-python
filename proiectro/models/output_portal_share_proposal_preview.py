from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_portal_share_proposal_preview_acceptance_info import (
        OutputPortalShareProposalPreviewAcceptanceInfo,
    )
    from ..models.output_portal_share_proposal_preview_company import (
        OutputPortalShareProposalPreviewCompany,
    )
    from ..models.output_portal_share_proposal_preview_customer import (
        OutputPortalShareProposalPreviewCustomer,
    )
    from ..models.output_portal_share_proposal_preview_executive_summary import (
        OutputPortalShareProposalPreviewExecutiveSummary,
    )
    from ..models.output_portal_share_proposal_preview_header import (
        OutputPortalShareProposalPreviewHeader,
    )
    from ..models.output_portal_share_proposal_preview_investment_summary import (
        OutputPortalShareProposalPreviewInvestmentSummary,
    )
    from ..models.output_portal_share_proposal_preview_payment_schedule_item import (
        OutputPortalShareProposalPreviewPaymentScheduleItem,
    )
    from ..models.output_portal_share_proposal_preview_products_item import (
        OutputPortalShareProposalPreviewProductsItem,
    )
    from ..models.output_portal_share_proposal_preview_terms_conditions import (
        OutputPortalShareProposalPreviewTermsConditions,
    )


T = TypeVar("T", bound="OutputPortalShareProposalPreview")


@_attrs_define
class OutputPortalShareProposalPreview:
    """
    Attributes:
        company (OutputPortalShareProposalPreviewCompany):
        customer (OutputPortalShareProposalPreviewCustomer):
        header (OutputPortalShareProposalPreviewHeader):
        executive_summary (OutputPortalShareProposalPreviewExecutiveSummary):
        products (list[OutputPortalShareProposalPreviewProductsItem]):
        payment_schedule (list[OutputPortalShareProposalPreviewPaymentScheduleItem]):
        investment_summary (OutputPortalShareProposalPreviewInvestmentSummary):
        terms_conditions (OutputPortalShareProposalPreviewTermsConditions):
        acceptance_info (OutputPortalShareProposalPreviewAcceptanceInfo):
        generated_at (datetime.datetime):
        tenant_path (str):
        proposal_id (str):
        share_id (str):
        item_id (str):
        has_product_pictures (bool | Unset):  Default: False.
        customer_org_id (None | str | Unset):
        updated_on (datetime.datetime | None | Unset):
    """

    company: OutputPortalShareProposalPreviewCompany
    customer: OutputPortalShareProposalPreviewCustomer
    header: OutputPortalShareProposalPreviewHeader
    executive_summary: OutputPortalShareProposalPreviewExecutiveSummary
    products: list[OutputPortalShareProposalPreviewProductsItem]
    payment_schedule: list[OutputPortalShareProposalPreviewPaymentScheduleItem]
    investment_summary: OutputPortalShareProposalPreviewInvestmentSummary
    terms_conditions: OutputPortalShareProposalPreviewTermsConditions
    acceptance_info: OutputPortalShareProposalPreviewAcceptanceInfo
    generated_at: datetime.datetime
    tenant_path: str
    proposal_id: str
    share_id: str
    item_id: str
    has_product_pictures: bool | Unset = False
    customer_org_id: None | str | Unset = UNSET
    updated_on: datetime.datetime | None | Unset = UNSET
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

        generated_at = self.generated_at.isoformat()

        tenant_path = self.tenant_path

        proposal_id = self.proposal_id

        share_id = self.share_id

        item_id = self.item_id

        has_product_pictures = self.has_product_pictures

        customer_org_id: None | str | Unset
        if isinstance(self.customer_org_id, Unset):
            customer_org_id = UNSET
        else:
            customer_org_id = self.customer_org_id

        updated_on: None | str | Unset
        if isinstance(self.updated_on, Unset):
            updated_on = UNSET
        elif isinstance(self.updated_on, datetime.datetime):
            updated_on = self.updated_on.isoformat()
        else:
            updated_on = self.updated_on

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
                "share_id": share_id,
                "item_id": item_id,
            }
        )
        if has_product_pictures is not UNSET:
            field_dict["has_product_pictures"] = has_product_pictures
        if customer_org_id is not UNSET:
            field_dict["customer_org_id"] = customer_org_id
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_portal_share_proposal_preview_acceptance_info import (
            OutputPortalShareProposalPreviewAcceptanceInfo,
        )
        from ..models.output_portal_share_proposal_preview_company import (
            OutputPortalShareProposalPreviewCompany,
        )
        from ..models.output_portal_share_proposal_preview_customer import (
            OutputPortalShareProposalPreviewCustomer,
        )
        from ..models.output_portal_share_proposal_preview_executive_summary import (
            OutputPortalShareProposalPreviewExecutiveSummary,
        )
        from ..models.output_portal_share_proposal_preview_header import (
            OutputPortalShareProposalPreviewHeader,
        )
        from ..models.output_portal_share_proposal_preview_investment_summary import (
            OutputPortalShareProposalPreviewInvestmentSummary,
        )
        from ..models.output_portal_share_proposal_preview_payment_schedule_item import (
            OutputPortalShareProposalPreviewPaymentScheduleItem,
        )
        from ..models.output_portal_share_proposal_preview_products_item import (
            OutputPortalShareProposalPreviewProductsItem,
        )
        from ..models.output_portal_share_proposal_preview_terms_conditions import (
            OutputPortalShareProposalPreviewTermsConditions,
        )

        d = dict(src_dict)
        company = OutputPortalShareProposalPreviewCompany.from_dict(d.pop("company"))

        customer = OutputPortalShareProposalPreviewCustomer.from_dict(d.pop("customer"))

        header = OutputPortalShareProposalPreviewHeader.from_dict(d.pop("header"))

        executive_summary = OutputPortalShareProposalPreviewExecutiveSummary.from_dict(
            d.pop("executive_summary")
        )

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = OutputPortalShareProposalPreviewProductsItem.from_dict(
                products_item_data
            )

            products.append(products_item)

        payment_schedule = []
        _payment_schedule = d.pop("payment_schedule")
        for payment_schedule_item_data in _payment_schedule:
            payment_schedule_item = (
                OutputPortalShareProposalPreviewPaymentScheduleItem.from_dict(
                    payment_schedule_item_data
                )
            )

            payment_schedule.append(payment_schedule_item)

        investment_summary = (
            OutputPortalShareProposalPreviewInvestmentSummary.from_dict(
                d.pop("investment_summary")
            )
        )

        terms_conditions = OutputPortalShareProposalPreviewTermsConditions.from_dict(
            d.pop("terms_conditions")
        )

        acceptance_info = OutputPortalShareProposalPreviewAcceptanceInfo.from_dict(
            d.pop("acceptance_info")
        )

        generated_at = isoparse(d.pop("generated_at"))

        tenant_path = d.pop("tenant_path")

        proposal_id = d.pop("proposal_id")

        share_id = d.pop("share_id")

        item_id = d.pop("item_id")

        has_product_pictures = d.pop("has_product_pictures", UNSET)

        def _parse_customer_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_org_id = _parse_customer_org_id(d.pop("customer_org_id", UNSET))

        def _parse_updated_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_on_type_0 = isoparse(data)

                return updated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_on = _parse_updated_on(d.pop("updated_on", UNSET))

        output_portal_share_proposal_preview = cls(
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
            share_id=share_id,
            item_id=item_id,
            has_product_pictures=has_product_pictures,
            customer_org_id=customer_org_id,
            updated_on=updated_on,
        )

        output_portal_share_proposal_preview.additional_properties = d
        return output_portal_share_proposal_preview

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
