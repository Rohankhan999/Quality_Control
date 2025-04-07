import streamlit as st
import plotly.graph_objects as go

# Input from user
freshness = st.slider("Enter Freshness (%)", 0, 100, 50)

# Set color and message based on freshness level
if freshness < 50:
    color = 'red'
    message = "Freshness is low!"
elif freshness == 50:
    color = 'orange'
    message = "Freshness is okay!"
else:
    color = 'green'
    message = "Good freshness!"

# Create the figure
fig = go.Figure()

# Plot the freshness level as a line
fig.add_trace(go.Scatter(
    x=[0, 100], y=[0, freshness],  # X axis from 0 to 100, Y axis representing freshness
    mode='lines+markers+text',  # Display both line and markers
    line=dict(color=color, width=6),  # Line color based on freshness
    marker=dict(size=12, color=color),  # Marker at the freshness level
    text=[None, freshness],  # Display freshness value at the end
    textposition="top center"
))

# Update layout for a cleaner look
fig.update_layout(
    title="Freshness Level",
    yaxis=dict(range=[0, 100]),  # Ensure the Y-axis is between 0 and 100
    xaxis=dict(title="Freshness %"),
    height=500,
    showlegend=False
)

# Display the plot
st.plotly_chart(fig)

# Show the freshness message with larger font size
st.markdown(f"<h2 style='color:{color};'>{message}</h2>", unsafe_allow_html=True)
