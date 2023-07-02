from main import my_card, welcome_page

def test_my_card():
    assert my_card("mainstreet 123 finland Jamaica") == "The provided address is not valid. Please enter a new one and respect the indicated format."
    assert my_card("123 sesame street 12345 helsinki finland") == "Thank you! The card should reach your specified address in 10 working days.\nBack to the main menu section....."

test_my_card()



def test_welcome_page():
    assert welcome_page(1) == True 
    assert welcome_page(9) == False

test_welcome_page()

