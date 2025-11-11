import streamlit as st


def main() -> None:
    """Simple Streamlit app that adds two numbers.

    Inputs: two numeric values (float)
    Output: their sum
    """
    st.set_page_config(page_title="Add Numbers", page_icon="➕", layout="centered")

    st.title("Add Numbers")
    # Tiny contract:
    # - inputs: two floats via number_input
    # - output: displayed sum as float

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Number 1", value=0.0, format="%.6f")
    with col2:
        b = st.number_input("Number 2", value=0.0, format="%.6f")

    # Add button for explicit action
    if st.button("Add"):
        result = a + b
        st.success(f"Result: {result}")

    # do multipication
    if st.button("Multiply"):
        result = a * b
        st.success(f"Result: {result}")

    # Also show live preview
    st.markdown("---")
    st.write("Live preview (updates immediately):")
    st.info(f"{a} + {b} = {a + b}")
    st.info(f"{a} * {b} = {a * b}")


if __name__ == "__main__":
    main()
