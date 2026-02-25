from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.guide_campaign import GuideCampaign


T = TypeVar("T", bound="OutputActiveCampaigns")


@_attrs_define
class OutputActiveCampaigns:
    """All active guidance campaigns for the user.

    Attributes:
        campaigns (list[GuideCampaign]):
    """

    campaigns: list[GuideCampaign]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaigns = []
        for campaigns_item_data in self.campaigns:
            campaigns_item = campaigns_item_data.to_dict()
            campaigns.append(campaigns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaigns": campaigns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guide_campaign import GuideCampaign

        d = dict(src_dict)
        campaigns = []
        _campaigns = d.pop("campaigns")
        for campaigns_item_data in _campaigns:
            campaigns_item = GuideCampaign.from_dict(campaigns_item_data)

            campaigns.append(campaigns_item)

        output_active_campaigns = cls(
            campaigns=campaigns,
        )

        output_active_campaigns.additional_properties = d
        return output_active_campaigns

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
