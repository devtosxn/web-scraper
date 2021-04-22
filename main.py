from scrape_panel import attempt_website_scrape


def get_user_choice():
    option = str(input('Would you like to scrape a website (y/n)? ').lower())
    return option


while True:
    answer = get_user_choice()
    if answer == 'n':
        print('Thank you for visiting, Goodbye!!!')
        break
    elif answer != 'y':
        print('Invalid input')
    else:
        attempt_website_scrape()
