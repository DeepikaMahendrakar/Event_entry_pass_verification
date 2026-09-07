import cv2
import numpy as np
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO


def create_participants():
    """Create the participant database as a NumPy array."""
    return np.array([
        ["E101", "Rahul", "Python Workshop", "Registered", "Not Entered"],
        ["E102", "Priya", "Python Workshop", "Registered", "Not Entered"],
        ["E103", "Arjun", "Python Workshop", "Not Registered", "Not Entered"],
        ["E104", "Sneha", "Python Workshop", "Registered", "Not Entered"],
        ["E105", "Kiran", "Python Workshop", "Registered", "Not Entered"]
    ], dtype=str)

def generate_qr(participant_id):
    """Generate QR code as PNG bytes."""
    
    qr = qrcode.make(str(participant_id))

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    return buffer.getvalue()


def decode_qr(uploaded_file):
    """Decode a QR code from an uploaded/captured image."""
    if uploaded_file is None:
        return None

    image_bytes = uploaded_file.getvalue()
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    image_array = np.array(image)

    # Convert RGB image to BGR for OpenCV
    frame = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

    results = decode(frame)

    if len(results) == 0:
        return None

    return results[0].data.decode("utf-8").strip()


def find_participant(participants, participant_id):
    """Find a participant using NumPy Boolean masking."""
    matching_rows = participants[participants[:, 0] == str(participant_id)]

    if matching_rows.size == 0:
        return None

    return matching_rows[0]


def verify_entry(participants, scanned_id):
    """
    Verify the scanned participant.
    Returns a result dictionary containing status and participant data.
    """
    participant = find_participant(participants, scanned_id)

    if participant is None:
        return {
            "result": "invalid",
            "participant": None,
            "message": "Invalid ID. Entry Denied."
        }

    if participant[3] != "Registered":
        return {
            "result": "not_registered",
            "participant": participant,
            "message": "Participant is not registered. Entry Denied."
        }

    if participant[4] == "Entered":
        return {
            "result": "already_entered",
            "participant": participant,
            "message": "QR already used. Duplicate entry denied."
        }

    return {
        "result": "allowed",
        "participant": participant,
        "message": "Registration verified. Entry Allowed."
    }


def mark_entry(participants, participant_id):
    """Update the entry status to Entered."""
    mask = participants[:, 0] == str(participant_id)
    participants[mask, 4] = "Entered"
    return participants


def get_participant_names(participants):
    """Return participant IDs and names for the QR generator."""
    return participants[:, 0] + " - " + participants[:, 1]
