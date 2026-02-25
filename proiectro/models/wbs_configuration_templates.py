from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.work_template import WorkTemplate


T = TypeVar("T", bound="WBSConfigurationTemplates")


@_attrs_define
class WBSConfigurationTemplates:
    """Root work item templates associated with a WBS Configuration

    Attributes:
        wbs_configuration_id (str):
        wbs_configuration_name (str):
        work_templates (list[WorkTemplate]):
    """

    wbs_configuration_id: str
    wbs_configuration_name: str
    work_templates: list[WorkTemplate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wbs_configuration_id = self.wbs_configuration_id

        wbs_configuration_name = self.wbs_configuration_name

        work_templates = []
        for work_templates_item_data in self.work_templates:
            work_templates_item = work_templates_item_data.to_dict()
            work_templates.append(work_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wbs_configuration_id": wbs_configuration_id,
                "wbs_configuration_name": wbs_configuration_name,
                "work_templates": work_templates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_template import WorkTemplate

        d = dict(src_dict)
        wbs_configuration_id = d.pop("wbs_configuration_id")

        wbs_configuration_name = d.pop("wbs_configuration_name")

        work_templates = []
        _work_templates = d.pop("work_templates")
        for work_templates_item_data in _work_templates:
            work_templates_item = WorkTemplate.from_dict(work_templates_item_data)

            work_templates.append(work_templates_item)

        wbs_configuration_templates = cls(
            wbs_configuration_id=wbs_configuration_id,
            wbs_configuration_name=wbs_configuration_name,
            work_templates=work_templates,
        )

        wbs_configuration_templates.additional_properties = d
        return wbs_configuration_templates

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
