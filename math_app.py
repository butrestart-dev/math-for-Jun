import streamlit as st
import random

# --- 🎨 디자인 & CSS 설정 (가독성 UP + 오류 해결) ---
def apply_custom_style():
    st.markdown("""
    <style>
    /* 1. 배경: 너무 하얗지 않은 따뜻한 크림색 (눈이 편안함) */
    .stApp {
        background-color: #FFF9C4; 
    }
    
    /* 2. 모든 글씨: 진한 흑갈색으로 고정 (가독성 확보) */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #3E2723 !important;
        font-family: 'Jua', 'Comic Sans MS', sans-serif;
    }
    
    /* 제목 강조 */
    h1 {
        text-shadow: 2px 2px #FFEB3B;
    }
    
    /* 3. 버튼: 눈에 확 띄는 귤색 */
    .stButton>button {
        background-color: #FF9800;
        color: white !important;
        border-radius: 15px;
        border: none;
        padding: 10px 20px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #F57C00;
        transform: scale(1.05);
    }
    
    /* 입력창 배경을 흰색으로 해서 글씨 잘 보이게 */
    .stTextInput>div>div>input {
        background-color: #FFFFFF;
        color: #000000 !important;
    }
    
    /* 설명 박스 (Info) 스타일 변경 */
    .stAlert {
        background-color: #FFFFFF;
        border: 2px solid #FF9800;
        color: #3E2723;
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

# 개념 설명 (이모지 활용하여 깨짐 방지)
CONCEPTS = {
    1: """
    ### 🍰 분수의 나눗셈 핵심 콕콕!
    
    **1. (자연수) ÷ (자연수)**
    * 피자 1판을 3명이 나누면? $$ 1 \div 3 = \\frac{1}{3} $$
    * 앞 숫자는 **위(분자)**로, 뒤 숫자는 **아래(분모)**로!
    
    **2. (분수) ÷ (자연수)**
    * 나누기는 **'곱하기 분의 1'**로 변신!
    * $$ \\frac{2}{3} \div 4 = \\frac{2}{3} \\times \\frac{1}{4} = \\frac{2}{12} $$
    """,
    
    2: """
    ### 📦 각기둥과 각뿔 친구들
    
    **1. 각기둥** (위아래가 똑같은 기둥)
    * 밑면 모양에 따라 이름이 정해져요.
    * 옆면은 모두 **직사각형**!
    
    **2. 각뿔** (위가 뾰족한 뿔)
    * 옆면은 모두 **삼각형**!
    
    **💡 공식 암기 (밑면 변의 수 = N)**
    * 각기둥 모서리: $$ N \\times 3 $$
    * 각기둥 꼭짓점: $$ N \\times 2 $$
    """,
    
    3: """
    ### 💧 소수의 나눗셈
    
    **자연수처럼 계산하고 점 찍기!**
    * $$ 3.6 \div 3 $$ 
    * ① $$ 36 \div 3 = 12 $$ (점 없다고 생각하기)
    * ② 원래 자리에 점 콕! $$ \\rightarrow 1.2 $$
    """,
    
    4: """
    ### 🍎 비와 비율
    
    **비교할 때 쓰는 말**
    * 사과 3개 : 배 2개
    * 기호로 쓰면? **3 : 2**
    * 읽을 때: "3 대 2", "2에 대한 3의 비"
    """
}

# --- ⚙️ 기능 함수 ---
def check_answer(user_input, correct_val_str):
    try:
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
    problem = {}
    
    if unit_num == 1:
        if difficulty == '하':
            a, b = random.randint(2, 9), random.randint(2, 9)
            problem['q'] = f"몫을 분수로 나타내세요: $${a} \div {b}$$"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"{a} 나누기 {b}는 {a}/{b} 입니다."
        else:
            ja, mo, nat = random.randint(2, 8), random.randint(3, 9), random.randint(2, 5)
            if ja >= mo: ja, mo = mo, ja 
            problem['q'] = f"계산해 보세요: $$\\frac{{{ja}}}{{{mo}}} \div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"나누기를 곱하기로 바꿔보세요. {ja}/{mo} × 1/{nat}"
            
    elif unit_num == 2:
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
        else:
            if target == '모서리': ans = n * 2
            elif target == '꼭짓점': ans = n + 1
            else: ans = n + 1
            
        problem['a'] = str(ans)
        problem['exp'] = f"{s_name}의 밑면 변의 수는 {n}개입니다."

    else:
        a, b = random.randint(10, 50), random.randint(1, 9)
        problem['q'] = f"다음 나눗셈의 몫은? (소수 첫째자리까지): $${a} \div {b}$$"
        problem['a'] = f"{a/b:.1f}"
        problem['exp'] = "소수점을 잘 찍었는지 확인해보세요."

    return problem

# --- 🚀 메인 앱 ---
def main():
    st.set_page_config(page_title="초등 수학 대장", page_icon="🐣", layout="centered")
    apply_custom_style()

    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False

    # 사이드바
    st.sidebar.header("🚩 지도")
    for u_num, u_name in UNITS.items():
        if st.sidebar.button(u_name):
            st.session_state.current_unit = u_num
            st.session_state.step = 'study'
            st.rerun()

    # [1] 개념 설명
    if st.session_state.step == 'intro' or st.session_state.step == 'study':
        u_name = UNITS[st.session_state.current_unit]
        st.title(f"오늘의 미션: {u_name}")
        st.markdown("---")
        
        # 개념 설명 텍스트
        st.markdown(CONCEPTS.get(st.session_state.current_unit, "준비 중인 단원입니다."))
        
        # 깨지는 외부 이미지 대신 대왕 이모지 사용
        st.markdown("<h1 style='text-align: center; font-size: 80px;'>👨‍🏫 👩‍🏫</h1>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.info("준비됐나요? 아래 버튼을 누르면 퀴즈가 시작돼요!")
        
        if st.button("🚀 퀴즈 풀러 가기!", use_container_width=True):
            st.session_state.step = 'quiz'
            st.session_state.score = 0
            st.session_state.q_idx = 0
            st.session_state.current_prob = None
            st.session_state.solved = False
            st.rerun()

    # [2] 퀴즈
    elif st.session_state.step == 'quiz':
        total_q = 5
        progress = st.session_state.q_idx / total_q
        st.progress(progress, text=f"문제 {st.session_state.q_idx + 1} / {total_q}")

        if st.session_state.current_prob is None:
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, '중')
            st.session_state.solved = False
        
        prob = st.session_state.current_prob
        
        st.subheader(f"Q{st.session_state.q_idx + 1}.")
        st.markdown(f"### {prob['q']}")

        with st.form(key='quiz_form'):
            user_val = st.text_input("정답:", disabled=st.session_state.solved)
            submit_text = "다음 문제로 넘어가기 ➡️" if st.session_state.solved else "채점하기 ✨"
            submit_btn = st.form_submit_button(submit_text)

        if submit_btn:
            if not st.session_state.solved:
                if check_answer(user_val, prob['a']):
                    st.balloons()
                    st.success(f"정답입니다! 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"땡! 틀렸어요. 😢")
                    st.markdown(f"**정답: {prob['a']}**")
                    st.warning(f"설명: {prob['exp']}")
                
                st.session_state.solved = True
                st.rerun()
            else:
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                
                if st.session_state.q_idx >= total_q:
                    st.session_state.step = 'result'
                st.rerun()

    # [3] 결과
    elif st.session_state.step == 'result':
        total_q = 5
        final_score = st.session_state.score * (100 // total_q)
        
        st.title("🎉 학습 완료!")
        st.markdown(f"### 내 점수는: **{final_score}점**")
        
        # 외부 이미지 대신 이모지 사용
        if final_score >= 60:
            st.markdown("<div style='text-align: center; font-size: 100px;'>🏆</div>", unsafe_allow_html=True)
            st.success("참 잘했어요! 다음 단원으로 가볼까요?")
        else:
            st.markdown("<div style='text-align: center; font-size: 100px;'>💪</div>", unsafe_allow_html=True)
            st.error("조금 더 연습해볼까요? 화이팅!")
        
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
