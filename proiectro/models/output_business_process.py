from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_process_artifact import BusinessProcessArtifact
    from ..models.business_process_dependency import BusinessProcessDependency
    from ..models.business_process_link import BusinessProcessLink
    from ..models.business_process_task import BusinessProcessTask


T = TypeVar("T", bound="OutputBusinessProcess")


@_attrs_define
class OutputBusinessProcess:
    """Business process details with all tasks

    Attributes:
        process_name (str):
        description (str):
        tasks (list[BusinessProcessTask]):
        input_artifacts (list[BusinessProcessArtifact]):
        modification_artifacts (list[BusinessProcessArtifact]):
        output_artifacts (list[BusinessProcessArtifact]):
        dependencies (list[BusinessProcessDependency] | Unset):
        enabled (list[BusinessProcessDependency] | Unset):
        process_key (str | Unset):  Default: ''.
        back (BusinessProcessLink | None | Unset):
        highlight_task (int | None | Unset):
    """

    process_name: str
    description: str
    tasks: list[BusinessProcessTask]
    input_artifacts: list[BusinessProcessArtifact]
    modification_artifacts: list[BusinessProcessArtifact]
    output_artifacts: list[BusinessProcessArtifact]
    dependencies: list[BusinessProcessDependency] | Unset = UNSET
    enabled: list[BusinessProcessDependency] | Unset = UNSET
    process_key: str | Unset = ""
    back: BusinessProcessLink | None | Unset = UNSET
    highlight_task: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.business_process_link import BusinessProcessLink

        process_name = self.process_name

        description = self.description

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)

        input_artifacts = []
        for input_artifacts_item_data in self.input_artifacts:
            input_artifacts_item = input_artifacts_item_data.to_dict()
            input_artifacts.append(input_artifacts_item)

        modification_artifacts = []
        for modification_artifacts_item_data in self.modification_artifacts:
            modification_artifacts_item = modification_artifacts_item_data.to_dict()
            modification_artifacts.append(modification_artifacts_item)

        output_artifacts = []
        for output_artifacts_item_data in self.output_artifacts:
            output_artifacts_item = output_artifacts_item_data.to_dict()
            output_artifacts.append(output_artifacts_item)

        dependencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = dependencies_item_data.to_dict()
                dependencies.append(dependencies_item)

        enabled: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = []
            for enabled_item_data in self.enabled:
                enabled_item = enabled_item_data.to_dict()
                enabled.append(enabled_item)

        process_key = self.process_key

        back: dict[str, Any] | None | Unset
        if isinstance(self.back, Unset):
            back = UNSET
        elif isinstance(self.back, BusinessProcessLink):
            back = self.back.to_dict()
        else:
            back = self.back

        highlight_task: int | None | Unset
        if isinstance(self.highlight_task, Unset):
            highlight_task = UNSET
        else:
            highlight_task = self.highlight_task

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_name": process_name,
                "description": description,
                "tasks": tasks,
                "input_artifacts": input_artifacts,
                "modification_artifacts": modification_artifacts,
                "output_artifacts": output_artifacts,
            }
        )
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if process_key is not UNSET:
            field_dict["process_key"] = process_key
        if back is not UNSET:
            field_dict["back"] = back
        if highlight_task is not UNSET:
            field_dict["highlight_task"] = highlight_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_process_artifact import BusinessProcessArtifact
        from ..models.business_process_dependency import BusinessProcessDependency
        from ..models.business_process_link import BusinessProcessLink
        from ..models.business_process_task import BusinessProcessTask

        d = dict(src_dict)
        process_name = d.pop("process_name")

        description = d.pop("description")

        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = BusinessProcessTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        input_artifacts = []
        _input_artifacts = d.pop("input_artifacts")
        for input_artifacts_item_data in _input_artifacts:
            input_artifacts_item = BusinessProcessArtifact.from_dict(
                input_artifacts_item_data
            )

            input_artifacts.append(input_artifacts_item)

        modification_artifacts = []
        _modification_artifacts = d.pop("modification_artifacts")
        for modification_artifacts_item_data in _modification_artifacts:
            modification_artifacts_item = BusinessProcessArtifact.from_dict(
                modification_artifacts_item_data
            )

            modification_artifacts.append(modification_artifacts_item)

        output_artifacts = []
        _output_artifacts = d.pop("output_artifacts")
        for output_artifacts_item_data in _output_artifacts:
            output_artifacts_item = BusinessProcessArtifact.from_dict(
                output_artifacts_item_data
            )

            output_artifacts.append(output_artifacts_item)

        _dependencies = d.pop("dependencies", UNSET)
        dependencies: list[BusinessProcessDependency] | Unset = UNSET
        if _dependencies is not UNSET:
            dependencies = []
            for dependencies_item_data in _dependencies:
                dependencies_item = BusinessProcessDependency.from_dict(
                    dependencies_item_data
                )

                dependencies.append(dependencies_item)

        _enabled = d.pop("enabled", UNSET)
        enabled: list[BusinessProcessDependency] | Unset = UNSET
        if _enabled is not UNSET:
            enabled = []
            for enabled_item_data in _enabled:
                enabled_item = BusinessProcessDependency.from_dict(enabled_item_data)

                enabled.append(enabled_item)

        process_key = d.pop("process_key", UNSET)

        def _parse_back(data: object) -> BusinessProcessLink | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                back_type_0 = BusinessProcessLink.from_dict(data)

                return back_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BusinessProcessLink | None | Unset, data)

        back = _parse_back(d.pop("back", UNSET))

        def _parse_highlight_task(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        highlight_task = _parse_highlight_task(d.pop("highlight_task", UNSET))

        output_business_process = cls(
            process_name=process_name,
            description=description,
            tasks=tasks,
            input_artifacts=input_artifacts,
            modification_artifacts=modification_artifacts,
            output_artifacts=output_artifacts,
            dependencies=dependencies,
            enabled=enabled,
            process_key=process_key,
            back=back,
            highlight_task=highlight_task,
        )

        output_business_process.additional_properties = d
        return output_business_process

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
