from django.shortcuts import render
from .models import Book, Rating, Book_Topic
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import searchForm
from .utils import normalize_vietnamese, pagePaginator
from django.shortcuts import redirect

# Logic xử lí
def checkRate(userid = None, bookid = None):
    rate = Rating.objects.filter(user_id = userid, book_id = bookid).first()
    if rate:
        return rate
    return 0

def rateBook(userid, bookid, point):
    rate = checkRate(userid=userid, bookid=bookid)
    if not rate:
        rate1 = Rating(user_id=userid, book_id = bookid, rating = point)
        rate1.save()
        return
    rate.rating = point
    rate.save()


# Ajax Response
def searchPost(request):
    skey = request.POST.get('skey')
    # Loại bỏ dấu câu của skey
    skey = normalize_vietnamese(skey)
    if len(skey)>=3:
        # sử dùng hàm __unaccent để có thể truy xuất băng tiếng việt không dấu
        books = Book.objects.filter(book_title__unaccent__icontains=skey)[:5]
        if books:
            context = ""
            # Chỉnh sửa phần context để hiển thị ra đúng
            for book in books:
                # chỉnh sủa để hiển thị suggest dựa theo từ khóa
                context+= f'<li><a href="/book/detail/id={book.book_id}">{ book.book_title }</a></li>'
            return HttpResponse(context)
    return HttpResponse('')

def categoryPost(request):
    pass

# middle logic
def searchSlug(request):
    skey = request.GET.get('skey')
    skey.replace(" ", "+")
    return redirect('search', skey = skey)
                   
        
# Các view để trả về trang HTML theo url.
def index(request):
    forms = {}
    # thanh tim kiem
    forms['searchbar'] = searchForm()
    
    bookList = {}
    bookList['popular'] = Book.objects.order_by('book_view')[0:10]  
    bookList['topVn'] = Book.objects.filter(book_lang = 'Vietnamese').order_by('book_view')[0:10]
    bookList['topFL'] = Book.objects.filter(book_lang = 'Foreign').order_by('book_view')[0:10]
    context = {
        'bookList' : bookList,
        'forms' : forms,
    }
    return render(request, 'index.html', context)
    
def bookDetail(request, id):
    detail = Book.objects.filter(book_id = id).first()
    topicList = Book_Topic.objects.prefetch_related('topic_id').filter(book_id = detail.book_id)
    context = {
        'detail':detail,
        'topicList':topicList,
    }
    return render(request, 'bookDetail.html', context)

# pagepanigtion, su dung lai cau lenh truy xuat book o tren, 
def search(request, skey):
    form = searchForm()
    # Take skey and execute query
    skey.replace('+',' ')
    skey = normalize_vietnamese(skey)
    books = Book.objects.filter(book_title__unaccent__icontains=skey)
    # pagnition
    page_obj = pagePaginator(request, books)
    context = {
        'form': form,
        'page_obj' : page_obj,
    }
    return render(request, 'searchBook.html', context)

def categoryFilter(request,id):
    Book_TopicList = Book_Topic.objects.prefetch_related('topic_id').filter(topic_id = id)
    bookList = None
    topicTitle =False
    for book in Book_TopicList:
        if not topicTitle:
            topicTitle = book.topic_id.topic_name
        # Chinh sua hien thi cho cac quyen sach
        bookList+= f'<li><a href="/book/detail/id={book.book_id}">{ book.book_title }</a></li>'
    context = {
        'topicTitle': topicTitle,
        'bookList': bookList
    }
    return render(request, 'bookDetail.html', context)