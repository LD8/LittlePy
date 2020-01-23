from random import choice, shuffle
import string
from plotly import offline
from plotly.graph_objs import Bar, Scatter

def ticket_generator(digit=10, alph=5):
    alphabet = list(string.ascii_uppercase)
    numbers = [str(n) for n in range(10)]
    draw_list = []

    # generate a number of random ints from 0-9
    for d in range(digit):
        draw_list.append(choice(numbers))

    # choose a number of alphabet randomly
    for d in range(alph):
        draw_list.append(choice(alphabet))

    # shuffle the list... maybe this is not necessary
    shuffle(draw_list)
    # print(draw_list)
    
    draw = []
    for d in range(3):
        draw.append(choice(draw_list))

    ticket = ''.join(draw)
    return ticket

def match(ticket):
    n = 0
    while True:
        n += 1
        my_ticket = ticket_generator()
        if my_ticket == ticket:
            break
    return n


def plot_win(win_cost_nums, win_cost_average):
    
    data = [
    {
        'type': 'bar',
        'x': [(i+1) for i, win in enumerate(win_cost_nums)],
        'y': win_cost_nums,
    },
    {
        'type': 'scatter',
        'x': [(i+1) for i, win in enumerate(win_cost_nums)],
        'y': [win_cost_average for i in range(len(win_cost_nums))],
        'text': [win_cost_average for i in range(len(win_cost_nums))],
    }]

    layout = {
        'title': 'How many times to win?',
    }

    fig = {'data': data, 'layout': layout}
    offline.plot(fig, filename='win_lottery.html')


if __name__ == "__main__":
    lotery_ticket = ticket_generator()
    print(f'The lottery ticket is: {lotery_ticket}\n')

    testing_time = int(input('Please enter testing times: '))
    win_cost_nums = []
    win_cost_average = 0
    
    for i in range(testing_time):
        match_num = match(lotery_ticket)
        win_cost_average += match_num
        win_cost_nums.append(match_num)
    win_cost_average = win_cost_average / testing_time

    print(f"We've tested {testing_time} times.\n\nFor you to win, you need to spend in average $ {win_cost_average} for {win_cost_average} tickets!\n")

    plot_win(win_cost_nums, win_cost_average)
