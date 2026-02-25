from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_webhook_delivery import OutputWebhookDelivery


T = TypeVar("T", bound="OutputWebhookDeliveries")


@_attrs_define
class OutputWebhookDeliveries:
    """
    Attributes:
        deliveries (list[OutputWebhookDelivery]):
        total (int | Unset):  Default: 0.
    """

    deliveries: list[OutputWebhookDelivery]
    total: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deliveries = []
        for deliveries_item_data in self.deliveries:
            deliveries_item = deliveries_item_data.to_dict()
            deliveries.append(deliveries_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deliveries": deliveries,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_webhook_delivery import OutputWebhookDelivery

        d = dict(src_dict)
        deliveries = []
        _deliveries = d.pop("deliveries")
        for deliveries_item_data in _deliveries:
            deliveries_item = OutputWebhookDelivery.from_dict(deliveries_item_data)

            deliveries.append(deliveries_item)

        total = d.pop("total", UNSET)

        output_webhook_deliveries = cls(
            deliveries=deliveries,
            total=total,
        )

        output_webhook_deliveries.additional_properties = d
        return output_webhook_deliveries

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
