from django.urls import path, include

urlpatterns = [
    path('', include('src.web.dashboard.urls')),
    path('invoice/', include('src.services.invoice.urls')),
    path('customer/', include('src.services.customer.urls')),
    path('projects/', include('src.services.project.urls')),
    path('quotation/', include('src.services.quotation.urls')),
    path('loans/', include('src.services.loan.urls')),
    path('expense/', include('src.services.expense.urls')),
    path('assets/', include('src.services.assets.urls')),
    path('vendor/', include('src.services.vendor.urls')),
    path('transaction/', include('src.services.transaction.urls')),
    path('charts/', include('src.services.charts.urls')),
    path('accounts/', include('src.web.accounts.urls')),
]
