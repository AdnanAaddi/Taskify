from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Board, Project, List, Card
from django.urls import reverse
from boards.forms import CardForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def boards_page(request, project_id):
    project = Project.objects.get(pk=project_id)
    boards = Board.objects.filter(project_id=project_id)

    if request.method == 'POST':
        board_name = request.POST.get('board_name')
        # Create a new board associated with the project
        new_board = Board.objects.create(project=project, title=board_name)
        List.objects.create(title='To Do', board=new_board)
        List.objects.create(title='Doing', board=new_board)
        List.objects.create(title='Completed', board=new_board)
        # Redirect the user back to the boards page after creating the board
        return redirect(reverse('boards_page', kwargs={'project_id': project_id}))
    return render(request, 'boards/boards.html', {'project': project, 'boards': boards})

def board_lists(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    lists = List.objects.filter(board=board)
    
    # Fetch cards for each list
    if request.method == 'POST':
        # Handling the form submission for creating a new list
        list_title = request.POST.get('list_title')
        if list_title:  # Ensure the list title is not empty
            List.objects.create(board=board, title=list_title)
            # Redirect to the same page to display the updated list of lists and avoid form resubmission
            return redirect(reverse('lists', kwargs={'board_id': board_id}))

    # This part will execute for GET requests and also for POST if no redirect happens
    lists = List.objects.filter(board=board)
    return render(request, 'boards/lists.html', {'board': board, 'lists': lists})

# Add a Card throgh the Card Model Form
def add_card(request, list_id):
    list_instance = List.objects.get(id=list_id)
    board_id = list_instance.board.id
    if request.method == 'POST':
        form = CardForm(request.POST)
        print(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.opened_by = request.user  # Assuming the user is logged in
            card.list_id=list_id
            card.save()
            form.save_m2m()  # Required for saving ManyToMany relations
            return redirect(reverse('lists', kwargs={'board_id': board_id}))
    else:
        form = CardForm()
    return render(request, 'boards/create_card.html', {'form': form})

@require_POST
def move_card_to_list(request):
    card_id = request.POST.get('card_id')
    target_list_id = request.POST.get('target_list_id')

    card = get_object_or_404(Card, pk=card_id)
    target_list = get_object_or_404(List, pk=target_list_id)

    card.list = target_list
    card.save()

    return JsonResponse({"message": "Card moved successfully."})