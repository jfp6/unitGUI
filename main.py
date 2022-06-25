import streamlit as st
from pint import UnitRegistry
import math
ur = UnitRegistry()
ur_ = ur.Quantity
pi = math.pi

st.write("# Unit Conversions")

conversion = st.radio("Select Conversion",("Length","Area","Volume","Volumetric Flow","Mass","Mass Flow"),horizontal=True)

col1,col1b, col2,col2b = st.columns([2,2,2,2])

with col1:
    if conversion == "Mass":
        st.header("Mass SI")
        mass_kg = st.number_input("Enter kg",step=1.0)*ur("kg")
        st.write('{:.2f}'.format(mass_kg.to("lb")))
        st.write('{:.4f}'.format(mass_kg.to("tonne")))
    elif conversion == "Length":
        st.header("Length SI")
        length_m = st.number_input("Enter m",step=1.0)*ur("m")
        st.write('{:.2f}'.format(length_m.to("in")))
with col1b:
    if conversion == "Mass":
        st.header("Unit In")
        massu = st.selectbox("Unit",("kg","tonne"))
        st.write(' ')
        st.write(' ')
    elif conversion == "Length":
        st.header("Length SI")
        length_m = st.number_input("Enter m",step=1.0)*ur("m")
        st.write('{:.2f}'.format(length_m.to("in")))
with col2:
    if conversion == "Mass":
        st.header("Mass USCS")
        mass_lbm = st.number_input("Enter lbm",step=1.0)*ur("lb")
        st.write('{:.2f}'.format(mass_lbm.to("kg")))
        st.write('{:.4f}'.format(mass_lbm.to("tonne")))
    elif conversion == "Length":
        st.header("Length USCS")
    
