import subprocess
import os

def download(url, output):
    if not os.path.exists(output):
        os.makedirs(output)
    print("Processing...")
    try: # have spotdl download the song, save in output
        subprocess.run(['spotdl', url, '--output', os.path.join(output, '%(title)s.%(ext)s')], check=True)
        print(f"Downloaded successfully to {output}")
    except subprocess.CalledProcessError as e: # if error
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Please enter the Spotify song URL: ")
    output = "C:/Users/Chris_2yelyef/OneDrive/Desktop/spotifytodownloads"
    download(url, output)
