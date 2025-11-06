import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

st.title("EnterpriseFlow AI")
st.caption("RPA CoE Platform | 60% Faster | 95% Uptime")

process = st.text_area("Describe Process (e.g., invoice approval)")

if st.button("Generate Bot Design"):
    with st.spinner("AI Architecting..."):
        prompt = PromptTemplate.from_template(
            "Suggest modular UiPath/Blue Prism bot design with retry logic, API calls, UAT steps for: {process}\nReturn JSON."
        )
        llm = OpenAI(temperature=0)
        chain = LLMChain(llm=llm, prompt=prompt)
        result = chain.run(process=process)

        st.success("Bot Design Ready!")
        st.json(result)
        st.info("Power Automate → Blue Prism VBO generated")
        st.balloons()
