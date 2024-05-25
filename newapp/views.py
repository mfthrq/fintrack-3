from django.shortcuts import render, redirect, get_object_or_404
from .models import Income, Outcome
from .forms import IncomeForm, OutcomeForm  
from django.http import JsonResponse
from django.contrib import messages
from django.db import models  
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth

# Menampilkan daftar data
def index(request):
    incomes = Income.objects.all()  
    outcomes = Outcome.objects.all()  
    total_pemasukan = float(incomes.aggregate(total=models.Sum('jumlah'))['total'] or 0)
    total_pengeluaran = float(outcomes.aggregate(total=models.Sum('jumlah'))['total'] or 0)
    sisa_uang = total_pemasukan - total_pengeluaran
    
    monthly_incomes = (
        Income.objects.annotate(month=TruncMonth('tanggal'))
        .values('month')
        .annotate(total=models.Sum('jumlah'))
        .order_by('month')
    )
    
    monthly_outcomes = (
        Outcome.objects.annotate(month=TruncMonth('tanggal'))
        .values('month')
        .annotate(total=models.Sum('jumlah'))
        .order_by('month')
    )
    
    total_per_month_income = {i: 0 for i in range(1, 13)}
    total_per_month_outcome = {i: 0 for i in range(1, 13)}
    
    for data in monthly_incomes:
        month = data['month'].month
        total_per_month_income[month] = float(data['total']) if data['total'] else 0.0
    
    for data in monthly_outcomes:
        month = data['month'].month
        total_per_month_outcome[month] = float(data['total']) if data['total'] else 0.0
    
    income_data = [total_per_month_income[i] for i in range(1, 13)]
    outcome_data = [total_per_month_outcome[i] for i in range(1, 13)]
    
    return render(request, 'index.html', {
        'incomes': incomes, 
        'outcomes': outcomes, 
        'total_pemasukan': total_pemasukan,
        'total_pengeluaran': total_pengeluaran,
        'sisa_uang': float(sisa_uang),
        'income_data': income_data,
        'outcome_data': outcome_data
        })

def pemasukan(request):
    incomes = Income.objects.all()  # Mengambil semua data pendapatan
    form = IncomeForm()  # Form untuk menambahkan pendapatan
    return render(request, 'pemasukan.html', {'incomes': incomes, 'form': form})

def pengeluaran(request):
    outcomes = Outcome.objects.all()
    form = OutcomeForm()  # Form untuk menambahkan pendapatan
    return render(request, 'pengeluaran.html', {'outcomes': outcomes, 'form': form})

# ======= AKSI UNTUK PEMASUKAN ======== 

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data ke database
            messages.success(request, "Berhasil tambah data!")  # Pesan untuk SweetAlert
            return redirect('pemasukan')  # Kembali ke halaman pemasukan
    return redirect('pemasukan')  # Jika tidak valid, kembali ke halaman pemasukan

def update_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()  # Simpan perubahan ke database
            messages.success(request, "Berhasil update data!")  # Pesan untuk SweetAlert
            return redirect('pemasukan')  # Kembali ke halaman pemasukan
    return redirect('pemasukan')  # Redirect jika bukan POST

def delete_income(request, id):
    income = get_object_or_404(Income, id=id)
    income.delete()  # Hapus objek
    messages.success(request, "Berhasil hapus data!")  # Pesan untuk SweetAlert
    return redirect('pemasukan')  # Kembali ke halaman pemasukan setelah berhasil dihapus


# ======= AKSI UNTUK PENGELUARAN ======== 

def add_outcome(request):
    if request.method == 'POST':
        form = OutcomeForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data ke database
            messages.success(request, "Berhasil tambah data!")  # Pesan untuk SweetAlert
            return redirect('pengeluaran')  # Kembali ke halaman pengeluaran
    return redirect('pengeluaran')  # Jika tidak valid, kembali ke halaman pengeluaran

def update_outcome(request, id):
    outcome = get_object_or_404(Outcome, id=id)
    if request.method == 'POST':
        form = OutcomeForm(request.POST, instance=outcome)
        if form.is_valid():
            form.save()  # Simpan perubahan ke database
            messages.success(request, "Berhasil update data!")  # Pesan untuk SweetAlert
            return redirect('pengeluaran')  # Kembali ke halaman pengeluaran
    return redirect('pengeluaran')  # Redirect jika bukan POST

def delete_outcome(request, id):
    outcome = get_object_or_404(Outcome, id=id)
    outcome.delete()  # Hapus objek
    messages.success(request, "Berhasil hapus data!")  # Pesan untuk SweetAlert
    return redirect('pengeluaran')  # Kembali ke halaman pengeluaran setelah berhasil dihapus