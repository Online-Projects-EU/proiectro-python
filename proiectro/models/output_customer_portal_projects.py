from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_customer_portal_projects_org import (
        OutputCustomerPortalProjectsOrg,
    )
    from ..models.output_customer_portal_projects_projects_item import (
        OutputCustomerPortalProjectsProjectsItem,
    )


T = TypeVar("T", bound="OutputCustomerPortalProjects")


@_attrs_define
class OutputCustomerPortalProjects:
    """Customer portal projects view with payment aggregations

    Attributes:
        projects (list[OutputCustomerPortalProjectsProjectsItem]):
        total_accepted_amount (float):
        currency_symbol (str):
        org (OutputCustomerPortalProjectsOrg):
        next_payment_date (None | str | Unset):
    """

    projects: list[OutputCustomerPortalProjectsProjectsItem]
    total_accepted_amount: float
    currency_symbol: str
    org: OutputCustomerPortalProjectsOrg
    next_payment_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        total_accepted_amount = self.total_accepted_amount

        currency_symbol = self.currency_symbol

        org = self.org.to_dict()

        next_payment_date: None | str | Unset
        if isinstance(self.next_payment_date, Unset):
            next_payment_date = UNSET
        else:
            next_payment_date = self.next_payment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects": projects,
                "total_accepted_amount": total_accepted_amount,
                "currency_symbol": currency_symbol,
                "org": org,
            }
        )
        if next_payment_date is not UNSET:
            field_dict["next_payment_date"] = next_payment_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_portal_projects_org import (
            OutputCustomerPortalProjectsOrg,
        )
        from ..models.output_customer_portal_projects_projects_item import (
            OutputCustomerPortalProjectsProjectsItem,
        )

        d = dict(src_dict)
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = OutputCustomerPortalProjectsProjectsItem.from_dict(
                projects_item_data
            )

            projects.append(projects_item)

        total_accepted_amount = d.pop("total_accepted_amount")

        currency_symbol = d.pop("currency_symbol")

        org = OutputCustomerPortalProjectsOrg.from_dict(d.pop("org"))

        def _parse_next_payment_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_payment_date = _parse_next_payment_date(d.pop("next_payment_date", UNSET))

        output_customer_portal_projects = cls(
            projects=projects,
            total_accepted_amount=total_accepted_amount,
            currency_symbol=currency_symbol,
            org=org,
            next_payment_date=next_payment_date,
        )

        output_customer_portal_projects.additional_properties = d
        return output_customer_portal_projects

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
