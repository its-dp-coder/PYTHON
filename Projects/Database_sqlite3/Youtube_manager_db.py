import sqlite3
con=sqlite3.connect('youtube_videos_db')
cursor=con.cursor()
cursor.execute(''' 

CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )

''')

def list_videos():
    print("\n")  
    print("*" *80)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")  
    print("*" *80)  
def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_videos(video_id,name,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    con.commit()
def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()

def main():
    while(True):


        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")

        choice=input("Enter your choice: ")
        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enetr the time of the video: ")
                add_videos(name,time) 
            case '3':
                video_id=input("Enetr the vide ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enetr the time of the video: ")
                update_videos(video_id,name,time) 
            case '4':
                video_id=input("Enetr the vide ID to update: ")
                delete_videos(video_id) 
            case '5':
                break
            case _:
                print("Inavlid choice ")
    
    con.close()


        



if __name__ =="__main__":
    main()