import streamlit as st
from pint import UnitRegistry
import math
ur = UnitRegistry()
ur_ = ur.Quantity
pi = math.pi

st.write("# Unit Conversions")

conversion = st.radio("Select Conversion",("Pressure","Temperature","Length","Area","Volume","Volumetric Flow","Mass","Mass Flow","Energy"),horizontal=True)

col1, col2 = st.columns([3,2])

if conversion == "Pressure":
    unit = col2.selectbox("Unit",("Pa","kPa","MPa","bar","psi"))
    qty = col1.number_input("Input",step=1.0)
    col1.write('{:.0f}'.format(qty.to("Pa").magnitude,"Pa")
    col1.write('{:.0f}'.format(qty*ur(unit).to("kPa")))
    col1.write('{:.3f}'.format(qty*ur(unit).to("MPa")))
    col1.write('{:.2f}'.format(qty*ur(unit).to("bar")))
    col1.write('{:.1f}'.format(qty*ur(unit).to("psi")))
elif conversion == "Temperature":
    unit = col2.selectbox("Unit",("K","C","F","R"))
    qty = col1.number_input("Input",step=1.0)
    col1.write('{:.1f}'.format(qty*ur_(unit).to("C")))
    col1.write('{:.1f}'.format(qty*ur_(unit).to("K")))
    col1.write('{:.1f}'.format(qty*ur_(unit).to("F")))
    col1.write('{:.1f}'.format(qty*ur_(unit).to("R")))
elif conversion == "Mass":
    unit = col2.selectbox("Unit",("kg","tonne","lb","slug"))
    qty = col1.number_input("Input",step=1.0)
    col1.write('{:.2f}'.format(qty*ur(unit).to("kg")))
    col1.write('{:.4f}'.format(qty*ur(unit).to("tonne")))
    col1.write('{:.2f}'.format(qty*ur(unit).to("lb")))
    col1.write('{:.4f}'.format(qty*ur(unit).to("slug")))
