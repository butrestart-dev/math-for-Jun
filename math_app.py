import streamlit as st
import random

# --- 설정 및 데이터 ---
TOTAL_QUESTIONS = 5   # 테스트를 위해 20문제 -> 5문제로 줄였습니다 (원하는 대로 수정 가능)
PASS_SCORE = 60
UNITS = {
    1: "1. 분수의 나눗셈",
    2: "2. 각기둥과 각뿔",
    3: "3. 소수의 나눗셈",
    4: "4. 비와 비율"
}

# --- 함수 1: 똑똑한 정답 판정 (수치 비교) ---
def check_answer(user_input, correct_val_str):
    """
    사용자 입력과 정답을 수치적으로 비교합니다.
    예: 정답이 '3/4'일 때, 사용자가 '0.75'라고 써도 정답 처리.
    """
    try:
        # 1. 정답 값 계산 (문자열 -> 숫자)
        if '/' in str(correct_val_str):
            n, d = map(float, str(correct_val_str).split('/'))
            ans_val = n / d
        else:
            ans_val = float(correct_val_str)

        # 2. 사용자 입력 값 계산
        user_input = user_input.strip()
        if '/' in user_input:
            n, d = map(float, user_input.split('/'))
            user_val = n / d
        else:
            user_val = float(user_input)

        # 3. 비교 (오차 범위 0.001 이내면 정답)
        return abs(ans_val - user_val) < 0.001
        
    except:
        # 숫자로 변환 안 되는 문자열(예: 텍스트 답변)인 경우 그냥 문자열 비교
        return user_input.strip() == str(correct_val_str).strip()

# --- 함수 2: 문제 생성기 (이미지 기능 추가) ---
def generate_problem(unit_num, difficulty):
    problem = {}
    problem['unit'] = unit_num # 나중에 오답노트에서 단원 구분용
    
    # [1단원]
    if unit_num == 1:
        if difficulty == '하':
            a, b = random.randint(2, 9), random.randint(2, 9)
            problem['question'] = f"다음 나눗셈의 몫을 분수로 나타내시오: $${a} \div {b}$$"
            problem['answer'] = f"{a}/{b}"
            problem['explanation'] = f"{a}÷{b} = {a}/{b}"
        elif difficulty == '중':
            ja, mo, nat = random.randint(1, 9), random.randint(2, 9), random.randint(2, 5)
            problem['question'] = f"계산하시오: $$\\frac{{{ja}}}{{{mo}}} \div {nat}$$"
            problem['answer'] = f"{ja}/{mo*nat}"
            problem['explanation'] = f"분모에 자연수를 곱합니다: {ja}/{mo*nat}"
        else:
            a, b, c = random.randint(10, 20), random.randint(21, 30), random.randint(2, 5)
            problem['question'] = f"계산하시오: $$\\frac{{{a}}}{{{b}}} \div {c}$$"
            problem['answer'] = f"{a}/{b*c}"
            problem['explanation'] = "분모에 나누는 수를 곱하여 계산합니다."

    # [2단원] 이미지 문제 예시
    elif unit_num == 2:
        # 실제 앱에서는 'assets/prism.png' 처럼 로컬 파일 경로를 넣으세요.
        # 여기서는 테스트를 위해 플레이스홀더 이미지 서비스를 사용합니다.
        shapes_data = [
            {'name': '삼각기둥', 'edges': 9, 'faces': 5, 'img': 'https://placehold.co/300x200/png?text=Triangular+Prism'},
            {'name': '사각기둥', 'edges': 12, 'faces': 6, 'img': 'https://placehold.co/300x200/png?text=Rectangular+Prism'},
            {'name': '오각기둥', 'edges': 15, 'faces': 7, 'img': 'https://placehold.co/300x200/png?text=Pentagonal+Prism'},
            {'name': '사각뿔', 'edges': 8, 'faces': 5, 'img': 'https://placehold.co/300x200/png?text=Rectangular+Pyramid'}
        ]
        
        data = random.choice(shapes_data)
        q_type = random.choice(['모서리', '면'])
        
        problem['question'] = f"아래 도형은 **{data['name']}**입니다. 이 도형의 **{q_type}**의 수는 몇 개입니까?"
        problem['image'] = data['img']  # 이미지 URL 또는 파일 경로 저장
        
        if q_type == '모서리':
            problem['answer'] = str(data['edges'])
            problem['explanation'] = f"{data['name']}의 모서리 개수는 {data['edges']}개입니다."
        else:
            problem['answer'] = str(data['faces'])
            problem['explanation'] = f"{data['name']}의 면의 개수는 {data['faces']}개입니다."

    else:
        a, b = random.randint(1, 50), random.randint(1, 50)
        problem['question'] = f"다음 덧셈을 하시오: $${a} + {b}$$"
        problem['answer'] = str(a + b)
        problem['explanation'] = "기본 덧셈 문제입니다."

    return problem

