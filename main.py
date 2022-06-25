import streamlit as st
from pint import UnitRegistry
import math
ur = UnitRegistry()
ur_ = ur.Quantity
pi = math.pi

st.write("# Unit Conversions")

conversion = st.radio("Select Conversion",("Pressure","Temperature","Length","Area","Volume","Volumetric Flow","Mass","Mass Flow"),horizontal=True)

col1, col2 = st.columns([3,2])

if conversion == "Mass":
    massu = col2.selectbox("Unit",("kg","tonne","lb","slug"))
    mass = col1.number_input("Input",step=1.0)
    col1.write('{:.2f}'.format(mass*ur(massu).to("kg")))
    col1.write('{:.2f}'.format(mass*ur(massu).to("lb")))
    col1.write('{:.4f}'.format(mass*ur(massu).to("tonne")))
    
