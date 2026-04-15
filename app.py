import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="오승택 포트폴리오 대시보드", layout="wide")

# 1. 데이터 정의 (이력서 내용 전체)
resume_data = {
    "name": "오승택",
    "role": "사용자 중심의 프론트엔드 개발자",
    "contact": "010-3468-3496 | tmdxor0102@naver.com",
    "skills": {
        "Frontend": ["HTML5", "CSS3", "JavaScript", "TypeScript", "React", "Next.js", "SASS", "Jquery"],
        "Backend/DB": ["PHP", "ASP.NET", "C#", "Codeigniter", "MSSQL", "Oracle", "python"],
        "AI/Tools": ["Gemini", "Supabase", "Git", "Figma", "Postman"]
    },
    "experience": [
        {"회사": "퍼플스", "직급": "대리(팀장)", "기간": "2025.05-현재", "개월": 11},
        {"회사": "양재아이티", "직급": "사원", "기간": "2022.09-2024.09", "개월": 25},
        {"회사": "티벨", "직급": "사원", "기간": "2022.01-2022.08", "개월": 8},
        {"회사": "트리플앤", "직급": "인턴", "기간": "2020.12-2021.10", "개월": 11}
    ]
}

# 사이드바 - 인적사항 및 링크
st.sidebar.title(resume_data["name"])
st.sidebar.write(resume_data["role"])
st.sidebar.info(resume_data["contact"])
st.sidebar.markdown("[GitHub](https://github.com/ost0102)")
st.sidebar.markdown("[Portfolio](https://git-dash-dun.vercel.app/)")

# 메인 화면
st.title("🚀 Interactive Resume Dashboard")

# 섹션 1: 경력 타임라인 (Plotly 차트)
st.header("📍 Career Timeline")
df_exp = pd.DataFrame(resume_data["experience"])
fig = px.bar(df_exp, x="개월", y="회사", text="직급", orientation='h',
             color="개월", color_continuous_scale="Viridis",
             title="근무지별 경력 기간 (개월)")
st.plotly_chart(fig, use_container_width=True)

# 섹션 2: 기술 스택 (필터링 기능)
st.header("🛠 Tech Stacks")
category = st.selectbox("역량 카테고리를 선택하세요", list(resume_data["skills"].keys()))
st.write(f"**{category} 주요 기술:**")
st.success(", ".join(resume_data["skills"][category]))

# 섹션 3: 주요 프로젝트 & 상세 이력
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌟 Key Projects")
    st.markdown("""
    - **신도리코 홈페이지 외주**: GDWeb 수상, GSAP 애니메이션 구현
    - **특송 화물 Tracking 개발**: ASP.NET 기반 실시간 추적 시스템
    - **AI CRM 제작**: Gemini API 및 Supabase 활용 바이브 코딩
    """)

with col2:
    st.subheader("📝 Self Introduction")
    st.write("MBTI: **ESTP**")
    st.write("강점: 주도적인 문제 해결, 소통과 협업, 빠른 기술 습득")
    if st.button("담당자님께 드리는 한마디 보기"):
        st.balloons()
        st.write("늦게 시작한 만큼 누구보다 빠르게 성장할 준비가 되어 있습니다!")