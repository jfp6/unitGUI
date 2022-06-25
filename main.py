import streamlit as st
from pint import UnitRegistry
import math
ur = UnitRegistry()
ur_ = ur.Quantity
pi = math.pi

ur.default_format = '.3f'
st.write("# Unit Conversions")

col1, col2 = st.columns(2)

with col1:
    st.header("Mass SI")
    mass_kg = st.number_input("Enter kg")*ur("kg")
    st.write(mass_kg.to("lb"))

with col2:
    st.header("Mass USCS")
    mass_lbm = st.number_input("Enter lbm")*ur("lb")
    st.write(mass_lbm.to("kg"))
    
