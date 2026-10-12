from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wbs_config_detail import WBSConfigDetail


T = TypeVar("T", bound="ProjectWBSConfig")


@_attrs_define
class ProjectWBSConfig:
    """
    Attributes:
        project_id (str):
        project_name (str):
        wbs_config (None | Unset | WBSConfigDetail):
        has_work_items (bool | Unset):  Default: False.
    """

    project_id: str
    project_name: str
    wbs_config: None | Unset | WBSConfigDetail = UNSET
    has_work_items: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wbs_config_detail import WBSConfigDetail

        project_id = self.project_id

        project_name = self.project_name

        wbs_config: dict[str, Any] | None | Unset
        if isinstance(self.wbs_config, Unset):
            wbs_config = UNSET
        elif isinstance(self.wbs_config, WBSConfigDetail):
            wbs_config = self.wbs_config.to_dict()
        else:
            wbs_config = self.wbs_config

        has_work_items = self.has_work_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "project_name": project_name,
            }
        )
        if wbs_config is not UNSET:
            field_dict["wbs_config"] = wbs_config
        if has_work_items is not UNSET:
            field_dict["has_work_items"] = has_work_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wbs_config_detail import WBSConfigDetail

        d = dict(src_dict)
        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        def _parse_wbs_config(data: object) -> None | Unset | WBSConfigDetail:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                wbs_config_type_0 = WBSConfigDetail.from_dict(data)

                return wbs_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WBSConfigDetail, data)

        wbs_config = _parse_wbs_config(d.pop("wbs_config", UNSET))

        has_work_items = d.pop("has_work_items", UNSET)

        project_wbs_config = cls(
            project_id=project_id,
            project_name=project_name,
            wbs_config=wbs_config,
            has_work_items=has_work_items,
        )

        project_wbs_config.additional_properties = d
        return project_wbs_config

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
