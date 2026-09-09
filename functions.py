import cv2
import numpy as np
import qrcode
from PIL import Image
from io import BytesIO


# =====================================================
# CREATE PARTICIPANTS
# =====================================================

def create_participants():

    """Create participant database."""

    participants = np.array([
        ["E101", "Rahul", "Python Workshop", "Registered", "Not Entered"],
        ["E102", "Priya", "Python Workshop", "Registered", "Not Entered"],
        ["E103", "Arjun", "Python Workshop", "Registered", "Not Entered"],
        ["E104", "Sneha", "Python Workshop", "Registered", "Not Entered"],
        ["E105", "Kiran", "Python Workshop", "Not Registered", "Not Entered"],
        ["E106", "Anjali", "Python Workshop", "Registered", "Not Entered"],
        ["E107", "Vijay", "Python Workshop", "Registered", "Not Entered"],
        ["E108", "Meena", "Python Workshop", "Registered", "Not Entered"],
        ["E109", "Ravi", "Python Workshop", "Not Registered", "Not Entered"],
        ["E110", "Divya", "Python Workshop", "Registered", "Not Entered"]
    ])

    return participants


# =====================================================
# GENERATE QR CODE
# =====================================================

def generate_qr(participant_id):

    """Generate a QR code as PNG bytes."""

    qr = qrcode.make(str(participant_id))

    # Convert PIL image to PNG bytes
    buffer = BytesIO()

    qr.save(
        buffer,
        format="PNG"
    )

    return buffer.getvalue()


# =====================================================
# DECODE QR CODE
# =====================================================

def decode_qr(image_file):

    """
    Decode a QR code from a camera image or uploaded image.

    Uses OpenCV QRCodeDetector instead of pyzbar.
    """

    try:

        # Read uploaded/camera image bytes
        image_bytes = image_file.getvalue()

        # Convert bytes to NumPy array
        image_array = np.frombuffer(
            image_bytes,
            np.uint8
        )

        # Decode image using OpenCV
        image = cv2.imdecode(
            image_array,
            cv2.IMREAD_COLOR
        )

        if image is None:
            return None

        # Create QR detector
        detector = cv2.QRCodeDetector()

        # Detect and decode QR code
        scanned_id, points, _ = detector.detectAndDecode(image)

        # Check result
        if scanned_id:

            return scanned_id.strip()

        return None

    except Exception:

        return None


# =====================================================
# VERIFY ENTRY
# =====================================================

def verify_entry(participants, scanned_id):

    """
    Verify participant registration and entry status.
    """

    # Find participant
    matching_rows = participants[
        participants[:, 0] == scanned_id
    ]

    # Participant not found
    if len(matching_rows) == 0:

        return {
            "result": "invalid",
            "participant": None
        }

    # Get participant
    participant = matching_rows[0]

    registration = participant[3]
    entry_status = participant[4]

    # Check registration
    if registration != "Registered":

        return {
            "result": "not_registered",
            "participant": participant
        }

    # Check duplicate entry
    if entry_status == "Entered":

        return {
            "result": "already_entered",
            "participant": participant
        }

    # Entry allowed
    return {
        "result": "allowed",
        "participant": participant
    }


# =====================================================
# MARK ENTRY
# =====================================================

def mark_entry(participants, scanned_id):

    """
    Update participant entry status to Entered.
    """

    # Create a copy so the original array
    # is not modified unexpectedly
    updated_participants = participants.copy()

    # Find matching participant
    matching_rows = (
        updated_participants[:, 0] == scanned_id
    )

    # Update entry status
    updated_participants[
        matching_rows,
        4
    ] = "Entered"

    return updated_participants
