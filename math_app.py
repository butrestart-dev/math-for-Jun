import streamlit as st
import random

# --- 1. 폰트 및 스타일 설정 (깨짐 방지) ---
def apply_custom_style():
    # 구글 폰트(Jua)를 웹에서 직접 가져오는 링크 추가
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    
    /* 전체 폰트 강제 적용 */
    html, body, [class*="css"] {
        font-family: 'Jua', sans-serif !important;
    }
    
    /* 배경색: 눈이 편안한 크림색 */
    .stApp {
        background-color: #FFF9C4;
    }
    
    /* 글씨 색상: 진한 갈색 (가독성) */
    h1, h2, h3, p, div, label, span, li {
        color: #3E2723 !important;
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #FF9800;
        color: white !important;
        border-radius: 12px;
        border: none;
        padding: 10px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #F57C00;
        transform: scale(1.02);
    }
    
    /* 선택지(라디오 버튼) 텍스트 크기 */
    .stRadio label {
        font-size: 20px !important;
        background-color: #FFFFFF;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
        border: 1px solid #FFCC80;
        width: 100%;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터: 단원 및 개념 ---
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

CONCEPTS = {
    1: """
    **🍰 (자연수) ÷ (자연수)**
    * 1 ÷ 3 = 1/3 (뒤에 있는 수가 분모!)
    * 5 ÷ 4 = 5/4 = 1과 1/4 (가분수는 대분수로)
    
    **🍰 (분수) ÷ (자연수)**
    * 나누기를 **곱하기**로 바꿔요!
    * 2/3 ÷ 4  ➡  2/3 × 1/4 = 2/12 = 1/6
    """,
    
    2: """
    **📦 각기둥**
    * 위아래가 똑같은 합동이고 평행해요.
    * 옆면은 모두 **직사각형**!
    
    **📐 각뿔**
    * 바닥은 다각형, 위는 뾰족!
    * 옆면은 모두 **삼각형**!
    
    **💡 공식 (N = 밑면의 변의 수)**
    * 각기둥 모서리 = N × 3
    * 각기둥 꼭짓점 = N × 2
    """,
    
    3: """
    **💧 소수의 나눗셈 방법**
    1. 점이 없다고 생각하고 자연수처럼 계산해요.
    2. 원래 소수점 자리에 맞춰서 점을 콕! 찍어요.
    
    **예시:** 3.6 ÷ 3
    * 36 ÷ 3 = 12
    * 점 찍으면 ➡ **1.2**
    """,
    
    4: """
    **🍎 비 (Ratio)**
    * 3 : 2 (3 대 2)
    * 왼쪽이 비교하는 양, 오른쪽이 기준량
    
    **🍎 비율 (Rate)**
    * 비를 분수로 나타낸 것
    * 3 : 2 ➡ 3/2 (또는 1.5)
    """
}

# --- 3. 함수: 문제 생성 및 정답 확인 ---
def check_answer(user_input, correct_val):
    try:
        user_str = str(user_input).strip().replace(" ", "")
        correct_str = str(correct_val).strip().replace(" ", "")
        
        if user_str == correct_str: return True
        
        # 수치 비교
        if '/' in str(correct_val):
            n, d = map(float, str(correct_val).split('/'))
            ans_val = n / d
        else:
            ans_val = float(correct_val)

        if '/' in user_str:
            n, d = map(float, user_str.split('/'))
            user_val = n / d
        else:
            user_val = float(user_str)
            
        return abs(ans_val - user_val) < 0.001
    except:
        return False

def generate_problem(unit_num, difficulty):
    problem = {}
    problem['unit'] = unit_num
    q_type = 'obj' if (random.random() > 0.5 or unit_num == 2) else 'subj'
    problem['type'] = q_type
    
    # [1단원]
    if unit_num == 1:
        if difficulty == '하':
            a, b = random.randint(1, 9), random.randint(2, 9)
            if a == b: b += 1
            problem['q'] = f"몫을 분수로 나타내면? $${a} \div {b}$$"
            problem['a'] = f"{a}/{b}"
            problem['exp'] = f"{a} 나누기 {b}는 {a}/{b} 입니다."
        else:
            ja, mo = random.randint(1, 9), random.randint(2, 9)
            nat = random.randint(2, 5)
            problem['q'] = f"계산하시오: $$\\frac{{{ja}}}{{{mo}}} \div {nat}$$"
            problem['a'] = f"{ja}/{mo*nat}"
            problem['exp'] = f"곱셈으로 변신! {ja}/{mo} × 1/{nat}"
            
        if q_type == 'obj':
            opts = [problem['a'], f"{b}/{a}", f"{a+1}/{b}", f"{a}/{b+1}"]
            random.shuffle(opts)
            problem['options'] = opts

    # [2단원]
    elif unit_num == 2:
        shapes = [('삼각기둥',3), ('사각기둥',4), ('오각기둥',5), ('삼각뿔',3), ('사각뿔',4)]
        name, n = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        is_prism = '기둥' in name
        
        problem['q'] = f"**{name}**의 **{target}** 수는?"
        
        if is_prism:
            ans = n*3 if target=='모서리' else (n*2 if target=='꼭짓점' else n+2)
        else:
            ans = n*2 if target=='모서리' else n+1
            
        problem['a'] = str(ans)
        problem['exp'] = f"{name}의 밑면 변의 수는 {n}개입니다."
        
        if q_type == 'obj':
            opts = list(set([str(ans), str(ans+1), str(ans-1), str(ans*2)]))
            while len(opts) < 4: opts.append(str(random.randint(5, 20)))
            random.shuffle(opts)
            problem['options'] = opts

    # [3단원]
    elif unit_num == 3:
        d = random.randint(2, 5)
        q = random.randint(11, 49)
        dividend = q * d # 몫이 자연수가 되도록
        problem['q'] = f"계산하시오: $${dividend/10} \div {d}$$"
        problem['a'] = str(q/10)
        problem['exp'] = f"자연수 {dividend}÷{d}={q} 입니다. 소수점을 찍으세요."
        
        if q_type == 'obj':
            opts = [str(q/10), str(q), str(q/100), str(q+1)]
            random.shuffle(opts)
            problem['options'] = opts

    # [4단원]
    elif unit_num == 4:
        a, b = random.randint(2, 9), random.randint(2, 9)
        problem['q'] = f"비 {a}:{b} 에서 **전항**(비교하는 양)은?"
        problem['a'] = str(a)
        problem['exp'] = "왼쪽이 전항, 오른쪽이 후항입니다."
        if q_type == 'obj':
            problem['options'] = [str(a), str(b), str(a+b), "없음"]
            random.shuffle(problem['options'])

    return problem

# --- 4. 메인 앱 ---
def main():
    st.set_page_config(page_title="초등 수학 짱", page_icon="💯", layout="wide")
    apply_custom_style()

    # [상태 초기화]
    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False
    if 'wrong_notes' not in st.session_state: st.session_state.wrong_notes = []
    
    # 단원 선택 상태 (기본값 1)
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1

    # ================= 사이드바 (메뉴) =================
    with st.sidebar:
        st.title("🚩 메뉴")
        
        # 1. 단원 선택 (라디오 버튼)
        st.markdown("### 공부할 단원")
        selected_unit_label = st.radio(
            "단원을 선택하세요:",
            list(UNITS.values()),
            index=st.session_state.current_unit - 1
        )
        
        # 선택한 단원 번호 찾기
        new_unit = [k for k, v in UNITS.items() if v == selected_unit_label][0]
        
        # 단원이 바뀌면 학습 모드로 리셋
        if new_unit != st.session_state.current_unit:
            st.session_state.current_unit = new_unit
            st.session_state.step = 'intro'
            st.session_state.score = 0
            st.session_state.q_idx = 0
            st.rerun()

        st.markdown("---")
        
        # 2. 오답노트 메뉴
        wrong_cnt = len(st.session_state.wrong_notes)
        if wrong_cnt > 0:
            st.error(f"❌ 오답 노트: {wrong_cnt}개")
            if st.button("📝 오답 풀러 가기"):
                st.session_state.step = 'wrong_note_view'
                st.rerun()
        else:
            st.info("오답 노트가 비어있어요. 👍")
            
        st.markdown("---")
        if st.button("🏠 처음 화면으로"):
            st.session_state.step = 'intro'
            st.session_state.score = 0
            st.session_state.q_idx = 0
            st.rerun()

    # ================= 메인 화면 =================
    
    # [화면 1] 개념 학습 (Intro)
    if st.session_state.step == 'intro':
        u_name = UNITS[st.session_state.current_unit]
        st.title(f"오늘의 공부: {u_name}")
        
        # 개념 설명 박스 (st.info 사용으로 깨짐 방지)
        st.info(CONCEPTS[st.session_state.current_unit])
        
        st.markdown("### 준비됐나요? 👇")
        if st.button("🚀 퀴즈 풀기 시작!", use_container_width=True):
            st.session_state.step = 'quiz'
            st.session_state.q_idx = 0
            st.session_state.score = 0
            st.session_state.current_prob = None
            st.session_state.solved = False
            st.rerun()

    # [화면 2] 퀴즈 (Quiz)
    elif st.session_state.step == 'quiz':
        total_q = 5
        st.markdown(f"**{UNITS[st.session_state.current_unit]}** (문제 {st.session_state.q_idx + 1}/{total_q})")
        st.progress((st.session_state.q_idx) / total_q)

        # 문제 생성
        if st.session_state.current_prob is None:
            diff = random.choice(['하', '중', '상'])
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, diff)
            st.session_state.solved = False
        
        prob = st.session_state.current_prob
        
        # 문제 표시
        st.markdown(f"### Q{st.session_state.q_idx + 1}.")
        st.markdown(f"#### {prob['q']}") # h4 태그 사용

        # 정답 입력 폼
        with st.form(key=f"q_form_{st.session_state.q_idx}"): # 키값 변경으로 자동 초기화
            if prob['type'] == 'obj':
                user_val = st.radio("정답 선택:", prob['options'], index=None, disabled=st.session_state.solved)
            else:
                user_val = st.text_input("정답 입력:", disabled=st.session_state.solved)
            
            # 버튼
            btn_txt = "다음 문제 ➡️" if st.session_state.solved else "채점하기 ✨"
            submit = st.form_submit_button(btn_txt)

        if submit:
            if not st.session_state.solved:
                # 채점 로직
                if not user_val:
                    st.warning("답을 입력해주세요!")
                else:
                    if check_answer(user_val, prob['a']):
                        st.success("정답입니다! 🎉")
                        st.session_state.score += 1
                        st.balloons()
                    else:
                        st.error("틀렸습니다. 😢")
                        st.markdown(f"**정답: {prob['a']}**")
                        st.warning(f"해설: {prob['exp']}")
                        # 오답노트 저장
                        if prob not in st.session_state.wrong_notes:
                            prob['user_wrong'] = user_val
                            st.session_state.wrong_notes.append(prob)
                    
                    st.session_state.solved = True
                    st.rerun()
            else:
                # 다음 문제 로직
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                if st.session_state.q_idx >= total_q:
                    st.session_state.step = 'result'
                st.rerun()

    # [화면 3] 결과
    elif st.session_state.step == 'result':
        total_q = 5
        final_score = st.session_state.score * 20
        st.title("🏆 학습 완료!")
        st.metric("내 점수", f"{final_score}점")
        
        if final_score >= 60:
            st.success("참 잘했어요! 통과입니다!")
        else:
            st.warning("조금 더 연습해볼까요?")
            
        if st.button("다시 풀기"):
            st.session_state.step = 'intro'
            st.rerun()

    # [화면 4] 오답 노트 뷰
    elif st.session_state.step == 'wrong_note_view':
        st.title("📝 오답 노트")
        if not st.session_state.wrong_notes:
            st.info("오답 노트가 비어있습니다.")
        else:
            for i, note in enumerate(st.session_state.wrong_notes):
                with st.expander(f"{i+1}번 문제 확인"):
                    st.write(f"**문제:** {note['q']}")
                    st.write(f"**내가 쓴 답:** {note.get('user_wrong','?')}")
                    st.success(f"**정답:** {note['a']}")
                    st.info(f"**해설:** {note['exp']}")
        
        if st.button("돌아가기"):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
