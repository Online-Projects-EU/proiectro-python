from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AllPartnersPaymentItem")


@_attrs_define
class AllPartnersPaymentItem:
    """Payment item with partner context for aggregated view

    Attributes:
        id (str):
        project_name (str):
        amount (str):
        due_date (None | str):
        paid (bool):
        paid_date (None | str):
        currency_code (str):
        is_project (bool):
        is_due (bool):
        project_id (str):
        partner_tenant_name (str):
        proxy_subtenant_id (str):
    """

    id: str
    project_name: str
    amount: str
    due_date: None | str
    paid: bool
    paid_date: None | str
    currency_code: str
    is_project: bool
    is_due: bool
    project_id: str
    partner_tenant_name: str
    proxy_subtenant_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_name = self.project_name

        amount = self.amount

        due_date: None | str
        due_date = self.due_date

        paid = self.paid

        paid_date: None | str
        paid_date = self.paid_date

        currency_code = self.currency_code

        is_project = self.is_project

        is_due = self.is_due

        project_id = self.project_id

        partner_tenant_name = self.partner_tenant_name

        proxy_subtenant_id = self.proxy_subtenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project_name": project_name,
                "amount": amount,
                "due_date": due_date,
                "paid": paid,
                "paid_date": paid_date,
                "currency_code": currency_code,
                "is_project": is_project,
                "is_due": is_due,
                "project_id": project_id,
                "partner_tenant_name": partner_tenant_name,
                "proxy_subtenant_id": proxy_subtenant_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        project_name = d.pop("project_name")

        amount = d.pop("amount")

        def _parse_due_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        due_date = _parse_due_date(d.pop("due_date"))

        paid = d.pop("paid")

        def _parse_paid_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        paid_date = _parse_paid_date(d.pop("paid_date"))

        currency_code = d.pop("currency_code")

        is_project = d.pop("is_project")

        is_due = d.pop("is_due")

        project_id = d.pop("project_id")

        partner_tenant_name = d.pop("partner_tenant_name")

        proxy_subtenant_id = d.pop("proxy_subtenant_id")

        all_partners_payment_item = cls(
            id=id,
            project_name=project_name,
            amount=amount,
            due_date=due_date,
            paid=paid,
            paid_date=paid_date,
            currency_code=currency_code,
            is_project=is_project,
            is_due=is_due,
            project_id=project_id,
            partner_tenant_name=partner_tenant_name,
            proxy_subtenant_id=proxy_subtenant_id,
        )

        all_partners_payment_item.additional_properties = d
        return all_partners_payment_item

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
