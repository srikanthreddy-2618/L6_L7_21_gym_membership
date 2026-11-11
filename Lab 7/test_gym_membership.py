from hypothesis import given, strategies as st

from gym_membership import parse_plan, calculate_bmi, average_workout


@given(st.one_of(st.text(), st.none()))
def test_parse_plan_no_crash(value):
    try:
        parse_plan(value)
    except Exception as exc:
        assert False, f"parse_plan crashed with input {value!r}: {exc}"


@given(st.one_of(st.text(), st.none()))
def test_calculate_bmi_no_crash(value):
    try:
        calculate_bmi(value)
    except Exception as exc:
        assert False, f"calculate_bmi crashed with input {value!r}: {exc}"


@given(st.one_of(st.text(), st.none()))
def test_average_workout_no_crash(value):
    try:
        average_workout(value)
    except Exception as exc:
        assert False, f"average_workout crashed with input {value!r}: {exc}"
