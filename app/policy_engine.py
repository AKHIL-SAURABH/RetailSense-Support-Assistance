def load_warranty_policy():
    with open("app/data/warranty.txt", "r") as f:
        return f.read()


def evaluate_warranty(issue_type: str):
    """
    issue_type can be:
    - manufacturing_defect
    - physical_damage
    - unclear
    """

    if issue_type == "manufacturing_defect":
        return {
            "covered": True,
            "message": "This issue appears to be a manufacturing defect, which is generally covered under warranty."
        }

    if issue_type == "physical_damage":
        return {
            "covered": False,
            "message": "The issue appears to be physical damage, which is not covered under warranty."
        }

    return {
        "covered": False,
        "message": "We are unable to determine warranty eligibility based on the provided information."
    }
