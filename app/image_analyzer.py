from PIL import Image
import os


def analyze_image(image_path: str):
    """
    Very simple image analysis placeholder.
    This simulates defect detection logic.
    """

    if not os.path.exists(image_path):
        return "unclear"

    # For demo purposes (PM-grade explanation)
    # Real systems use ML models here
    filename = image_path.lower()

    if any(word in filename for word in ["crack", "broken", "damage"]):
        return "physical_damage"

    return "unclear"
