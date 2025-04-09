import streamlit as st
import plotly.graph_objects as go


freshness_day = st.number_input("Enter Freshness Day (1-5)", min_value=1, max_value=5, step=1)


if freshness_day  == 1:
    freshness_value = 100
    color = 'green'
    message = "Excellent freshness detected! The product is in optimal condition and safe for consumption."
elif freshness_day  == 2:
    freshness_value = 80
    color = 'palegreen'
    message = "good freshness detected! The product is in optimal condition and safe for consumption."
    
   
elif freshness_day == 3:
    freshness_value = 75
    color = 'yellow'
    message = "Freshness is reducing. The product is still safe to consume but should be used soon."
elif freshness_day == 4:
    freshness_value = 50
    color = 'orange'
    message = "Freshness is low. Caution advised — check texture and smell before using the product."
else:  
    freshness_value = 25
    color = 'red'
    message = "Warning! The product has lost its freshness and may be harmful. Do not consume."


fig = go.Figure()


fig.add_trace(go.Scatter(
    x=[0, 100], y=[0, freshness_value],
    mode='lines+markers+text',
    line=dict(color=color, width=6),
    marker=dict(size=12, color=color),
    text=[None, f"{freshness_value}%"],
    textposition="top center"
))


fig.update_layout(
    title="Freshness Level",
    yaxis=dict(range=[0, 100]),
    xaxis=dict(title="Freshness %"),
    height=500,
    showlegend=False
)


st.plotly_chart(fig)


st.markdown(f"<h3 style='color:{color};'>{message}</h3>", unsafe_allow_html=True)
