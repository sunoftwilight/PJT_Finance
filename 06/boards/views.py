from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_http_methods(["GET"])
def index(request):
    boards = Board.objects.all().order_by('-created_at')
    context = {
        'boards': boards
    }
    return render(request, 'boards/index.html', context)


@require_http_methods(["GET", "POST"])
def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        if request.user == board.author:
            board.delete()
        return redirect('boards:index')

    comments = board.comments.all()
    comment_form = CommentForm()
    
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user == board.author:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)
        context = {
            'board': board,
            'form': form,
        }        
        return render(request, 'boards/update.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            form.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)


@login_required
@require_http_methods(["POST"])
def delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user == board.author:
        board.delete()
    return redirect('boards:index')


@login_required
@require_http_methods(["POST"])
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.author = request.user
            comment.save()
            return redirect('boards:detail', board.pk)


@login_required
@require_http_methods(["POST"])
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        if request.method == 'POST':
            comment.delete()
    return redirect('boards:detail', board_pk)
        

@login_required
@require_http_methods(['POST'])
def likes(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    
    if request.user in board.like_user.all():
        board.like_user.remove(request.user)
    else:
        board.like_user.add(request.user)
    return redirect('boards:detail', board_pk)