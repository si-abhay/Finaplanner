from django.shortcuts import render, redirect
from .forms import loanForm,investForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from joblib import load
import pandas as pd
from .models import loanoffers,Creditoffers

pipeline=load('/Users/yatingoyal/Desktop/Data_signals 2/mysite/savedmodels/pipeline.joblib')
pipeline2=load('/Users/yatingoyal/Desktop/Data_signals 2/mysite/savedmodels2/pipeline2.joblib')

@login_required
def loanreq(request):
    if request.method == 'POST':
        form = loanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            CurrentLoanAmount=form.cleaned_data.get('current_loan_amount')
            Term=form.cleaned_data.get('term')
            AnnualIncome=form.cleaned_data.get('annual_income')
            Yearsjob=form.cleaned_data.get('years_in_current_job')
            HomeOwnership=form.cleaned_data.get('home_ownership')
            MonthlyDebt=form.cleaned_data.get('monthly_debt')
            NumberAccounts=form.cleaned_data.get('number_of_open_accounts')
            MaxCredit=form.cleaned_data.get('maximum_open_credit')
            Bankruptcies=form.cleaned_data.get('bankruptcies')
            input_data = pd.DataFrame([[CurrentLoanAmount, Term, AnnualIncome, Yearsjob, HomeOwnership, MonthlyDebt, NumberAccounts, MaxCredit, Bankruptcies]],
                                      columns=['CurrentLoanAmount', 'Term', 'Annual Income', 'Years in current job', 'Home Ownership', 'Monthly Debt', 'Number of Open Accounts', 'Maximum Open Credit', 'Bankruptcies'])

            y_pred = pipeline.predict(input_data)
            score=y_pred[0,0]
            # take fields for ML model from here for ref check user/views.py
            if score>=750:
                cate=1
            elif 650<=score<750:
                cate=2
            elif 550<=score<650:
                cate=3
            else:
                cate=4        
            
            
            filtered_data1 = loanoffers.objects.all()  
            filtered_data2 = Creditoffers.objects.all() 
            
            filtered_data1=filtered_data1.filter(category=cate) 
            filtered_data2=filtered_data2.filter(category=cate) 
            context = {
               'filter_data1': filtered_data1,
               'filter_data2': filtered_data2
            }
            
            messages.success(request, f'File Uploaded Successfully.')
            
            return render(request,'investment/loanoffers.html',context)
    else:
        form = loanForm()
    return render(request, 'investment/upload.html', {'form': form})

@login_required
def investreq(request):
    if request.method == 'POST':
        form = investForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            

            messages.success(request, f'Submitted Successfully.')
            return render(request,'investment/funds.html',{})
    else:
        form = investForm()
    return render(request, 'investment/invest.html',{'form': form})