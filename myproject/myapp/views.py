from django.http import HttpResponse

def index(request):
    return HttpResponse("""
                        <h1>Hello, Welcome to My Django Project!</h1>
                    """)

def user(request):
    return HttpResponse("""
                        <h2>Hello, User! This is the user page.</h2>
                    """)

def product(request):
    return HttpResponse("""
                        <h2>Hello, Product! This is the product page.</h2>
                    """)

def payment(request):
    return HttpResponse("""
                        <h2>Hello, Payment! This is the payment page.</h2>
                    """)

def prediction(request):
    return HttpResponse("""
                        <h2>Hello, Prediction! This is the prediction page.</h2>
                    """)

def report(request):
    return HttpResponse("""
                        <h2>Hello, Report! This is the report page.</h2>
                    """)