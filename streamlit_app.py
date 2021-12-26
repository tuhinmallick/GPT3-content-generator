import streamlit as st
import os
import openai

# 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

st.set_page_config(page_title="GPT3 Content Generator", page_icon="📢")

# ----------------------Hide Streamlit footer----------------------------
hide_st_style = """

    <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

st.markdown(hide_st_style, unsafe_allow_html=True)
# --------------------------------------------------------------------


def _max_width_():
    max_width_str = f"max-width: 800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


_max_width_()


hide_expander_border = """
<style>
.st-bd {border-style: none;}
</style>

"""

st.markdown(hide_expander_border, unsafe_allow_html=True)

st.sidebar.image(
    "logo.png",
    width=310,
)

st.sidebar.caption("")
st.sidebar.caption("")

API_Key = st.sidebar.text_input("Enter your OpenAI API key")

st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.header("")
st.sidebar.header("")
st.sidebar.header("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.caption("")
st.sidebar.title("")
st.sidebar.caption("")

st.sidebar.caption(
    "Made in [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://www.charlywargnier.com/)"
)


if not API_Key:

    c30, c31, c32 = st.columns([1, 0.9, 3])

    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.info("Please enter your API key")
    st.image("arrow.png", width=150)

    st.stop()

c30, c31, c32 = st.columns([1, 0.9, 3])

openai.api_key = API_Key

st.title("")
st.title("")
st.header("")
st.subheader("")
st.header("")
st.caption("")

with st.form("my_form"):

    ce, c1, cf = st.columns([0.1, 5, 0.1])
    with c1:

        text_input = st.text_input(
            "What would you like to ask?",
            key="2",
            # placeholder="How do you start a business in the UK",
            placeholder="Make a list of great French authors of the past 100 years",
        )

    with st.expander("⚙️ Advanced Settings"):

        cMargin, c1, cMargin, c2, cMargin = st.columns([0.1, 2, 0.1, 2, 0.1])

        with c1:

            st.selectbox(
                "Select your GPT3 engine",
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
                1500,
                value=1200,
                step=100,
                key="1",
                help="""

                Select the number of characters

                """,
            )

        response = openai.Completion.create(
            engine="davinci-instruct-beta-v3",
            max_tokens=maxTokens,
            # max_tokens=60,
            # prompt="Make a list of great french authors of the past 100 years",
            # prompt="Make a list of great French authors of the past 100 years",
            prompt=text_input,
        )

    st.text("")

    submitted = st.form_submit_button(
        "✨ Let's go!", help="Generate text from your instructions"
    )

if submitted:
    # st.text("")
    # st.header("👇 Output")
    st.text("")
    output_code = response["choices"][0]["text"]
    output_code

    # st.download_button("label", output_code, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None)

    st.text("")
    st.download_button(
        "Download output",
        output_code,
        file_name="GPT_output.txt",
        help="Download the output",
    )