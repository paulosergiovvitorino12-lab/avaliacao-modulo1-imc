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
            st.image("https://images3.memedroid.com/images/UPLOADED58/57164ef325ef3.jpeg")

        elif imc < 24.9:
            st.write("Peso normal")
            st.image("https://media.tenor.com/WyxtAFPzvVMAAAAe/spongebob-square-pants.png")
        
        elif imc < 29.9:
            st.write("Sobrepeso")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3UBbyf8ix-GkpL1T_5g13sifoa7huysAv0g&s",width=600)
        
        elif imc < 34.9:
            st.write("Obesidade Grau I")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmLezNYJBm4rzWH83Vqx1o0nQoCbaT30ZHIA&s",width=600)
        
        elif imc < 39.9:
            st.write("Obesidade Grau II")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ20YmfzJBPSCKyHOQHwEF2CEihdEa8BDCtg&s",width=600)
        
        else:
            st.write("Obesidade Grau III")
            st.image("https://pbs.twimg.com/media/GnewS1PXQAAd03H.jpg",width=600)