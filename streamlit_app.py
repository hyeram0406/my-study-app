import streamlit as st

# 앱 제목 및 설정
st.set_page_config(page_title="임용 암기 대시보드", layout="wide")
st.title("📚 전공 & 교육학 암기 앱")

# 사이드바 메뉴
menu = st.sidebar.radio("대메뉴 선택", ["전공", "교육학"])

# 데이터 저장소 설정
if 'categories' not in st.session_state:
    st.session_state['categories'] = ["교육과정", "교육심리"]
if 'theory_data' not in st.session_state:
    st.session_state['theory_data'] = []

if menu == "교육학":
    st.header("📖 교육학 학습 관리")
    
    # 카테고리 추가
    with st.expander("카테고리 관리"):
        new_cat = st.text_input("새 카테고리 이름")
        if st.button("추가"):
            if new_cat and new_cat not in st.session_state['categories']:
                st.session_state['categories'].append(new_cat)
                st.rerun()
    
    # 이론 등록
    st.subheader("➕ 이론 등록")
    selected_cat = st.selectbox("카테고리 선택", st.session_state['categories'])
    title = st.text_input("이론 제목")
    content = st.text_area("이론 내용")
    
    if st.button("저장하기"):
        if title and content:
            st.session_state['theory_data'].append({
                "category": selected_cat,
                "title": title,
                "content": content
            })
            st.success(f"'{title}' 저장 완료!")

    # 목록 확인
    st.divider()
    st.subheader("🔍 이론 목록")
    for item in st.session_state['theory_data']:
        if item['category'] == selected_cat:
            with st.expander(item['title']):
                st.write(item['content'])
                st.button(f"'{item['title']}' 퀴즈 풀기 (준비 중)")

else:
    st.header("🎓 전공 학습 관리")
    st.info("준비 중인 기능입니다.")
