from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_tag import OutputTag


T = TypeVar("T", bound="ProjectListItem")


@_attrs_define
class ProjectListItem:
    """Individual project item for lists

    Attributes:
        id (str):
        name (str):
        stage_name (str):
        stage_id (str):
        product_count (int):
        owner_name (str):
        owner_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        internal_code (None | str | Unset):
        customer_name (None | str | Unset):
        customer_id (None | str | Unset):
        project_start_date (datetime.date | None | Unset):
        project_end_date (datetime.date | None | Unset):
        tags (list[OutputTag] | Unset):
    """

    id: str
    name: str
    stage_name: str
    stage_id: str
    product_count: int
    owner_name: str
    owner_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    internal_code: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    customer_id: None | str | Unset = UNSET
    project_start_date: datetime.date | None | Unset = UNSET
    project_end_date: datetime.date | None | Unset = UNSET
    tags: list[OutputTag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        stage_name = self.stage_name

        stage_id = self.stage_id

        product_count = self.product_count

        owner_name = self.owner_name

        owner_id = self.owner_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        project_start_date: None | str | Unset
        if isinstance(self.project_start_date, Unset):
            project_start_date = UNSET
        elif isinstance(self.project_start_date, datetime.date):
            project_start_date = self.project_start_date.isoformat()
        else:
            project_start_date = self.project_start_date

        project_end_date: None | str | Unset
        if isinstance(self.project_end_date, Unset):
            project_end_date = UNSET
        elif isinstance(self.project_end_date, datetime.date):
            project_end_date = self.project_end_date.isoformat()
        else:
            project_end_date = self.project_end_date

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "stage_name": stage_name,
                "stage_id": stage_id,
                "product_count": product_count,
                "owner_name": owner_name,
                "owner_id": owner_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if project_start_date is not UNSET:
            field_dict["project_start_date"] = project_start_date
        if project_end_date is not UNSET:
            field_dict["project_end_date"] = project_end_date
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tag import OutputTag

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        stage_name = d.pop("stage_name")

        stage_id = d.pop("stage_id")

        product_count = d.pop("product_count")

        owner_name = d.pop("owner_name")

        owner_id = d.pop("owner_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_project_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_start_date_type_0 = isoparse(data).date()

                return project_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        project_start_date = _parse_project_start_date(
            d.pop("project_start_date", UNSET)
        )

        def _parse_project_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_end_date_type_0 = isoparse(data).date()

                return project_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        project_end_date = _parse_project_end_date(d.pop("project_end_date", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[OutputTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = OutputTag.from_dict(tags_item_data)

                tags.append(tags_item)

        project_list_item = cls(
            id=id,
            name=name,
            stage_name=stage_name,
            stage_id=stage_id,
            product_count=product_count,
            owner_name=owner_name,
            owner_id=owner_id,
            created_at=created_at,
            updated_at=updated_at,
            internal_code=internal_code,
            customer_name=customer_name,
            customer_id=customer_id,
            project_start_date=project_start_date,
            project_end_date=project_end_date,
            tags=tags,
        )

        project_list_item.additional_properties = d
        return project_list_item

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
