# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

st.title("Kanitham Rate Calculator (Excel Style)")

st.write("### Enter quantities directly in the table")

ROWS = 30

# Create empty editable table
input_df = pd.DataFrame({
    "Qty Rs.30": [0] * ROWS,
    "Qty Rs.12": [0] * ROWS,
    "Qty Rs.60": [0] * ROWS,
    "Qty Rs.130": [0] * ROWS,
})

# Editable grid
edited_df = st.data_editor(
    input_df,
    num_rows="fixed",
    use_container_width=True
)

# Calculate amounts
result_df = pd.DataFrame({
    "Amount Rs.30": edited_df["Qty Rs.30"] * 30,
    "Amount Rs.12": edited_df["Qty Rs.12"] * 12,
    "Amount Rs.60": edited_df["Qty Rs.60"] * 60,
    "Amount Rs.130": edited_df["Qty Rs.130"] * 130,
})

st.write("### Calculated Amounts")
st.dataframe(result_df, use_container_width=True)

# Grand total
grand_total = result_df.sum().sum()

st.markdown("---")
st.subheader(f"Grand Total: Rs. {int(grand_total)}")
