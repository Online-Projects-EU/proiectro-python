from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tenant_funnel_configuration_stage import (
        TenantFunnelConfigurationStage,
    )


T = TypeVar("T", bound="TenantFunnelConfigurationStages")


@_attrs_define
class TenantFunnelConfigurationStages:
    """
    Attributes:
        funnel_configuration (str):
        stages (list[TenantFunnelConfigurationStage]):
        has_lead_stage (bool):
        has_closed_won_stage (bool):
        has_closed_lost_stage (bool):
    """

    funnel_configuration: str
    stages: list[TenantFunnelConfigurationStage]
    has_lead_stage: bool
    has_closed_won_stage: bool
    has_closed_lost_stage: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funnel_configuration = self.funnel_configuration

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        has_lead_stage = self.has_lead_stage

        has_closed_won_stage = self.has_closed_won_stage

        has_closed_lost_stage = self.has_closed_lost_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "funnel_configuration": funnel_configuration,
                "stages": stages,
                "has_lead_stage": has_lead_stage,
                "has_closed_won_stage": has_closed_won_stage,
                "has_closed_lost_stage": has_closed_lost_stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_funnel_configuration_stage import (
            TenantFunnelConfigurationStage,
        )

        d = dict(src_dict)
        funnel_configuration = d.pop("funnel_configuration")

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = TenantFunnelConfigurationStage.from_dict(stages_item_data)

            stages.append(stages_item)

        has_lead_stage = d.pop("has_lead_stage")

        has_closed_won_stage = d.pop("has_closed_won_stage")

        has_closed_lost_stage = d.pop("has_closed_lost_stage")

        tenant_funnel_configuration_stages = cls(
            funnel_configuration=funnel_configuration,
            stages=stages,
            has_lead_stage=has_lead_stage,
            has_closed_won_stage=has_closed_won_stage,
            has_closed_lost_stage=has_closed_lost_stage,
        )

        tenant_funnel_configuration_stages.additional_properties = d
        return tenant_funnel_configuration_stages

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
