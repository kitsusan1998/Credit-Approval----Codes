import streamlit as st
import joblib


def app():
    model = joblib.load('log.model')

    if 'submited_form' not in st.session_state:
        test_x = None
    else:
        test_x = st.session_state.submited_form

    if test_x is not None:
        rs_prob = model.predict_proba(test_x)
        rs = model.predict(test_x)

        prob = rs_prob[0][1]

        st.markdown('Success probability: {:.2%}'.format(prob))

        if rs[0] == 1:
            st.markdown('Success!')
        else:
            st.markdown('Application Faild')
            """
                0 debt_to_income_ratio_60,
                1 income,
                2 load_amount,
                3 property_value,
                4 open_end_line_of_credit,
                5 debt_to_income_ratio_50,
                6 co_applicant_credit_score_type_9,
                7 co_applicant_age_above_62,
                8 lien_status,
            """

            text_x = test_x[0]

            if text_x[0] == 0:
                st.markdown('- You may increase your dept to income ratio')

            if text_x[4] == 0:
                st.markdown('- Use open-end line credit may help')

            st.markdown('- You may increase your property value')
            st.markdown('- Or decrease load amount')

    else:
        st.markdown('Please submit your application form.')