# --- 메인 앱 로직 ---
def main():
    st.set_page_config(page_title="똑똑한 초6 수학", page_icon="🎓", layout="centered")

    # 세션 상태 초기화
    if 'mode' not in st.session_state: st.session_state.mode = 'study' # study, quiz, wrong_note
    if 'current_unit' not in st.session_state: st.session_state.current_unit = 1
    if 'unlocked_unit' not in st.session_state: st.session_state.unlocked_unit = 1
    if 'incorrect_problems' not in st.session_state: st.session_state.incorrect_problems = []
    
    # 퀴즈 관련 상태
    if 'q_index' not in st.session_state: st.session_state.q_index = 0
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'current_problem' not in st.session_state: st.session_state.current_problem = None
    if 'user_answer_state' not in st.session_state: st.session_state.user_answer_state = None

    # 사이드바
    st.sidebar.title("메뉴")
    
    # 1. 단원 선택
    st.sidebar.subheader("📚 단원 학습")
    for u_num, u_name in UNITS.items():
        if u_num <= st.session_state.unlocked_unit:
            if st.sidebar.button(f"{u_name}", key=f"unit_{u_num}"):
                st.session_state.current_unit = u_num
                st.session_state.mode = 'study'
                st.session_state.current_problem = None
                st.rerun()
        else:
            st.sidebar.button(f"🔒 {u_name}", disabled=True, key=f"unit_{u_num}")

    # 2. 오답 노트 메뉴
    st.sidebar.markdown("---")
    wrong_count = len(st.session_state.incorrect_problems)
    st.sidebar.subheader(f"📝 오답 노트 ({wrong_count}문제)")
    if wrong_count > 0:
        if st.sidebar.button("오답 문제 다시 풀기"):
            st.session_state.mode = 'wrong_note'
            st.session_state.current_problem = None
            st.session_state.user_answer_state = None
            st.rerun()
    else:
        st.sidebar.caption("틀린 문제가 없습니다. 훌륭해요!")

    # --- 메인 화면 로직 ---
    
    # [모드 1] 학습 대기 화면
    if st.session_state.mode == 'study':
        u_name = UNITS.get(st.session_state.current_unit)
        st.title(f"{u_name} 학습")
        st.info("준비가 되면 아래 버튼을 눌러 문제를 풀어보세요.")
        if st.button("🚀 문제 풀기 시작"):
            st.session_state.mode = 'quiz'
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.current_problem = None
            st.session_state.user_answer_state = None
            st.rerun()

    # [모드 2 & 3] 퀴즈 모드 또는 오답 노트 모드
    elif st.session_state.mode in ['quiz', 'wrong_note']:
        
        # 헤더 표시
        if st.session_state.mode == 'quiz':
            st.caption(f"현재 단원: {UNITS[st.session_state.current_unit]}")
            prog = st.session_state.q_index / TOTAL_QUESTIONS
            st.progress(prog, text=f"문제 {st.session_state.q_index + 1} / {TOTAL_QUESTIONS}")
        else:
            st.subheader("🔥 오답 정복하기")
            st.caption("틀린 문제를 다시 풀어보세요. 맞히면 목록에서 사라집니다!")

        # 문제 가져오기 (없으면 생성 또는 오답 목록에서 가져옴)
        if st.session_state.current_problem is None:
            if st.session_state.mode == 'quiz':
                # 새 문제 생성
                diff = random.choice(['하', '하', '중', '중', '상'])
                st.session_state.current_problem = generate_problem(st.session_state.current_unit, diff)
            else:
                # 오답 노트에서 문제 가져오기 (첫 번째 문제)
                if len(st.session_state.incorrect_problems) > 0:
                    st.session_state.current_problem = st.session_state.incorrect_problems[0]
                else:
                    st.success("모든 오답을 해결했습니다!")
                    if st.button("돌아가기"):
                        st.session_state.mode = 'study'
                        st.rerun()
                    st.stop()

        problem = st.session_state.current_problem

        # --- 문제 화면 출력 ---
        st.markdown(f"### Q. {problem['question']}")
        
        # 이미지가 있는 문제라면 출력
        if 'image' in problem and problem['image']:
            st.image(problem['image'], caption="참고 이미지")

        # 입력 폼
        with st.form(key='q_form'):
            user_val = st.text_input("정답 입력 (분수는 3/4 처럼 입력)", key="ans_input")
            sub_btn = st.form_submit_button("제출")

        if sub_btn:
            # 정답 판정 (check_answer 함수 사용)
            is_correct = check_answer(user_val, problem['answer'])
            
            if is_correct:
                st.session_state.user_answer_state = 'correct'
                st.success("🎉 정답입니다!")
                
                # 오답 노트 모드였다면, 맞혔으니 목록에서 제거
                if st.session_state.mode == 'wrong_note':
                    if problem in st.session_state.incorrect_problems:
                        st.session_state.incorrect_problems.remove(problem)
            else:
                st.session_state.user_answer_state = 'wrong'
                st.error(f"💥 틀렸습니다. 정답: {problem['answer']}")
                st.warning(f"💡 해설: {problem['explanation']}")
                
                # 퀴즈 모드였다면, 틀렸으니 오답 노트에 추가 (중복 방지)
                if st.session_state.mode == 'quiz':
                    if problem not in st.session_state.incorrect_problems:
                        st.session_state.incorrect_problems.append(problem)

        # 다음 버튼 로직
        if st.session_state.user_answer_state is not None:
            btn_text = "다음 문제 ➡️" if st.session_state.mode == 'quiz' else "다음 오답 문제 ➡️"
            
            if st.button(btn_text):
                # 상태 초기화
                st.session_state.user_answer_state = None
                st.session_state.current_problem = None
                
                if st.session_state.mode == 'quiz':
                    st.session_state.q_index += 1
                    if st.session_state.user_answer_state == 'correct':
                        st.session_state.score += 1
                    
                    # 퀴즈 종료 체크
                    if st.session_state.q_index >= TOTAL_QUESTIONS:
                        st.session_state.mode = 'result'
                        st.rerun()
                
                st.rerun()

    # [모드 4] 결과 화면
    elif st.session_state.mode == 'result':
        final_score = (st.session_state.score / TOTAL_QUESTIONS) * 100
        st.balloons()
        st.title("🏆 학습 완료!")
        st.metric(label="최종 점수", value=f"{final_score}점")
        
        if final_score >= PASS_SCORE:
            st.success("통과했습니다! 다음 단원이 열립니다.")
            if st.session_state.current_unit == st.session_state.unlocked_unit:
                st.session_state.unlocked_unit += 1
        else:
            st.error("아쉽게도 통과하지 못했습니다.")
            
        col1, col2 = st.columns(2)
        if col1.button("다시 풀기"):
            st.session_state.mode = 'study'
            st.rerun()
        if len(st.session_state.incorrect_problems) > 0:
            if col2.button("오답 노트 바로가기"):
                st.session_state.mode = 'wrong_note'
                st.session_state.current_problem = None
                st.rerun()

if __name__ == "__main__":
    main()
