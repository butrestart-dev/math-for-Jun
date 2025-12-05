import streamlit as st
import random

# --- 🎨 디자인 & CSS (가독성 테마 유지) ---
def apply_custom_style():
    st.markdown("""
    <style>
    /* 따뜻한 크림색 배경 */
    .stApp { background-color: #FFF9C4; }
    
    /* 가독성 좋은 진한 글씨 */
    h1, h2, h3, p, div, span, label, .stMarkdown {
        color: #3E2723 !important;
        font-family: 'Jua', 'Comic Sans MS', sans-serif;
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #FF9800;
        color: white !important;
        border-radius: 15px;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); background-color: #F57C00; }
    
    /* 객관식 라디오 버튼 텍스트 크기 키우기 */
    .stRadio label { font-size: 20px !important; }
    
    /* 정답/오답 알림 박스 */
    .stAlert { background-color: white; border: 2px solid #FF9800; color: #3E2723; }
    </style>
    """, unsafe_allow_html=True)

# --- 📚 데이터 ---
UNITS = { 1: "1. 분수의 나눗셈", 2: "2. 각기둥과 각뿔", 3: "3. 소수의 나눗셈", 4: "4. 비와 비율" }

CONCEPTS = {
    1: "### 🍰 분수의 나눗셈\n(자연수)÷(자연수)는 분수로! 곱셈으로 바꿔서 계산해요.",
    2: "### 📦 각기둥과 각뿔\n각기둥은 위아래가 같고, 각뿔은 위가 뾰족해요.",
    3: "### 💧 소수의 나눗셈\n자연수처럼 나누고 소수점을 원래 자리에 콕!",
    4: "### 🍎 비와 비율\n두 수를 비교할 때 3:2 처럼 써요."
}

# --- ⚙️ 기능 함수 ---

def check_answer(user_input, correct_val):
    """정답 확인 로직"""
    try:
        # 문자열 비교 (공백 제거)
        if str(user_input).strip() == str(correct_val).strip():
            return True
        # 수치 비교 (소수/분수)
        if '/' in str(correct_val):
            n, d = map(float, str(correct_val).split('/'))
            ans_val = n / d
        else:
            ans_val = float(correct_val)

        if '/' in str(user_input):
            n, d = map(float, str(user_input).split('/'))
            user_val = n / d
        else:
            user_val = float(user_input)
            
        return abs(ans_val - user_val) < 0.001
    except:
        return False

