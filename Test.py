import sqlite3

conn = sqlite3.connect('PlasticPollution.db')
cur = conn.cursor()

while True:

    ans1 = input("Would you like to delete (d), modify (m), insert (i), print all (a), commit (c), or exit (esc)")

    if ans1 == 'd':
        while True:
            ans1 = input("which country would you like to delete? Please use the country Code.\nUse '/help' for the list of all country codes.\nTo exit delete mode, type 'esc'")

            if ans1 == 'esc':
                break
            elif ans1 == '/help':
                cur.execute("SELECT * FROM plasticPollution")
                all_results = cur.fetchall()
                for data in all_results:
                    print(f"{data[0]}, {data[1]}")
            else:
                cur.execute("SELECT * FROM plasticPollution")
                all_results = cur.fetchall()
                for data in all_results:
                    found = False
                    if ans1 == data[1]:
                        found = True
                        cur.execute(f"DELETE FROM plasticPollution WHERE Code='{ans1}';")

                        print("done!")
                        break
                if not(found):
                    print("Could not find the country")
    elif ans1 == 'a':
        cur.execute("SELECT * FROM plasticPollution")
        all_results = cur.fetchall()
        print(all_results)
    elif ans1 == 'i':
        Entity = input('Please enter a country')
        Code = input('What is the 3 letter country code?')
        Year = input('What year was the data recorded?')
        Plastic = input('Mismanaged plastic waste to ocean per capita (kg per year)')

        myTuple = (Entity, Code, Year, Plastic)

        cur.execute(f"INSERT INTO plasticPollution VALUES(?,?,?,?);", myTuple)
    elif ans1 == 'c':
        conn.commit()
    elif ans1 == 'm':
        row = input('Which country would you like to modify?')
        while True:
            ans1 = input('Would you like to modify Entity (e), Code (c), Year (y), or Plastic Pollution (p), or exit (esc')

            if ans1 == 'e':
                Entity = input('Please enter a country')
                cur.execute(f"UPDATE plasticPollution SET Entity = '{Entity}' WHERE '{ans1}';")
            if ans1 == 'c':
                Code = input('What is the 3 letter country code?')
            if ans1 == 'y':
                Year = input('What year was the data recorded?')
            if ans1 == 'p':
                Plastic = input('Mismanaged plastic waste to ocean per capita (kg per year)')
            if ans1 == 'esc':
                break
        
    elif ans1 == 'esc':
        break

