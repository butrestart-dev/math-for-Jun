import streamlit as st
import random

# --- 🎨 디자인 & CSS 설정 (귀여운 테마) ---
def apply_custom_style():
    st.markdown("""
    <style>
    /* 전체 배경: 귀여운 파스텔 그라데이션 */
    .stApp {
        background: linear-gradient(to bottom, #E0F7FA, #FCE4EC);
        font-family: 'Comic Sans MS', 'Jua', sans-serif;
    }
    
    /* 제목 스타일 */
    h1 {
        color: #FF4081;
        text-shadow: 2px 2px #FFFFFF;
        font-family: 'Jua', sans-serif;
    }
    
    /* 버튼 스타일: 둥글고 젤리 같은 느낌 */
    .stButton>button {
        background-color: #FFD54F;
        color: #5D4037;
        border-radius: 20px;
        border: 3px solid #FFECB3;
        font-weight: bold;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FFCA28;
        transform: scale(1.05);
    }
    
    /* 정답/오답 메시지 박스 */
    .stAlert {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 📚 데이터: 단원별 개념 설명 & 문제 ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

# 개념 설명 데이터
CONCEPTS = {
    1: """
    ### 🍰 분수의 나눗셈, 어렵지 않아요!
    
    **1. (자연수) ÷ (자연수)**
    * 피자 1판을 3명이 나눠 먹으면? 
    * $$ 1 \div 3 = \\frac{1}{3} $$
    * 앞의 숫자는 **분자**, 뒤의 숫자는 **분모**로 슝!
    
    **2. (분수) ÷ (자연수)**
    * "나누기"는 "곱하기 분의 1"로 변신할 수 있어요.
    * $$ \\frac{2}{3} \div 4 = \\frac{2}{3} \\times \\frac{1}{4} = \\frac{2}{12} $$
    * 약분도 잊지 마세요!
    """,
    
    2: """
    ### 📦 각기둥과 각뿔 친구들
    
    **1. 각기둥이 뭐예요?**
    * 위와 아래가 똑같은 모양(합동)이고 평행한 기둥 모양이에요.
    * 옆면은 모두 **직사각형** 모양입니다.
    
    **2. 각뿔이 뭐예요?**
    * 밑에는 다각형, 위는 뾰족한 뿔 모양이에요.
    * 옆면은 모두 **삼각형** 모양입니다.
    
    **💡 꿀팁 공식 (밑면의 변의 수 = N)**
    * **각기둥 모서리**: $$ N \\times 3 $$
    * **각기둥 꼭짓점**: $$ N \\times 2 $$
    """,
    
    3: """
    ### 💧 소수의 나눗셈
    
    **자연수처럼 계산하고 점만 잘 찍으면 돼요!**
    * $$ 3.6 \div 3 $$ 을 계산할 때,
    * 먼저 $$ 36 \div 3 = 12 $$ 를 계산해요.
    * 그 다음 소수점을 원래 자리만큼 콕! 찍어주면 $$ 1.2 $$ 가 됩니다.
    """,
    
    4: """
    ### 🍎 비와 비율
    
    **두 수를 비교할 때 사용해요.**
    * 사과 3개와 배 2개가 있을 때, 사과 대 배의 비는?
    * **3 : 2** 라고 씁니다.
    * 읽는 법: "3 대 2", "3의 2에 대한 비", "2에 대한 3의 비"
    """
}

# --- ⚙️ 기능 함수 ---
def check_answer(user_input, correct_val_str):
    """정답 확인 (숫자/문자 모두 처리)"""
    try:
        # 분수/소수 비교를 위해 수치로 변환
        if '/' in str(correct_val_str):
            n, d = map(float, str(correct_val_str).split('/'))
            ans_val = n / d
        else:
            ans_val = float(correct_val_str)

        user_input = user_input.strip()
        if user_input == "": return False
        
        if '/' in user_input:
            n, d = map(float, user_input.split('/'))
            user_val = n / d
        else:
            user_val = float(user_input)

        return abs(ans_val - user_val) < 0.001
    except:
        return user_input.strip() == str(correct_val_str).strip()

def generate_problem(unit_num, difficulty):
    """문제 출제 로직"""
    problem = {}
    
    if unit_num == 1: # 분수의 나눗셈
        if difficulty == '하':
            a, b = random.randint(2, 9), random.randint(2, 9)
            problem['q'] = f"몫을 분수로 나타내세요: $${a} \div {b}$$"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"자연수의 나눗셈 몫은 분수입니다. {a}가 분자, {b}가 분모가 돼요."
        else:
            ja, mo, nat = random.randint(2, 8), random.randint(3, 9), random.randint(2, 5)
            # 분자가 분모보다 작은 진분수 조건
            if ja >= mo: ja, mo = mo, ja 
            problem['q'] = f"계산해 보세요: $$\\frac{{{ja}}}{{{mo}}} \div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"나누기를 곱하기로 바꿔보세요. {ja}/{mo} × 1/{nat}"
            
    elif unit_num == 2: # 각기둥/각뿔
        shapes = [
            ('삼각기둥', 3, '기둥'), ('사각기둥', 4, '기둥'), 
            ('오각기둥', 5, '기둥'), ('육각기둥', 6, '기둥'),
            ('삼각뿔', 3, '뿔'), ('사각뿔', 4, '뿔')
        ]
        s_name, n, s_type = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        
        problem['q'] = f"**{s_name}**의 **{target}** 개수는?"
        
        if s_type == '기둥':
            if target == '모서리': ans = n * 3
            elif target == '꼭짓점': ans = n * 2
            else: ans = n + 2
        else: # 뿔
            if target == '모서리': ans = n * 2
            elif target == '꼭짓점': ans = n + 1
            else: ans = n + 1
            
        problem['a'] = str(ans)
        problem['exp'] = f"{s_name}의 밑면 변의 수는 {n}개입니다. 공식을 떠올려보세요!"

    # 3, 4단원 및 기타는 간단한 연산으로 대체 (확장 가능)
    else:
        a, b = random.randint(10, 50), random.randint(1, 9)
        problem['q'] = f"다음 나눗셈의 몫은? (소수 첫째자리까지): $${a} \div {b}$$"
        problem['a'] = f"{a/b:.1f}"
        problem['exp'] = "소수점을 잘 찍었는지 확인해보세요."

    return problem

# --- 🚀 메인 앱 ---
def main():
    st.set_page_config(page_title="초등 수학 대장", page_icon="🐣", layout="centered")
    apply_custom_style() # CSS 적용

    # 세션 상태 초기화
    if 'step' not in st.session_state: st.session_state.step = 'intro' # intro -> study -> quiz -> result
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False # 현재 문제를 풀었는지 여부

    # 사이드바 (단원 선택)
    st.sidebar.header("🚩 지도")
    for u_num, u_name in UNITS.items():
        if st.sidebar.button(u_name):
            st.session_state.current_unit = u_num
            st.session_state.step = 'study' # 단원 바꾸면 개념 설명부터
            st.rerun()

    # --- 1. 개념 설명 화면 (Study Mode) ---
    if st.session_state.step == 'intro' or st.session_state.step == 'study':
        u_name = UNITS[st.session_state.current_unit]
        st.title(f"오늘의 미션: {u_name}")
        st.markdown("---")
        
        # 개념 설명 표시
        st.markdown(CONCEPTS.get(st.session_state.current_unit, "준비 중인 단원입니다."))
        st.image("https://media.giphy.com/media/l0HlO4p8l4XQjQ1UY/giphy.gif", width=200) # 귀여운 움짤 (예시)
        
        st.markdown("---")
        st.info("준비됐나요? 아래 버튼을 누르면 퀴즈가 시작돼요!")
        
        if st.button("🚀 퀴즈 풀러 가기!", use_container_width=True):
            st.session_state.step = 'quiz'
            st.session_state.score = 0
            st.session_state.q_idx = 0
            st.session_state.current_prob = None
            st.session_state.solved = False
            st.rerun()

    # --- 2. 퀴즈 화면 (Quiz Mode) ---
    elif st.session_state.step == 'quiz':
        # 진행 상황
        total_q = 5 # 테스트용 5문제
        progress = st.session_state.q_idx / total_q
        st.progress(progress, text=f"영차영차! {st.session_state.q_idx + 1}번째 산을 넘고 있어요.")

        # 문제 생성 (없으면 새로 만듦)
        if st.session_state.current_prob is None:
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, '중')
            st.session_state.solved = False # 새 문제니까 아직 안 풂
        
        prob = st.session_state.current_prob
        
        # 문제 보여주기
        st.subheader(f"Q{st.session_state.q_idx + 1}.")
        st.markdown(f"### {prob['q']}")

        # 정답 입력 (이미 풀었으면 입력창 비활성화)
        with st.form(key='quiz_form'):
            user_val = st.text_input("정답:", disabled=st.session_state.solved)
            # 이미 풀었으면 '다음 문제', 안 풀었으면 '채점하기' 버튼 보여주기
            if st.session_state.solved:
                submit_text = "다음 문제로 넘어가기 ➡️"
            else:
                submit_text = "채점하기 ✨"
            
            submit_btn = st.form_submit_button(submit_text)

        # 버튼 클릭 시 동작
        if submit_btn:
            if not st.session_state.solved:
                # [채점 로직]
                if check_answer(user_val, prob['a']):
                    st.balloons() # 정답이면 풍선 팡팡!
                    st.success(f"와우! 정답입니다! 🎉")
                    st.session_state.score += 1 # 점수 즉시 반영
                else:
                    st.error(f"땡! 아쉽네요. 😢")
                    st.markdown(f"**정답은 {prob['a']} 입니다.**")
                    st.warning(f"설명: {prob['exp']}")
                
                st.session_state.solved = True # 풀었다고 표시
                st.rerun() # 화면 갱신해서 '다음 문제' 버튼으로 바꾸기
            
            else:
                # [다음 문제 로직]
                st.session_state.q_idx += 1
                st.session_state.current_prob = None # 문제 초기화
                st.session_state.solved = False
                
                # 다 풀었는지 확인
                if st.session_state.q_idx >= total_q:
                    st.session_state.step = 'result'
                
                st.rerun()

    # --- 3. 결과 화면 (Result Mode) ---
    elif st.session_state.step == 'result':
        total_q = 5
        final_score = st.session_state.score * (100 // total_q)
        
        st.title("🎉 학습 완료!")
        
        if final_score >= 60:
            st.markdown(f"""
            ### 🌟 대단해요! 통과했습니다!
            내 점수: **{final_score}점** ({st.session_state.score} / {total_q}개 정답)
            """)
            st.image("https://media.giphy.com/media/fxsqOYnGDpWxjBNhve/giphy.gif")
        else:
            st.markdown(f"""
            ### 🥺 조금만 더 노력해봐요!
            내 점수: **{final_score}점** ({st.session_state.score} / {total_q}개 정답)
            """)
        
        col1, col2 = st.columns(2)
        if col1.button("다시 풀기 🔄"):
            st.session_state.step = 'study'
            st.rerun()
        if col2.button("다른 단원 공부하기 📖"):
            st.session_state.step = 'intro'
            st.session_state.current_unit = 1
            st.rerun()

if __name__ == "__main__":
    main()
