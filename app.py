
import streamlit as st
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a',0.00)
b = st.number_input('Tham số b',0.00)
if st.button('Giải'):
    x = -b/a
    st.success(f'Phương trình có 1 nghiệm: {x}')

