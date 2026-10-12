from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tenant_product_lifecycle_stage import TenantProductLifecycleStage


T = TypeVar("T", bound="TenantProductLifecycleStages")


@_attrs_define
class TenantProductLifecycleStages:
    """
    Attributes:
        productlifecycle_id (str):
        stages (list[TenantProductLifecycleStage]):
        has_todo_stage (bool):
        has_accepted_stage (bool):
        has_completed_stage (bool):
    """

    productlifecycle_id: str
    stages: list[TenantProductLifecycleStage]
    has_todo_stage: bool
    has_accepted_stage: bool
    has_completed_stage: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        productlifecycle_id = self.productlifecycle_id

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        has_todo_stage = self.has_todo_stage

        has_accepted_stage = self.has_accepted_stage

        has_completed_stage = self.has_completed_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productlifecycle_id": productlifecycle_id,
                "stages": stages,
                "has_todo_stage": has_todo_stage,
                "has_accepted_stage": has_accepted_stage,
                "has_completed_stage": has_completed_stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_product_lifecycle_stage import TenantProductLifecycleStage

        d = dict(src_dict)
        productlifecycle_id = d.pop("productlifecycle_id")

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = TenantProductLifecycleStage.from_dict(stages_item_data)

            stages.append(stages_item)

        has_todo_stage = d.pop("has_todo_stage")

        has_accepted_stage = d.pop("has_accepted_stage")

        has_completed_stage = d.pop("has_completed_stage")

        tenant_product_lifecycle_stages = cls(
            productlifecycle_id=productlifecycle_id,
            stages=stages,
            has_todo_stage=has_todo_stage,
            has_accepted_stage=has_accepted_stage,
            has_completed_stage=has_completed_stage,
        )

        tenant_product_lifecycle_stages.additional_properties = d
        return tenant_product_lifecycle_stages

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
