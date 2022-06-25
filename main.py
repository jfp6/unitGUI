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
    value = qty*ur(unit)
    col1.write('{:.0f}'.format(value.to("Pa").magnitude)+" Pa")
    col1.write('{:.0f}'.format(value.to("kPa").magnitude)+" kPa")
    col1.write('{:.3f}'.format(value.to("MPa").magnitude)+" MPa")
    col1.write('{:.2f}'.format(value.to("bar").magnitude)+" bar")
    col1.write('{:.1f}'.format(value.to("psi").magnitude)+" psi")
elif conversion == "Temperature":
    unit = col2.selectbox("Unit",("K","degC","degF","degR"))
    qty = col1.number_input("Input",step=1.0)
    value = ur_(qty,unit)
    col1.write('{:.1f}'.format(value.to("K").magnitude)+" K")
    col1.write('{:.1f}'.format(value.to("degC").magnitude)+" degC")
    col1.write('{:.1f}'.format(value.to("degF").magnitude)+" degF")
    col1.write('{:.1f}'.format(value.to("degR").magnitude)+" degR")
elif conversion == "Length":
    unit = col2.selectbox("Unit",("mm","m","in","ft"))
    qty = col1.number_input("Input",step=1.0)
    value = qty*ur(unit)
    col1.write('{:.2f}'.format(value.to("mm").magnitude)+" mm")
    col1.write('{:.2f}'.format(value.to("m").magnitude)+" m")
    col1.write('{:.3f}'.format(value.to("in").magnitude)+" in")
    col1.write('{:.2f}'.format(value.to("ft").magnitude)+" ft")
elif conversion == "Mass":
    unit = col2.selectbox("Unit",("kg","tonne","lb","slug"))
    qty = col1.number_input("Input",step=1.0)
    value = qty*ur(unit)
    col1.write('{:.2f}'.format(value.to("kg").magnitude)+" kg")
    col1.write('{:.1f}'.format(value.to("tonne").magnitude)+" tonne")
    col1.write('{:.2f}'.format(value.to("lb").magnitude)+" lb")
    col1.write('{:.2f}'.format(value.to("slug").magnitude)+" slug")
