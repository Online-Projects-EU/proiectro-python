from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWBSConfiguration")


@_attrs_define
class AddWBSConfiguration:
    """
    Attributes:
        name (str):
        active (bool | None | Unset):  Default: False.
        description (None | str | Unset):
        terminology_deliverable (None | str | Unset):
        terminology_activity (None | str | Unset):
        terminology_work_package (None | str | Unset):
        terminology_task (None | str | Unset):
        terminology_milestone (None | str | Unset):
        terminology_stage (None | str | Unset):
        terminology_phase (None | str | Unset):
    """

    name: str
    active: bool | None | Unset = False
    description: None | str | Unset = UNSET
    terminology_deliverable: None | str | Unset = UNSET
    terminology_activity: None | str | Unset = UNSET
    terminology_work_package: None | str | Unset = UNSET
    terminology_task: None | str | Unset = UNSET
    terminology_milestone: None | str | Unset = UNSET
    terminology_stage: None | str | Unset = UNSET
    terminology_phase: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        terminology_deliverable: None | str | Unset
        if isinstance(self.terminology_deliverable, Unset):
            terminology_deliverable = UNSET
        else:
            terminology_deliverable = self.terminology_deliverable

        terminology_activity: None | str | Unset
        if isinstance(self.terminology_activity, Unset):
            terminology_activity = UNSET
        else:
            terminology_activity = self.terminology_activity

        terminology_work_package: None | str | Unset
        if isinstance(self.terminology_work_package, Unset):
            terminology_work_package = UNSET
        else:
            terminology_work_package = self.terminology_work_package

        terminology_task: None | str | Unset
        if isinstance(self.terminology_task, Unset):
            terminology_task = UNSET
        else:
            terminology_task = self.terminology_task

        terminology_milestone: None | str | Unset
        if isinstance(self.terminology_milestone, Unset):
            terminology_milestone = UNSET
        else:
            terminology_milestone = self.terminology_milestone

        terminology_stage: None | str | Unset
        if isinstance(self.terminology_stage, Unset):
            terminology_stage = UNSET
        else:
            terminology_stage = self.terminology_stage

        terminology_phase: None | str | Unset
        if isinstance(self.terminology_phase, Unset):
            terminology_phase = UNSET
        else:
            terminology_phase = self.terminology_phase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if description is not UNSET:
            field_dict["description"] = description
        if terminology_deliverable is not UNSET:
            field_dict["terminology_deliverable"] = terminology_deliverable
        if terminology_activity is not UNSET:
            field_dict["terminology_activity"] = terminology_activity
        if terminology_work_package is not UNSET:
            field_dict["terminology_work_package"] = terminology_work_package
        if terminology_task is not UNSET:
            field_dict["terminology_task"] = terminology_task
        if terminology_milestone is not UNSET:
            field_dict["terminology_milestone"] = terminology_milestone
        if terminology_stage is not UNSET:
            field_dict["terminology_stage"] = terminology_stage
        if terminology_phase is not UNSET:
            field_dict["terminology_phase"] = terminology_phase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_terminology_deliverable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terminology_deliverable = _parse_terminology_deliverable(
            d.pop("terminology_deliverable", UNSET)
        )

        def _parse_terminology_activity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terminology_activity = _parse_terminology_activity(
            d.pop("terminology_activity", UNSET)
        )

        def _parse_terminology_work_package(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terminology_work_package = _parse_terminology_work_package(
            d.pop("terminology_work_package", UNSET)
        )

        def _parse_terminology_task(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terminology_task = _parse_terminology_task(d.pop("terminology_task", UNSET))

        def _parse_terminology_milestone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terminology_milestone = _parse_terminology_milestone(
            d.pop("terminology_milestone", UNSET)
        )

        def _parse_terminology_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terminology_stage = _parse_terminology_stage(d.pop("terminology_stage", UNSET))

        def _parse_terminology_phase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        terminology_phase = _parse_terminology_phase(d.pop("terminology_phase", UNSET))

        add_wbs_configuration = cls(
            name=name,
            active=active,
            description=description,
            terminology_deliverable=terminology_deliverable,
            terminology_activity=terminology_activity,
            terminology_work_package=terminology_work_package,
            terminology_task=terminology_task,
            terminology_milestone=terminology_milestone,
            terminology_stage=terminology_stage,
            terminology_phase=terminology_phase,
        )

        add_wbs_configuration.additional_properties = d
        return add_wbs_configuration

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
