# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import MainManu,SecondaryManu,Article,Product,CustomerAppraise,FAQ,RotateImage,BackGroudImage
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import ConsultForm
from django.shortcuts import render

def createBaseContext():
    main_manu =MainManu.objects.all()
    main_manu_list=[]
    product_category=[]
    for manu in main_manu:
        manu_secondary=SecondaryManu.objects.filter(mainmanu=manu.id)
        if manu.template=='PL':
            product_category=manu_secondary
        manu_dict={"main_manu":manu,"manu_secondary":manu_secondary}
        main_manu_list.append(manu_dict)
    form = ConsultForm()
    back_groud_images=BackGroudImage.objects.all()
    context={'main_manu': main_manu,'main_manu_list':main_manu_list,'product_category':product_category,'form':form,"back_groud_images":back_groud_images}
    return context

def index(request):
    template = loader.get_template('polls/index.html')
    appraise_list=CustomerAppraise.objects.all().order_by('-id')[:6]
    customer_list=appraise_list
    context=createBaseContext()
    article_list=Article.objects.all().order_by('id')[:10]
    product_list=Product.objects.all().order_by('id')[:12]
    context['customer_list']=customer_list
    context['appraise_list']=appraise_list
    context['article_list']=article_list
    context['product_list']=product_list
    faq_list=FAQ.objects.all().order_by('-id')[:3]
    context['faq_list']=faq_list
    rotate_list=RotateImage.objects.all().order_by('id')[:5]
    context['rotate_list']=rotate_list
    return HttpResponse(template.render(context, request))

#use category to represent MainManu
def category(request, category_id):
    try:
        category =MainManu.objects.get(pk=category_id)
    except MainManu.DoesNotExist:
        raise Http404("MainManu does not exist")
    context=createBaseContext()
    context['category']=category
    page = request.GET.get('page')
    if page is None:
        page=1
    if category.template=='AD':
        template='polls/articles.html'
        article_list=Article.objects.filter(mainmanu=category.id)
        paginator = Paginator(article_list,1) # Show 1 articles per page
        articles= paginator.page(page)
        context['test']=article_list
        context['articles']=articles
        return render(request, template,context)
    elif category.template=='AL':
        template='polls/article_list.html'
        article_list=Article.objects.filter(mainmanu=category.id)
        paginator = Paginator(article_list,20) # Show 20 contacts per page
        articles= paginator.get_page(page)
        context['articles']=articles
        return render(request, template,context)
    elif category.template=='PL':
        template='polls/product_list.html'
        product_list=Product.objects.filter(mainmanu=category.id)
        paginator = Paginator(product_list,20) # Show 20 contacts per page
        products= paginator.get_page(page)
        context['products']=products
        return render(request, template,context)

#use sub_category to represent SecondaryManu
def subcategory(request, sub_category_id):
    try:
        sub_category =SecondaryManu.objects.get(pk=sub_category_id)
        category =MainManu.objects.get(pk=sub_category.mainmanu.id)
    except SecondaryManu.DoesNotExist:
        raise Http404("SecondaryManu does not exist")
    except MainManu.DoesNotExist:
        raise Http404("MainManu does not exist")
    context=createBaseContext()
    context['category']=category
    page = request.GET.get('page')
    if page is None:
        page=1
    if category.template=='AD':
        template='polls/article.html'
        article_list=Article.objects.filter(secondarymanu=sub_category.id)
        paginator = Paginator(article_list,1) # Show 1 articles per page
        articles= paginator.get_page(page)
        context['articles']=articles
        return render(request, template,context)
    elif category.template=='AL':
        template='polls/article_list.html'
        article_list=Article.objects.filter(secondarymanu=sub_category.id)
        paginator = Paginator(article_list,20) # Show 20 contacts per page
        articles= paginator.get_page(page)
        context['articles']=articles
        return render(request, template,context)
    elif category.template=='PL':
        template='polls/product_list.html'
        product_list=Product.objects.filter(secondarymanu=sub_category.id)
        paginator = Paginator(product_list,20) # Show 20 contacts per page
        products= paginator.get_page(page)
        context['products']=products
        return render(request,template,context)

def complete_consult(request):
    context=createBaseContext()
    return render(request, 'polls/complete_consult.html',context)

def article_detail(request, article_id):
    #question = get_object_or_404(Article, pk=article_id)
    try:
        article =Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    context=createBaseContext()
    context['article']=article
    return render(request, 'polls/article.html',context)

def product_detail(request, product_id):
    #question = get_object_or_404(Article, pk=article_id)
    try:
        product =Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    context=createBaseContext()
    context['product']=product
    return render(request, 'polls/product.html',context)


def consult(request):
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            #process the data in form.cleaned_data as required
            form.save()
            return HttpResponseRedirect('/polls/complete_consult')
    else:
        form = ConsultForm()
    context=createBaseContext()
    context['form']=form
    return render(request, 'polls/index.html',context)

def faq(request):
    faq=FAQ.objects.all()
    context=createBaseContext()
    paginator = Paginator(faq,20)
    page = request.GET.get('page')
    if page is None:
        page=1
    faq= paginator.get_page(page)
    context['faq']=faq
    return render(request, 'polls/faq.html',context)

'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
