import streamlit as st

st.title("Cálculo de IMC")

peso = st.number_input("Digite seu peso")
altura = st.number_input("Digite sua altura")

if st.button("Calcular"):
    if altura > 0:
        imc = peso / altura**2
        st.write("IMC:", imc)

        if imc < 18.5:
            st.write("Abaixo do peso")
         

        elif imc < 24.9:
            st.write("Peso normal")
           
        
        elif imc < 29.9:
            st.write("Sobrepeso")
         
        
        elif imc < 34.9:
            st.write("Obesidade Grau I")
          
        
        elif imc < 39.9:
            st.write("Obesidade Grau II")
         
        else:
            st.write("Obesidade Grau III")
       
