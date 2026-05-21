# =========================================================
# 🩺 AI CLINICAL DECISION SUPPORT SYSTEM
# Diploma 6th Semester Project
# =========================================================

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from fpdf import FPDF

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Clinical System",
    page_icon="🩺",
    layout="wide"
)

# =========================================================
# SIMPLE PREMIUM CSS
# =========================================================

st.markdown("""

<style>
/* HIDE PRESS ENTER TO APPLY */

[data-testid="InputInstructions"]{
    display:none !important;
}

.stTextInput div div div div input + div{
    display:none !important;
}
.stApp{
    background:#0f172a;
    color:white;
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background:#111827;
}

/* TITLES */

h1,h2,h3,h4{
    color:white;
}

/* GENERATE BUTTON */

.stButton>button{

    width:100%;

    background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    color:white;

    border:none;

    border-radius:14px;

    font-size:18px;

    font-weight:bold;

    height:55px;

    transition:0.3s;
}

.stButton>button:hover{

    transform:scale(1.02);
}

/* EXPORT BUTTON */

div.stDownloadButton > button{

    width:100%;

    background:linear-gradient(
        90deg,
        #06b6d4,
        #7c3aed
    );

    color:white;

    border:none;

    border-radius:14px;

    font-size:20px;

    font-weight:bold;

    height:60px;

    animation:pulse 2s infinite;
}

/* ANIMATION */

@keyframes pulse {

    0%{
        transform:scale(1);
    }

    50%{
        transform:scale(1.03);
    }

    100%{
        transform:scale(1);
    }
}

/* RESULT BOX */

.result-box{

    background:#111827;

    padding:25px;

    border-radius:18px;

    border:1px solid #334155;

    margin-top:20px;
}

/* MEDICINE CARDS */

.med-card{

    padding:18px;

    border-radius:16px;

    margin-bottom:15px;

    color:white;

    font-size:20px;

    font-weight:bold;

    box-shadow:0px 0px 15px rgba(0,0,0,0.4);
}

</style>

""", unsafe_allow_html=True)

# =========================================================
# LOGIN SYSTEM
# =========================================================

PASSWORD = "admin123"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.title("🔐 Secure Clinical Login")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Login"):

        if password == PASSWORD:

            st.session_state.login = True
            st.rerun()

        else:

            st.error("❌ Wrong Password")

    st.stop()

# =========================================================
# DATABASE
# =========================================================

disease_db = {

    "Pneumonia": {

        "symptoms":[
            "cough",
            "fever",
            "chest pain"
        ],

        "risk":"HIGH",

        "medicine":[
            "Azithromycin",
            "Paracetamol",
            "Amoxicillin"
        ]
    },

    "Heart Disease": {

        "symptoms":[
            "chest pain",
            "fatigue",
            "shortness of breath"
        ],

        "risk":"CRITICAL",

        "medicine":[
            "Aspirin",
            "Beta Blocker",
            "Nitroglycerin"
        ]
    },

    "Malaria": {

        "symptoms":[
            "fever",
            "body pain",
            "chills"
        ],

        "risk":"MEDIUM",

        "medicine":[
            "Chloroquine",
            "Paracetamol",
            "ORS"
        ]
    },

    "Dengue": {

        "symptoms":[
            "fever",
            "body pain",
            "rash"
        ],

        "risk":"HIGH",

        "medicine":[
            "ORS",
            "Paracetamol",
            "Fluid Therapy"
        ]
    }
}

# =========================================================
# ALL SYMPTOMS
# =========================================================

all_symptoms = sorted(list(set(

    symptom

    for disease in disease_db.values()

    for symptom in disease["symptoms"]

)))

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("👤 Patient Information")

name = st.sidebar.text_input("Patient Name")

age = st.sidebar.number_input(
    "Age",
    1,
    120,
    18
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male","Female","Other"]
)

mobile = st.sidebar.text_input(
    "Mobile Number"
)

# =========================================================
# MAIN TITLE
# =========================================================

st.title("🩺 AI Clinical Decision Support System")

st.success("✅ AI Clinical Engine Ready")

# =========================================================
# SELECT SYMPTOMS
# =========================================================

selected_symptoms = st.multiselect(

    "🧾 Select Symptoms",

    all_symptoms
)

# =========================================================
# PDF REPORT FUNCTION
# =========================================================

