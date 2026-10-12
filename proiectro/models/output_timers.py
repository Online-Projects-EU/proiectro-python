from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_timer_item import OutputTimerItem


T = TypeVar("T", bound="OutputTimers")


@_attrs_define
class OutputTimers:
    """
    Attributes:
        timers (list[OutputTimerItem]):
    """

    timers: list[OutputTimerItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timers = []
        for timers_item_data in self.timers:
            timers_item = timers_item_data.to_dict()
            timers.append(timers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timers": timers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_timer_item import OutputTimerItem

        d = dict(src_dict)
        timers = []
        _timers = d.pop("timers")
        for timers_item_data in _timers:
            timers_item = OutputTimerItem.from_dict(timers_item_data)

            timers.append(timers_item)

        output_timers = cls(
            timers=timers,
        )

        output_timers.additional_properties = d
        return output_timers

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
