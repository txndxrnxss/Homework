from django.shortcuts import render
from blog.models import Post, Comment

def cookies_and_comm(request):    

    """
    Функция обрабатывает GET и POST запросы для страницы 'home/'.
    Если метод запроса - GET, функция создает словарь с информацией о всех постах из модели Post и комментариями к ним.
    Если метод запроса - POST, функция сохраняет новый комментарий в базу данных Comment.

    """

    if request.method == 'POST':

        # Получаем информацию о комментарии
        comment = request.POST['comment']
        post_id = request.POST['post_id']
        user=request.user

        # Сохраняем новый комментарий в базу данных
        post = Post.objects.get(id=post_id)
        Comment(user=user, post=post, info_comm=comment, nickname=user).save()

    # Получаем информацию о всех постах и комментариях к ним из базы данных
    get_posts_name = Post.objects.all()
    info_db_dict = {}
    comm_inf = {}

    # Создаем словари с информацией о постах и о комментариях
    for i in get_posts_name:
        info_db_dict[i]= list(Post.objects.filter(title= str(i)).values('title', 'description', 'image','id'))
        post_id = list(Post.objects.filter(title= str(i)).values('id'))[0]['id']

        # получаем список комментариев к текущему посту
        comment_info = list(Comment.objects.filter(post_id = post_id).values('info_comm', 'nickname'))
        comm_inf[f"comment_info_{i}"] = list(
            Comment.objects.filter(post_id = post_id).values('info_comm', 'nickname')
            )

    # Возвращаем страницу home/ и передаем информацию о пользователях, постах и комментариях.    
    return render(
        request, 'home.html', {'users_name': request.user,'big_data': info_db_dict}
        )


def post_info(request,post_id):    

    """
    Функция обрабатывает GET и POST запросы для страницы 'home/'.
    Если метод запроса - GET, функция создает словарь с информацией о всех постах из модели Post и комментариями к ним.
    Если метод запроса - POST, функция сохраняет новый комментарий в базу данных Comment.

    """
   
    if request.method == 'POST':

        # Получаем информацию о комментарии
        comment = request.POST['comment']
  
        user=request.user

        # Сохраняем новый комментарий в базу данных
        post = Post.objects.get(id=post_id)
        Comment(user=user, post=post, info_comm=comment, nickname=user).save()

    # Создаем словари с информацией о постах
    info_db_dict = list(Post.objects.filter(id = post_id).values('title', 'description', 'image'))

    # получаем список комментариев к текущему посту
    comm_info = list(
        Comment.objects.filter(post_id = post_id).values('info_comm', 'nickname')
        )
  
    return render(
        request, 'post_info.html', {'users_name': request.user,'big_data':info_db_dict,'comm_info':comm_info}
        )
