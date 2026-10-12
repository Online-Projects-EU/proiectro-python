from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PartnerRejectProduct")


@_attrs_define
class PartnerRejectProduct:
    """Input schema for partner rejecting a deliverable in partner portal

    Attributes:
        bridge_id (str):
        project_id (str):
        product_id (str):
        status_id (str):
        reason (str):
    """

    bridge_id: str
    project_id: str
    product_id: str
    status_id: str
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        project_id = self.project_id

        product_id = self.product_id

        status_id = self.status_id

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "project_id": project_id,
                "product_id": product_id,
                "status_id": status_id,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        project_id = d.pop("project_id")

        product_id = d.pop("product_id")

        status_id = d.pop("status_id")

        reason = d.pop("reason")

        partner_reject_product = cls(
            bridge_id=bridge_id,
            project_id=project_id,
            product_id=product_id,
            status_id=status_id,
            reason=reason,
        )

        partner_reject_product.additional_properties = d
        return partner_reject_product

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
