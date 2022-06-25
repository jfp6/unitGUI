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
    mass_kg = st.number_input("Enter kg",step=1.0)*ur("kg")
    st.write('{:.2f}'.format(mass_kg.to("lb")))
    st.write('{:.4f}'.format(mass_kg.to("tonne"))
    st.header("Length SI")
    

with col2:
    st.header("Mass USCS")
    mass_lbm = st.number_input("Enter lbm",step=1.0)*ur("lb")
    st.write('{:.2f}'.format(mass_lbm.to("kg")))
    st.write('{:.4f}'.format(mass_lbm.to("tonne")))
    st.header("Length USCS")
    
