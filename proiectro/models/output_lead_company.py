from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_lead_at_company import OutputLeadAtCompany


T = TypeVar("T", bound="OutputLeadCompany")


@_attrs_define
class OutputLeadCompany:
    """What the workspace already has at a lead's company, which its domain identifies.

    Attributes:
        domain (str):
        customer_id (None | str | Unset):
        customer_name (None | str | Unset):
        leads (list[OutputLeadAtCompany] | Unset):
        more (int | Unset):  Default: 0.
        hidden (bool | Unset):  Default: False.
    """

    domain: str
    customer_id: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    leads: list[OutputLeadAtCompany] | Unset = UNSET
    more: int | Unset = 0
    hidden: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        leads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.leads, Unset):
            leads = []
            for leads_item_data in self.leads:
                leads_item = leads_item_data.to_dict()
                leads.append(leads_item)

        more = self.more

        hidden = self.hidden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
            }
        )
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if leads is not UNSET:
            field_dict["leads"] = leads
        if more is not UNSET:
            field_dict["more"] = more
        if hidden is not UNSET:
            field_dict["hidden"] = hidden

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_at_company import OutputLeadAtCompany

        d = dict(src_dict)
        domain = d.pop("domain")

        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        _leads = d.pop("leads", UNSET)
        leads: list[OutputLeadAtCompany] | Unset = UNSET
        if _leads is not UNSET:
            leads = []
            for leads_item_data in _leads:
                leads_item = OutputLeadAtCompany.from_dict(leads_item_data)

                leads.append(leads_item)

        more = d.pop("more", UNSET)

        hidden = d.pop("hidden", UNSET)

        output_lead_company = cls(
            domain=domain,
            customer_id=customer_id,
            customer_name=customer_name,
            leads=leads,
            more=more,
            hidden=hidden,
        )

        output_lead_company.additional_properties = d
        return output_lead_company

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
