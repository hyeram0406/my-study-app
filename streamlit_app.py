import streamlit as st
from streamlit_quill import st_quill  # 에디터 도구 불러오기

# 1. 앱 설정 및 테마
st.set_page_config(page_title="임용 암기 대시보드", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F7FAF2; }
    .stButton>button { background-color: #A8D1D1; color: white; border-radius: 12px; }
    h1 { color: #4A55A2; text-align: center; }
    /* 에디터 배경색 하얗게 설정 */
    .ql-container { background-color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 교육학 & 전공 암기 노트")

# 데이터 저장소
if 'categories' not in st.session_state:
    st.session_state['categories'] = ["교육과정", "교육심리"]
if 'theory_data' not in st.session_state:
    st.session_state['theory_data'] = []

# 메뉴
menu = st.sidebar.radio("📚 대메뉴", ["교육학", "전공"])

# --- 팝업 함수 ---
@st.dialog("새로운 이론 등록", width="large")
def add_theory_popup():
    cat = st.selectbox("카테고리 선택", st.session_state['categories'])
    title = st.text_input("이론 제목")
    
    st.write("내용 작성 (상단 도구 모음으로 글자를 꾸며보세요!)")
    # 볼드, 이탤릭, 밑줄, 글자색 등을 지원하는 에디터
    content = st_quill(
        placeholder="암기할 내용을 작성하세요...",
        toolbar=["bold", "italic", "underline", "strike", {"color": []}, {"background": []}, "clean"],
        key="quill_editor"
    )
    
    if st.button("저장하기"):
        if title and content:
            st.session_state['theory_data'].append({
                "category": cat,
                "title": title,
                "content": content
            })
            st.success("저장 완료!")
            st.rerun()

# --- 메인 화면 ---
if menu == "교육학":
    st.header("📖 교육학 학습 관리")
    if st.button("➕ 새 이론 등록"):
        add_theory_popup()
    
    st.divider()
    
    st.subheader("🔍 이론 조회")
    selected_cat = st.selectbox("카테고리 선택", ["선택하세요"] + st.session_state['categories'])

    if selected_cat != "선택하세요":
        items = [i for i in st.session_state['theory_data'] if i['category'] == selected_cat]
        if not items:
            st.warning("등록된 이론이 없습니다.")
        else:
            titles = [item['title'] for item in items]
            selected_title = st.selectbox("이론 선택", ["선택하세요"] + titles)

            if selected_title != "선택하세요":
                final_item = next(item for item in items if item['title'] == selected_title)
                st.info(f"📍 {final_item['title']}")
                # 에디터로 작성된 서식(HTML)을 그대로 화면에 뿌려줌
                st.markdown(final_item['content'], unsafe_allow_html=True)
