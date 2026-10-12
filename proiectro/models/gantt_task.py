from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GanttTask")


@_attrs_define
class GanttTask:
    """Single task for Frappe Gantt visualization

    Attributes:
        id (str):
        name (str):
        start (str):
        end (str):
        progress (int):
        dependencies (str):
        custom_class (str):
        bg_color (str):
        text_color (str):
    """

    id: str
    name: str
    start: str
    end: str
    progress: int
    dependencies: str
    custom_class: str
    bg_color: str
    text_color: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        start = self.start

        end = self.end

        progress = self.progress

        dependencies = self.dependencies

        custom_class = self.custom_class

        bg_color = self.bg_color

        text_color = self.text_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "start": start,
                "end": end,
                "progress": progress,
                "dependencies": dependencies,
                "custom_class": custom_class,
                "bg_color": bg_color,
                "text_color": text_color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        start = d.pop("start")

        end = d.pop("end")

        progress = d.pop("progress")

        dependencies = d.pop("dependencies")

        custom_class = d.pop("custom_class")

        bg_color = d.pop("bg_color")

        text_color = d.pop("text_color")

        gantt_task = cls(
            id=id,
            name=name,
            start=start,
            end=end,
            progress=progress,
            dependencies=dependencies,
            custom_class=custom_class,
            bg_color=bg_color,
            text_color=text_color,
        )

        gantt_task.additional_properties = d
        return gantt_task

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