def generate_problem(unit_num, difficulty):
    """문제 생성 (객관식/주관식 랜덤)"""
    problem = {}
    problem['unit'] = unit_num
    
    # 문제 유형 결정 (50% 확률로 객관식 or 주관식)
    # 2단원(도형)은 객관식이 더 어울림
    q_type = 'obj' if (random.random() > 0.5 or unit_num == 2) else 'subj'
    problem['type'] = q_type
    
    # [1단원: 분수]
    if unit_num == 1:
        a, b = random.randint(2, 9), random.randint(2, 9)
        problem['q'] = f"몫을 분수로 나타내면? $${a} \div {b}$$"
        problem['a'] = f"{a}/{b}"
        problem['exp'] = f"{a} 나누기 {b}는 {a}/{b} 입니다."
        
        if q_type == 'obj':
            # 오답 보기 생성
            options = [f"{a}/{b}", f"{b}/{a}", f"{a+1}/{b}", f"{a}/{b+1}"]
            random.shuffle(options)
            problem['options'] = options

    # [2단원: 도형]
    elif unit_num == 2:
        shapes = [('삼각기둥', 3), ('사각기둥', 4), ('오각기둥', 5), ('육각기둥', 6)]
        name, n = random.choice(shapes)
        target = random.choice(['모서리', '꼭짓점', '면'])
        
        problem['q'] = f"**{name}**의 **{target}** 개수는?"
        
        if target == '모서리': ans = n * 3
        elif target == '꼭짓점': ans = n * 2
        else: ans = n + 2 # 면
        
        problem['a'] = str(ans)
        problem['exp'] = f"{name}의 {target} 구하는 공식 기억나나요?"
        
        if q_type == 'obj':
            options = [str(ans), str(ans+1), str(ans-1), str(ans*2)]
            # 중복 제거 및 섞기
            options = list(set(options))
            while len(options) < 4: options.append(str(random.randint(5, 20)))
            random.shuffle(options)
            problem['options'] = options

    # [기타 단원]
    else:
        a, b = random.randint(10, 50), random.randint(2, 9)
        problem['q'] = f"나눗셈의 몫은? (자연수 부분만) $${a} \div {b}$$"
        problem['a'] = str(a // b)
        problem['exp'] = "나머지는 버리고 몫만 구하세요."
        
        if q_type == 'obj':
            ans = int(problem['a'])
            options = [str(ans), str(ans+1), str(ans-1), str(ans+2)]
            random.shuffle(options)
            problem['options'] = options

    return problem

# --- 🚀 메인 앱 ---
def main():
    st.set_page_config(page_title="초등 수학 대장", page_icon="✏️", layout="centered")
    apply_custom_style()

    # 세션 상태 초기화
    if 'step' not in st.session_state: st.session_state.step = 'intro'
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
    if 'current_prob' not in st.session_state: st.session_state.current_prob = None
    if 'solved' not in st.session_state: st.session_state.solved = False
    if 'wrong_notes' not in st.session_state: st.session_state.wrong_notes = [] # 오답노트 리스트

    # 사이드바
    st.sidebar.header("🚩 메뉴")
    if st.sidebar.button("🏠 처음으로"):
        st.session_state.step = 'intro'
        st.rerun()
    
    # 오답노트 메뉴 표시
    wrong_count = len(st.session_state.wrong_notes)
    if wrong_count > 0:
        st.sidebar.markdown("---")
        st.sidebar.write(f"❌ 틀린 문제: {wrong_count}개")
        if st.sidebar.button("📝 오답 노트 확인하기"):
            st.session_state.step = 'wrong_note_view'
            st.rerun()

    # --- [1] 개념 설명 (Intro) ---
    if st.session_state.step == 'intro' or st.session_state.step == 'study':
        st.title("오늘의 수학 공부 🏫")
        
        # 단원 선택 (셀렉트박스로 변경하여 깔끔하게)
        selected_unit_name = st.selectbox(
            "공부할 단원을 선택하세요:", 
            options=list(UNITS.values())
        )
        # 선택된 단원 번호 찾기
        for k, v in UNITS.items():
            if v == selected_unit_name:
                st.session_state.current_unit = k
                break
        
        st.markdown(f"<div style='background-color: white; padding: 20px; border-radius: 10px;'>{CONCEPTS[st.session_state.current_unit]}</div>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 80px;'>🤔 💡</h1>", unsafe_allow_html=True)
        
        if st.button("🚀 문제 풀기 시작!", use_container_width=True):
            st.session_state.step = 'quiz'
            st.session_state.score = 0
            st.session_state.q_idx = 0
            st.session_state.current_prob = None
            st.session_state.solved = False
            st.session_state.wrong_notes = [] # 새 게임 시작 시 오답노트 초기화 (원하면 유지 가능)
            st.rerun()

    # --- [2] 퀴즈 (Quiz) ---
    elif st.session_state.step == 'quiz':
        total_q = 5
        st.markdown(f"**{UNITS[st.session_state.current_unit]}**")
        st.progress(st.session_state.q_idx / total_q, text=f"문제 {st.session_state.q_idx + 1} / {total_q}")

        # 문제 생성
        if st.session_state.current_prob is None:
            st.session_state.current_prob = generate_problem(st.session_state.current_unit, '중')
            st.session_state.solved = False
        
        prob = st.session_state.current_prob
        
        st.markdown(f"### Q{st.session_state.q_idx + 1}. {prob['q']}")

        # 폼 생성 (입력창/버튼)
        with st.form(key='quiz_form'):
            user_val = ""
            
            # [기능 2] 문제 유형에 따른 입력 방식 변화
            if prob['type'] == 'obj': # 객관식
                # key를 q_idx로 설정하여 문제 바뀔 때마다 초기화 [기능 1 해결]
                user_val = st.radio(
                    "정답을 고르세요:", 
                    prob['options'], 
                    key=f"radio_{st.session_state.q_idx}", 
                    index=None, # 초기 선택 없음
                    disabled=st.session_state.solved
                )
            else: # 주관식
                # key를 q_idx로 설정하여 문제 바뀔 때마다 비워짐 [기능 1 해결]
                user_val = st.text_input(
                    "정답을 입력하세요:", 
                    key=f"text_{st.session_state.q_idx}", 
                    disabled=st.session_state.solved
                )

            # 버튼 상태 관리
            submit_text = "다음 문제 ➡️" if st.session_state.solved else "채점하기 ✨"
            submit_btn = st.form_submit_button(submit_text)

        if submit_btn:
            if not user_val and not st.session_state.solved:
                st.warning("정답을 입력하거나 선택해주세요!")
            elif not st.session_state.solved:
                # [채점]
                if check_answer(user_val, prob['a']):
                    st.success("정답입니다! 🎉")
                    st.session_state.score += 1
                else:
                    st.error("틀렸습니다. 😢")
                    st.markdown(f"**정답: {prob['a']}**")
                    st.info(f"해설: {prob['exp']}")
                    
                    # [기능 3] 오답 노트에 자동 추가 (중복 방지)
                    if prob not in st.session_state.wrong_notes:
                        # 사용자 입력값도 함께 저장해두면 좋음
                        prob_copy = prob.copy()
                        prob_copy['user_wrong_ans'] = user_val
                        st.session_state.wrong_notes.append(prob_copy)
                
                st.session_state.solved = True
                st.rerun()
            else:
                # [다음 문제]
                st.session_state.q_idx += 1
                st.session_state.current_prob = None
                st.session_state.solved = False
                
                if st.session_state.q_idx >= total_q:
                    st.session_state.step = 'result'
                st.rerun()

    # --- [3] 결과 (Result) ---
    elif st.session_state.step == 'result':
        total_q = 5
        final_score = st.session_state.score * (100 // total_q)
        
        st.title("수고했어요! 👏")
        st.markdown(f"## 점수: {final_score}점")
        
        if len(st.session_state.wrong_notes) > 0:
            st.warning(f"틀린 문제가 {len(st.session_state.wrong_notes)}개 있어요. 오답 노트를 확인해볼까요?")
            if st.button("📝 오답 노트 보러가기"):
                st.session_state.step = 'wrong_note_view'
                st.rerun()
        else:
            st.success("모든 문제를 맞혔어요! 완벽해요! 💯")
            st.balloons()
            
        if st.button("🔄 처음부터 다시 하기"):
            st.session_state.step = 'intro'
            st.rerun()

    # --- [4] 오답 노트 뷰 (Wrong Note View) ---
    elif st.session_state.step == 'wrong_note_view':
        st.title("📝 오답 노트")
        st.markdown("틀린 문제를 다시 한번 확인해보세요.")
        
        for idx, note in enumerate(st.session_state.wrong_notes):
            with st.expander(f"{idx+1}번 문제 다시보기 (클릭)"):
                st.markdown(f"**문제:** {note['q']}")
                st.error(f"내가 쓴 답: {note.get('user_wrong_ans', '없음')}")
                st.success(f"정답: {note['a']}")
                st.info(f"💡 해설: {note['exp']}")
        
        if st.button("🔙 메인 화면으로 돌아가기"):
            st.session_state.step = 'intro'
            st.rerun()

if __name__ == "__main__":
    main()
