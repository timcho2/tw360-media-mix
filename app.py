import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="TW360 미디어 믹스 시스템 이전 안내", page_icon="📢", layout="centered")

# 2. 메인 안내문
st.markdown("<h1 style='text-align: center; color: #0056b3;'>📢 시스템 이전 안내</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #333;'>TW360 미디어 믹스 자동 생성기가<br>더욱 안전한 사내 전용 서버로 이전되었습니다.</h3>", unsafe_allow_html=True)

st.write("---")

# 3. 새로운 링크 안내
st.warning("⚠️ **보안 강화를 위해 기존 링크는 더 이상 사용되지 않습니다.**\n\n아래 버튼을 눌러 새로운 링크로 접속하신 후, 브라우저 즐겨찾기(북마크)를 꼭 업데이트해 주세요!")

# 4. 새 링크 버튼
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px; margin-bottom: 30px;'>
        <a href='https://mix-private.onrender.com/' target='_blank' style='background-color: #0056b3; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; font-weight: bold; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            👉 새로운 TW360 시스템으로 이동하기
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.info("💡 기타 접속 관련 문의: Tim")