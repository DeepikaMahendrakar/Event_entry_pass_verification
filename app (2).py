
import pandas as pd
import streamlit as st

from functions import (
    create_participants,
    generate_qr,
    decode_qr,
    verify_entry,
    mark_entry,
)


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Python Workshop Event Entry Pass Verification",
    page_icon="🎟️",
    layout="wide"
)


# =====================================================
# SESSION STATE
# =====================================================

if "participants" not in st.session_state:

    st.session_state.participants = create_participants()

participants = st.session_state.participants


# =====================================================
# MAIN HEADING
# =====================================================

st.markdown(
    """
    <h1 style="
        color:#3949AB;
        font-weight:700;
        margin-bottom:5px;
    ">
        🎟️ Python Workshop Event Entry Pass Verification System
    </h1>
    """,
    unsafe_allow_html=True
)

st.write(
    "Generate QR passes, scan using your webcam, and verify entry."
)

st.divider()


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("Main Menu")

menu = st.sidebar.radio(
    "Choose an option",
    [   "Dashboard",
        "Participants Database",
        "Generate QR Code",
        "Scan & Verify"
    ]
)
# =====================================================
# DASHBOARD
# =====================================================

if menu == "Dashboard":

    # =================================================
    # WORKSHOP INFORMATION
    # =================================================

    st.info(
        """
        This system is designed to manage participant entry for the Python Workshop using QR Code-based verification. 
        Each registered participant is provided with a unique QR Code that can be generated and downloaded as an entry pass.
        At the event entrance, the QR Code can be scanned using a camera or uploaded as an image. 
        The system verifies the participant's registration status and allows entry only to valid registered participants. 
        It also tracks entry status and prevents duplicate entries.
        """
    )


    st.divider()

    st.markdown(
    """
    <h2 style="
        color:#3949AB;
        font-weight:700;
    ">
        Python Workshop Dashboard
    </h2>
    """,
    unsafe_allow_html=True
    )

    # =================================================
    # CALCULATE STATISTICS
    # =================================================

    total_participants = len(participants)

    registered_count = sum(
        participants[:, 3] == "Registered"
    )

    not_registered_count = total_participants - registered_count

    entered_count = sum(
        participants[:, 4] == "Entered"
    )

    not_entered_count = (
        total_participants - entered_count
    )


    # =================================================
    # DASHBOARD METRICS
    # =================================================

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Total Participants",
            total_participants
        )


    with col2:

        st.metric(
            "Registered",
            registered_count
        )


    with col3:

        st.metric(
            "Entered",
            entered_count
        )


    with col4:

        st.metric(
            "Not Entered",
            not_entered_count
        )


    st.divider()


    # =================================================
    # ENTRY STATUS
    # =================================================

    st.subheader("Entry Status")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Participants Entered",
            entered_count
        )

        st.progress(
            entered_count / total_participants
            if total_participants > 0
            else 0
        )


    with col2:

        st.metric(
            "Participants Waiting",
            not_entered_count
        )

        st.progress(
            not_entered_count / total_participants
            if total_participants > 0
            else 0
        )


    st.divider()


    # =================================================
    # WORKSHOP HIGHLIGHTS
    # =================================================

    st.subheader("System Features")

    st.info(
        """
        **i) Participant Database**  
        Manage and view participant registration details.

        **ii) QR Code Generation**  
        Generate a unique QR Code for each participant.

        **iii) QR Code Download**  
        Download the generated QR Code as an entry pass.

        **iv) QR Code Scanning**  
        Scan the participant's QR Code using the camera.

        **v) Participant Verification**  
        Verify the participant's registration before allowing entry.

        **vi) Duplicate Entry Prevention**  
        Prevent participants from entering more than once.

        **vii) Entry Status Tracking**  
        Track whether each participant has entered the event.
        """
    )
 

# =====================================================
# PARTICIPANTS DATABASE
# =====================================================

