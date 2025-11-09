import streamlit as st

def init_page() -> None:
    st.set_page_config(
        page_title="My Streamlit App",
        page_icon=""
    )

def main() -> None:
    init_page()

    st.write("Hello, Streamlit!")

    st.markdown(
        """
        # AIチャットアプリへようこそ！
        
        このアプリは、Google Geminiモデルを使用してユーザーと対話します。
        サイドバーからオプションを選択し、チャットを開始してください。
        """
    )

if __name__ == "__main__":
    main()