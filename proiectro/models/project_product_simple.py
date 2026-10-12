from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_status_detail import ProductStatusDetail


T = TypeVar("T", bound="ProjectProductSimple")


@_attrs_define
class ProjectProductSimple:
    """
    Attributes:
        external_id (str):
        product_count (int):
        name (str):
        is_active (bool):
        current_status (ProductStatusDetail): Product status for lifecycle display.
            Used in status dropdowns to show current status and all available lifecycle stages.
            Use lifecycle_type with templatetags for styling (status_bg, status_text, status_icon, etc.)
        lifecycle_statuses (list[ProductStatusDetail]):
        description (str | Unset):  Default: ''.
        description_for_customer (str | Unset):  Default: ''.
        planned_start (datetime.datetime | None | Unset):
        planned_end (datetime.datetime | None | Unset):
        is_linked (bool | Unset):  Default: False.
    """

    external_id: str
    product_count: int
    name: str
    is_active: bool
    current_status: ProductStatusDetail
    lifecycle_statuses: list[ProductStatusDetail]
    description: str | Unset = ""
    description_for_customer: str | Unset = ""
    planned_start: datetime.datetime | None | Unset = UNSET
    planned_end: datetime.datetime | None | Unset = UNSET
    is_linked: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        product_count = self.product_count

        name = self.name

        is_active = self.is_active

        current_status = self.current_status.to_dict()

        lifecycle_statuses = []
        for lifecycle_statuses_item_data in self.lifecycle_statuses:
            lifecycle_statuses_item = lifecycle_statuses_item_data.to_dict()
            lifecycle_statuses.append(lifecycle_statuses_item)

        description = self.description

        description_for_customer = self.description_for_customer

        planned_start: None | str | Unset
        if isinstance(self.planned_start, Unset):
            planned_start = UNSET
        elif isinstance(self.planned_start, datetime.datetime):
            planned_start = self.planned_start.isoformat()
        else:
            planned_start = self.planned_start

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        elif isinstance(self.planned_end, datetime.datetime):
            planned_end = self.planned_end.isoformat()
        else:
            planned_end = self.planned_end

        is_linked = self.is_linked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "product_count": product_count,
                "name": name,
                "is_active": is_active,
                "current_status": current_status,
                "lifecycle_statuses": lifecycle_statuses,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if description_for_customer is not UNSET:
            field_dict["description_for_customer"] = description_for_customer
        if planned_start is not UNSET:
            field_dict["planned_start"] = planned_start
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end
        if is_linked is not UNSET:
            field_dict["is_linked"] = is_linked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_status_detail import ProductStatusDetail

        d = dict(src_dict)
        external_id = d.pop("external_id")

        product_count = d.pop("product_count")

        name = d.pop("name")

        is_active = d.pop("is_active")

        current_status = ProductStatusDetail.from_dict(d.pop("current_status"))

        lifecycle_statuses = []
        _lifecycle_statuses = d.pop("lifecycle_statuses")
        for lifecycle_statuses_item_data in _lifecycle_statuses:
            lifecycle_statuses_item = ProductStatusDetail.from_dict(
                lifecycle_statuses_item_data
            )

            lifecycle_statuses.append(lifecycle_statuses_item)

        description = d.pop("description", UNSET)

        description_for_customer = d.pop("description_for_customer", UNSET)

        def _parse_planned_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_start_type_0 = isoparse(data)

                return planned_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        planned_start = _parse_planned_start(d.pop("planned_start", UNSET))

        def _parse_planned_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_end_type_0 = isoparse(data)

                return planned_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        is_linked = d.pop("is_linked", UNSET)

        project_product_simple = cls(
            external_id=external_id,
            product_count=product_count,
            name=name,
            is_active=is_active,
            current_status=current_status,
            lifecycle_statuses=lifecycle_statuses,
            description=description,
            description_for_customer=description_for_customer,
            planned_start=planned_start,
            planned_end=planned_end,
            is_linked=is_linked,
        )

        project_product_simple.additional_properties = d
        return project_product_simple

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
