from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.contact_invitation import ContactInvitation
    from ..models.org_contact import OrgContact


T = TypeVar("T", bound="OrgContacts")


@_attrs_define
class OrgContacts:
    """
    Attributes:
        org_id (str):
        contacts (list[OrgContact]):
        invitations (list[ContactInvitation]):
    """

    org_id: str
    contacts: list[OrgContact]
    invitations: list[ContactInvitation]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        contacts = []
        for contacts_item_data in self.contacts:
            contacts_item = contacts_item_data.to_dict()
            contacts.append(contacts_item)

        invitations = []
        for invitations_item_data in self.invitations:
            invitations_item = invitations_item_data.to_dict()
            invitations.append(invitations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "contacts": contacts,
                "invitations": invitations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_invitation import ContactInvitation
        from ..models.org_contact import OrgContact

        d = dict(src_dict)
        org_id = d.pop("org_id")

        contacts = []
        _contacts = d.pop("contacts")
        for contacts_item_data in _contacts:
            contacts_item = OrgContact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        invitations = []
        _invitations = d.pop("invitations")
        for invitations_item_data in _invitations:
            invitations_item = ContactInvitation.from_dict(invitations_item_data)

            invitations.append(invitations_item)

        org_contacts = cls(
            org_id=org_id,
            contacts=contacts,
            invitations=invitations,
        )

        org_contacts.additional_properties = d
        return org_contacts

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
