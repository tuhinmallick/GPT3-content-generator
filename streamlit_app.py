import streamlit as st
import os
import openai

# CSS tweaks

# hide_expander_border = """
# <style>
# .st-bd {border-style: none;}
# </style>
# """
# 
# if st.checkbox("Remove expander border"):
#     st.markdown(hide_expander_border, unsafe_allow_html=True)
# 
# with st.expander("Click to expand"):
#     st.header("Test")


hide_expander_border = """
<style>
.st-bd {border-style: none;}
</style>

"""

st.markdown(hide_expander_border, unsafe_allow_html=True)

st.sidebar.text("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")
API_Key = st.sidebar.text_input("Enter your OpenAI API key")

if not API_Key:
    st.caption("")
    st.caption("")
    st.warning("👈 Please enter your API key")
    st.stop()

# st.button("Generate", key="4")
st.title("🧠 GPT-3 Content Generator")

openai.api_key = API_Key

with st.form("my_form"):

    with st.expander("⚙️ Settings"):

        cMargin, c1, cMargin, c2, cMargin = st.columns([0.1, 2, 0.1, 2, 0.1])

        with c1:

            st.selectbox(
                "Select your engine",
                [
                    "davinci-instruct-beta-v3",
                    "curie-instruct-beta-v2",
                    "babbage-instruct-beta",
                ],
                key="3",
                help="""

                    # Davinci-instruct-beta-v3
                    Davinci-instruct is the most capable model in the Instruct series, which is better at following instructions than the Base series. 

                    **Strengths:** Shorter and more naturally phrased prompts, complex intent, cause and effect.
                    # Curie-instruct-beta-v2
                    Curie-instruct is very capable but faster and lower cost than davinci-instruct. Part of the Instruct series is better at following instructions than the Base series. 

                    **Strengths:** Shorter and more naturally phrased prompts, language translation, complex classification, sentiment.
                    # Babbage-instruct-beta 
                    This model is part of our Instruct series, which is better at following instructions than the Base series.

                    """,
            )

        with c2:
            maxTokens = st.slider(
                "Select the number of characters",
                60,
                500,
                step=30,
                key="1",
                help="""

                # Davinci-instruct-beta-v3
                Davinci-instruct is the most capable model in the Instruct series, which is better at following instructions than the Base series. 

                **Strengths:** Shorter and more naturally phrased prompts, complex intent, cause and effect.
                # Curie-instruct-beta-v2
                Curie-instruct is very capable but faster and lower cost than davinci-instruct. Part of the Instruct series is better at following instructions than the Base series. 

                **Strengths:** Shorter and more naturally phrased prompts, language translation, complex classification, sentiment.
                # Babbage-instruct-beta 
                This model is part of our Instruct series, which is better at following instructions than the Base series.

                """,
            )

    ce, c1, cf = st.columns([0.1, 5, 0.1])
    with c1:

        text_input = st.text_input(
            "What would you like to ask?",
            key="2",
            placeholder="Make a list of great french authors of the past 100 years",
        )

        # text_input = st.text_input("text", test01, key="1", placeholder="Enter your text")
        # text_input = st.text_input(
        #    "text", "Make a list of great french authors of the past 100 years", key="1"
        # )

        response = openai.Completion.create(
            engine="davinci-instruct-beta-v3",
            max_tokens=maxTokens,
            # max_tokens=60,
            # prompt="Make a list of great french authors of the past 100 years",
            prompt=text_input,
        )

        st.text("")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    if submitted:
        # st.write("slider", slider_val, "checkbox", checkbox_val)
        output_code = response["choices"][0]["text"]
        # response
        output_code

st.stop()