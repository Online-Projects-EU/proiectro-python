from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_product_work_template import OutputProductWorkTemplate


T = TypeVar("T", bound="OutputProductWorkTemplates")


@_attrs_define
class OutputProductWorkTemplates:
    """Templates linked to product via catalog

    Attributes:
        project_id (str):
        product_id (str):
        catalog_id (str):
        catalog_name (str):
        templates (list[OutputProductWorkTemplate]):
    """

    project_id: str
    product_id: str
    catalog_id: str
    catalog_name: str
    templates: list[OutputProductWorkTemplate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        product_id = self.product_id

        catalog_id = self.catalog_id

        catalog_name = self.catalog_name

        templates = []
        for templates_item_data in self.templates:
            templates_item = templates_item_data.to_dict()
            templates.append(templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "product_id": product_id,
                "catalog_id": catalog_id,
                "catalog_name": catalog_name,
                "templates": templates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_product_work_template import OutputProductWorkTemplate

        d = dict(src_dict)
        project_id = d.pop("project_id")

        product_id = d.pop("product_id")

        catalog_id = d.pop("catalog_id")

        catalog_name = d.pop("catalog_name")

        templates = []
        _templates = d.pop("templates")
        for templates_item_data in _templates:
            templates_item = OutputProductWorkTemplate.from_dict(templates_item_data)

            templates.append(templates_item)

        output_product_work_templates = cls(
            project_id=project_id,
            product_id=product_id,
            catalog_id=catalog_id,
            catalog_name=catalog_name,
            templates=templates,
        )

        output_product_work_templates.additional_properties = d
        return output_product_work_templates

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
