from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveProposalItem")


@_attrs_define
class ActiveProposalItem:
    """Proposal item for projects view (active proposals list)

    Attributes:
        id (str):
        name (str):
        stage_name (str):
        stage_type (str):
        product_count (int):
        customer_name (None | str | Unset):
    """

    id: str
    name: str
    stage_name: str
    stage_type: str
    product_count: int
    customer_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        stage_name = self.stage_name

        stage_type = self.stage_type

        product_count = self.product_count

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "stage_name": stage_name,
                "stage_type": stage_type,
                "product_count": product_count,
            }
        )
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        product_count = d.pop("product_count")

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        active_proposal_item = cls(
            id=id,
            name=name,
            stage_name=stage_name,
            stage_type=stage_type,
            product_count=product_count,
            customer_name=customer_name,
        )

        active_proposal_item.additional_properties = d
        return active_proposal_item

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
