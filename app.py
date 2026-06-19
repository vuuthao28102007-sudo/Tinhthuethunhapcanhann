import streamlit as st
st.image("thao.npg", width=150)
# Tiêu đề app
st.title("Ứng dụng tính thuế thu nhập cá nhân_VuThanhThao")

st.write("Nhập thông tin để tính số thuế phải nộp")

# Nhập dữ liệu
income = st.number_input(
    "Thu nhập tháng (VNĐ)",
    min_value=0
)

dependent = st.number_input(
    "Số người phụ thuộc",
    min_value=0
)

# Nút tính
if st.button("Tính thuế"):

    # Giảm trừ
    personal_deduction = 11000000
    dependent_deduction = dependent * 4400000

    taxable_income = (
        income 
        - personal_deduction 
        - dependent_deduction
    )


    # Tính thuế đơn giản
    if taxable_income <= 0:
        tax = 0

    elif taxable_income <= 5000000:
        tax = taxable_income * 0.05

    elif taxable_income <= 10000000:
        tax = taxable_income * 0.1

    elif taxable_income <= 18000000:
        tax = taxable_income * 0.15

    else:
        tax = taxable_income * 0.2


    st.success(
        f"Thu nhập chịu thuế: {taxable_income:,.0f} VNĐ"
    )

    st.info(
        f"Thuế TNCN phải nộp: {tax:,.0f} VNĐ"
    )
