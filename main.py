def GetCreditCardVendor(card_number):

    """ Task 1 """

    vendors_INN = { 
                        'AmericanExpress'   : list(range(340000, 350000)) + list(range(370000, 380000)),
                        'Maestro'           : list(range(500000, 510000)) + list(range(560000, 700000)),
                        'MasterCard'        : list(range(510000, 560000)),
                        'VISA'              : list(range(400000, 500000)),
                        'JSB'               : list(range(352800, 359000))
    }

    vendors_length = {
                        'AmericanExpress'   : [15,],
                        'Maestro'           : list(range(12, 20)),
                        'MasterCard'        : [16,],
                        'VISA'              : [13, 16, 19],
                        'JSB'               : [16,]
    }

    card_INN = int(card_number[:6]) 

    for vendor in vendors_INN:  
        for vendor_INN in vendors_INN[vendor]:  
            if card_INN == vendor_INN:
                for vendor_length in vendors_length[vendor]:
                    if len(card_number) == vendor_length:
                        return vendor
                else:
                    print('Your card INN looks like {}`s INN, but length of your credit number is {}.'.format(vendor, len(card_number)))
                    print('Valid length for {} is {}.'.format(vendor, vendors_length[vendor])) 
                    global formatted_card_number # rewriting for correct output
                    formatted_card_number = formatting_input()
                    vendor = GetCreditCardVendor(formatted_card_number)
                    return vendor
    return 'Unknown'


def IsCreditCardNumberValid(card_number):

    """ Task 2 """

    double = ''
    
    # step 1
    card_number = card_number[::-1] # we have to move from the rightmost digit 
    # doubling every other
    for index in range(1, len(card_number)+1):
        
        digit = int(card_number[index-1])
        
        if index % 2 == 0:  
            if 2 * digit < 10 :
                double += str(2 * digit)
            else:
                double += str(2 * digit - 9)
            continue;

        double += str(digit)
 
    # step 2
    # calculation sum of digits
    total_sum = 0
    for digit in double:
        total_sum += int(digit)

    # step 3
    # check the card number to valid
    if total_sum % 10 == 0:
        return True
    else:
        return False


def GenerateNextCreditNumber(card_number):
    
    """ Task 3 """

    valid = False
    next_card_number = int(card_number)

    while not valid:
        
        next_card_number += 1
        valid = IsCreditCardNumberValid(str(next_card_number))
        
    return str(next_card_number)


def formatting_input():
    
    '''Checking, formatting input card number. 
        * if card number length not equal 12 .. 19, then input is incorrect'''
    
    print('''
         ___________________________________
        |                                   |
        |  KottansBank                      |
        |               /\_/\               |
        |             =(/\./\)=             | 
        |              (")_(")              |
        |                                   |
------> |       XXXX  XXXX  XXXX  XXXX      |                    
|       |                                   |
|       |___________________________________|
|
------- Write your card number : ''', end = '')

    card_number = input()
    formatted_card_number = ''

    for digit in card_number:
        
        # delete space
        if digit == ' ':
            continue;
       
        # check input to correct
        # if input is not correct, then input starts again (recursion)
        try:
            int(digit)
        except ValueError:
            print('Incorrect input. Credit number can`t have symbols only digits. Please try again.', end = '')
            formatted_card_number = formatting_input()
            return formatted_card_number
        formatted_card_number += digit

    # check card number to legth
    # if input is not correct, then input starts again (recursion)
    lenght_list = list(range(12, 20))
    if len(formatted_card_number) not in lenght_list:
        print('Incorrect input. Credit number is valid if length equal 12..19. Please try again.', end = '')
        formatted_card_number = formatting_input()
        return formatted_card_number

    return formatted_card_number


def interface():
   
    """ Showing interface """

    print('''
-------Get credit card number vendor------- 1
-------Check credit number to valid ------- 2
-------Generate next credit number -------- 3
-------Point 1, 2 and 3 at one time ------- 4
-------Exit  ------------------------------ 5
        ''') 
    print('Write your command: ', end = '')


def card(formatted_card_number, last_part):

    """ Showing card"""
    
    card = '''
         ___________________________________
        |                                   |
        |  KottansBank                      |
        |               /\_/\               |
        |             =(/\./\)=             | 
        |              (")_(")              |
        |                                   |
        |    {:>5}  {:>5}  {:>5}  {:>5}     |                       
        |          {:>24} |
        |___________________________________|
    '''.format(formatted_card_number[ : len(formatted_card_number)//4], formatted_card_number[len(formatted_card_number)//4 : 2*len(formatted_card_number)//4], \
        formatted_card_number[2*len(formatted_card_number)//4 : 3*len(formatted_card_number)//4], formatted_card_number[3*len(formatted_card_number)//4 : ], last_part)
    print(card)

#
# main part
#

interface()               
menu = input()

while menu != '5':

    if menu == '1':
        
        # task 1
        formatted_card_number = formatting_input()
        card_vendor = GetCreditCardVendor(formatted_card_number)
        card(formatted_card_number, 'Vendor - ' + card_vendor)
        print('Card vender is', card_vendor)

        break;

    elif menu == '2':
        
        # task 2
        formatted_card_number = formatting_input()
        bool_valid = IsCreditCardNumberValid(formatted_card_number)
        
        if bool_valid:
            card(formatted_card_number, '')
            print('Card number is valid')
        else:
            card(formatted_card_number, '')
            print('Card number is invalid')
  
        break;
   
    elif menu == '3':
       
       # task 3
        formatted_card_number = formatting_input()
        next_card_number = GenerateNextCreditNumber(formatted_card_number)
        card(next_card_number, '')
        print('Next valid card number is ', next_card_number)

        break;



    elif menu == '4': 
        
        formatted_card_number = formatting_input()
       
        # task 1
        card_vendor = GetCreditCardVendor(formatted_card_number)
        card(formatted_card_number, 'Vendor - ' + card_vendor)
        print('Card vender is', card_vendor)
       
        # task 2
        bool_valid = IsCreditCardNumberValid(formatted_card_number)
       
        if bool_valid:
            print('Card number is valid')
        else:
            print('Card number is invalid')   
        
        # task 3
        next_card_number = GenerateNextCreditNumber(formatted_card_number)
        print('Next valid credit number is ', next_card_number)
        
        break;

    else:
        
        # incorrect choice
        print(menu, " command not found")
        interface()
        menu = input()