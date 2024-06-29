import mysql.connector
import datetime
import smtplib


# Create a connection to the database
mydb=mysql.connector.connect(
  host='localhost',
  user='root',
  password='Gopi@2001',
  database='sathiyam_cinemas'
)


# Create a cursor object
mycursor = mydb.cursor()



def ticket_booking():

    print(f'\n***welcome to Sathiyam Cineamas***\n')

    items={
        'Leo':150,
        'Gilli':120,
        'Goat':250,
        'Master':150,
        'Mersal':150,

    }
    email_data=[]
    booking=[]
    total_cost=0
    while True:
        name=input('enter your name: ').capitalize()
        mail=input('enter your mail id: ') 
        email_data.append(mail) 
        for movie, price in items.items():
            print(f'{movie}:₹{price}')
        select_movie=input('enter movie name: ').capitalize()
        if select_movie in items:

            print(f'Your "movie:{select_movie}" tickets are available..')
            how_many=int(input(f'enter no of {select_movie} movie ticket: '))
            cost=items[select_movie]*how_many
            booking.append((select_movie,how_many,cost))
            print(f'{how_many} x {select_movie} total cost is : ₹{cost}')

            if select_movie=='Leo':
                mycursor.execute(f'update ticket_booking set tickets={how_many} where movie="Leo"')
                mydb.commit() # Commit the changes to the database
            if select_movie=='Gilli':
                mycursor.execute(f'update ticket_booking set tickets={how_many} where movie="Gilli"')
                mydb.commit() # Commit the changes to the database
            elif select_movie=='Goat':
                mycursor.execute(f'update ticket_booking set tickets={how_many} where movie="Goat"')
                mydb.commit() # Commit the changes to the database
            elif select_movie=='Master':
                mycursor.execute(f'update ticket_booking set tickets={how_many} where movie="Master"')
                mydb.commit() # Commit the changes to the database
            elif select_movie=='Mersal':
                mycursor.execute(f'update ticket_booking set tickets={how_many} where movie="Mersal"')
                mydb.commit() # Commit the changes to the database
        else:
            print('Your movie ticket is not available\nthanks for coming..')  

        
        # GST 
        selling_price = cost
        gst_rate = 18
        gst_price = selling_price * 18 / 100
        net_price = selling_price + gst_price   
        total_cost += net_price

        if total_cost > 500:
            discount=total_cost*0.10
            print(f'\nYou are eligible for a discount of ₹{discount:.2f}')
            total_cost-=discount
        else:
            discount= 0
            print('\nNo discount applied')

        print("\n--- Bill Summary ---")
        for select_movie, how_many, cost in booking:
            print(f"{how_many} x {select_movie} = ₹{cost}")

        print(f"GST : ₹{gst_price:.2f}")
        print(f"Subtotal: ₹{total_cost + discount:.2f}")
        if discount > 0:
            print(f"Discount: -₹{discount:.2f}")  

        print(f"Total: ₹{total_cost:.2f}")
        print("--------------------")

        payment = float(input("\nEnter payment amount: ₹"))
        while payment < total_cost:
            print("Insufficient payment. Please enter an amount equal to or greater than the total bill.")
            payment = float(input("Enter payment amount: ₹"))

        change = payment - total_cost
        print(f"\nChange: ₹{change:.2f}")
        print("Thank you for booking tickets at Sathiyam Cinemas!")

        # bill
        f=open('bill.txt','a')
        x=datetime.datetime.now()
        f.write(f'\nHi {name} \nYour tickets Total Price: {total_cost}\n{x}')

        # mail sending
        try:
            for i in email_data:
                print(i,f'Your total price: {total_cost}\n{x}')
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login('11062001gopinath@gmail.com','1234567890')
                msg=(f'thanks for booking tickets\n{x}\nRegards from:\nSathiyam Cinemas')
                s.sendmail('11062001gopinath@gmail.com',i,msg)
                s.quit()
                print('mail sent')
        except:
            print('mail not sent')


        
        again=input('do you want to continue..press "Yes": ')
        if again!='yes':
            break

ticket_booking()

    