if menu == "Participants Database":

    st.markdown(
        """
        <h2 style="
            color:#5E35B1;
            font-weight:700;
        ">
            👥 Participants Database
        </h2>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # CREATE DATAFRAME
    # -------------------------------------------------

    df = pd.DataFrame(
        participants,
        columns=[
            "ID",
            "Name",
            "Event",
            "Registration Status",
            "Entry Status"
        ]
    )


    # -------------------------------------------------
    # REGISTRATION COLOR
    # -------------------------------------------------

    def registration_color(value):

        if value == "Registered":

            return (
                "background-color: #C8E6C9;"
                "color: #1B5E20;"
                "font-weight: bold;"
            )

        return (
            "background-color: #FFCDD2;"
            "color: #B71C1C;"
            "font-weight: bold;"
        )


    # -------------------------------------------------
    # ENTRY STATUS COLOR
    # -------------------------------------------------

    def entry_color(value):

        if value == "Entered":

            return (
                "background-color: #BBDEFB;"
                "color: #0D47A1;"
                "font-weight: bold;"
            )

        return (
            "background-color: #FFF9C4;"
            "color: #F57F17;"
            "font-weight: bold;"
        )


    # -------------------------------------------------
    # APPLY COLORS
    # -------------------------------------------------

    styled_df = (
        df.style
        .map(
            registration_color,
            subset=["Registration Status"]
        )
        .map(
            entry_color,
            subset=["Entry Status"]
        )
    )


    # -------------------------------------------------
    # DISPLAY DATAFRAME
    # -------------------------------------------------

    st.dataframe(
        styled_df,
        hide_index=True,
        use_container_width=True
    )


# =====================================================
# GENERATE QR CODE
# =====================================================

elif menu == "Generate QR Code":

    st.markdown(
        """
        <h2 style="
            color:#1565C0;
            font-weight:700;
        ">
            🎟️ Generate QR Code
        </h2>
        """,
        unsafe_allow_html=True
    )


    st.header("Generate QR Code")


    # -------------------------------------------------
    # PARTICIPANT SELECTION
    # -------------------------------------------------

    participant_ids = participants[:, 0]

    selected_id = st.selectbox(
        "Select Participant",
        participant_ids
    )


    # -------------------------------------------------
    # SELECTED PARTICIPANT
    # -------------------------------------------------

    selected = participants[
        participants[:, 0] == selected_id
    ][0]


    # -------------------------------------------------
    # PARTICIPANT INFORMATION
    # -------------------------------------------------

    st.write(
        "**Name:**",
        selected[1]
    )

    st.write(
        "**Event:**",
        selected[2]
    )

    st.write(
        "**Registration:**",
        selected[3]
    )


    # -------------------------------------------------
    # GENERATE QR CODE
    # -------------------------------------------------

    if st.button(
        "Generate QR Code",
        type="primary"
    ):

        qr_image = generate_qr(
            selected_id
        )


        # -------------------------------------------------
        # DISPLAY QR
        # -------------------------------------------------

        st.image(
            qr_image,
            caption=f"QR Code for {selected_id}",
            width=300
        )


        st.success(
            f"QR code generated for {selected_id}"
        )


        # -------------------------------------------------
        # DOWNLOAD QR CODE
        # -------------------------------------------------

        st.download_button(
            label="Download QR Code",
            data=qr_image,
            file_name=f"{selected_id}_QR_Code.png",
            mime="image/png",
            type="primary"
        )


# =====================================================
# SCAN & VERIFY
# =====================================================

elif menu == "Scan & Verify":

    st.markdown(
        """
        <h2 style="
            color:#00897B;
            font-weight:700;
        ">
            📷 Scan & Verify QR Code
        </h2>
        """,
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # INSTRUCTIONS
    # -------------------------------------------------

    st.info(
        """
        **How to verify entry**

        1. Scan the QR code using the camera
        2. Or upload a QR code image
        3. The system will detect the Participant ID
        4. Participant registration will be verified
        5. Entry status will be updated
        """
    )


    # =================================================
    # CHOOSE VERIFICATION METHOD
    # =================================================

    verification_method = st.radio(
        "Choose verification method",
        [
            "Upload QR Code",
            "Scan using Camera"
        ],
        index=0,
        horizontal=True
    )


    # =================================================
    # UPLOAD QR CODE
    # =================================================

    if verification_method == "Upload QR Code":

        uploaded_image = st.file_uploader(
            "Upload the QR Code",
            type=["png", "jpg", "jpeg"],
            key="qr_upload"
        )


        if uploaded_image is not None:

            scanned_id = decode_qr(
                uploaded_image
            )


            # ---------------------------------------------
            # QR NOT DETECTED
            # ---------------------------------------------

            if scanned_id is None:

                st.error(
                    "❌ QR Code could not be detected."
                )

                st.write(
                    "Please upload a clear QR code image."
                )


            # ---------------------------------------------
            # QR DETECTED
            # ---------------------------------------------

            else:

                st.success(
                    f"🔍 QR Code detected: **{scanned_id}**"
                )


                # =============================================
                # VERIFY PARTICIPANT
                # =============================================

                verification = verify_entry(
                    participants,
                    scanned_id
                )


                participant = verification["participant"]


                # =============================================
                # INVALID PARTICIPANT
                # =============================================

                if participant is None:

                    st.error(
                        "❌ INVALID PARTICIPANT ID"
                    )

                    st.error(
                        "🚫 ENTRY DENIED"
                    )


                # =============================================
                # VALID PARTICIPANT
                # =============================================

                else:

                    st.subheader(
                        "Participant Details"
                    )


                    col1, col2 = st.columns(2)


                    # -----------------------------------------
                    # PARTICIPANT INFORMATION
                    # -----------------------------------------

                    with col1:

                        st.info(
                            f"""
                            **Participant Information**

                            **ID:** {participant[0]}

                            **Name:** {participant[1]}

                            **Event:** {participant[2]}
                            """
                        )


                    # -----------------------------------------
                    # REGISTRATION INFORMATION
                    # -----------------------------------------

                    with col2:

                        st.info(
                            f"""
                            **Registration Information**

                            **Registration:** {participant[3]}

                            **Entry Status:** {participant[4]}
                            """
                        )


                    st.divider()


                    # =============================================
                    # ENTRY ALLOWED
                    # =============================================

                    if verification["result"] == "allowed":

                        st.success(
                            "✅ REGISTRATION VERIFIED"
                        )

                        st.success(
                            "🎟️ ENTRY ALLOWED"
                        )


                        st.session_state.participants = mark_entry(
                            participants,
                            scanned_id
                        )


                        st.info(
                            "🟢 Entry status updated to Entered."
                        )


                    # =============================================
                    # NOT REGISTERED
                    # =============================================

                    elif verification["result"] == "not_registered":

                        st.error(
                            "❌ NOT REGISTERED"
                        )

                        st.error(
                            "🚫 ENTRY DENIED"
                        )


                    # =============================================
                    # ALREADY ENTERED
                    # =============================================

                    elif verification["result"] == "already_entered":

                        st.warning(
                            "⚠️ QR CODE ALREADY USED"
                        )

                        st.error(
                            "🚫 DUPLICATE ENTRY DENIED"
                        )


# =====================================================
# SCAN USING CAMERA
# =====================================================

    elif verification_method == "Scan using Camera":

        camera_image = st.camera_input(
            "Scan the QR Code",
            key="qr_camera"
        )


        if camera_image is not None:

            scanned_id = decode_qr(
                camera_image
            )


            # ---------------------------------------------
            # QR NOT DETECTED
            # ---------------------------------------------

            if scanned_id is None:

                st.error(
                    "❌ QR Code could not be detected."
                )

                st.write(
                    "Please try again with a clear QR code."
                )


            # ---------------------------------------------
            # QR DETECTED
            # ---------------------------------------------

            else:

                st.success(
                    f"🔍 QR Code detected: **{scanned_id}**"
                )


                # =============================================
                # VERIFY PARTICIPANT
                # =============================================

                verification = verify_entry(
                    participants,
                    scanned_id
                )


                participant = verification["participant"]


                # =============================================
                # INVALID PARTICIPANT
                # =============================================

                if participant is None:

                    st.error(
                        "❌ INVALID PARTICIPANT ID"
                    )

                    st.error(
                        "🚫 ENTRY DENIED"
                    )


                # =============================================
                # VALID PARTICIPANT
                # =============================================

                else:

                    st.subheader(
                        "Participant Details"
                    )


                    col1, col2 = st.columns(2)


                    # -----------------------------------------
                    # PARTICIPANT INFORMATION
                    # -----------------------------------------

                    with col1:

                        st.info(
                            f"""
                            **Participant Information**

                            **ID:** {participant[0]}

                            **Name:** {participant[1]}

                            **Event:** {participant[2]}
                            """
                        )


                    # -----------------------------------------
                    # REGISTRATION INFORMATION
                    # -----------------------------------------

                    with col2:

                        st.info(
                            f"""
                            **Registration Information**

                            **Registration:** {participant[3]}

                            **Entry Status:** {participant[4]}
                            """
                        )


                    st.divider()


                    # =============================================
                    # ENTRY ALLOWED
                    # =============================================

                    if verification["result"] == "allowed":

                        st.success(
                            "✅ REGISTRATION VERIFIED"
                        )

                        st.success(
                            "🎟️ ENTRY ALLOWED"
                        )


                        st.session_state.participants = mark_entry(
                            participants,
                            scanned_id
                        )


                        st.info(
                            "🟢 Entry status updated to Entered."
                        )


                    # =============================================
                    # NOT REGISTERED
                    # =============================================

                    elif verification["result"] == "not_registered":

                        st.error(
                            "❌ NOT REGISTERED"
                        )

                        st.error(
                            "🚫 ENTRY DENIED"
                        )


                    # =============================================
                    # ALREADY ENTERED
                    # =============================================

                    elif verification["result"] == "already_entered":

                        st.warning(
                            "⚠️ QR CODE ALREADY USED"
                        )

                        st.error(
                            "🚫 DUPLICATE ENTRY DENIED"
                        )
