from django.shortcuts import render
from django.views import View

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')

class AboutPageView(View):
    def get(self, request):
        return render(request, 'about.html')

class BlogPageView(View):  # เพิ่มการนิยามของ BlogPageView
    def get(self, request):
        return render(request, 'blog.html')

class ContactPageView(View):  # เพิ่มการนิยามของ ContactPageView
    def get(self, request):
        return render(request, 'contact.html')