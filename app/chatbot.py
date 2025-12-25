from app.policy_engine import evaluate_warranty
from app.image_analyzer import analyze_image
from app.llm_helper import llm_reason
from app.logger import logger


def detect_issue_type_from_text(user_query: str) -> str:
    query = user_query.lower()

    if any(word in query for word in ["crack", "broken", "dent", "damage"]):
        return "physical_damage"

    if any(word in query for word in ["not working", "battery", "overheating", "speaker"]):
        return "manufacturing_defect"

    return "unclear"


def fallback_explanation(issue: str, covered: bool) -> str:
    if covered:
        return (
            "Based on the provided information, the issue appears to be a manufacturing defect, "
            "which is generally covered under warranty. Final approval requires manual verification."
        )
    else:
        return (
            "The issue appears to be physical damage, which is not covered under warranty "
            "as per policy guidelines. Final confirmation will be done after inspection."
        )


def generate_response(user_query: str, image_path: str = None) -> dict:
    # Defensive check (extra safety)
    if not user_query or not user_query.strip():
        logger.warning("Empty user query received")
        return {
            "detected_issue": "unclear",
            "warranty_covered": False,
            "ai_response": "Please describe the issue so we can assist you better.",
            "image_used": False,
            "disclaimer": "This is an AI-based assistant. Final approval depends on manual verification."
        }

    # Detect issues from text and image
    text_issue = detect_issue_type_from_text(user_query)
    image_issue = analyze_image(image_path) if image_path else "unclear"

    final_issue = image_issue if image_issue != "unclear" else text_issue
    warranty_result = evaluate_warranty(final_issue)

    # 🔍 Logging (Day 5 requirement)
    logger.info(f"User query: {user_query}")
    logger.info(f"Detected issue: {final_issue}")
    logger.info(f"Warranty covered: {warranty_result['covered']}")

    # Prompt for LLM
    prompt = f"""
Customer issue: {user_query}
Detected issue type: {final_issue}
Warranty covered: {warranty_result['covered']}

Explain the decision politely and clearly.
Mention that final approval requires manual verification.
"""

    ai_explanation = llm_reason(prompt)

    # Graceful fallback if LLM fails
    if not ai_explanation:
        logger.warning("LLM unavailable, using fallback explanation")
        ai_explanation = fallback_explanation(final_issue, warranty_result["covered"])

    return {
        "detected_issue": final_issue,
        "warranty_covered": warranty_result["covered"],
        "ai_response": ai_explanation,
        "image_used": image_path is not None,
        "disclaimer": "This is an AI-based assistant. Final approval depends on manual verification."
    }
