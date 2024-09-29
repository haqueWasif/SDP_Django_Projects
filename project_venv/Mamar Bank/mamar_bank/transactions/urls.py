from django.urls import path
from .views import deposit_money_view, withdraw_money_view,TransactionReportView,LoanRequestView,LoanListView,PayLoanView,TransferMoneyView


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", deposit_money_view.as_view(), name="deposit_money"),
    path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path("withdraw/", withdraw_money_view.as_view(), name="withdraw_money"),
    path("loan_request/", LoanRequestView.as_view(), name="loan_request"),
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loans/<int:loan_id>/", PayLoanView.as_view(), name="pay"),
    path('transfer/', TransferMoneyView.as_view(), name='transfer_money'),
]