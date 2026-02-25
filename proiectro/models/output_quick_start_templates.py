from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_start_category_info import QuickStartCategoryInfo
    from ..models.quick_start_template import QuickStartTemplate


T = TypeVar("T", bound="OutputQuickStartTemplates")


@_attrs_define
class OutputQuickStartTemplates:
    """Available templates for a category.

    Attributes:
        category (str):
        templates (list[QuickStartTemplate]):
        category_info (None | QuickStartCategoryInfo | Unset):
        error (None | str | Unset):
    """

    category: str
    templates: list[QuickStartTemplate]
    category_info: None | QuickStartCategoryInfo | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_start_category_info import QuickStartCategoryInfo

        category = self.category

        templates = []
        for templates_item_data in self.templates:
            templates_item = templates_item_data.to_dict()
            templates.append(templates_item)

        category_info: dict[str, Any] | None | Unset
        if isinstance(self.category_info, Unset):
            category_info = UNSET
        elif isinstance(self.category_info, QuickStartCategoryInfo):
            category_info = self.category_info.to_dict()
        else:
            category_info = self.category_info

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "templates": templates,
            }
        )
        if category_info is not UNSET:
            field_dict["category_info"] = category_info
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_start_category_info import QuickStartCategoryInfo
        from ..models.quick_start_template import QuickStartTemplate

        d = dict(src_dict)
        category = d.pop("category")

        templates = []
        _templates = d.pop("templates")
        for templates_item_data in _templates:
            templates_item = QuickStartTemplate.from_dict(templates_item_data)

            templates.append(templates_item)

        def _parse_category_info(data: object) -> None | QuickStartCategoryInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_info_type_0 = QuickStartCategoryInfo.from_dict(data)

                return category_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QuickStartCategoryInfo | Unset, data)

        category_info = _parse_category_info(d.pop("category_info", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        output_quick_start_templates = cls(
            category=category,
            templates=templates,
            category_info=category_info,
            error=error,
        )

        output_quick_start_templates.additional_properties = d
        return output_quick_start_templates

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
