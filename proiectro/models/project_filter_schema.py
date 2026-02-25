from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectFilterSchema")


@_attrs_define
class ProjectFilterSchema:
    """Filter schema for projects (closed_won stage) with comprehensive search and attribute filtering.

    Attributes:
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by project name, description, or customer name
        name (None | str | Unset): Filter by project name
        customer (None | str | Unset): Filter by customer external ID
        owner (None | str | Unset): Filter by project owner external ID
        manager (None | str | Unset): Filter by project manager external ID
        created_after (None | str | Unset): Show projects created after this date (YYYY-MM-DD)
        created_before (None | str | Unset): Show projects created before this date (YYYY-MM-DD)
        closed_won_after (None | str | Unset): Show projects that moved to closed_won after this date (YYYY-MM-DD)
        closed_won_before (None | str | Unset): Show projects that moved to closed_won before this date (YYYY-MM-DD)
        has_products (bool | None | Unset): Filter projects that have products attached
        tags1 (list[str] | None | Unset): Filter by tags (first set - match ANY tag in this set)
        tags2 (list[str] | None | Unset): Filter by tags (second set - match ANY tag in this set)
        tags3 (list[str] | None | Unset): Filter by tags (third set - match ANY tag in this set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)
    """

    exclude_mode: bool | None | Unset = UNSET
    search: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    customer: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    manager: None | str | Unset = UNSET
    created_after: None | str | Unset = UNSET
    created_before: None | str | Unset = UNSET
    closed_won_after: None | str | Unset = UNSET
    closed_won_before: None | str | Unset = UNSET
    has_products: bool | None | Unset = UNSET
    tags1: list[str] | None | Unset = UNSET
    tags2: list[str] | None | Unset = UNSET
    tags3: list[str] | None | Unset = UNSET
    label_id1: None | str | Unset = UNSET
    label_op1: None | str | Unset = UNSET
    label_val1: None | str | Unset = UNSET
    label_id2: None | str | Unset = UNSET
    label_op2: None | str | Unset = UNSET
    label_val2: None | str | Unset = UNSET
    label_id3: None | str | Unset = UNSET
    label_op3: None | str | Unset = UNSET
    label_val3: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude_mode: bool | None | Unset
        if isinstance(self.exclude_mode, Unset):
            exclude_mode = UNSET
        else:
            exclude_mode = self.exclude_mode

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        customer: None | str | Unset
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        manager: None | str | Unset
        if isinstance(self.manager, Unset):
            manager = UNSET
        else:
            manager = self.manager

        created_after: None | str | Unset
        if isinstance(self.created_after, Unset):
            created_after = UNSET
        else:
            created_after = self.created_after

        created_before: None | str | Unset
        if isinstance(self.created_before, Unset):
            created_before = UNSET
        else:
            created_before = self.created_before

        closed_won_after: None | str | Unset
        if isinstance(self.closed_won_after, Unset):
            closed_won_after = UNSET
        else:
            closed_won_after = self.closed_won_after

        closed_won_before: None | str | Unset
        if isinstance(self.closed_won_before, Unset):
            closed_won_before = UNSET
        else:
            closed_won_before = self.closed_won_before

        has_products: bool | None | Unset
        if isinstance(self.has_products, Unset):
            has_products = UNSET
        else:
            has_products = self.has_products

        tags1: list[str] | None | Unset
        if isinstance(self.tags1, Unset):
            tags1 = UNSET
        elif isinstance(self.tags1, list):
            tags1 = self.tags1

        else:
            tags1 = self.tags1

        tags2: list[str] | None | Unset
        if isinstance(self.tags2, Unset):
            tags2 = UNSET
        elif isinstance(self.tags2, list):
            tags2 = self.tags2

        else:
            tags2 = self.tags2

        tags3: list[str] | None | Unset
        if isinstance(self.tags3, Unset):
            tags3 = UNSET
        elif isinstance(self.tags3, list):
            tags3 = self.tags3

        else:
            tags3 = self.tags3

        label_id1: None | str | Unset
        if isinstance(self.label_id1, Unset):
            label_id1 = UNSET
        else:
            label_id1 = self.label_id1

        label_op1: None | str | Unset
        if isinstance(self.label_op1, Unset):
            label_op1 = UNSET
        else:
            label_op1 = self.label_op1

        label_val1: None | str | Unset
        if isinstance(self.label_val1, Unset):
            label_val1 = UNSET
        else:
            label_val1 = self.label_val1

        label_id2: None | str | Unset
        if isinstance(self.label_id2, Unset):
            label_id2 = UNSET
        else:
            label_id2 = self.label_id2

        label_op2: None | str | Unset
        if isinstance(self.label_op2, Unset):
            label_op2 = UNSET
        else:
            label_op2 = self.label_op2

        label_val2: None | str | Unset
        if isinstance(self.label_val2, Unset):
            label_val2 = UNSET
        else:
            label_val2 = self.label_val2

        label_id3: None | str | Unset
        if isinstance(self.label_id3, Unset):
            label_id3 = UNSET
        else:
            label_id3 = self.label_id3

        label_op3: None | str | Unset
        if isinstance(self.label_op3, Unset):
            label_op3 = UNSET
        else:
            label_op3 = self.label_op3

        label_val3: None | str | Unset
        if isinstance(self.label_val3, Unset):
            label_val3 = UNSET
        else:
            label_val3 = self.label_val3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude_mode is not UNSET:
            field_dict["exclude_mode"] = exclude_mode
        if search is not UNSET:
            field_dict["search"] = search
        if name is not UNSET:
            field_dict["name"] = name
        if customer is not UNSET:
            field_dict["customer"] = customer
        if owner is not UNSET:
            field_dict["owner"] = owner
        if manager is not UNSET:
            field_dict["manager"] = manager
        if created_after is not UNSET:
            field_dict["created_after"] = created_after
        if created_before is not UNSET:
            field_dict["created_before"] = created_before
        if closed_won_after is not UNSET:
            field_dict["closed_won_after"] = closed_won_after
        if closed_won_before is not UNSET:
            field_dict["closed_won_before"] = closed_won_before
        if has_products is not UNSET:
            field_dict["has_products"] = has_products
        if tags1 is not UNSET:
            field_dict["tags1"] = tags1
        if tags2 is not UNSET:
            field_dict["tags2"] = tags2
        if tags3 is not UNSET:
            field_dict["tags3"] = tags3
        if label_id1 is not UNSET:
            field_dict["label_id1"] = label_id1
        if label_op1 is not UNSET:
            field_dict["label_op1"] = label_op1
        if label_val1 is not UNSET:
            field_dict["label_val1"] = label_val1
        if label_id2 is not UNSET:
            field_dict["label_id2"] = label_id2
        if label_op2 is not UNSET:
            field_dict["label_op2"] = label_op2
        if label_val2 is not UNSET:
            field_dict["label_val2"] = label_val2
        if label_id3 is not UNSET:
            field_dict["label_id3"] = label_id3
        if label_op3 is not UNSET:
            field_dict["label_op3"] = label_op3
        if label_val3 is not UNSET:
            field_dict["label_val3"] = label_val3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_exclude_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_mode = _parse_exclude_mode(d.pop("exclude_mode", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_customer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer = _parse_customer(d.pop("customer", UNSET))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_manager(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manager = _parse_manager(d.pop("manager", UNSET))

        def _parse_created_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_after = _parse_created_after(d.pop("created_after", UNSET))

        def _parse_created_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_before = _parse_created_before(d.pop("created_before", UNSET))

        def _parse_closed_won_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closed_won_after = _parse_closed_won_after(d.pop("closed_won_after", UNSET))

        def _parse_closed_won_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closed_won_before = _parse_closed_won_before(d.pop("closed_won_before", UNSET))

        def _parse_has_products(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_products = _parse_has_products(d.pop("has_products", UNSET))

        def _parse_tags1(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags1_type_0 = cast(list[str], data)

                return tags1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags1 = _parse_tags1(d.pop("tags1", UNSET))

        def _parse_tags2(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags2_type_0 = cast(list[str], data)

                return tags2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags2 = _parse_tags2(d.pop("tags2", UNSET))

        def _parse_tags3(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags3_type_0 = cast(list[str], data)

                return tags3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags3 = _parse_tags3(d.pop("tags3", UNSET))

        def _parse_label_id1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_id1 = _parse_label_id1(d.pop("label_id1", UNSET))

        def _parse_label_op1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_op1 = _parse_label_op1(d.pop("label_op1", UNSET))

        def _parse_label_val1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_val1 = _parse_label_val1(d.pop("label_val1", UNSET))

        def _parse_label_id2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_id2 = _parse_label_id2(d.pop("label_id2", UNSET))

        def _parse_label_op2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_op2 = _parse_label_op2(d.pop("label_op2", UNSET))

        def _parse_label_val2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_val2 = _parse_label_val2(d.pop("label_val2", UNSET))

        def _parse_label_id3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_id3 = _parse_label_id3(d.pop("label_id3", UNSET))

        def _parse_label_op3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_op3 = _parse_label_op3(d.pop("label_op3", UNSET))

        def _parse_label_val3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_val3 = _parse_label_val3(d.pop("label_val3", UNSET))

        project_filter_schema = cls(
            exclude_mode=exclude_mode,
            search=search,
            name=name,
            customer=customer,
            owner=owner,
            manager=manager,
            created_after=created_after,
            created_before=created_before,
            closed_won_after=closed_won_after,
            closed_won_before=closed_won_before,
            has_products=has_products,
            tags1=tags1,
            tags2=tags2,
            tags3=tags3,
            label_id1=label_id1,
            label_op1=label_op1,
            label_val1=label_val1,
            label_id2=label_id2,
            label_op2=label_op2,
            label_val2=label_val2,
            label_id3=label_id3,
            label_op3=label_op3,
            label_val3=label_val3,
        )

        project_filter_schema.additional_properties = d
        return project_filter_schema

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
