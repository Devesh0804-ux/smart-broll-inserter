from typing import List, Dict


def load_broll_metadata() -> List[Dict]:
    """
    Load B-roll metadata.
    In real systems this could come from a DB or CMS.
    """

    # Example hardcoded metadata (sufficient for assignment)
    brolls = [
        {
            "broll_id": "broll_1",
            "description": "Wide shot of a busy street food market"
        },
        {
            "broll_id": "broll_2",
            "description": "Vendor preparing food with gloves"
        },
        {
            "broll_id": "broll_3",
            "description": "Close-up of uncovered food highlighting hygiene concerns"
        },
        {
            "broll_id": "broll_4",
            "description": "Customer washing hands before eating"
        }
    ]

    return brolls
