"""stage02_validate_hennelly.py.

Author: Kevin Hennelly
Date: 2026-11

(EDIT YOUR VERSION OF THIS FILE)

Source: raw JSON object
Sink: validated JSON object

Purpose

  Inspect JSON structure and validate that the data is usable.

Analytical Questions

- What is the top-level structure of the JSON data?
- What keys are present in each record?
- What data types are associated with each field?
- Does the data meet expectations for transformation?

Edit your Python file to:
- inspect the JSON structure for your API,
- validate required keys and types,
- confirm the data is usable for your analysis.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from typing import Any

# ============================================================
# Section 2. Define Run Validate Function
# ============================================================


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> list[dict]:
    """Inspect and validate JSON structure.

    Args:
        json_data (Any): The raw JSON data from the Extract stage.
        LOG (logging.Logger): The logger instance.

    Returns:
        list[dict]: The validated JSON data.
    """
    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE starting...")
    LOG.info("========================")

    # ============================================================
    # INSPECT JSON STRUCTURE
    # ============================================================

    LOG.info("JSON STRUCTURE INSPECTION:")
    LOG.info(f"Top-level type: {type(json_data).__name__}")

    if (
        isinstance(json_data, list)
        and len(json_data) > 0
        and isinstance(json_data[0], dict)
    ):
        first_comment = json_data[0]

        LOG.info(f"Keys in first comment: {list(first_comment.keys())}")
        LOG.info("Field types:")
        for key, value in first_comment.items():
            LOG.info(f"{key}: {type(value).__name__}")

    # ============================================================
    # VALIDATE EXPECTATIONS
    # ============================================================

    if not isinstance(json_data, list):
        raise TypeError("Expected JSON data to be a list of comments.")

    if not json_data:
        raise ValueError("Expected at least one comment.")

    if not all(isinstance(record, dict) for record in json_data):
        raise ValueError("Expected each comment to be a dictionary.")

    # Check the fields used by the Transform stage.
    required_fields = {"postId": int, "id": int, "name": str, "body": str}
    for index, record in enumerate(json_data, start=1):
        for field, expected_type in required_fields.items():
            if type(record.get(field)) is not expected_type:
                raise ValueError(
                    f"Comment {index}: expected {field} to be {expected_type.__name__}."
                )

    LOG.info("Validation passed.")
    LOG.info("Sink: validated JSON object")

    # Return the validated JSON data for use in the next stage.
    return json_data
