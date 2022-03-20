import streamlit as st
import requests
import pandas as pd


def main():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Improved Musinsa FAQ.",
        page_icon=None,
    )
    st.title("Improved Musinsa FAQ")
    
    ex_names = [
        """ 이사를 가게되면 배송지는 어떻게 하나요? """,
        """ 제가 산 상품이 모조품인것 같아요. """
        ]
    example = st.selectbox("무신사 FAQ에 궁금한 내용을 여기에서 클릭할 수 있어요.", ex_names)
    
    user_input = st.text_area(
        "무신사 FAQ에 묻고 싶은 내용을 적어보세요!", example[0], max_chars=2000, height=150,
    )
    
    try:
        rec = ex_names.index(user_input)
    except ValueError:
        rec = 0
        
    response = None
    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="질문해보기!")
        
        if submit_button:
            payload = {
                "requested_sentence": user_input,
            }
            headers = {'Content-Type': 'application/json; charset=utf-8'}

            
            resp = requests.get("http://localhost:9999/search_knn/async_vector_search", params=payload, headers=headers)
            
            responsed_sentences = dict(resp.json())["query_result"]
            
            rst_df = pd.DataFrame.from_dict(responsed_sentences)
            st.write("FAQ Query Result.")
            st.table(rst_df)
            
    
    st.text("from junwoo.kim")


if __name__ == "__main__":
    main()
