from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://henjcdjcdnccdb:nickdcdbhxdhidbcdbhcdl@cluster0.joatyap.mongodb.net/',tlsAllowInvalidCertificates=True)

print(client)

db = client["youtube"]
video_collection = ["videos"]

print(video_collection)

def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time": time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id': ObjectId(video_id)},{"$set": {"name":new_name,"time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List all the videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice :")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter the video id to update: ")
            delete_video(video_id,name,time)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")
        

        

if __name__ == "__main__":
    main()