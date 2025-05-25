import streamlit as st

def converter(value, from_unit, to_unit):

    conversion_pair = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000, # 1 kilometr =1000 meter
        "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000 # 1 kilogram = 1000 gram

    }

    key = f"{from_unit}_{to_unit}" # generate a unique key for conversion

    if key in conversion_pair:
            cnvrsin = conversion_pair[key] # key kay andar jo value hain unko store kary ga 1000 wagaira hai 
            return value * cnvrsin  
    else:
            return("conversion not found")
    
st.title("Unit Converter")

value = st.number_input("Enter the value to convert", min_value=1.0, step=1.0)

from_unit = st.selectbox( "Convert from", ["meter","kilometer","gram","kilogram"])
to_unit = st.selectbox( " Convert to", ["meter","kilometer","gram","kilogram"])

if st.button("Convert"):
       result = converter(value, from_unit, to_unit)
       st.write(f"Converted value: {result}")
