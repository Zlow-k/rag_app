import streamlit as st

ai_list = ["件名に案件名", "宛名の有無", "敬称の統一", "署名の電話番号"]
if "ai_list" not in st.session_state:
    st.session_state.ai_list = ai_list

with st.form("review_form"):
    checked_ids = []
    for i, item in enumerate(st.session_state.ai_list):
        if st.checkbox(item, key=f"chk_{i}"):
            checked_ids.append(i)

    common_note = st.text_area("修正の指示（まとめて）", placeholder="例）2を削除、3は『様』に統一")
    submitted = st.form_submit_button("送信")

if submitted:
    payload = {
        "targets": [st.session_state.ai_list[i] for i in checked_ids],
        "instruction": common_note
    }
    st.write("送信ペイロード:", payload)
    # call_ai(payload)
