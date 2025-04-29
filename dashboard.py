import streamlit as st

# Set page config
st.set_page_config(page_title="My Experiments Dashboard", layout="wide")

# Main title
st.title("🚀 My Container Orchestration & Automation Experiments Dashboard")
st.subheader("By Rakshan Sharma")

st.markdown("---")

# Sidebar Navigation
st.sidebar.title("Navigation")
exp = st.sidebar.radio("Go to Experiment:", [f"Experiment {i}" for i in range(1, 11)])

# Function to display experiment
def show_experiment(exp_num):
    st.header(f"📄 Experiment {exp_num}")
    st.write(f"**Description:** This is a brief overview of Experiment {exp_num}.")
    
    # Display image if available
    img_path = f"images/exp{exp_num}.png"
    try:
        st.image(img_path, caption=f"Experiment {exp_num} Snapshot", use_column_width=True)
    except Exception as e:
        st.warning("No image available for this experiment yet!")

    # Allow download/view of summary if available
    summary_path = f"experiments/exp{exp_num}_summary.pdf"
    try:
        with open(summary_path, "rb") as file:
            btn = st.download_button(
                label=f"📥 Download Experiment {exp_num} Summary",
                data=file,
                file_name=f"exp{exp_num}_summary.pdf",
                mime="application/pdf"
            )
    except Exception:
        st.info("Summary not uploaded yet for this experiment.")

# Display based on sidebar selection
exp_num = int(exp.split()[-1])
show_experiment(exp_num)

# Footer
st.markdown("---")
st.write("Made with ❤️ using [Streamlit](https://streamlit.io/)")

