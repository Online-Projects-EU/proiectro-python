from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_wbs_configuration import TenantWBSConfiguration


T = TypeVar("T", bound="TenantWBSConfigurations")


@_attrs_define
class TenantWBSConfigurations:
    """
    Attributes:
        wbsconfigurations (list[TenantWBSConfiguration]):
        work_item_types (list[list[str]] | None | Unset):
    """

    wbsconfigurations: list[TenantWBSConfiguration]
    work_item_types: list[list[str]] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wbsconfigurations = []
        for wbsconfigurations_item_data in self.wbsconfigurations:
            wbsconfigurations_item = wbsconfigurations_item_data.to_dict()
            wbsconfigurations.append(wbsconfigurations_item)

        work_item_types: list[list[str]] | None | Unset
        if isinstance(self.work_item_types, Unset):
            work_item_types = UNSET
        elif isinstance(self.work_item_types, list):
            work_item_types = []
            for work_item_types_type_0_item_data in self.work_item_types:
                work_item_types_type_0_item = []
                for (
                    work_item_types_type_0_item_item_data
                ) in work_item_types_type_0_item_data:
                    work_item_types_type_0_item_item: str
                    work_item_types_type_0_item_item = (
                        work_item_types_type_0_item_item_data
                    )
                    work_item_types_type_0_item.append(work_item_types_type_0_item_item)

                work_item_types.append(work_item_types_type_0_item)

        else:
            work_item_types = self.work_item_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wbsconfigurations": wbsconfigurations,
            }
        )
        if work_item_types is not UNSET:
            field_dict["work_item_types"] = work_item_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_wbs_configuration import TenantWBSConfiguration

        d = dict(src_dict)
        wbsconfigurations = []
        _wbsconfigurations = d.pop("wbsconfigurations")
        for wbsconfigurations_item_data in _wbsconfigurations:
            wbsconfigurations_item = TenantWBSConfiguration.from_dict(
                wbsconfigurations_item_data
            )

            wbsconfigurations.append(wbsconfigurations_item)

        def _parse_work_item_types(data: object) -> list[list[str]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_item_types_type_0 = []
                _work_item_types_type_0 = data
                for work_item_types_type_0_item_data in _work_item_types_type_0:
                    work_item_types_type_0_item = []
                    _work_item_types_type_0_item = work_item_types_type_0_item_data
                    for (
                        work_item_types_type_0_item_item_data
                    ) in _work_item_types_type_0_item:

                        def _parse_work_item_types_type_0_item_item(
                            data: object,
                        ) -> str:
                            return cast(str, data)

                        work_item_types_type_0_item_item = (
                            _parse_work_item_types_type_0_item_item(
                                work_item_types_type_0_item_item_data
                            )
                        )

                        work_item_types_type_0_item.append(
                            work_item_types_type_0_item_item
                        )

                    work_item_types_type_0.append(work_item_types_type_0_item)

                return work_item_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[str]] | None | Unset, data)

        work_item_types = _parse_work_item_types(d.pop("work_item_types", UNSET))

        tenant_wbs_configurations = cls(
            wbsconfigurations=wbsconfigurations,
            work_item_types=work_item_types,
        )

        tenant_wbs_configurations.additional_properties = d
        return tenant_wbs_configurations

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
