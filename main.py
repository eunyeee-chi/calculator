import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

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
    ["사칙연산", "모듈러 연산", "지수 연산", "로그 연산", "다항함수 그래프"]
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

# 다항함수 그래프
elif mode == "다항함수 그래프":
    st.header("📊 다항함수 그래프")
    st.write("다항함수를 입력하면 인터랙티브 그래프를 그려줍니다.")
    
    # 다항함수 차수 선택
    degree = st.selectbox("다항식의 최고차수 선택", [1, 2, 3, 4, 5], index=1)
    
    st.write("**계수 입력** (높은 차수부터)")
    
    # 계수 입력
    coefficients = []
    cols = st.columns(degree + 1)
    
    for i in range(degree + 1):
        with cols[i]:
            if degree - i == 0:
                coef = st.number_input(f"상수항", value=0.0, key=f"coef_{i}")
            else:
                coef = st.number_input(f"x^{degree - i} 계수", value=1.0 if i == 0 else 0.0, key=f"coef_{i}")
            coefficients.append(coef)
    
    # 다항식 문자열 생성
    polynomial_str = ""
    for i, coef in enumerate(coefficients):
        if coef != 0:
            power = degree - i
            if polynomial_str and coef > 0:
                polynomial_str += " + "
            elif coef < 0:
                polynomial_str += " - " if polynomial_str else "-"
                coef = abs(coef)
            
            if power == 0:
                polynomial_str += f"{coef:.2f}" if coef != 1 or not polynomial_str else "1"
            elif power == 1:
                if coef == 1:
                    polynomial_str += "x"
                else:
                    polynomial_str += f"{coef:.2f}x"
            else:
                if coef == 1:
                    polynomial_str += f"x^{power}"
                else:
                    polynomial_str += f"{coef:.2f}x^{power}"
    
    if not polynomial_str:
        polynomial_str = "0"
    
    st.info(f"**다항식**: y = {polynomial_str}")
    
    # x 범위 설정
    col1, col2 = st.columns(2)
    with col1:
        x_min = st.number_input("x 최솟값", value=-10.0)
    with col2:
        x_max = st.number_input("x 최댓값", value=10.0)
    
    # 그래프 그리기
    if st.button("그래프 그리기", type="primary"):
        if x_min >= x_max:
            st.error("x 최솟값은 최댓값보다 작아야 합니다!")
        else:
            try:
                # x 값 생성 (500개 점)
                x = np.linspace(x_min, x_max, 500)
                
                # y 값 계산
                y = np.zeros_like(x)
                for i, coef in enumerate(coefficients):
                    power = degree - i
                    y += coef * (x ** power)
                
                # Plotly 인터랙티브 그래프 생성
                fig = go.Figure()
                
                # 함수 그래프 추가
                fig.add_trace(go.Scatter(
                    x=x, y=y,
                    mode='lines',
                    name=f'y = {polynomial_str}',
                    line=dict(color='blue', width=2.5),
                    hovertemplate='x: %{x:.2f}<br>y: %{y:.2f}<extra></extra>'
                ))
                
                # x축, y축 (0선) 추가
                fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.3, line_width=1)
                fig.add_vline(x=0, line_dash="dash", line_color="black", opacity=0.3, line_width=1)
                
                # 레이아웃 설정
                fig.update_layout(
                    title={
                        'text': f"다항함수: y = {polynomial_str}",
                        'x': 0.5,
                        'xanchor': 'center',
                        'font': {'size': 20}
                    },
                    xaxis_title="x",
                    yaxis_title="y",
                    showlegend=True,
                    hovermode='closest',
                    height=550,
                    template="plotly_white",
                    xaxis=dict(
                        showgrid=True,
                        gridwidth=1,
                        gridcolor='lightgray',
                        zeroline=True,
                        zerolinewidth=2,
                        zerolinecolor='black'
                    ),
                    yaxis=dict(
                        showgrid=True,
                        gridwidth=1,
                        gridcolor='lightgray',
                        zeroline=True,
                        zerolinewidth=2,
                        zerolinecolor='black'
                    )
                )
                
                # 줌, 팬 등 인터랙티브 기능 활성화
                fig.update_xaxes(fixedrange=False)
                fig.update_yaxes(fixedrange=False)
                
                # 그래프 표시
                st.plotly_chart(fig, use_container_width=True)
                
                # 함수 분석 (Expander)
                with st.expander("📈 함수 분석 보기"):
                    # y절편
                    y_intercept = coefficients[-1]
                    st.write(f"**y절편**: (0, {y_intercept:.3f})")
                    
                    # 1차 함수 분석
                    if degree == 1 and coefficients[0] != 0:
                        x_intercept = -coefficients[1] / coefficients[0]
                        st.write(f"**x절편**: ({x_intercept:.3f}, 0)")
                        slope = coefficients[0]
                        st.write(f"**기울기**: {slope:.3f}")
                    
                    # 2차 함수 분석
                    elif degree == 2:
                        a, b, c = coefficients
                        if a != 0:
                            # 판별식
                            discriminant = b**2 - 4*a*c
                            st.write(f"**판별식 D**: {discriminant:.3f}")
                            
                            # x절편 (근)
                            if discriminant > 0:
                                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                                x2 = (-b - math.sqrt(discriminant)) / (2*a)
                                st.write(f"**x절편 (두 실근)**: ({x1:.3f}, 0), ({x2:.3f}, 0)")
                            elif abs(discriminant) < 1e-10:  # 거의 0
                                x_intercept = -b / (2*a)
                                st.write(f"**x절편 (중근)**: ({x_intercept:.3f}, 0)")
                            else:
                                st.write("**x절편**: 실근이 없음 (허근)")
                            
                            # 꼭짓점
                            vertex_x = -b / (2*a)
                            vertex_y = a*vertex_x**2 + b*vertex_x + c
                            st.write(f"**꼭짓점**: ({vertex_x:.3f}, {vertex_y:.3f})")
                            
                            # 포물선 방향
                            if a > 0:
                                st.write("**포물선 방향**: 위로 볼록 (최솟값 존재)")
                            else:
                                st.write("**포물선 방향**: 아래로 볼록 (최댓값 존재)")
                    
                    # 함수값 계산기
                    st.markdown("---")
                    st.subheader("🔢 특정 점에서의 함수값")
                    x_calc = st.number_input("x 값 입력", value=0.0, key="x_calc", step=0.1)
                    y_calc = sum(coef * (x_calc ** (degree - i)) for i, coef in enumerate(coefficients))
                    st.success(f"f({x_calc:.2f}) = {y_calc:.3f}")
                
                # 계산 기록에 추가
                st.session_state.history.append(f"그래프: y = {polynomial_str}")
                
            except Exception as e:
                st.error(f"그래프 생성 중 오류 발생: {e}")

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
