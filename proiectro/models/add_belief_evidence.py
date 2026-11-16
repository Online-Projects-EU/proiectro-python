from enum import Enum


class AddBeliefEvidence(str, Enum):
    FORM = "form"
    LEAD_CUSTOMER = "lead_customer"
    LEAD_OPPORTUNITY = "lead_opportunity"
    LEAD_QUALIFIED = "lead_qualified"
    LEAD_REPLIED = "lead_replied"
    PROPOSAL_WON = "proposal_won"

    def __str__(self) -> str:
        return str(self.value)
