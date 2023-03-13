"""Movie theatre ticketing system - v1
Welcome screen and set up variables
Created my Jack Lowe
"""


def sell_ticket():
    print("******** Fanfair Movies - ticketing system ********\n")

    adult_tickets = 0
    child_tickets = 0
    student_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0


    ticket_wanted ="Y"
    while ticket_wanted != "N":
        ticket_type = input("What kind of ticket do you want?: \n"
                            "\t'A' for adult, or\n"
                            "\t'S' for student, or\n"
                            "\t'C' for Child, or\n"
                            "\t'S' for Gift voucher\n"
                            ">> ").upper()
        ticket = ticket_type
        num_tickets = int(input(f"How many {ticket} tickets do you want: "))

        print(f"\nYou have ordered{num_tickets} {ticket} ticket(s)!")
        ticket_wanted = input("Do you want to sell another ticket (Y/N:"
                              "").upper()



sell_ticket()
