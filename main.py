import streamlit as st
import math

# 페이지 설정
st.set_page_config(
    page_title="다기능 계산기",
    page_icon="🧮",
    layout="centered"
)

# 제목
st.title("🧮 다기능 계산기")
st.markdown("---")

# 사이드바에 계산 모드 선택
mode = st.sidebar.selectbox(
    "계산 모드 선택",
    ["사칙연산", "모듈러 연산", "지수 연산", "로그 연산"]
)

# 계산 기록을 세션 상태에 저장
if 'history' not in st.session_state:
    st.session_state.history = []

# 사칙연산
if mode == "사칙연산":
    st.header("📐 사칙연산")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        num1 = st.number_input("첫 번째 숫자", value=0.0, format="%.2f")
    
    with col2:
        operation = st.selectbox("연산자", ["+", "-", "×", "÷"])
    
    with col3:
        num2 = st.number_input("두 번째 숫자", value=0.0, format="%.2f")
    
    if st.button("계산하기", type="primary"):
        try:
            if operation == "+":
                result = num1 + num2
                st.success(f"결과: {num1} + {num2} = {result}")
            elif operation == "-":
                result = num1 - num2
                st.success(f"결과: {num1} - {num2} = {result}")
            elif operation == "×":
                result = num1 * num2
                st.success(f"결과: {num1} × {num2} = {result}")
            elif operation == "÷":
                if num2 == 0:
                    st.error("오류: 0으로 나눌 수 없습니다!")
                else:
                    result = num1 / num2
                    st.success(f"결과: {num1} ÷ {num2} = {result}")
            
            # 계산 기록 저장
            if 'result' in locals():
                st.session_state.history.append(f"{num1} {operation} {num2} = {result}")
        except Exception as e:
            st.error(f"계산 중 오류 발생: {e}")

# 모듈러 연산
elif mode == "모듈러 연산":
    st.header("🔄 모듈러 연산")
    st.write("a mod n 형태의 나머지 연산을 수행합니다.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        a = st.number_input("피제수 (a)", value=10, step=1, format="%d")
    
    with col2:
        n = st.number_input("제수 (n)", value=3, step=1, format="%d")
    
    if st.button("계산하기", type="primary"):
        try:
            if n == 0:
                st.error("오류: 0으로 나눌 수 없습니다!")
            else:
                result = a % n
                quotient = a // n
                st.success(f"결과: {a} mod {n} = {result}")
                st.info(f"몫: {quotient}, 나머지: {result}")
                
                # 계산 기록 저장
                st.session_state.history.append(f"{a} mod {n} = {result}")
        except Exception as e:
            st.error(f"계산 중 오류 발생: {e}")

# 지수 연산
elif mode == "지수 연산":
    st.header("📈 지수 연산")
    st.write("밑^지수 형태의 거듭제곱을 계산합니다.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        base = st.number_input("밑 (base)", value=2.0, format="%.2f")
    
    with col2:
        exponent = st.number_input("지수 (exponent)", value=3.0, format="%.2f")
    
    if st.button("계산하기", type="primary"):
        try:
            result = math.pow(base, exponent)
            st.success(f"결과: {base}^{exponent} = {result:,.2f}")
            
            # 특수한 경우 추가 정보 제공
            if base == 2:
                st.info(f"참고: 2^{exponent} = {result:,.0f}")
            elif base == 10:
                st.info(f"참고: 10^{exponent} = {result:,.0f}")
            
            # 계산 기록 저장
            st.session_state.history.append(f"{base}^{exponent} = {result:,.2f}")
        except Exception as e:
            st.error(f"계산 중 오류 발생: {e}")

# 로그 연산
elif mode == "로그 연산":
    st.header("📉 로그 연산")
    
    log_type = st.radio("로그 유형 선택", ["상용로그 (log₁₀)", "자연로그 (ln)", "임의의 밑 로그"])
    
    if log_type == "상용로그 (log₁₀)":
        x = st.number_input("진수 (x)", value=100.0, min_value=0.0001, format="%.4f")
        
        if st.button("계산하기", type="primary"):
            try:
                result = math.log10(x)
                st.success(f"결과: log₁₀({x}) = {result:.6f}")
                st.info(f"검증: 10^{result:.6f} ≈ {10**result:.2f}")
                
                # 계산 기록 저장
                st.session_state.history.append(f"log₁₀({x}) = {result:.6f}")
            except Exception as e:
                st.error(f"계산 중 오류 발생: {e}")
    
    elif log_type == "자연로그 (ln)":
        x = st.number_input("진수 (x)", value=math.e, min_value=0.0001, format="%.4f")
        
        if st.button("계산하기", type="primary"):
            try:
                result = math.log(x)
                st.success(f"결과: ln({x}) = {result:.6f}")
                st.info(f"검증: e^{result:.6f} ≈ {math.e**result:.2f}")
                
                # 계산 기록 저장
                st.session_state.history.append(f"ln({x}) = {result:.6f}")
            except Exception as e:
                st.error(f"계산 중 오류 발생: {e}")
    
    else:  # 임의의 밑 로그
        col1, col2 = st.columns(2)
        
        with col1:
            base = st.number_input("밑 (base)", value=2.0, min_value=0.0001, format="%.4f")
        
        with col2:
            x = st.number_input("진수 (x)", value=8.0, min_value=0.0001, format="%.4f")
        
        if st.button("계산하기", type="primary"):
            try:
                if base == 1:
                    st.error("오류: 밑이 1일 수 없습니다!")
                else:
                    result = math.log(x, base)
                    st.success(f"결과: log{base}({x}) = {result:.6f}")
                    st.info(f"검증: {base}^{result:.6f} ≈ {base**result:.2f}")
                    
                    # 계산 기록 저장
                    st.session_state.history.append(f"log{base}({x}) = {result:.6f}")
            except Exception as e:
                st.error(f"계산 중 오류 발생: {e}")

# 계산 기록 표시
st.markdown("---")
st.subheader("📜 계산 기록")

if st.session_state.history:
    # 최근 계산이 위에 오도록 역순으로 표시
    for i, calc in enumerate(reversed(st.session_state.history[-10:]), 1):
        st.text(f"{i}. {calc}")
    
    # 기록 삭제 버튼
    if st.button("기록 삭제", type="secondary"):
        st.session_state.history = []
        st.rerun()
else:
    st.info("아직 계산 기록이 없습니다.")

# 푸터
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>🧮 다기능 계산기 v1.0 | Made with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
