from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddCustomerAsset")


@_attrs_define
class AddCustomerAsset:
    """
    Attributes:
        customer (str):
        category (str):
        name (str):
        customer_location (None | str | Unset):
        project (None | str | Unset):
        product (None | str | Unset):
        parent (None | str | Unset):
        description (None | str | Unset):
        internal_code (None | str | Unset):
        serial_number_or_uri (None | str | Unset):
        status (str | Unset):  Default: 'active'.
        installation_date (None | str | Unset):
        warranty_expiration (None | str | Unset):
        is_customer_visible (bool | Unset):  Default: False.
    """

    customer: str
    category: str
    name: str
    customer_location: None | str | Unset = UNSET
    project: None | str | Unset = UNSET
    product: None | str | Unset = UNSET
    parent: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    serial_number_or_uri: None | str | Unset = UNSET
    status: str | Unset = "active"
    installation_date: None | str | Unset = UNSET
    warranty_expiration: None | str | Unset = UNSET
    is_customer_visible: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer = self.customer

        category = self.category

        name = self.name

        customer_location: None | str | Unset
        if isinstance(self.customer_location, Unset):
            customer_location = UNSET
        else:
            customer_location = self.customer_location

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        product: None | str | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

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

        status = self.status

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

        is_customer_visible = self.is_customer_visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "category": category,
                "name": name,
            }
        )
        if customer_location is not UNSET:
            field_dict["customer_location"] = customer_location
        if project is not UNSET:
            field_dict["project"] = project
        if product is not UNSET:
            field_dict["product"] = product
        if parent is not UNSET:
            field_dict["parent"] = parent
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if serial_number_or_uri is not UNSET:
            field_dict["serial_number_or_uri"] = serial_number_or_uri
        if status is not UNSET:
            field_dict["status"] = status
        if installation_date is not UNSET:
            field_dict["installation_date"] = installation_date
        if warranty_expiration is not UNSET:
            field_dict["warranty_expiration"] = warranty_expiration
        if is_customer_visible is not UNSET:
            field_dict["is_customer_visible"] = is_customer_visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer = d.pop("customer")

        category = d.pop("category")

        name = d.pop("name")

        def _parse_customer_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_location = _parse_customer_location(d.pop("customer_location", UNSET))

        def _parse_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project = _parse_project(d.pop("project", UNSET))

        def _parse_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_parent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

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

        status = d.pop("status", UNSET)

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

        is_customer_visible = d.pop("is_customer_visible", UNSET)

        add_customer_asset = cls(
            customer=customer,
            category=category,
            name=name,
            customer_location=customer_location,
            project=project,
            product=product,
            parent=parent,
            description=description,
            internal_code=internal_code,
            serial_number_or_uri=serial_number_or_uri,
            status=status,
            installation_date=installation_date,
            warranty_expiration=warranty_expiration,
            is_customer_visible=is_customer_visible,
        )

        add_customer_asset.additional_properties = d
        return add_customer_asset

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
