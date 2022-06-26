import streamlit as st
from pint import UnitRegistry
import math
ur = UnitRegistry()
ur_ = ur.Quantity
pi = math.pi

st.write("# Unit Conversions")

conversion = st.radio("Select Conversion",("Pressure","Temperature","Length","Area","Volume","Volumetric Flow","Mass","Mass Flow"),horizontal=True)

col1, col2 = st.columns([3,3])

if conversion == "Pressure":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("Pa","kPa","MPa","bar","psi"))
    value = qty*ur(unit)
    col1.write('{:.3g}'.format(value.to("Pa").magnitude)+" Pa")
    col1.write('{:.3g}'.format(value.to("kPa").magnitude)+" kPa")
    col1.write('{:.3g}'.format(value.to("MPa").magnitude)+" MPa")
    col1.write('{:.3g}'.format(value.to("bar").magnitude)+" bar")
    col1.write('{:.3g}'.format(value.to("psi").magnitude)+" psi")
elif conversion == "Temperature":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("K","degC","degF","degR"))
    value = ur_(qty,unit)
    col1.write('{:.3g}'.format(value.to("K").magnitude)+" K")
    col1.write('{:.3g}'.format(value.to("degC").magnitude)+" degC")
    col1.write('{:.3g}'.format(value.to("degF").magnitude)+" degF")
    col1.write('{:.3g}'.format(value.to("degR").magnitude)+" degR")
elif conversion == "Length":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("mm","m","in","ft"))
    value = qty*ur(unit)
    col1.write('{:.3g}'.format(value.to("mm").magnitude)+" mm")
    col1.write('{:.3g}'.format(value.to("m").magnitude)+" m")
    col1.write('{:.3g}'.format(value.to("in").magnitude)+" in")
    col1.write('{:.3g}'.format(value.to("ft").magnitude)+" ft")
elif conversion == "Area":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("mm2","m2","in2","ft2"))
    if unit == "mm2":
        unit = "mm**2"
    elif unit == "m2":
        unit = "m**2"
    elif unit == "in2":
        unit = "in**2"
    elif unit == "ft2":
        unit = "ft**2"
    value = qty*ur(unit)
    col1.write('{:.3g}'.format(value.to("mm**2").magnitude)+" mm2")
    col1.write('{:.3g}'.format(value.to("m**2").magnitude)+" m2")
    col1.write('{:.3g}'.format(value.to("in**2").magnitude)+" in2")
    col1.write('{:.3g}'.format(value.to("ft**2").magnitude)+" ft2")
elif conversion == "Volume":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("mm3","m3","in3","ft3"))
    if unit == "mm3":
        unit = "mm**3"
    elif unit == "m3":
        unit = "m**3"
    elif unit == "in3":
        unit = "in**3"
    elif unit == "ft3":
        unit = "ft**3"
    value = qty*ur(unit)
    col1.write('{:.3g}'.format(value.to("mm**3").magnitude)+" mm3")
    col1.write('{:.3g}'.format(value.to("m**3").magnitude)+" m3")
    col1.write('{:.3g}'.format(value.to("in**3").magnitude)+" in3")
    col1.write('{:.3g}'.format(value.to("ft**3").magnitude)+" ft3")
elif conversion == "Volumetric Flow":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("m3/hr","m3/s","gpm","ft3/s"))
    if unit == "m3/hr":
        unit = "m**3/hr"
    elif unit == "m3/s":
        unit = "m**3/s"
    elif unit == "gpm":
        unit = "gallon/min"
    elif unit == "ft3/s":
        unit = "ft**3/s"
    value = qty*ur(unit)
    col1.write('{:.3g}'.format(value.to("m**3/hr").magnitude)+" m3/hr")
    col1.write('{:.3g}'.format(value.to("m**3/s").magnitude)+" m3/s")
    col1.write('{:.3g}'.format(value.to("gallon/min").magnitude)+" gpm")
    col1.write('{:.3g}'.format(value.to("ft**3/s").magnitude)+" ft3/s")
elif conversion == "Mass":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("kg","tonne","lb","slug"))
    value = qty*ur(unit)
    col1.write('{:.3g}'.format(value.to("kg").magnitude)+" kg")
    col1.write('{:.3g}'.format(value.to("tonne").magnitude)+" tonne")
    col1.write('{:.3g}'.format(value.to("lb").magnitude)+" lb")
    col1.write('{:.3g}'.format(value.to("slug").magnitude)+" slug")
elif conversion == "Mass Flow":
    qty = col1.number_input("Input",step=1.0)
    unit = col2.selectbox("Unit",("kg/hr","tonne/hr","kg/s","lb/hr","lb/s"))
    value = qty*ur(unit)
    col1.write('{:.3g}'.format(value.to("kg/hr").magnitude)+" kg/hr")
    col1.write('{:.3g}'.format(value.to("tonne/hr").magnitude)+" tonne/hr")
    col1.write('{:.3g}'.format(value.to("kg/s").magnitude)+" kg/s")
    col1.write('{:.3g}'.format(value.to("lb/hr").magnitude)+" lb/hr")
    col1.write('{:.3g}'.format(value.to("lb/s").magnitude)+" lb/s")