def generate_pdf(

    patient_name,
    mobile,
    disease,
    medicines,
    symptoms,
    risk

):

    pdf = FPDF()

    pdf.add_page()

    # HEADER

    pdf.set_fill_color(15,23,42)

    pdf.rect(0,0,220,40,'F')

    pdf.set_text_color(255,255,255)

    pdf.set_font("Arial","B",26)

    pdf.cell(
        200,
        18,
        "AI CLINICAL REPORT",
        ln=True,
        align="C"
    )

    pdf.set_font("Arial","",12)

    pdf.cell(
        200,
        5,
        "Advanced Healthcare Prediction System",
        ln=True,
        align="C"
    )

    pdf.ln(20)

    # PATIENT BOX

    pdf.set_fill_color(240,248,255)

    pdf.rect(15,50,180,40,'F')

    pdf.set_text_color(0,0,0)

    pdf.set_font("Arial","B",13)

    pdf.cell(45,10,"Patient Name:")

    pdf.set_font("Arial","",13)

    pdf.cell(100,10,patient_name,ln=True)

    pdf.set_font("Arial","B",13)

    pdf.cell(45,10,"Mobile Number:")

    pdf.set_font("Arial","",13)

    pdf.cell(100,10,mobile,ln=True)

    pdf.set_font("Arial","B",13)

    pdf.cell(45,10,"Date:")

    pdf.set_font("Arial","",13)

    pdf.cell(
        100,
        10,
        datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        ln=True
    )

    pdf.ln(15)

    # DISEASE

    pdf.set_fill_color(220,38,38)

    pdf.set_text_color(255,255,255)

    pdf.set_font("Arial","B",18)

    pdf.cell(
        190,
        12,
        f" Predicted Disease: {disease}",
        ln=True,
        fill=True
    )

    pdf.ln(8)

    pdf.set_text_color(0,0,0)

    pdf.set_font("Arial","B",14)

    pdf.cell(
        200,
        10,
        f"Risk Level: {risk}",
        ln=True
    )

    pdf.ln(5)

    # SYMPTOMS

    pdf.set_font("Arial","B",16)

    pdf.cell(
        200,
        10,
        "Symptoms",
        ln=True
    )

    pdf.set_font("Arial","",12)

    for symptom in symptoms:

        pdf.cell(
            200,
            10,
            f"-{symptom}",
            ln=True
        )

    pdf.ln(5)

    # MEDICINES

    pdf.set_font("Arial","B",16)

    pdf.cell(
        200,
        10,
        "Suggested Medicines",
        ln=True
    )

    pdf.set_font("Arial","",12)

    for med in medicines:

        pdf.cell(
            200,
            10,
            f"- {med}",
            ln=True
        )

    pdf.ln(10)

    # FOOTER

    pdf.set_draw_color(180,180,180)

    pdf.line(15,250,195,250)

    pdf.ln(8)

    pdf.set_font("Arial","I",10)

    pdf.multi_cell(
        180,
        6,
        "Disclaimer: Educational project only. Consult a licensed doctor for professional medical advice."
    )

    pdf.output("Clinical_Report.pdf")


# =========================================================
# GENERATE DIAGNOSIS
# =========================================================

if st.button("🧠 Generate Diagnosis"):

    if len(selected_symptoms) == 0:

        st.warning("⚠️ Please select symptoms")

    else:

        best_match = None
        best_score = 0

        for disease, info in disease_db.items():

            matched = len(

                set(selected_symptoms)

                &

                set(info["symptoms"])
            )

            if matched > best_score:

                best_score = matched

                best_match = disease

        disease_info = disease_db[best_match]

        confidence = int(

            (best_score / len(disease_info["symptoms"])) * 100
        )

        # RESULT BOX

        st.markdown(f"""

        <div class="result-box">

        <h2>
        🦠 Predicted Disease
        </h2>

        <h1 style="color:#38bdf8;">
        {best_match}
        </h1>

        <h3>
        ⚠ Risk Level:
        {disease_info['risk']}
        </h3>

        <h3>
        📊 Match Confidence:
        {confidence}%
        </h3>

        </div>

        """, unsafe_allow_html=True)

        # SYMPTOMS

        st.write("## ✅ Matched Symptoms")

        for symptom in selected_symptoms:

            st.success(symptom)

        # MEDICINES

        st.write("## 💊 Suggested Medicines")

        colors = [

            "#2563eb",
            "#7c3aed",
            "#06b6d4",
            "#0f766e"
        ]

        for i, med in enumerate(disease_info["medicine"]):

            color = colors[i % len(colors)]

            st.markdown(f"""

            <div class="med-card"
            style="
            background:{color};
            ">

            💊 {med}

            </div>

            """, unsafe_allow_html=True)

        # GENERATE PDF

        generate_pdf(

            name,
            mobile,
            best_match,
            disease_info["medicine"],
            selected_symptoms,
            disease_info["risk"]
        )

        # OPEN PDF

        with open(
            "Clinical_Report.pdf",
            "rb"
        ) as file:

            pdf_data = file.read()

        # EXPORT BUTTON

        exported = st.download_button(

            label="✨ EXPORT REPORT",

            data=pdf_data,

            file_name="Clinical_Report.pdf",

            mime="application/pdf"
        )

        # SAVE EXCEL

        if exported:

            save_excel(

                name,
                age,
                gender,
                mobile,
                best_match,
                disease_info["risk"]
            )

            st.balloons()

            st.success(
                "✅ Report Exported Successfully!"
            )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "🔒 AI Clinical System | Diploma 6th Semester Project"
)
