from django.urls import path
from eligibility import  views

urlpatterns=[
    path('create_technical_eligibility/',views.TechnicalEligibilityCreate.as_view()),
    path('create_financial_eligibility/',views.FinancialEligibilityCreate.as_view()),
    path('create_initial_costing/',views.InitialCostingCreate.as_view()),



]