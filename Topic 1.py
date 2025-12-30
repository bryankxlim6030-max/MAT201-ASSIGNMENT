import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("MAT201: Function Visualization App")
st.write("This app visualizes functions of two variables, z = f(x, y).")

# User Input for the function
func_input = st.sidebar.text_input("Enter your function (use 'np' for math functions):", "np.sin(np.sqrt(x**2 + y**2))")

# Sliders for range
x_range = st.sidebar.slider("X range", -10.0, 10.0, (-5.0, 5.0))
y_range = st.sidebar.slider("Y range", -10.0, 10.0, (-5.0, 5.0))

# Create the data
x = np.linspace(x_range[0], x_range[1], 100)
y = np.linspace(y_range[0], y_range[1], 100)
X, Y = np.meshgrid(x, y)

try:
    # Evaluate the function
    Z = eval(func_input.replace('x', 'X').replace('y', 'Y'))
    
    # 3D Plotly Surface
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
    fig.update_layout(title='3D Surface Plot', autosize=False,
                      width=700, height=700,
                      margin=dict(l=65, r=50, b=65, t=90))
    
    st.plotly_chart(fig)
    
except Exception as e:
    st.error(f"Error in formula: {e}. Use 'x' and 'y' as variables.")

