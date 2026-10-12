from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_customer_portal_projects_org import (
        OutputCustomerPortalProjectsOrg,
    )
    from ..models.output_customer_portal_projects_projects_item import (
        OutputCustomerPortalProjectsProjectsItem,
    )
    from ..models.portal_currency_total import PortalCurrencyTotal


T = TypeVar("T", bound="OutputCustomerPortalProjects")


@_attrs_define
class OutputCustomerPortalProjects:
    """Customer portal projects view with payment aggregations

    Attributes:
        projects (list[OutputCustomerPortalProjectsProjectsItem]):
        currency_symbol (str):
        org (OutputCustomerPortalProjectsOrg):
        total_accepted_amount (float | None | str | Unset):
        total_by_currency (list[PortalCurrencyTotal] | Unset):
        next_payment_date (datetime.date | None | Unset):
    """

    projects: list[OutputCustomerPortalProjectsProjectsItem]
    currency_symbol: str
    org: OutputCustomerPortalProjectsOrg
    total_accepted_amount: float | None | str | Unset = UNSET
    total_by_currency: list[PortalCurrencyTotal] | Unset = UNSET
    next_payment_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        currency_symbol = self.currency_symbol

        org = self.org.to_dict()

        total_accepted_amount: float | None | str | Unset
        if isinstance(self.total_accepted_amount, Unset):
            total_accepted_amount = UNSET
        else:
            total_accepted_amount = self.total_accepted_amount

        total_by_currency: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.total_by_currency, Unset):
            total_by_currency = []
            for total_by_currency_item_data in self.total_by_currency:
                total_by_currency_item = total_by_currency_item_data.to_dict()
                total_by_currency.append(total_by_currency_item)

        next_payment_date: None | str | Unset
        if isinstance(self.next_payment_date, Unset):
            next_payment_date = UNSET
        elif isinstance(self.next_payment_date, datetime.date):
            next_payment_date = self.next_payment_date.isoformat()
        else:
            next_payment_date = self.next_payment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects": projects,
                "currency_symbol": currency_symbol,
                "org": org,
            }
        )
        if total_accepted_amount is not UNSET:
            field_dict["total_accepted_amount"] = total_accepted_amount
        if total_by_currency is not UNSET:
            field_dict["total_by_currency"] = total_by_currency
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
        from ..models.portal_currency_total import PortalCurrencyTotal

        d = dict(src_dict)
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = OutputCustomerPortalProjectsProjectsItem.from_dict(
                projects_item_data
            )

            projects.append(projects_item)

        currency_symbol = d.pop("currency_symbol")

        org = OutputCustomerPortalProjectsOrg.from_dict(d.pop("org"))

        def _parse_total_accepted_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_accepted_amount = _parse_total_accepted_amount(
            d.pop("total_accepted_amount", UNSET)
        )

        _total_by_currency = d.pop("total_by_currency", UNSET)
        total_by_currency: list[PortalCurrencyTotal] | Unset = UNSET
        if _total_by_currency is not UNSET:
            total_by_currency = []
            for total_by_currency_item_data in _total_by_currency:
                total_by_currency_item = PortalCurrencyTotal.from_dict(
                    total_by_currency_item_data
                )

                total_by_currency.append(total_by_currency_item)

        def _parse_next_payment_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_payment_date_type_0 = isoparse(data).date()

                return next_payment_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        next_payment_date = _parse_next_payment_date(d.pop("next_payment_date", UNSET))

        output_customer_portal_projects = cls(
            projects=projects,
            currency_symbol=currency_symbol,
            org=org,
            total_accepted_amount=total_accepted_amount,
            total_by_currency=total_by_currency,
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
