from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposal_product import ProposalProduct
    from ..models.proposal_product_summary import ProposalProductSummary
    from ..models.proposal_products_proposal import ProposalProductsProposal


T = TypeVar("T", bound="ProposalProducts")


@_attrs_define
class ProposalProducts:
    """
    Attributes:
        products (list[ProposalProduct]):
        proposal (ProposalProductsProposal):
        proposal_summary (ProposalProductSummary):
        is_locked (bool):
    """

    products: list[ProposalProduct]
    proposal: ProposalProductsProposal
    proposal_summary: ProposalProductSummary
    is_locked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        proposal = self.proposal.to_dict()

        proposal_summary = self.proposal_summary.to_dict()

        is_locked = self.is_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "proposal": proposal,
                "proposal_summary": proposal_summary,
                "is_locked": is_locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_product import ProposalProduct
        from ..models.proposal_product_summary import ProposalProductSummary
        from ..models.proposal_products_proposal import ProposalProductsProposal

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = ProposalProduct.from_dict(products_item_data)

            products.append(products_item)

        proposal = ProposalProductsProposal.from_dict(d.pop("proposal"))

        proposal_summary = ProposalProductSummary.from_dict(d.pop("proposal_summary"))

        is_locked = d.pop("is_locked")

        proposal_products = cls(
            products=products,
            proposal=proposal,
            proposal_summary=proposal_summary,
            is_locked=is_locked,
        )

        proposal_products.additional_properties = d
        return proposal_products

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
