from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputCustomerAsset")


@_attrs_define
class OutputCustomerAsset:
    """
    Attributes:
        id (str):
        customer_id (str):
        customer_name (str):
        category_id (str):
        category_name (str):
        name (str):
        status (str):
        status_display (str):
        is_customer_visible (bool):
        is_parent (bool):
        depth (int):
        customer_location_id (None | str | Unset):
        customer_location_name (None | str | Unset):
        project_id (None | str | Unset):
        project_name (None | str | Unset):
        product_id (None | str | Unset):
        product_name (None | str | Unset):
        description (None | str | Unset):
        internal_code (None | str | Unset):
        serial_number_or_uri (None | str | Unset):
        installation_date (None | str | Unset):
        warranty_expiration (None | str | Unset):
        hierarchy_id (None | str | Unset):
        parent_id (None | str | Unset):
        parent_name (None | str | Unset):
    """

    id: str
    customer_id: str
    customer_name: str
    category_id: str
    category_name: str
    name: str
    status: str
    status_display: str
    is_customer_visible: bool
    is_parent: bool
    depth: int
    customer_location_id: None | str | Unset = UNSET
    customer_location_name: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    project_name: None | str | Unset = UNSET
    product_id: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    serial_number_or_uri: None | str | Unset = UNSET
    installation_date: None | str | Unset = UNSET
    warranty_expiration: None | str | Unset = UNSET
    hierarchy_id: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    parent_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        customer_name = self.customer_name

        category_id = self.category_id

        category_name = self.category_name

        name = self.name

        status = self.status

        status_display = self.status_display

        is_customer_visible = self.is_customer_visible

        is_parent = self.is_parent

        depth = self.depth

        customer_location_id: None | str | Unset
        if isinstance(self.customer_location_id, Unset):
            customer_location_id = UNSET
        else:
            customer_location_id = self.customer_location_id

        customer_location_name: None | str | Unset
        if isinstance(self.customer_location_name, Unset):
            customer_location_name = UNSET
        else:
            customer_location_name = self.customer_location_name

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        project_name: None | str | Unset
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        serial_number_or_uri: None | str | Unset
        if isinstance(self.serial_number_or_uri, Unset):
            serial_number_or_uri = UNSET
        else:
            serial_number_or_uri = self.serial_number_or_uri

        installation_date: None | str | Unset
        if isinstance(self.installation_date, Unset):
            installation_date = UNSET
        else:
            installation_date = self.installation_date

        warranty_expiration: None | str | Unset
        if isinstance(self.warranty_expiration, Unset):
            warranty_expiration = UNSET
        else:
            warranty_expiration = self.warranty_expiration

        hierarchy_id: None | str | Unset
        if isinstance(self.hierarchy_id, Unset):
            hierarchy_id = UNSET
        else:
            hierarchy_id = self.hierarchy_id

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_name: None | str | Unset
        if isinstance(self.parent_name, Unset):
            parent_name = UNSET
        else:
            parent_name = self.parent_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "customer_id": customer_id,
                "customer_name": customer_name,
                "category_id": category_id,
                "category_name": category_name,
                "name": name,
                "status": status,
                "status_display": status_display,
                "is_customer_visible": is_customer_visible,
                "is_parent": is_parent,
                "depth": depth,
            }
        )
        if customer_location_id is not UNSET:
            field_dict["customer_location_id"] = customer_location_id
        if customer_location_name is not UNSET:
            field_dict["customer_location_name"] = customer_location_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if serial_number_or_uri is not UNSET:
            field_dict["serial_number_or_uri"] = serial_number_or_uri
        if installation_date is not UNSET:
            field_dict["installation_date"] = installation_date
        if warranty_expiration is not UNSET:
            field_dict["warranty_expiration"] = warranty_expiration
        if hierarchy_id is not UNSET:
            field_dict["hierarchy_id"] = hierarchy_id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if parent_name is not UNSET:
            field_dict["parent_name"] = parent_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customer_id")

        customer_name = d.pop("customer_name")

        category_id = d.pop("category_id")

        category_name = d.pop("category_name")

        name = d.pop("name")

        status = d.pop("status")

        status_display = d.pop("status_display")

        is_customer_visible = d.pop("is_customer_visible")

        is_parent = d.pop("is_parent")

        depth = d.pop("depth")

        def _parse_customer_location_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_location_id = _parse_customer_location_id(
            d.pop("customer_location_id", UNSET)
        )

        def _parse_customer_location_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_location_name = _parse_customer_location_name(
            d.pop("customer_location_name", UNSET)
        )

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_name = _parse_project_name(d.pop("project_name", UNSET))

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_serial_number_or_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number_or_uri = _parse_serial_number_or_uri(
            d.pop("serial_number_or_uri", UNSET)
        )

        def _parse_installation_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installation_date = _parse_installation_date(d.pop("installation_date", UNSET))

        def _parse_warranty_expiration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        warranty_expiration = _parse_warranty_expiration(
            d.pop("warranty_expiration", UNSET)
        )

        def _parse_hierarchy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hierarchy_id = _parse_hierarchy_id(d.pop("hierarchy_id", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_parent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_name = _parse_parent_name(d.pop("parent_name", UNSET))

        output_customer_asset = cls(
            id=id,
            customer_id=customer_id,
            customer_name=customer_name,
            category_id=category_id,
            category_name=category_name,
            name=name,
            status=status,
            status_display=status_display,
            is_customer_visible=is_customer_visible,
            is_parent=is_parent,
            depth=depth,
            customer_location_id=customer_location_id,
            customer_location_name=customer_location_name,
            project_id=project_id,
            project_name=project_name,
            product_id=product_id,
            product_name=product_name,
            description=description,
            internal_code=internal_code,
            serial_number_or_uri=serial_number_or_uri,
            installation_date=installation_date,
            warranty_expiration=warranty_expiration,
            hierarchy_id=hierarchy_id,
            parent_id=parent_id,
            parent_name=parent_name,
        )

        output_customer_asset.additional_properties = d
        return output_customer_asset

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
