# 🎟️ Python Workshop Event Entry Pass Verification System

A **QR Code-based Event Entry Pass Verification System** developed using Python and Streamlit to manage participant registration, generate digital entry passes, verify participants, and prevent duplicate entries.

## 📌 Project Overview

The **Python Workshop Event Entry Pass Verification System** is designed to simplify and automate participant entry management at a workshop or event.

Each registered participant is assigned a unique QR Code that acts as their digital entry pass. The QR Code can be generated and downloaded, and at the event entrance it can be verified either by:

* 📷 Scanning the QR Code using a camera
* 📁 Uploading a QR Code image

The system checks the participant's registration status before allowing entry. It also maintains the entry status and prevents the same QR Code from being used for duplicate entry.

## ✨ Key Features

* 👥 **Participant Database**

  * View participant details
  * Track registration status
  * Track entry status

* 🎟️ **QR Code Generation**

  * Generate a unique QR Code for each participant
  * Display the generated QR Code

* 📥 **QR Code Download**

  * Download the QR Code as a PNG image
  * Use the downloaded QR Code as an entry pass

* 📷 **QR Code Scanning**

  * Scan QR Codes using a camera
  * Verify QR Codes at the event entrance

* 📁 **QR Code Upload**

  * Upload an existing QR Code image
  * Verify the uploaded QR Code

* ✅ **Participant Verification**

  * Check participant ID
  * Verify registration status
  * Allow entry only to valid registered participants

* 🚫 **Duplicate Entry Prevention**

  * Detect previously used QR Codes
  * Prevent duplicate entry

* 📊 **Entry Status Tracking**

  * Track participants who have entered
  * Identify participants who have not yet entered

* 📈 **Dashboard**

  * View total participants
  * View registered participants
  * View entered participants
  * View participants who have not entered

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **NumPy**
* **Pandas**
* **QRCode**
* **OpenCV**
* **PyZbar**

## 📂 Project Structure

```text
Python-Workshop-Entry-Verification/
│
├── app.py
├── functions.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit user interface and application flow.

### `functions.py`

Contains the main Python functions for:

* Creating participant data
* Generating QR Codes
* Decoding QR Codes
* Verifying participants
* Updating entry status

### `requirements.txt`

Contains the Python packages required to run the application.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/DeepikaMahendrakar/Event_entry_pass_verification/tree/main
```

### 2. Open the project folder

```bash
cd Python-Workshop-Entry-Verification
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔄 Application Workflow

```text
Participant Database
        ↓
Select Participant
        ↓
Generate QR Code
        ↓
Download QR Code
        ↓
Participant Presents QR Code
        ↓
Scan / Upload QR Code
        ↓
Decode Participant ID
        ↓
Verify Registration
        ↓
     ┌───────────────┐
     │ Valid &       │
     │ Registered?   │
     └───────┬───────┘
             │
       ┌─────┴─────┐
       ↓           ↓
      YES          NO
       ↓           ↓
ENTRY ALLOWED   ENTRY DENIED
       ↓
Update Entry Status
       ↓
Prevent Duplicate Entry
```

## 🔐 Entry Verification Logic

The system verifies participants based on three main conditions:

### 1. Registered Participant

If the participant is registered and has not entered previously:

**Registration Verified → Entry Allowed**

### 2. Not Registered

If the participant ID exists but the registration status is not valid:

**Not Registered → Entry Denied**

### 3. Already Entered

If the participant has already used the QR Code:

**QR Code Already Used → Duplicate Entry Denied**

## 📊 Dashboard

The dashboard provides an overview of the event and displays important statistics such as:

* Total Participants
* Registered Participants
* Participants Entered
* Participants Not Entered

This provides event organizers with a quick view of the current entry status.

## 🎯 Purpose of the Project

This project demonstrates how Python can be used to build a practical event management application using:

* Data management
* QR Code technology
* Image processing
* Participant verification
* Streamlit web application development

It can be adapted for **workshops, seminars, conferences, training programs, college events, and other registration-based events**.

## 🚀 Future Enhancements

Possible future improvements include:

* Database integration using MySQL
* Automatic entry timestamp recording
* Entry history and reports
* CSV/Excel report generation
* Admin authentication
* Multiple event support
* Email or WhatsApp notifications
* Cloud deployment
* Real-time attendance analytics

## 👩‍💻 Author

**Deepika M**

This project was developed as a practical Python and Streamlit application for QR-based event entry management.
