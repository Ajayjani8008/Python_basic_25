import json

def load_data():
    try: 
        with open('youtube.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Creating a new file...")
        return []

def save_data_helper(videos):
    with open('youtube.json', 'w') as file:
        json.dump(videos, file, indent=1)
        
def list_all_youtube_videos(videos):
    if not videos:
        print("No videos found.")
    else:
        print("\n")
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Title: {video['name']}, Time: {video['time']}")
            
def add_video(videos):
    print("\n")
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("Video added successfully!")
    
def update_video(videos):
    print("\n")
    list_all_youtube_videos(videos)
    try:
        videos_id = int(input("Enter the video ID to update: ")) - 1
        if 0 <= videos_id < len(videos):
            name = input("Enter new video title: ")
            time = input("Enter new video time: ")
            videos[videos_id] = {"name": name, "time": time}
            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid video ID.")
    except ValueError:
        print("Please enter a valid number.")
        
def delete_video(videos):
    print("\n")
    list_all_youtube_videos(videos)
    try:
        video_id = int(input("Enter the video ID to delete: ")) - 1
        if 0 <= video_id < len(videos):
            deleted_video = videos.pop(video_id)
            save_data_helper(videos)
            print(f"Video '{deleted_video['name']}' deleted successfully!")
        else:
            print("Invalid video ID.")
    except ValueError:
        print("Please enter a valid number.")
        
        
def main():
    videos = load_data()
    
    while True:
        print("\nYoutube Manager | choose an option:")
        print("1. List all Youtube Videos")
        print("2. Add Youtube video")
        print("3. Update a Youtube video details")
        print("4. Delete Youtube video")
        print("5. Exit Youtube Manager")
    
        choice = input("\nEnter your choice: ")
        
        match choice:
            case "1":
                list_all_youtube_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting Youtube Manager...")
                break
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    main()
        
        