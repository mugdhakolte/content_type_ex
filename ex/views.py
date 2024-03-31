from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.contrib.contenttypes.models import ContentType
from ex.models import (
    Article,
    Comment,
    BlogPost,
    Photo,
)


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article_content_type = ContentType.objects.get_for_model(Article)
    comments = Comment.objects.filter(
        content_type=article_content_type, object_id=article.id
    )
    return render(
        request,
        "article_detail.html",
        {"article": article, "comments": comments},
    )


def add_comment(request, content_type, object_id):
    if request.method == "POST":
        text = request.POST.get("text")
        content_class = ContentType.objects.get(model=content_type).model_class()
        content_object = get_object_or_404(content_class, pk=object_id)
        comment = Comment.objects.create(content_object=content_object, text=text)
        return render(
            request,
            "comment_detail.html",
            {"comment": comment, "content_object": content_object},
        )

    return redirect("/")
