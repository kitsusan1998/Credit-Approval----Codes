import streamlit as st
import joblib
import global_var


def app():
    st.title('Loan')

    model = joblib.load('log.model')

    with st.form("my_form"):

        income = st.number_input('Please input your income')
        load_amount = st.number_input('Please input load amount')
        property_value = st.number_input('Please input your property value')
        open_end_line_of_credit = st.radio(
            'Please specific open-end_line_of_credit', [True, False])
        co_applicant_credit_score_type = st.radio(
            'Please specific co_applicant_credit_score_type',
            ['1.0', '2.0', '3.0', '8.0', '9.0', '10.0'])
        co_applicant_age_above62 = st.radio('Is co-applicant age above 62?',
                                            [True, False])

        lien_status = st.number_input(
            'Please input tract_one_to_four_family_homes')
        debt_to_income_ratio = st.radio('debt_to_income_ratio',
                                        ['>60%', '36%-<50%'])

        if open_end_line_of_credit:
            open_end_line = 1
        else:
            open_end_line = 0

        if debt_to_income_ratio == '>60%':
            debt_to_income_ratio_60 = 1
            debt_to_income_ratio_50 = 0
        else:
            debt_to_income_ratio_60 = 0
            debt_to_income_ratio_50 = 1

        co_applicant_credit_score_type_9 = 1 if co_applicant_credit_score_type == '9.0' else 0  # noqa

        co_applicant_age_above_62 = 1 if co_applicant_age_above62 else 0

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:

            submited_form = [[
                debt_to_income_ratio_60,
                income,
                load_amount,
                property_value,
                open_end_line,
                debt_to_income_ratio_50,
                co_applicant_credit_score_type_9,
                co_applicant_age_above_62,
                lien_status,
            ]]

            global_var.set_value('submited_form', submited_form)

            st.session_state.submited_form = submited_form

            st.success(
                'Application submited. Please check your application at result page!'  # noqa
            )
