import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# Membership cost: valid and invalid plans, age limits, discounts and trainer options

def test_invalid_plan():
    with pytest.raises(ValueError):
        membership_cost("weekly", 30, False, False)


def test_age_below_minimum():
    with pytest.raises(ValueError):
        membership_cost("monthly", 13, False, False)


def test_age_exactly_14():
    assert membership_cost("monthly", 14, False, False) == 1500


def test_senior_discount():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_senior_discount_takes_precedence_over_student():
    assert membership_cost("monthly", 60, True, False) == 1125


def test_student_discount_for_non_senior():
    assert membership_cost("monthly", 59, True, False) == 1350


def test_no_discount_for_non_student():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_trainer_addon():
    assert membership_cost("monthly", 30, False, True) == 3500


def test_yearly_trainer_discount():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_quarterly_without_trainer():
    assert membership_cost("quarterly", 30, False, False) == 4000


# Gym entry: both outcomes of membership, hour limits, women-only slot and gender

def test_inactive_membership_denies_entry():
    assert can_enter(10, False, False, "M") is False


def test_active_membership_during_regular_hours():
    assert can_enter(10, True, False, "M") is True


def test_entry_before_opening():
    assert can_enter(4, True, False, "M") is False


def test_entry_after_closing():
    assert can_enter(23, True, False, "M") is False


def test_entry_exactly_at_opening():
    assert can_enter(5, True, False, "M") is True


def test_entry_exactly_at_closing():
    assert can_enter(22, True, False, "M") is True


def test_women_only_slot_allows_female_member():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_denies_male_member():
    assert can_enter(10, True, True, "M") is False


# BMI: invalid height and all category boundaries/outcomes

def test_zero_height_raises_error():
    with pytest.raises(ValueError):
        bmi_category(60, 0)


def test_negative_height_raises_error():
    with pytest.raises(ValueError):
        bmi_category(60, -1.7)


def test_underweight_category():
    assert bmi_category(45, 1.7) == "underweight"


def test_normal_category():
    assert bmi_category(65, 1.7) == "normal"


def test_overweight_category():
    assert bmi_category(80, 1.7) == "overweight"


def test_obese_category():
    assert bmi_category(100, 1.7) == "obese"


def test_bmi_exactly_18_5_is_normal():
    assert bmi_category(18.5, 1.0) == "normal"


def test_bmi_exactly_25_is_overweight():
    assert bmi_category(25, 1.0) == "overweight"


def test_bmi_exactly_30_is_obese():
    assert bmi_category(30, 1.0) == "obese"
