import streamlit as st

st.title("🎫 Sistema de Taquilla")

# Inicializamos las listas por categorías dentro de la memoria de la sesión web
if "historial" not in st.session_state:
    st.session_state.historial = [[], []]  # [0] Lista de adultos, [1] Lista de niños

# Menú desplegable para la exoneración (reemplaza al input de texto)
exonerada = st.selectbox("¿Institución exonerada?", ["No", "Sí"])

if exonerada == "Sí":
    st.success("¡Entrada Gratuita!")
else:
    # Campos numéricos para evitar errores de texto (reemplazan a int(input()))
    adulto = st.number_input("¿Cuántos adultos?", min_value=0, step=1, format="%d")
    niño = st.number_input("¿Cuántos niños?", min_value=0, step=1, format="%d")

    # Botón de registro (reemplaza el flujo del bucle while por evento táctil)
    if st.button("Registrar Entrada"):
        # Guardamos en tu estructura de listas anidadas por categorías
        st.session_state.historial[0].append(adulto)
        st.session_state.historial[1].append(niño)

        total_turno = adulto + (niño * 0.5)
        st.info(f"Total a cancelar en este turno: {total_turno}")

# Sección de estadísticas y cierre
st.markdown("---")
if st.button("Mostrar Resumen Final"):
    st.write("### 📊 Reporte General")
    st.write(f"Estructura de listas: {st.session_state.historial}")
    st.write(f"**Total acumulado de adultos:** {sum(st.session_state.historial[0])}")
    st.write(f"**Total acumulado de niños:** {sum(st.session_state.historial[1])}")
