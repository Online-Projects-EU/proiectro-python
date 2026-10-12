from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWorkItemStatus")


@_attrs_define
class UpdateWorkItemStatus:
    """Schema for updating work item status (execution-type work items only).

    Dynamic behavior based on current state:
    - NOT finished: Send finished_at to mark as complete (auto-sets is_finished=True, percent=100)
    - IS finished: Send is_finished=False to unmark (clears finished_at, resets percent if was 100)
    - Always: Send percent_complete to adjust progress independently

        Attributes:
            percent_complete (int | None | Unset):
            is_finished (bool | None | Unset):
            finished_at (None | str | Unset):
    """

    percent_complete: int | None | Unset = UNSET
    is_finished: bool | None | Unset = UNSET
    finished_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percent_complete: int | None | Unset
        if isinstance(self.percent_complete, Unset):
            percent_complete = UNSET
        else:
            percent_complete = self.percent_complete

        is_finished: bool | None | Unset
        if isinstance(self.is_finished, Unset):
            is_finished = UNSET
        else:
            is_finished = self.is_finished

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = self.finished_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent_complete is not UNSET:
            field_dict["percent_complete"] = percent_complete
        if is_finished is not UNSET:
            field_dict["is_finished"] = is_finished
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_percent_complete(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        percent_complete = _parse_percent_complete(d.pop("percent_complete", UNSET))

        def _parse_is_finished(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_finished = _parse_is_finished(d.pop("is_finished", UNSET))

        def _parse_finished_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        update_work_item_status = cls(
            percent_complete=percent_complete,
            is_finished=is_finished,
            finished_at=finished_at,
        )

        update_work_item_status.additional_properties = d
        return update_work_item_status

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
