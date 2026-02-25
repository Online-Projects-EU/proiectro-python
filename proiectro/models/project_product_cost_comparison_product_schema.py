from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectProductCostComparisonProductSchema")


@_attrs_define
class ProjectProductCostComparisonProductSchema:
    """Individual product cost comparison data for grouped bar chart

    Attributes:
        product_id (str):
        product_name (str):
        proposal_cost (str):
        project_cost (str):
        currency_symbol (str):
        has_work_items (bool):
        product_code (None | str | Unset):
    """

    product_id: str
    product_name: str
    proposal_cost: str
    project_cost: str
    currency_symbol: str
    has_work_items: bool
    product_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_name = self.product_name

        proposal_cost = self.proposal_cost

        project_cost = self.project_cost

        currency_symbol = self.currency_symbol

        has_work_items = self.has_work_items

        product_code: None | str | Unset
        if isinstance(self.product_code, Unset):
            product_code = UNSET
        else:
            product_code = self.product_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "product_name": product_name,
                "proposal_cost": proposal_cost,
                "project_cost": project_cost,
                "currency_symbol": currency_symbol,
                "has_work_items": has_work_items,
            }
        )
        if product_code is not UNSET:
            field_dict["product_code"] = product_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        product_name = d.pop("product_name")

        proposal_cost = d.pop("proposal_cost")

        project_cost = d.pop("project_cost")

        currency_symbol = d.pop("currency_symbol")

        has_work_items = d.pop("has_work_items")

        def _parse_product_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_code = _parse_product_code(d.pop("product_code", UNSET))

        project_product_cost_comparison_product_schema = cls(
            product_id=product_id,
            product_name=product_name,
            proposal_cost=proposal_cost,
            project_cost=project_cost,
            currency_symbol=currency_symbol,
            has_work_items=has_work_items,
            product_code=product_code,
        )

        project_product_cost_comparison_product_schema.additional_properties = d
        return project_product_cost_comparison_product_schema

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
