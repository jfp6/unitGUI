import streamlit as st
from pint import UnitRegistry
import math
ur = UnitRegistry()
ur_ = ur.Quantity
pi = math.pi

st.write("# Unit Conversions")

conversion = st.radio("Select Conversion",("Length","Area","Volume","Volumetric Flow","Mass","Mass Flow"),horizontal=True)

if conversion == "Mass":
    st.header("Mass")
    st.header("Unit In")
    massu = st.selectbox("Unit",("kg","tonne","lb","slug"))
    mass = st.number_input("Enter kg",step=1.0)
    st.write('{:.2f}'.format(mass*ur(massu).to("kg")))
    st.write('{:.2f}'.format(mass*ur(massu).to("lb")))
    st.write('{:.4f}'.format(mass*ur(massu).to("tonne")))
elif conversion == "Length":
    st.header("Length")
    length_m = st.number_input("Enter m",step=1.0)*ur("m")
    st.write('{:.2f}'.format(length_m.to("in")))
