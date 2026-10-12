from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_details import BridgeDetails
    from ..models.output_subtenant_bridge_grant_labels import (
        OutputSubtenantBridgeGrantLabels,
    )


T = TypeVar("T", bound="OutputSubtenantBridge")


@_attrs_define
class OutputSubtenantBridge:
    """Bridge details for a subtenant

    Attributes:
        subtenant_id (str):
        subtenant_name (str):
        grant_labels (OutputSubtenantBridgeGrantLabels):
        bridge (BridgeDetails | None | Unset):
    """

    subtenant_id: str
    subtenant_name: str
    grant_labels: OutputSubtenantBridgeGrantLabels
    bridge: BridgeDetails | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bridge_details import BridgeDetails

        subtenant_id = self.subtenant_id

        subtenant_name = self.subtenant_name

        grant_labels = self.grant_labels.to_dict()

        bridge: dict[str, Any] | None | Unset
        if isinstance(self.bridge, Unset):
            bridge = UNSET
        elif isinstance(self.bridge, BridgeDetails):
            bridge = self.bridge.to_dict()
        else:
            bridge = self.bridge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subtenant_id": subtenant_id,
                "subtenant_name": subtenant_name,
                "grant_labels": grant_labels,
            }
        )
        if bridge is not UNSET:
            field_dict["bridge"] = bridge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bridge_details import BridgeDetails
        from ..models.output_subtenant_bridge_grant_labels import (
            OutputSubtenantBridgeGrantLabels,
        )

        d = dict(src_dict)
        subtenant_id = d.pop("subtenant_id")

        subtenant_name = d.pop("subtenant_name")

        grant_labels = OutputSubtenantBridgeGrantLabels.from_dict(d.pop("grant_labels"))

        def _parse_bridge(data: object) -> BridgeDetails | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bridge_type_0 = BridgeDetails.from_dict(data)

                return bridge_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BridgeDetails | None | Unset, data)

        bridge = _parse_bridge(d.pop("bridge", UNSET))

        output_subtenant_bridge = cls(
            subtenant_id=subtenant_id,
            subtenant_name=subtenant_name,
            grant_labels=grant_labels,
            bridge=bridge,
        )

        output_subtenant_bridge.additional_properties = d
        return output_subtenant_bridge

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
